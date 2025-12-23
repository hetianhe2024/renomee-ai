# Bing 提交快速开始 🚀

只需 3 步，让 Bing 索引你的博客！

## ⚡ 快速步骤

### 第 1 步：安装依赖

```bash
pip install requests
```

### 第 2 步：首次运行生成密钥

```bash
python submit_to_bing.py
```

脚本会生成类似 `a1b2c3d4e5f6g7h8.txt` 的验证文件。

### 第 3 步：提交验证文件到 GitHub

```bash
# 添加生成的验证文件（文件名会不同）
git add a1b2c3d4e5f6g7h8.txt

# 提交
git commit -m "Add Bing verification file"

# 推送
git push origin main
```

### 第 4 步：等待部署完成后重新运行

等待 GitHub Pages 部署完成（通常 1-3 分钟），然后再次运行：

```bash
python submit_to_bing.py
```

选择 `1` 提交默认重要页面，或选择 `2` 提交所有URL。

---

## ✅ 完成！

查看提交结果：
- 访问 [Bing Webmaster Tools](https://www.bing.com/webmasters)
- 通常需要几天时间才能在搜索结果中看到

## 📖 详细说明

查看 [BING-SUBMIT-GUIDE.md](BING-SUBMIT-GUIDE.md) 了解更多信息。

## 💡 提示

- 每次发布新文章后运行脚本提交新URL
- 不要在24小时内重复提交相同URL
- 验证文件必须在网站根目录可访问

