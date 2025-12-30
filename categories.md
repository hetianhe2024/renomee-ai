---
layout: page
title: 分类
permalink: /categories/
description: 按主题浏览博客文章
sitemap: true
---

<div class="categories-page">
  {% assign categories = site.categories | sort %}
  
  <div class="categories-grid">
    {% for category in categories %}
      <div class="category-card">
        <h3>{{ category[0] }}</h3>
        <p class="category-count">{{ category[1].size }} 篇文章</p>
        <ul class="category-posts">
          {% for post in category[1] limit:5 %}
            <li>
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              <time>{{ post.date | date: "%Y-%m-%d" }}</time>
            </li>
          {% endfor %}
        </ul>
        {% if category[1].size > 5 %}
          <a href="#{{ category[0] | slugify }}" class="view-all">查看全部 →</a>
        {% endif %}
      </div>
    {% endfor %}
  </div>
  
  <div class="categories-detail">
    <h2>所有文章</h2>
    {% for category in categories %}
      <div class="category-section" id="{{ category[0] | slugify }}">
        <h3>📁 {{ category[0] }}</h3>
        <ul class="post-list-simple">
          {% for post in category[1] %}
            <li>
              <time>{{ post.date | date: "%Y-%m-%d" }}</time>
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </li>
          {% endfor %}
        </ul>
      </div>
    {% endfor %}
  </div>
</div>

<style>
.categories-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.category-card {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 0.75rem;
  padding: 1.5rem;
  transition: all 0.3s;
}

.category-card:hover {
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);
  transform: translateY(-2px);
}

.category-card h3 {
  color: #1e293b;
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
}

.category-count {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.category-posts {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
}

.category-posts li {
  margin-bottom: 0.75rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.category-posts a {
  color: #2563eb;
  text-decoration: none;
  font-size: 0.95rem;
}

.category-posts a:hover {
  text-decoration: underline;
}

.category-posts time {
  color: #94a3b8;
  font-size: 0.85rem;
}

.view-all {
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
}

.categories-detail {
  margin-top: 4rem;
}

.category-section {
  margin-bottom: 3rem;
}

.category-section h3 {
  color: #1e293b;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 0.5rem;
  margin-bottom: 1rem;
}

.post-list-simple {
  list-style: none;
  padding: 0;
}

.post-list-simple li {
  padding: 0.75rem 0;
  border-bottom: 1px solid #f1f5f9;
  display: flex;
  gap: 1rem;
  align-items: baseline;
}

.post-list-simple time {
  color: #94a3b8;
  font-size: 0.9rem;
  min-width: 6rem;
}

.post-list-simple a {
  color: #334155;
  text-decoration: none;
  flex: 1;
}

.post-list-simple a:hover {
  color: #2563eb;
}
</style>

