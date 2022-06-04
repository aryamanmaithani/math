--- 
layout: page
title: Math
image: /img/avatar-icon.png
light-image: /img/avatar-icon-light.png
---

Hi, here's where I post (links to) the math stuff that I've written.  
With all my $$\LaTeX$$'d files, I also upload the source `.tex` code.  
To view those, you can go to the appropriate folder that you may find [here](https://github.com/aryamanmaithani/math). (Mostly, just changing the `.pdf` to `.tex` in the URL works as well but sometimes I have split the document into many `.tex` files.)

# Reports and Presentations

<ul>
    {%- for blink in site.data.math-links -%}
        {%- assign link = blink[1] -%}
        <li>
          <a href="/math{{ blink[0] | relative_url }}">
          <h2 class="post-title">{{ link.tit }}</h2>
          </a><br>
          {%- if link.desc -%}
          <div class="post-entry-container">
            <div class="post-entry">
              <a href="/math{{ blink[0] | relative_url }}"> {{ link.desc }} </a>
            </div>
          </div>
          {%- endif -%}
        <li>
    {%- endfor -%}
</ul>

# Class Notes
Here are notes I've made for various courses I've taken at IITB. These are many notes that I haven't yet linked here but you can dig around and find them at [this link](https://github.com/aryamanmaithani/math).

<ul>
  {%- for blink in site.data.notes-links -%}
    {%- assign link = blink[1] -%}
      <li> <a href="/math{{ blink[0] | relative_url }}">
      <h3 class="post-title">{{ link.tit }} ({{ blink[0] }})</h3>
      </a> </li>
  {%- endfor -%}
</ul>
