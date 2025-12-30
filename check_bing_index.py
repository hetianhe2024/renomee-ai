#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查 URL 是否被 Bing 索引
使用方法: python check_bing_index.py [urls_file.txt]
"""

import sys
import io
import requests
import time
from urllib.parse import quote
from pathlib import Path

# Windows 中文显示支持
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_bing_index(url):
    """检查 URL 是否被 Bing 索引"""
    # 使用 url: 搜索（更精确）
    search_query = f"url:{url}"
    search_url = f"https://www.bing.com/search?q={quote(search_query)}"
    
    try:
        response = requests.get(search_url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        
        # 检查响应
        if response.status_code == 200:
            # 如果响应中包含 URL 和没有 "no results" 字样，可能已索引
            text_lower = response.text.lower()
            
            if 'no results found' in text_lower or 'did not match any documents' in text_lower:
                return False, "❌ 未索引"
            elif url.lower() in text_lower or url.replace('https://', '').lower() in text_lower:
                return True, "✅ 已索引"
            else:
                return None, "⚠️ 无法确定"
        else:
            return None, f"⚠️ 请求失败 (HTTP {response.status_code})"
            
    except Exception as e:
        return None, f"⚠️ 检查失败: {str(e)[:50]}"

def check_site_indexed(domain):
    """检查整个网站是否被索引（使用 site: 搜索）"""
    search_query = f"site:{domain}"
    search_url = f"https://www.bing.com/search?q={quote(search_query)}"
    
    try:
        response = requests.get(search_url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            text_lower = response.text.lower()
            if 'no results found' in text_lower:
                return False, 0
            else:
                # 尝试提取结果数量（简单方法）
                return True, "有结果"
        else:
            return None, "检查失败"
            
    except Exception as e:
        return None, f"检查失败: {e}"

def main():
    print("=" * 60)
    print("Bing 索引状态检查工具")
    print("=" * 60)
    print()
    
    # 获取 URL 列表
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("请输入 URL 列表文件名（默认: wix_urls.txt）: ").strip()
        if not filename:
            filename = 'wix_urls.txt'
    
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"❌ 文件不存在: {filename}")
        print()
        print("你可以:")
        print("1. 手动创建文件并添加 URL（每行一个）")
        print("2. 运行 extract_wix_urls.py 生成 URL 列表")
        return
    
    # 读取 URL
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        return
    
    if not urls:
        print("❌ 文件中没有有效的 URL")
        return
    
    print(f"📂 从 {filename} 读取了 {len(urls)} 个 URL")
    print()
    
    # 首先检查整个网站是否被索引
    if urls:
        # 提取域名
        first_url = urls[0]
        if '://' in first_url:
            domain_part = first_url.split('://')[1].split('/')[0]
            print(f"🔍 首先检查整个网站是否被 Bing 索引...")
            print(f"   域名: {domain_part}")
            indexed, result = check_site_indexed(domain_part)
            
            if indexed:
                print(f"   ✅ 网站已被索引！")
            elif indexed is False:
                print(f"   ❌ 网站尚未被 Bing 索引")
                print(f"   💡 建议：先提交主要页面到 Bing URL Submission Tool")
            else:
                print(f"   ⚠️ 无法确定网站索引状态")
            
            print()
            time.sleep(3)  # 避免请求过快
    
    # 询问是否继续检查每个 URL
    print("⏱️  逐个检查 URL 需要较长时间（每个 URL 约 3-5 秒）")
    check_choice = input(f"是否继续检查所有 {len(urls)} 个 URL？(y/N): ").lower().strip()
    
    if check_choice not in ['y', 'yes']:
        print("\n✅ 已取消详细检查")
        return
    
    print()
    print(f"正在检查 {len(urls)} 个 URL...")
    print("=" * 60)
    print()
    
    indexed_count = 0
    not_indexed_count = 0
    unknown_count = 0
    
    results = []
    
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        indexed, status = check_bing_index(url)
        print(f"        {status}")
        
        results.append((url, indexed, status))
        
        if indexed:
            indexed_count += 1
        elif indexed is False:
            not_indexed_count += 1
        else:
            unknown_count += 1
        
        # 避免请求过快（重要！）
        if i < len(urls):
            time.sleep(3)  # 每次请求间隔 3 秒
    
    print()
    print("=" * 60)
    print("检查完成！")
    print("=" * 60)
    print()
    print(f"📊 统计结果:")
    print(f"   ✅ 已索引:    {indexed_count:3d} 个 ({indexed_count/len(urls)*100:.1f}%)")
    print(f"   ❌ 未索引:    {not_indexed_count:3d} 个 ({not_indexed_count/len(urls)*100:.1f}%)")
    print(f"   ⚠️  无法确定:  {unknown_count:3d} 个 ({unknown_count/len(urls)*100:.1f}%)")
    print(f"   📝 总计:      {len(urls):3d} 个")
    print()
    
    # 保存结果
    save_choice = input("是否保存详细结果到文件？(y/N): ").lower().strip()
    if save_choice in ['y', 'yes']:
        result_file = 'bing_index_results.txt'
        with open(result_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("Bing 索引状态检查结果\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("已索引的 URL:\n")
            f.write("-" * 60 + "\n")
            for url, indexed, status in results:
                if indexed:
                    f.write(f"{url}\n")
            f.write("\n")
            
            f.write("未索引的 URL:\n")
            f.write("-" * 60 + "\n")
            for url, indexed, status in results:
                if indexed is False:
                    f.write(f"{url}\n")
            f.write("\n")
            
            f.write("无法确定的 URL:\n")
            f.write("-" * 60 + "\n")
            for url, indexed, status in results:
                if indexed is None:
                    f.write(f"{url} - {status}\n")
            f.write("\n")
            
            f.write("=" * 60 + "\n")
            f.write(f"统计: 已索引 {indexed_count}, 未索引 {not_indexed_count}, 无法确定 {unknown_count}\n")
        
        print(f"\n✅ 结果已保存到: {result_file}")
    
    print()
    print("💡 建议:")
    if not_indexed_count > 0:
        print(f"   - 未索引的 {not_indexed_count} 个 URL 需要提交到 Bing")
        print(f"   - 使用 Bing URL Submission Tool: https://www.bing.com/webmasters/url-submission")
        print(f"   - 每天最多提交 10 个 URL")
    
    if indexed_count > 0:
        print(f"   - 已有 {indexed_count} 个页面被索引，继续保持更新！")
    
    if indexed_count == 0 and not_indexed_count > 0:
        print(f"   - 网站可能是新站，需要耐心等待（通常 1-3 周）")
        print(f"   - 建议定期更新内容，保持活跃")
    
    print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  用户中断操作")
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()


