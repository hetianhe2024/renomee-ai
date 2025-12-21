# 快速启动指南

## 📦 首次使用

### 1. 安装依赖

```bash
bundle install
```

### 2. 启动本地服务器

```bash
bundle exec jekyll serve
```

或者使用增量构建（更快）：

```bash
bundle exec jekyll serve --incremental
```

### 3. 访问网站

打开浏览器访问：http://localhost:4000/renomee-ai

## 🔧 常用命令

### 构建网站
```bash
bundle exec jekyll build
```

### 清理缓存
```bash
bundle exec jekyll clean
```

### 查看草稿
```bash
bundle exec jekyll serve --drafts
```

### 指定端口
```bash
bundle exec jekyll serve --port 4001
```

## 📝 发布新文章

1. 在 `_posts` 目录创建文件：`YYYY-MM-DD-title.md`

2. 添加 Front Matter：

```yaml
---
layout: post
title: "文章标题"
date: 2025-01-20
categories: [分类1, 分类2]
tags: [标签1, 标签2, 标签3]
description: "文章描述（用于 SEO）"
image: /assets/images/cover.jpg  # 可选
---
```

3. 编写 Markdown 内容

4. 本地预览确认无误

5. 提交到 Git

## 🚀 部署到 GitHub Pages

### 方法 1: 通过 Git 推送（推荐）

```bash
git add .
git commit -m "更新博客内容"
git push origin main
```

GitHub Pages 会自动构建和部署。

### 方法 2: 手动上传

1. 构建网站：`bundle exec jekyll build`
2. 将 `_site` 目录内容上传到 GitHub

## ✅ 部署前检查

- [ ] 本地测试运行正常
- [ ] 所有链接可访问
- [ ] 图片正常显示
- [ ] 移动端显示正常
- [ ] 没有 404 错误
- [ ] sitemap.xml 更新
- [ ] 配置文件正确

## 🐛 常见问题

### 1. 依赖安装失败

```bash
# 更新 Bundler
gem install bundler

# 清理并重新安装
bundle clean --force
bundle install
```

### 2. 服务器启动失败

```bash
# 检查端口占用
# Windows
netstat -ano | findstr :4000

# 杀死进程或使用其他端口
bundle exec jekyll serve --port 4001
```

### 3. 样式不显示

检查 `_config.yml` 中的 `baseurl` 配置是否正确：
```yaml
baseurl: "/renomee-ai"  # 不要有结尾的斜杠
```

### 4. 文章 URL 结构

本博客已配置简化的 URL 结构：
```yaml
permalink: /posts/:title/
```

文章 URL 示例：
- ❌ 旧格式：`/分类1/分类2/2025/01/20/文章标题.html`
- ✅ 新格式：`/posts/文章标题/`

更简洁、更容易记忆！

### 5. 构建警告

忽略这些警告是安全的：
- Deprecation warnings
- Plugin warnings（如果使用 GitHub Pages）

## 📂 文件结构

```
renomee-ai/
├── _config.yml          # 网站配置
├── _data/              # 数据文件
├── _includes/          # 可复用组件
├── _layouts/           # 页面布局
├── _posts/             # 博客文章
├── assets/             # 静态资源
│   ├── css/           # 样式文件
│   └── images/        # 图片（需创建）
├── index.md            # 首页
├── about.md            # 关于页
├── categories.md       # 分类页
├── archive.md          # 归档页
└── 404.html            # 错误页
```

## 🎨 自定义

### 修改主色调

编辑 `assets/css/style.scss`：

```scss
:root {
  --primary-color: #2563eb;  // 修改为你的品牌色
  --primary-hover: #1d4ed8;
}
```

### 修改 Hero 背景

在 `assets/css/style.scss` 中找到 `.hero-section`：

```scss
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  // 改为你喜欢的渐变色
}
```

### 添加 Logo

1. 将 logo.png 放到 `assets/images/`
2. 在 `_config.yml` 中配置：
```yaml
logo: /assets/images/logo.png
```

## 📊 添加统计

### Google Analytics

在 `_config.yml` 添加：
```yaml
google_analytics: UA-XXXXXXXX-X
```

### 百度统计

在 `_config.yml` 添加：
```yaml
baidu_analytics: your_baidu_id
```

然后在 `_includes/head-custom.html` 中添加相应的跟踪代码。

## 💬 添加评论

### 使用 Utterances（推荐）

1. 在 GitHub 仓库安装 Utterances App
2. 创建 `_includes/comments.html`
3. 在文章布局中引入

## 🔄 更新主题

```bash
bundle update
```

## 📞 获取帮助

- 查看 Jekyll 文档：https://jekyllrb.com/docs/
- 查看 GitHub Pages 文档：https://docs.github.com/pages
- 查看本项目 OPTIMIZATION.md

---

享受博客写作！🎉

