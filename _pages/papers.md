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
    <li> <a href="{{ blink[0] | prepend: "/papers/" | prepend: base_path }}"><em>{{ link.title }}</em></a>, with {{ link.coauths }}, <br>
      <a href="{{ link.arXiv | prepend: "https://arxiv.org/abs/"}}">arXiv:{{ link.arXiv }}</a> </li>
  {%- endfor -%}
</ul>