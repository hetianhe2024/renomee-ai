#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 Wix Sitemap 提取 URL 列表并生成每日提交计划
使用方法: python extract_wix_urls.py
"""

import sys
import io
import requests
import xml.etree.ElementTree as ET

# Windows 中文显示支持
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def extract_urls_from_sitemap(sitemap_url):
    """从 Sitemap 提取所有 URL"""
    print(f"正在获取 Sitemap: {sitemap_url}")
    
    try:
        response = requests.get(sitemap_url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        
        # 解析 XML
        root = ET.fromstring(response.content)
        
        # 处理命名空间
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        # 提取所有 URL
        urls = []
        for url_elem in root.findall('ns:url', namespace):
            loc = url_elem.find('ns:loc', namespace)
            if loc is not None and loc.text:
                urls.append(loc.text)
        
        print(f"\n✅ 成功提取 {len(urls)} 个 URL\n")
        return urls
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return []

def save_urls_to_file(urls, filename='wix_urls.txt'):
    """保存 URL 到文本文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        for url in urls:
            f.write(url + '\n')
    print(f"✅ 已保存到: {filename}\n")

def split_urls_for_daily_submission(urls, per_day=10):
    """将 URL 分组，每组 10 个（每天提交一组）"""
    batches = [urls[i:i+per_day] for i in range(0, len(urls), per_day)]
    
    print(f"📅 提交计划（每天最多 {per_day} 个 URL）：")
    print(f"总共需要 {len(batches)} 天完成")
    print("=" * 60)
    print()
    
    for i, batch in enumerate(batches, 1):
        print(f"【第 {i} 天】提交 {len(batch)} 个 URL：")
        for j, url in enumerate(batch, 1):
            print(f"  {j}. {url}")
        print()
    
    return batches

def save_daily_batches(batches):
    """保存每日提交批次到单独文件"""
    for i, batch in enumerate(batches, 1):
        filename = f'day_{i}_urls.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            for url in batch:
                f.write(url + '\n')
        print(f"✅ 第 {i} 天的 URL 已保存到: {filename}")
    print()

def main():
    print("=" * 60)
    print("Wix Sitemap URL 提取工具")
    print("适用于 Bing URL Submission Tool 手动提交")
    print("=" * 60)
    print()
    
    # 输入 Wix Sitemap URL
    print("请输入你的 Wix Sitemap URL")
    print("格式: https://yourusername.wixsite.com/yoursite/sitemap.xml")
    print()
    sitemap_url = input("> ").strip()
    
    if not sitemap_url:
        print("❌ URL 不能为空")
        return
    
    # 自动补全 sitemap.xml
    if not sitemap_url.endswith('sitemap.xml'):
        if sitemap_url.endswith('/'):
            sitemap_url += 'sitemap.xml'
        else:
            sitemap_url += '/sitemap.xml'
    
    print()
    
    # 提取 URL
    urls = extract_urls_from_sitemap(sitemap_url)
    
    if not urls:
        print("❌ 未找到任何 URL")
        return
    
    # 保存所有 URL 到一个文件
    save_urls_to_file(urls)
    
    # 生成提交计划
    batches = split_urls_for_daily_submission(urls)
    
    # 询问是否保存每日批次
    print("=" * 60)
    save_choice = input("是否将每天的 URL 保存到单独文件？(y/N): ").lower().strip()
    if save_choice in ['y', 'yes']:
        print()
        save_daily_batches(batches)
    
    print("=" * 60)
    print("✅ 完成！")
    print("=" * 60)
    print()
    print("📝 下一步操作：")
    print()
    print("1. 打开 Bing URL Submission Tool:")
    print("   🔗 https://www.bing.com/webmasters/url-submission")
    print()
    print("2. 每天复制一组 URL（从上面的计划或 day_X_urls.txt 文件）")
    print()
    print("3. 粘贴到 Bing 提交框，完成验证码，点击 Submit")
    print()
    print("4. 重复直到所有 URL 提交完成")
    print()
    print("💡 提示：")
    print("   - Bing 限制每天最多提交 10 个 URL（无需验证网站）")
    print("   - 建议先提交首页和最重要的页面")
    print("   - 每次提交后等待 24 小时再提交下一批")
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断操作")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")


