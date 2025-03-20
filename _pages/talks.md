---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: true
redirect_from:
  - /presentations
---

{% include base_path %}

Below are (the links to) the slides/notes for various talks.

* [Polynomial invariants of \\(\operatorname{GL}_{2}\\): Conjugation over finite fields](conjugation-GL2.pdf), a talk at the [UoU CA Seminar](https://www.math.utah.edu/caseminar/) and the [UCSD Algebra seminar](https://mathweb.ucsd.edu/~asalehig/AlgebraSeminar-24.html), about [my paper with the same-ish name](https://arxiv.org/abs/2501.15080)
* Evil rings, a talk at [BIKES](https://www.brendan.phd/BIKES/BIKES.html): [Full slides](2024-08-28-bikes-evil-rings.pdf), [Handout](2024-08-28-bikes-evil-rings-handout.pdf)
* [Invariant Theory of Commutative Rings]({{base_path}}/talks/2024-08-13-iitb-invariant-theory.pdf), a talk at the IITB commutative algebra seminar 
* [Classical Invariant Theory]({{base_path}}/talks/2024-04-22-utah-rep-theory-invariants.pdf), a short course presentation for my Representation Theory course
* I gave two (slightly different) talks about [my work](https://arxiv.org/pdf/2401.01046) with H. Ananthnarayan and Omkar Javadekar
  * [The version at the commutative algebra seminar at the University of Utah]({{base_path}}/talks/2024-03-29-utah-ca-linear-quotients.pdf)
  * [The version at BIKES, the student commutative algebra seminar at the University of Utah]({{base_path}}/talks/2024-02-15-bikes-linear-quotients.pdf)
* [Gorenstein Rings]({{base_path}}/talks/2023-05-19-icts-gorenstein.pdf), a preparatory lecture at the program [_Dualities in Topology and Algebra_](https://www.icts.res.in/program/dta2023) that happened in [ICTS, Bangalore](https://www.icts.res.in/)

## Undergraduate days

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