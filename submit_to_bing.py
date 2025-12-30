#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bing IndexNow URL提交工具 - Renomee AI博客版
使用方法: python submit_to_bing.py [urls.txt]
"""

import json
import requests
import sys
import io
import xml.etree.ElementTree as ET
from typing import List
from pathlib import Path

# 设置标准输出编码为 UTF-8（解决 Windows 中文显示问题）
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# IndexNow配置
CONFIG = {
    'domain': 'hetianhe2024.github.io',
    'base_path': '/renomee-ai',
    'api_key': 'cccb4286654e4b24a35216f3d00bb49f',  # 留空，首次运行时自动生成
    'api_endpoint': 'https://api.indexnow.org/IndexNow'
}

# 默认提交的重要页面
DEFAULT_URLS = [
    'https://hetianhe2024.github.io/renomee-ai/',
    'https://hetianhe2024.github.io/renomee-ai/about/',
    'https://hetianhe2024.github.io/renomee-ai/categories/',
    'https://hetianhe2024.github.io/renomee-ai/archive/',
]

def generate_api_key() -> str:
    """生成随机API密钥（128位十六进制）"""
    import secrets
    return secrets.token_hex(16)

def get_or_create_api_key() -> str:
    """获取或创建API密钥"""
    key_file = Path('bing_api_key.txt')
    
    if key_file.exists():
        api_key = key_file.read_text().strip()
        print(f"📂 使用已存在的API密钥: {api_key}")
        return api_key
    
    # 生成新密钥
    api_key = generate_api_key()
    key_file.write_text(api_key)
    print(f"🔑 已生成新的API密钥: {api_key}")
    print(f"📝 密钥已保存到: {key_file}")
    
    # 创建验证文件
    verify_file = Path(f'{api_key}.txt')
    verify_file.write_text(api_key)
    print(f"✅ 已创建验证文件: {verify_file}")
    print()
    print("⚠️  重要: 请将验证文件提交到GitHub仓库根目录!")
    print(f"   文件名: {api_key}.txt")
    print(f"   内容: {api_key}")
    print()
    
    return api_key

def load_urls_from_sitemap() -> List[str]:
    """从sitemap.xml加载URL列表"""
    sitemap_file = Path('sitemap.xml')
    
    if not sitemap_file.exists():
        print("⚠️  未找到 sitemap.xml 文件")
        return []
    
    try:
        tree = ET.parse(sitemap_file)
        root = tree.getroot()
        
        # 处理XML命名空间
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = []
        
        for url_elem in root.findall('ns:url', namespace):
            loc = url_elem.find('ns:loc', namespace)
            if loc is not None and loc.text:
                urls.append(loc.text)
        
        print(f"📄 从 sitemap.xml 加载了 {len(urls)} 个URL")
        return urls
        
    except Exception as e:
        print(f"❌ 解析 sitemap.xml 失败: {e}")
        return []

def load_urls_from_file(filename: str) -> List[str]:
    """从文件加载URL列表"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        print(f"📂 从 {filename} 加载了 {len(urls)} 个URL")
        return urls
    except FileNotFoundError:
        print(f"❌ 文件 {filename} 不存在")
        return []

def validate_urls(urls: List[str]) -> List[str]:
    """验证URL列表"""
    valid_urls = []
    base_url = f"https://{CONFIG['domain']}{CONFIG['base_path']}"
    
    for url in urls:
        # 确保URL格式正确
        if not url.startswith(('http://', 'https://')):
            url = f"{base_url}/{url.lstrip('/')}"
        
        # 确保URL属于配置的域名
        if CONFIG['domain'] in url:
            # 去重
            if url not in valid_urls:
                valid_urls.append(url)
        else:
            print(f"⚠️  跳过无效URL: {url}")
    
    return valid_urls

def submit_to_indexnow(urls: List[str], api_key: str) -> bool:
    """提交URL到IndexNow API"""
    if not urls:
        print("❌ 没有有效的URL可提交")
        return False
    
    # IndexNow限制每次最多提交10,000个URL，但建议分批提交
    max_urls = 100
    if len(urls) > max_urls:
        print(f"⚠️  URL数量({len(urls)})超过推荐值，将只提交前{max_urls}个")
        urls = urls[:max_urls]
    
    # 构建请求数据
    key_location = f"https://{CONFIG['domain']}{CONFIG['base_path']}/{api_key}.txt"
    
    request_data = {
        'host': CONFIG['domain'],
        'key': api_key,
        'keyLocation': key_location,
        'urlList': urls
    }
    
    print(f"\n🚀 正在提交 {len(urls)} 个URL到Bing IndexNow...")
    print(f"域名: {CONFIG['domain']}")
    print(f"验证文件: {key_location}")
    print()
    
    # 显示部分URL（用于调试）
    print("📋 提交的URL (前10个):")
    for i, url in enumerate(urls[:10], 1):
        print(f"  {i}. {url}")
    if len(urls) > 10:
        print(f"  ... 还有 {len(urls) - 10} 个URL")
    print()
    
    try:
        # 发送POST请求
        response = requests.post(
            CONFIG['api_endpoint'],
            headers={
                'Content-Type': 'application/json; charset=utf-8'
            },
            json=request_data,
            timeout=30
        )
        
        print(f"📡 响应状态码: {response.status_code}")
        
        # 处理响应
        if response.status_code == 200:
            print(f"✅ 成功提交 {len(urls)} 个URL到Bing IndexNow!")
            return True
        elif response.status_code == 202:
            print(f"✅ Bing已接收提交请求 ({len(urls)} 个URL)，正在处理中")
            return True
        else:
            error_messages = {
                400: "请求格式无效",
                403: "API密钥无效或未找到密钥文件",
                422: "URL不属于指定域名或密钥格式不匹配",
                429: "请求频率过高，请稍后再试"
            }
            
            error_msg = error_messages.get(response.status_code, f"未知错误: HTTP {response.status_code}")
            print(f"❌ {error_msg}")
            
            # 显示响应内容（如果有的话）
            if response.text:
                print(f"响应内容: {response.text}")
            
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🔍 Bing IndexNow URL提交工具 - Renomee AI博客")
    print("=" * 60)
    print()
    
    # 获取或创建API密钥
    api_key = get_or_create_api_key()
    CONFIG['api_key'] = api_key
    
    # 检查验证文件是否存在
    verify_file = Path(f'{api_key}.txt')
    if not verify_file.exists():
        print(f"❌ 验证文件不存在: {verify_file}")
        print("请先运行脚本生成验证文件，并提交到GitHub仓库")
        sys.exit(1)
    
    # 收集URL
    urls = []
    
    if len(sys.argv) > 1:
        # 从命令行参数指定的文件读取URL
        filename = sys.argv[1]
        if filename == '--sitemap':
            urls = load_urls_from_sitemap()
        else:
            urls = load_urls_from_file(filename)
    else:
        # 提供选择
        print("请选择URL来源:")
        print("1. 使用默认重要页面")
        print("2. 从 sitemap.xml 读取所有URL")
        print("3. 从文本文件读取")
        print()
        
        choice = input("请选择 (1/2/3): ").strip()
        
        if choice == '1':
            print("📋 使用默认重要页面")
            urls = DEFAULT_URLS.copy()
        elif choice == '2':
            urls = load_urls_from_sitemap()
        elif choice == '3':
            filename = input("请输入文件名: ").strip()
            urls = load_urls_from_file(filename)
        else:
            print("❌ 无效选择")
            sys.exit(1)
    
    # 验证URL
    valid_urls = validate_urls(urls)
    
    if not valid_urls:
        print("❌ 没有有效的URL可提交")
        sys.exit(1)
    
    print()
    print(f"📊 共 {len(valid_urls)} 个有效URL待提交")
    print()
    
    # 确认提交
    if len(valid_urls) > 10:
        print("URL列表:")
        for i, url in enumerate(valid_urls[:5], 1):
            print(f"  {i}. {url}")
        print(f"  ... 还有 {len(valid_urls) - 5} 个URL")
    else:
        print("URL列表:")
        for i, url in enumerate(valid_urls, 1):
            print(f"  {i}. {url}")
    
    print()
    confirm = input("是否继续提交到Bing? (y/N): ").lower().strip()
    if confirm not in ['y', 'yes']:
        print("❌ 用户取消操作")
        sys.exit(0)
    
    # 提交URL
    success = submit_to_indexnow(valid_urls, api_key)
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 提交完成!")
        print("=" * 60)
        print()
        print("📝 后续步骤:")
        print("1. 访问 Bing Webmaster Tools 验证索引状态")
        print("   🔗 https://www.bing.com/webmasters")
        print()
        print("2. 通常需要几天时间才能在搜索结果中看到")
        print()
        print("3. 建议定期提交新内容（有新文章时运行此脚本）")
        print()
    else:
        print("\n💥 提交失败，请检查以下内容:")
        print("1. 验证文件是否已提交到GitHub并可访问")
        print(f"   {CONFIG['domain']}{CONFIG['base_path']}/{api_key}.txt")
        print("2. URL是否正确")
        print("3. 网络连接是否正常")
        sys.exit(1)

if __name__ == '__main__':
    main()

