#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动提交所有URL到Bing IndexNow
"""

import json
import requests
import sys
import io
from pathlib import Path

# 设置标准输出编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 配置
API_KEY = '7c9c6ea4c8f14b0e8febadcdbd11d73b'
HOST = 'hetianhe2024.github.io'
BASE_PATH = '/renomee-ai'
KEY_LOCATION = f'https://{HOST}{BASE_PATH}/{API_KEY}.txt'
API_ENDPOINT = 'https://api.indexnow.org/IndexNow'

# 所有要提交的URL
ALL_URLS = [
    # 主要页面
    f'https://{HOST}{BASE_PATH}/',
    f'https://{HOST}{BASE_PATH}/about/',
    f'https://{HOST}{BASE_PATH}/categories/',
    f'https://{HOST}{BASE_PATH}/archive/',
    # 文章页面
    f'https://{HOST}{BASE_PATH}/posts/welcome/',
    f'https://{HOST}{BASE_PATH}/posts/renomee-ai-goodbye-regex/',
    f'https://{HOST}{BASE_PATH}/posts/didafix-affordable-image-tools/',
]

def submit_urls(urls):
    """提交URL到IndexNow"""
    request_data = {
        'host': HOST,
        'key': API_KEY,
        'keyLocation': KEY_LOCATION,
        'urlList': urls
    }
    
    print("=" * 70)
    print("🚀 Bing IndexNow 批量提交")
    print("=" * 70)
    print()
    print(f"📊 准备提交 {len(urls)} 个URL:")
    for i, url in enumerate(urls, 1):
        print(f"  {i}. {url}")
    print()
    
    try:
        print("📡 正在发送请求...")
        response = requests.post(
            API_ENDPOINT,
            headers={'Content-Type': 'application/json; charset=utf-8'},
            json=request_data,
            timeout=30
        )
        
        print(f"响应状态码: {response.status_code}")
        print()
        
        if response.ok:
            print("=" * 70)
            print("✅ 提交成功！")
            print("=" * 70)
            print()
            print("📝 已提交的URL:")
            for i, url in enumerate(urls, 1):
                print(f"  {i}. {url}")
            print()
            print("📌 重要说明:")
            print("  1. Bing已接收你的提交请求")
            print("  2. IndexNow页面可能不会显示提交记录（这是正常的）")
            print("  3. 索引需要时间，通常需要1-7天")
            print("  4. 在Bing站长工具查看索引状态:")
            print("     https://www.bing.com/webmasters")
            print()
            print("🔍 验证索引:")
            print(f"  几天后在Bing搜索: site:{HOST}{BASE_PATH}")
            print()
            return True
        else:
            error_messages = {
                400: "请求格式无效",
                403: "API密钥无效或未找到验证文件",
                422: "URL不属于指定域名或格式不匹配",
                429: "请求频率过高，请稍后再试"
            }
            error_msg = error_messages.get(response.status_code, f"未知错误: HTTP {response.status_code}")
            print(f"❌ 提交失败: {error_msg}")
            if response.text:
                print(f"响应内容: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return False

if __name__ == '__main__':
    success = submit_urls(ALL_URLS)
    sys.exit(0 if success else 1)

