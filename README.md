This is an example docker template for beginners.  It will contrast a simple manual setup for a web application with docker's containerization approach to show how you can dockerize yourself.


# TODO
- Rename the dockerhub repo to something more like "template", looks we have to pull and retag, we should try pushing. <DONE>
- Run a basic python server which displays basic web page, where frontend (html/css) is isolated from server, separate containers. <DONE>
    - Right now, the goal is to have an nginx server hosting static content with HTML/CSS/JS for the frontend.  On the backend, a flask server handling requests for the IP information, and integration with Postgres to save messages. <DONE>
- Save messages persistently with Postgresql database <DONE>
- Document how to backup volumes so the database data is not lost 

# Low priority
- Document how to set postgres db user passwords with the postgres official docker images, Answer: Set the environment variable on db initalization.
- Userland-proxy and IPTables rules, are they required on a more enterprise cloud environment to get real user IP?
- Maybe documents the CORS stuff
- Document how docker volumes are automatically destroyed in the postgres container, why, and how to fix it.

# Continuing development

- I've been instructed to make a guide for deploying and developing with docker.  Right now, my issue is that development is hard with docker.  What I essentially have is a setup for deploying to prod, but usually two docker composes exist for prod and dev.  So my current goal is to make using docker for development faster.

# PROD SETUP
- For the production dockerfile, simply make 

# Todays Goal 7/28
- Try to map the Dockerfile patterns for the Django OWASPDefectDojo onto our project.  In other words,

1. Fully understand how and why the defect dojo prod vs dev dockerfiles and docker compose function.
    
2. Apply the understanding.

# Building in compose? 

- Starting to consider that the best way is not to build images in the dockerfile, just pull from dockerhub.  We can build images with something like a Makefile.
- It's more flexible, we don't need to worry about having two build sources, which is in general, really annoying as well.
    - Update: Decided that makefile was not the thing I wanted, I definitely could use it, but file content changes are something I didn't need.  Dockerfile change --> automatic rebuild with make could be good but I wanted precision with bash.  And for something more automated, why not just go all the way GH actions?  
