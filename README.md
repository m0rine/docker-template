This is an example docker template for beginners.  It will contrast a simple manual setup for a web application with docker's containerization approach to show how you can dockerize yourself.


# TODO
- Document how to backup volumes so the database data is not lost <INCOMPLETE, steps are not working>
- Rename the dockerhub repo to something more like "template", looks we have to pull and retag, we should try pushing. DONE
- Run a basic python server which displays basic web page, where frontend (html/css) is isolated from server, separate containers. DONE
    - Right now, the goal is to have an nginx server hosting static content with HTML/CSS/JS for the frontend.  On the middleware, a flask server handling requests for the IP information, and integration with Postgres to save messages. DONE
- Save messages persistently with Postgresql database DONE
- Document how docker volumes are automatically destroyed in the postgres container, why, and how to fix it. <PLANNED, LOW PRIORITY>

# Low priority
- Document how to set postgres db user passwords with the postgres official docker images, Answer: Set the environment variable on db initalization.
- Userland-proxy and IPTables rules, are they required on a more enterprise cloud environment to get real user IP? <NOT PLANNED>
- Maybe documents the CORS stuff <NOT PLANNED>
