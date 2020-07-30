--- 
layout: page
title: Math
image: /img/avatar-icon.png
light-image: /img/avatar-icon-light.png
---

Hi, here's where I post math stuff that I've written (in $$\LaTeX$$).  
With all my $$\LaTeX$$'d files, I also upload the source `.tex` code.  
To view those, you can go to the appropriate folder that you may find [here](https://github.com/aryamanmaithani/math). (Mostly, just changing the `.pdf` to `.tex` in the URL works as well but sometimes I have split the document into many `.tex` files.)

<div class="posts-list">
    {%- for blink in site.data.math-links -%}
        {%- assign link = blink[1] -%}
        <article class="post-preview">
          <a href="/math{{ blink[0] | relative_url }}">
          <h2 class="post-title">{{ link.tit }}</h2>
          </a>
          {%- if link.desc -%}
          <div class="post-entry-container">
            <div class="post-entry">
              <a href="/math{{ blink[0] | relative_url }}"> {{ link.desc }} </a>
            </div>
          </div>
          {%- endif -%}
        </article>
    {%- endfor -%}
</div>