# 隐藏说明文档配置

## 已完成的配置

在 `_config.yml` 中添加了两个配置项：

### 1. exclude（排除文件）

```yaml
exclude:
  - GIT-GUIDE.md
  - OPTIMIZATION.md
  - QUICKSTART.md
  - URL-OPTIMIZATION.md
  - URL-OPTIMIZATION-SUMMARY.md
  - README.md
  - Gemfile
  - Gemfile.lock
  - vendor/
```

这些文件将不会被 Jekyll 构建，不会出现在网站中。

### 2. header_pages（导航菜单）

```yaml
header_pages:
  - index.md
  - about.md
  - categories.md
  - archive.md
```

只有这4个页面会出现在导航菜单中。

## 网站结构

### 对外可见的页面

- **首页** (`/`) - 展示工具和最新文章
- **关于** (`/about/`) - 关于我们和产品介绍
- **分类** (`/categories/`) - 按分类浏览文章
- **归档** (`/archive/`) - 按时间浏览文章
- **文章页面** (`/posts/文章标题/`) - 所有博客文章

### 技术文件（对外可见，但不在导航中）

- `robots.txt` - 搜索引擎爬虫规则
- `sitemap.xml` - 网站地图
- `BingSiteAuth.xml` - 必应站长验证

### 隐藏的说明文档（不构建）

- `GIT-GUIDE.md` - Git 操作指南
- `OPTIMIZATION.md` - 优化说明
- `QUICKSTART.md` - 快速开始
- `URL-OPTIMIZATION.md` - URL 优化详解
- `URL-OPTIMIZATION-SUMMARY.md` - URL 优化总结
- `README.md` - 项目说明

这些文档只在 GitHub 仓库中可见，供您自己参考使用，不会出现在博客网站上。

## 测试

重启 Jekyll 服务器查看效果：

```bash
bundle exec jekyll clean
bundle exec jekyll serve
```

导航菜单中应该只显示：
- 首页
- 关于
- 分类
- 归档

那些说明文档不会再出现在网站中。

