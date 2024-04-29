---
layout: archive
title: "Papers"
permalink: /papers/
author_profile: true
---

Here are my preprints, listed in (reverse chronological) order of first upload to arXiv (recentmost first).

{% include base_path %}

<ul>
  {%- for blink in site.data.papers-links -%}
    {%- assign link = blink[1] -%}
    <li> {{ link.title }}, with {{ link.coauths }}, <br>
      <a href={{ link.arXiv | prepend: "https://arxiv.org/abs/"}}>arXiv:{{ link.arXiv }}</a> </li>
  {%- endfor -%}
</ul>