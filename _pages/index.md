---
layout: page
title: "Kiran's garden"
thumbnail: /assets/img/thumbnail/sample.png
bookmark: true
permalink: /
---

# Welcome to my digital garden 🌱🌻

Here is where I put some of my thoughts, opinions, and notes on topics of interest. My inspiration for creating this garden came from Anna Howard's YouTube video, [creating a digital garden to end my doomscrolling](https://youtu.be/0tY7Z53QJo8?si=KkDY0Oeo6jscMZCm), and subsequent work including:
* [Obsidian: The King of Learning Tools](https://youtu.be/hSTy_BInQs8?si=CMyUBAWJe4XvW0q-) by Odysseas on YouTube
* [A Brief History & Ethos of the Digital Garden](https://maggieappleton.com/garden-history/) by Maggie Appleton
* [The Garden and the Stream: A Technopastoral](https://hapgood.us/2015/10/17/the-garden-and-the-stream-a-technopastoral/) by Mike Caulfield

I don't think I have anything particular exciting or noteworthy to say, but this garden is more for me than anyone else, to have a place to store my more polished thoughts in a way that I can remix and reuse later. My notes are organized by topic below:
[[notetaking]] 
[[web-building]]

<strong>Recently updated notes</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit: 5 %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

This digital garden template is free, open-source, and [available on GitHub here](https://github.com/maximevaillancourt/digital-garden-jekyll-template).

<style>
  .wrapper {
    max-width: 46em;
  }
</style>
