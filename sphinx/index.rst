===============================
Introduction to Web Development
===============================

What is Web Development?
========================

* Making Websites and Web Applications
* Design
* Interactive components
* Scaling

How browsers work
=================

* User tries to visit a site
* Request IP through DNS lookup
* Send request for the data to that IP
* Request hits server and it decides what to do
* Server sends you a file containing page's contents and resources
* Browser renders the file (HTML, CSS, Javascript)


Client-side vs. Server-side
===========================

* Client-side: Things happening in browser
    * Doesn't require internet access
* Server-side:
    * Data shows up in request with method type
        * GET
        * POST
        * Others, but not used as often.
    * Server sends client data, which is rendered thorugh browser.

Languages
=========

* HTML: Hyper Text Markup Language
    * Building blocks for front-end web development
    * The language your browser renders to display raw data on the webpage
* CSS: Cascading Style Sheets
    * Mostly for styling (making it pretty)
    * "classes" for elements to tag groups then apply looks
* JavaScript
    * Changes page without reloading it
    * Example: multiple steps in a registration form; data only sent at the
      end

Dynamic vs Static webpages
==========================
* Static for infrequently changed pages -- OSULUG
* Dynamic for interactive or frequently updated -- Facebook
* Dynamic can use lots of resources, due to always regenerating pages.

Caching
=======
* This can be mitigated through caching 

.. figure:: /_static/caching.jpg
    :align: center
    :scale: 50%

MVC (Model View Controller)
==========================

* Views (templates)
    * structure how user sees data
    * should not contain logic
.. figure:: /_static/mvc.jpg
    :scale: 25%
    :align: right
* Models (objects)
    * database tables
    * attributes are columns
* Controllers (logic)
    * which URL maps to which function
    * isolate the logic here

Tools
=====

* Virtual Environments
    * Isolated installation of language and dependencies
* Databases
    * MySQL - Larger install, but faster for retrieval and storing of data. 
    * SQLite - Lightweight install, quick setup, but slower. 
    * Many more!
* Migrations
    * Add new columns/tables to database without direct interaction
    * Other option is destroy then recreate the DB

Important Concepts
==================

* Forms: This is what our user interacts with to send us data. When they
* submit a form, it's our responsibility to gather that information and store
* it in the database.

* Login: An integral portion to most web applications. We will be demo'ing
* this.

Extra?:
* Deployment strategies
 ** Apache (wsgi) -- Possibly a quick demo on how to set this up.
=======
>>>>>>> Stashed changes
