---
layout: archive
title: "Course Notes"
permalink: /course-notes/
author_profile: true
---

{% include base_path %}

# UoU Course Notes

Here are (the links to) the notes for some of the courses I took at (the?) UoU. I mainly put them on my GitHub for the sake of my personal access. Linking them here in case useful to others. Take them with a grain of salt since they have often not been looked at to spot errors.

<ul>
  {%- for blink in site.data.uou-notes-links -%}
    {%- assign link = blink[1] -%}
    <li> 
      <a href="{{ blink[0] | prepend: "/" | prepend: base_path }}">
      {{ link.tit }} ({{ blink[0] }}) </a> 
  </li>
  {%- endfor -%}
</ul>


# IITB Course Notes

Here are (the links to) the notes for some of the courses I took at IITB. A good majority of these are handwritten notes. These typically are self-contained (modulo the prerequisites one would expect to have), containing the proofs and motivations. 

Some of the also have a LaTeX'd set of notes accompanying them. These notes typically just contain the results and definitions and skip many proofs/motivations. The interested reader can then find the proof in the handwritten set of notes.

Lastly, some of these also contain presentations.

As usual, you can find the `.tex` files in [this repository]({{ site.full_link }}){:target="blank"}.

<ul>
  {%- for blink in site.data.notes-links -%}
    {%- assign link = blink[1] -%}
  	<li> 
      <a href="{{ blink[0] | prepend: "/" | prepend: base_path }}">
      {{ link.tit }} ({{ blink[0] }}) </a> 
	</li>
  {%- endfor -%}
</ul>
