---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: true
---

{% include base_path %}

Below are (the links to) the slides/notes for various talks.

## Graduate

* [Classical Invariant Theory]({{base_path}}/talks/2024-04-22-utah-rep-theory-invariants.pdf), a short course presentation for my Representation Theory course
* I gave two (slightly different) talks about [my work](https://arxiv.org/pdf/2401.01046) with H. Ananthnarayan and Omkar Javadekar
  * [The version at the commutative algebra seminar at the University of Utah]({{base_path}}/talks/2024-03-29-utah-ca-linear-quotients.pdf)
  * [The version at BIKES, the student commutative algebra seminar at the University of Utah]({{base_path}}/talks/2024-02-15-bikes-linear-quotients.pdf)
* [Gorenstein Rings]({{base_path}}/talks/2023-05-19-icts-gorenstein.pdf), a preparatory lecture at the program [_Dualities in Topology and Algebra_](https://www.icts.res.in/program/dta2023) that happened in [ICTS, Bangalore](https://www.icts.res.in/)

## Undergraduate

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