My experience with Pelican
##########################

:date: 2017-10-24 16:30
:modified: 2017-10-24 16:30
:tags: pelican, metablog
:category: web
:slug: experience-pelican
:authors: Ben Fedidat
:summary: Describing my experience setting up this website with Pelican

I just set up this website as a static site generator with Pelican.
It's rather easy to use, although it has its quirks.

First of all, if you're thinking about setting up a site with Pelican,
you may want to think about alternatives. Notably, Jekyll builds on Ruby, it is
very well supported by Github itself. Others includes Octopress (originally
built onto Jekyll to add features and simplicity, now a framework of its own),
Hexo (NodeJS) or Hugo (Golang). 

Ultimately, I chose Pelican because I have some experience with Python
and thought this may ease the configuration and maintainance. 
If you prefer something else, you can a static site generators for just about any 
(interpreted) language.

Installing and setting up
-------------------------

Basically, I started by installing it using::

    sudo apt-get install pelican

`The official guide <http://docs.getpelican.com/en/3.7.1/install.html>`_ advises 
setting up a virtalenv and installing through pip but it will probably work 
fine for you without that.

After that, I made a new website with ``pelican-quickstart``. This sets up the folder
tree, as well as some files for the generator. Your filer will look like this::

    yourproject/
    ├── content
    │   └── (pages)
    ├── output
    ├── develop_server.sh
    ├── fabfile.py
    ├── Makefile
    ├── pelicanconf.py       # Main settings file
    └── publishconf.py       # Settings to use when ready to publish

Format
------

At this point, you will want to decide what kind of markup tool you want to use
in order to write your articles. Pelican supports two formats:

* Markdown (.md): The consensus online seems to be that Markdown is well supported 
  accross many platforms but is a loosely-defined standard. This leads to some 
  inconsistencies and quirks but an otherwise smoother experience.
* reStrcturedText, on the other hand, is a well-defined standard with one large 
  implementation (Python Sphinx). It is however sometimes more verbose and less 
  commonplace, so you will find some missing features. 
  Note that Python's own docutils use rST.

Ultimately, these criteria didn't matter to me so I went ahead with Pelican's 
default format, which is rST.

Static files
------------

I recommend you to create an additional folder named ``extra`` inside the content 
folder, where you will place files that you want to later transfer to specific 
locations within your site. This includes, among others:

* Favicons
* robots.txt
* CNAME if you use Github pages with a custom domain like me
* README.txt


disqus: simply saying the disqus url didn't work, i followed 
https://github.com/DandyDev/pelican-bootstrap3/issues/219

pelican-bootstrap3: i18n-sub was missing, specific bootstrap theme (pelicanconf.py)

python: don't have to use (pretty much), but nice to know, run locally

pelican: just run "make devserver", regenerates, link to docs

github pages: ghp-import, push, settings (specify custom domain, master branch), 
separate repo for whole site

restructuredtext vs markdown

pelican plugins

favicon: generated it, recommend 32px

V extra folder with links to images/robots.txt/favicon/README (root stuff)