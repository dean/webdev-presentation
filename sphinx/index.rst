===============================
Introduction to Web Development
===============================

What is Web Development?
========================

* Doing any development work for a website
* Design
* Interactive components
* Scaling

How browsers work
=================

* User tries to visit a site
* Request IP through DNS lookup
* Send request for the site to that IP
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
        * HEAD
    * Server sends client a response, which updates the page

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

Concepts
========
* Dynamic vs Static webpages: Static webpages are used mostly for displaying
* content that won't be changing often, and have the advantage of bearing a
* very low load wherever they are hosted. This is because, none of the html
* has to be generated before sending the webpage to the client who requested
* it. Dynamic webpages use more resources on the server, but are basically
* webpages that are tailored based on the input provided by a user. This
* means, showing your specific username at the top of a page, or generating
* your news feed for facebook.

* MVC: Model View Controller
 ** Views (Templates): These are what the user sees, and what are (usually)
dynamically generated . It is important to note that none of your logic should
be in your template usually. If it's able to be abstracted out to the
controller, that's where it should be.  ** Models: These are your "Objects".
They're the database tables you have that you associate data with. Models have
attributes to them that are columns in the table. For example, a User might
have 'name', 'username', 'email', and 'password' fields.  ** Controllers: This
is where the logic for your application goes. With the framework we'll be
demo'ing with, you declare which url will map to which function, which in turn
returns a certain template back to the person who requested the data. Again,
we want to try and isolate most, if not all, the logic to the controller, and
not to the template.

Tools: We have a ton of tools at our disposal to help us manage and write
websites.

* Virtual Environments: Because we'll be talking mostly about Frameworks like
* Django, Flask, and Rails, we will want to have a virtual environment. These
* are basically a local install of the language and it's modules for the web
* framework we're developing in. 

* Databases (Relational Database Management Systems?) Flask - SQLAlchemy
 ** Different Types: MySQL, PostreSQL ** Migrations - Migrations are how we
add new columns and tables to our database without direct interaction with it,
and without having to destroy + recreate the database. 

Different things in web development:

* Forms: This is what our user interacts with to send us data. When they
* submit a form, it's our responsibility to gather that information and store
* it in the database.

* Login: An integral portion to most web applications. We will be demo'ing
* this.

Extra?:
* Deployment strategies
 ** Apache (wsgi) -- Possibly a quick demo on how to set this up.
