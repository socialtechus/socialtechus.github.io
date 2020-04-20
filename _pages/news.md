---
layout: page 
title: News 
description: Updates from the Social Tech Collaborative.
permalink: /news/
---

<div class="container news">
    <div class="row">
        <div class="col-lg-8">
            <h2> Latest </h2>
            {% for news_item in site.news %}
            <h3> {{ news_item.headline }} </h3>
            <p class="text-muted">{{ news_item.date | date: "%m/%d/%Y" }}</p>
            <p>{{ news_item.excerpt | strip_html | truncatewords:25 }}</p>
            {% endfor %}
        </div>
        <div class="col-lg-4"></div>
    </div>
    <div class="row">
        <div class="col-lg-12">
            <hr>
        </div>
    </div>
</div>
        