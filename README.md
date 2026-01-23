# Renomee AI 博客

🚀 基于 Jekyll 构建的现代化博客网站，分享实用工具和技术文章。

## 📖 关于

Renomee AI 致力于用 AI 技术让日常工作变得更简单、更高效。我们开发了多款实用工具产品：

- **滴答修**（xiaojingxiu.com）- 按次计费的图片处理工具
- **Renomee AI**（renomeeai.com）- AI 驱动的文件重命名工具

## ✨ 博客特性

- 🎨 现代化、响应式设计
- 📱 移动端完美适配
- 🔍 SEO 优化
- 📚 文章分类和归档
- 🏷️ 标签系统
- 🔗 社交分享功能
- 🌓 深色模式支持
- ⚡ 快速加载

## 🛠️ 技术栈

- Jekyll 4.x
- GitHub Pages
- Minima 主题（自定义增强）
- 响应式 CSS
- SEO 插件

## 🚀 本地运行

### 前提条件

- Ruby 2.7+
- Bundler

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/hetianhe2024/renomee-ai.git
cd renomee-ai

# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000/renomee-ai
```

## 📝 发布新文章

1. 在 `_posts` 目录下创建新文件，命名格式：`YYYY-MM-DD-title.md`
2. 添加 Front Matter：

```yaml
---
layout: post
title: "文章标题"
date: 2025-01-20
categories: [分类1, 分类2]
tags: [标签1, 标签2]
description: "文章描述，用于 SEO"
---
```

3. 编写 Markdown 内容
4. 提交并推送到 GitHub

## 📂 项目结构

```
renomee-ai/
├── _posts/              # 博客文章
├── _layouts/            # 页面布局
│   ├── home.html       # 首页布局
│   └── post.html       # 文章布局
├── _includes/           # 可复用组件
│   └── share-buttons.html
├── _data/              # 数据文件
│   └── navigation.yml  # 导航配置
├── assets/
│   └── css/
│       └── style.scss  # 自定义样式
├── _config.yml         # 网站配置
├── index.md            # 首页
├── about.md            # 关于页面
├── categories.md       # 分类页面
├── archive.md          # 归档页面
└── README.md
```

## 🎨 自定义样式

博客使用自定义 CSS 增强了默认的 Minima 主题：

- 渐变色 Hero 区域
- 工具卡片展示
- 优化的文章列表
- 美化的代码块
- 改进的表格样式
- 社交分享按钮

所有样式都在 `assets/css/style.scss` 中定义。

## 🔧 配置

主要配置在 `_config.yml` 中：

```yaml
title: Renomee AI 博客
description: 分享实用在线工具和技术文章
url: "https://hetianhe2024.github.io"
baseurl: "/renomee-ai"
```

## 📱 页面

- **首页** (`/`) - 展示工具和最新文章
- **关于** (`/about/`) - 团队和产品介绍
- **分类** (`/categories/`) - 按分类浏览文章
- **归档** (`/archive/`) - 按时间浏览文章

## 🌐 部署

本站自动部署到 GitHub Pages：

1. 推送代码到 `main` 分支
2. GitHub Actions 自动构建
3. 发布到 https://hetianhe2024.github.io/renomee-ai

## 📊 SEO 优化

- 使用 `jekyll-seo-tag` 插件
- 每篇文章都有 meta description
- 生成 sitemap.xml
- 配置 robots.txt
- 结构化数据标记

## 📮 联系方式

- 邮箱：hetianhe2009@163.com
- 滴答修官网：https://xiaojingxiu.com
- Renomee AI官网：https://renomeeai.com

## 📄 许可证

本项目仅供学习和个人使用。

---

💡 如有问题或建议，欢迎提 Issue 或 PR！