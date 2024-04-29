---
layout: archive
title: "Papers"
permalink: /papers/
author_profile: true
---

Here are my preprints, listed in (reverse chronological) order of first upload to arXiv (recentmost first).

{% include base_path %}

<ul>
  {%- for blink in site.papers-links -%}
    {%- assign link = blink[1] -%}
    <li> {{ link.title }} with {{ link.coauths }}, <a href={{ blink[0] | prepend: "https://arxiv.org/abs/"}}>arXiv:{{ blink[0] }}</a>
  </li>
  {%- endfor -%}
</ul>

<!-- {% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
 -->