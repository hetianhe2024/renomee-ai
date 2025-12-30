---
layout: page
title: 归档
permalink: /archive/
description: 按时间查看所有博客文章
sitemap: true
---

<div class="archive-page">
  {% assign postsByYear = site.posts | group_by_exp:"post", "post.date | date: '%Y'" %}
  
  <div class="archive-summary">
    <p class="archive-stats">
      📝 共有 <strong>{{ site.posts.size }}</strong> 篇文章
    </p>
  </div>
  
  {% for year in postsByYear %}
    <div class="archive-year">
      <h2 class="year-heading">
        <span class="year-number">{{ year.name }}</span>
        <span class="year-count">{{ year.items.size }} 篇</span>
      </h2>
      
      {% assign postsByMonth = year.items | group_by_exp:"post", "post.date | date: '%m'" %}
      
      {% for month in postsByMonth %}
        <div class="archive-month">
          <h3 class="month-heading">{{ month.items[0].date | date: "%m月" }}</h3>
          
          <ul class="archive-posts">
            {% for post in month.items %}
              <li class="archive-post">
                <time datetime="{{ post.date | date_to_xmlschema }}">
                  {{ post.date | date: "%d日" }}
                </time>
                <div class="post-info">
                  <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
                  {% if post.description %}
                    <p class="post-desc">{{ post.description | truncate: 100 }}</p>
                  {% endif %}
                  {% if post.categories %}
                    <div class="post-cats">
                      {% for category in post.categories %}
                        <span class="cat-tag">{{ category }}</span>
                      {% endfor %}
                    </div>
                  {% endif %}
                </div>
              </li>
            {% endfor %}
          </ul>
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>

<style>
.archive-page {
  max-width: 900px;
  margin: 0 auto;
}

.archive-summary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 0.75rem;
  margin-bottom: 3rem;
  text-align: center;
}

.archive-stats {
  font-size: 1.25rem;
  margin: 0;
}

.archive-year {
  margin-bottom: 3rem;
}

.year-heading {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  color: #1e293b;
  border-bottom: 3px solid #2563eb;
  padding-bottom: 0.75rem;
  margin-bottom: 2rem;
}

.year-number {
  font-size: 2rem;
  font-weight: 800;
}

.year-count {
  color: #64748b;
  font-size: 1rem;
  font-weight: 400;
}

.archive-month {
  margin-bottom: 2.5rem;
  margin-left: 2rem;
}

.month-heading {
  color: #475569;
  font-size: 1.25rem;
  margin-bottom: 1rem;
  padding-left: 1rem;
  border-left: 3px solid #cbd5e1;
}

.archive-posts {
  list-style: none;
  padding: 0;
}

.archive-post {
  display: flex;
  gap: 1.5rem;
  padding: 1rem;
  margin-bottom: 1rem;
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 0.5rem;
  transition: all 0.3s;
}

.archive-post:hover {
  box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  transform: translateX(5px);
}

.archive-post time {
  color: #94a3b8;
  font-weight: 600;
  min-width: 3rem;
  padding-top: 0.25rem;
}

.post-info {
  flex: 1;
}

.post-info a {
  color: #1e293b;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.1rem;
  display: block;
  margin-bottom: 0.5rem;
}

.post-info a:hover {
  color: #2563eb;
}

.post-desc {
  color: #64748b;
  font-size: 0.9rem;
  margin: 0.5rem 0;
  line-height: 1.5;
}

.post-cats {
  margin-top: 0.5rem;
}

.cat-tag {
  display: inline-block;
  background: #f1f5f9;
  color: #64748b;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  margin-right: 0.5rem;
}

@media (max-width: 768px) {
  .archive-post {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .archive-month {
    margin-left: 0;
  }
}
</style>

