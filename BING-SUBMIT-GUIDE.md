# Bing 站长工具提交指南

本指南说明如何使用 `submit_to_bing.py` 脚本将博客URL提交到 Bing 搜索引擎。

## 📋 准备工作

### 1. 安装依赖

```bash
pip install requests
```

### 2. 首次运行

第一次运行脚本时，会自动生成 API 密钥和验证文件：

```bash
python submit_to_bing.py
```

脚本会生成两个文件：
- `bing_api_key.txt` - 保存API密钥（本地使用，不要提交到Git）
- `<api_key>.txt` - 验证文件（需要提交到GitHub）

### 3. 提交验证文件到 GitHub

**重要：** 必须将验证文件提交到GitHub仓库根目录，Bing才能验证你的所有权。

```bash
# 将生成的验证文件添加到Git
git add <api_key>.txt

# 提交
git commit -m "Add Bing IndexNow verification file"

# 推送到GitHub
git push origin main
```

### 4. 等待部署

GitHub Pages 部署完成后，验证文件会在以下地址可访问：
```
https://hetianhe2024.github.io/renomee-ai/<api_key>.txt
```

在浏览器中访问这个URL，确保能看到API密钥内容。

## 🚀 使用方法

### 方式 1: 提交默认重要页面（推荐首次使用）

```bash
python submit_to_bing.py
```

然后选择 `1`，会提交以下页面：
- 首页
- 关于页面
- 分类页面
- 归档页面

### 方式 2: 从 sitemap.xml 提交所有URL

```bash
python submit_to_bing.py --sitemap
```

或交互式选择 `2`

这会读取 `sitemap.xml` 中的所有URL并提交。

### 方式 3: 从自定义文件提交

```bash
python submit_to_bing.py urls.txt
```

或交互式选择 `3`，然后输入文件名。

## 📝 URL列表文件格式

创建一个文本文件（如 `urls.txt`），每行一个URL：

```txt
# 这是注释行，会被忽略

# 主要页面
https://hetianhe2024.github.io/renomee-ai/
https://hetianhe2024.github.io/renomee-ai/about/

# 文章页面
https://hetianhe2024.github.io/renomee-ai/posts/welcome/
https://hetianhe2024.github.io/renomee-ai/posts/didafix-affordable-image-tools/
```

## 🔍 验证提交结果

### 1. 检查脚本输出

成功提交会显示：
```
✅ 成功提交 X 个URL到Bing IndexNow!
```

### 2. 访问 Bing Webmaster Tools

访问 [Bing Webmaster Tools](https://www.bing.com/webmasters) 查看索引状态。

**注意：** 索引需要时间，通常需要几天到几周才能在搜索结果中看到。

## ⚠️ 常见问题

### Q1: 提示 "403 API密钥无效或未找到密钥文件"

**原因：** 验证文件未成功部署或URL不正确

**解决方法：**
1. 确认验证文件已提交到GitHub
2. 确认GitHub Pages已成功部署
3. 在浏览器中访问验证文件URL，确保可以访问
4. 等待几分钟后重试

### Q2: 提示 "422 URL不属于指定域名"

**原因：** 提交的URL格式不正确

**解决方法：**
1. 确保URL以 `https://hetianhe2024.github.io/renomee-ai/` 开头
2. 检查 `_config.yml` 中的 `baseurl` 和 `url` 配置

### Q3: 提示 "429 请求频率过高"

**原因：** 短时间内提交过多次

**解决方法：**
- 等待至少 1 小时后再次提交
- Bing限制每个URL每天只能提交一次

### Q4: 如何知道是否已被索引？

在 Bing 搜索框输入：
```
site:hetianhe2024.github.io/renomee-ai
```

查看收录的页面数量。

## 📅 建议提交频率

- **新博客启动：** 首次提交所有重要页面
- **发布新文章：** 每次发布新文章后提交新URL
- **更新内容：** 重大内容更新后可重新提交
- **避免频繁提交：** 同一URL不要在24小时内重复提交

## 🔧 高级用法

### 只提交最新文章

创建 `latest_posts.txt`，只包含新发布的文章URL：

```txt
https://hetianhe2024.github.io/renomee-ai/posts/new-article/
```

然后运行：
```bash
python submit_to_bing.py latest_posts.txt
```

### 批量提交

如果文章很多，建议分批提交：

```bash
# 第一批：主要页面
python submit_to_bing.py  # 选择方式1

# 第二批：文章页面（等待1小时后）
python submit_to_bing.py urls.txt
```

## 📚 相关资源

- [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [IndexNow 协议说明](https://www.indexnow.org/)
- [Bing IndexNow 官方文档](https://www.bing.com/indexnow)

## 🆘 获取帮助

如果遇到问题：
1. 检查本文档的"常见问题"部分
2. 查看脚本输出的错误信息
3. 访问 Bing Webmaster Tools 查看详细诊断信息

---

**提示：** 将 `bing_api_key.txt` 添加到 `.gitignore`，避免将密钥提交到公开仓库。

