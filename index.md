--- 
layout: page
title: Math
image: /img/avatar-icon.png
light-image: /img/avatar-icon-light.png
---

Hi, here's where I post math stuff that I've written (in $$\LaTeX$$).  
With all my $$\LaTeX$$'d files, I also upload the source `.tex` code.  
To view those, you can go to the appropriate folder that you may find [here](https://github.com/aryamanmaithani/math). (Mostly, just changing the `.pdf` to `.tex` in the URL works as well but sometimes I have split the document into many `.tex` files.)

* [Numerical Analysis](ma-214)
* [Group theory GD](group-theory-gd)
* [ODEs](ma-108), a summary of the first undergraduate ODE course
* [MA 107 notes](ma-107)
* [Group theory notes](ma-419)
* [Category theory](cat-theory)
* [Posets](posets)
* [Infinities and beyond](infinities-and-beyond)
* [Classification of Surfaces](classification-of-surfaces), a topology report I made for the Summer of Science initiative by [MnP, IITB](https://mnp-club.github.io/).

<div class="posts-list">
    {% for post in site.math-links %}
        <article class="post-preview">
          <a href="{{ post.href | relative_url }}">
          <h2 class="post-title">{{ post.title }}</h2>
          </a>

          {% if post.desc}
          <div class="post-entry-container">
            <div class="post-entry">
              <a href="{{ post.href | relative_url }}"> {{ post.desc }} </a>
            </div>
          </div>
          {% endif %}

        </article>
    {% endfor %}
</div>