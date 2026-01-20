---
layout: home
title: "Renomee AI - 让工作更高效的智能工具"
description: "Renomee AI博客分享实用在线工具和技术文章,包括AI驱动的图片编辑工具和智能文件重命名工具,帮助提升工作效率。"
sitemap: true
---

<div class="hero-section">
  <h1>🚀 让工作更高效的智能工具</h1>
  <p class="lead">用AI技术简化日常工作，告别繁琐操作，让效率提升10倍</p>
</div>

## ⭐ 精选工具

<div class="tools-grid">
  <div class="tool-card">
    <div class="tool-icon">🖼️</div>
    <h3>滴答修 - 图片编辑工具</h3>
    <p>AI智能抠图、格式转换、压缩优化、去水印等9大功能</p>
    <ul>
      <li>按次计费，0.2-0.3元/次</li>
      <li>无需订阅，用多少付多少</li>
      <li>比传统工具便宜99%</li>
    </ul>
    <a href="https://xiaojingxiu.com" class="btn-primary" target="_blank">立即体验 →</a>
  </div>
  
  <div class="tool-card">
    <div class="tool-icon">📝</div>
    <h3>Renomee AI - 文件重命名</h3>
    <p>告别正则表达式，用自然语言描述重命名需求</p>
    <ul>
      <li>零学习成本，会说话就会用</li>
      <li>AI智能识别文件内容</li>
      <li>预览确认，安全可靠</li>
    </ul>
    <a href="https://xiaojingjia.top" class="btn-primary" target="_blank">立即下载 →</a>
  </div>
</div>

## 📚 最新文章

<div class="posts-list">
  <!-- 文章列表会自动显示在这里 -->
</div>

## 🔗 友情链接

<div class="blogroll-section">
  <p class="blogroll-intro">发现更多优质内容，与志同道合的博主一起交流学习</p>
  
  <div class="blogroll-list">
    {% for link in site.data.blogroll.links %}
    <div class="blogroll-item">
      <h3>
        <a href="{{ link.url }}" target="_blank" rel="noopener noreferrer nofollow">
          {{ link.name }} ↗
        </a>
      </h3>
      <p class="blogroll-description">{{ link.description }}</p>
      <div class="blogroll-tags">
        {% for tag in link.tags %}
        <span class="tag">{{ tag }}</span>
        {% endfor %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

