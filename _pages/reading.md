---
layout: archive
title: "Reading"
excerpt: "Notes of reading projects"
permalink: /reading/
author_profile: true
---

{% include base_path %}

Below are (the links to) the notes I made during various reading projects. 

<ul>
  {%- for blink in site.data.reading-links -%}
    {%- assign link = blink[1] -%}
  	<li> 
      <a href="{{ blink[0] | prepend: "/" | prepend: base_path }}">
      {{ link.tit }}</a> 
	</li>
  {%- endfor -%}
</ul>