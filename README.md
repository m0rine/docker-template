This is an example docker template for beginners.  It will contrast a simple manual setup for a web application with docker's containerization approach to show how you can dockerize yourself.


# TODO
- Rename the dockerhub repo to something more like "template", looks we have to pull and retag, we should try pushing. <DONE>
- Run a basic python server which displays basic web page, where frontend (html/css) is isolated from server, separate containers. <DONE>
    - Right now, the goal is to have an nginx server hosting static content with HTML/CSS/JS for the frontend.  On the backend, a flask server handling requests for the IP information, and integration with Postgres to save the IP and maybe other info.
