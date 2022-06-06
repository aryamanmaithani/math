---
layout: archive
title: "Presentations"
permalink: /presentations/
author_profile: true
---

{% include base_path %}

Below are (the links to) the presentations I made during various reading projects and courses. 

<ul>
  {%- for blink in site.data.presentations-links -%}
    {%- assign link = blink[1] -%}
  	<li> 
      <a href="{{ blink[0] | prepend: "/" | prepend: base_path }}">
      {{ link.tit }}</a> 
      {% if link.desc %}<br> {{ link.desc }} {% endif %}
	</li>
  {%- endfor -%}
</ul>