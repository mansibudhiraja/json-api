
#### This is a backend API which fetches all blog posts basis the tag provided from an external API and created unit tests for each of the function.

1. created dynamic routes ("/api/posts") basis the parameters(tag, sortBy, direction) provided by the user.
2. The user needs to add tag and test fails if the tag is missing. (/api/posts?tags=tech, health)
3. SortBy and direction are optional and if provided, they should be valid fields.
4. Sortby sorts the posts by any field in the post
5. Direction can be asc or desc and if user doesn't provide a direction, then we assume it to be ascending.
6. Created an abstract class called Cache which returns cached value when available. The request does not know whether we hit the cache or api. We saw an 100x improvement in the response time from 700-800ms to 6 ms when 7 tags were provided.
7. Used threading to introduce concurrency
8. created Performance method tp measure performance and got the following statistics:

        |Caching enabled|Threading enabled|Timing|
        |---|----|----|
        |       Yes       |         Yes       | 0.32 seconds                |
        |       Yes       |         No        | 1.5 seconds                 |
        |       No        |         Yes       | 2.6635391279999996 seconds  |
        |       No        |         No        | 15 seconds                  |


##### Usage:
1. used pip freeze to record all enviroment variables.
2. to install the dependencies in virtual env, create and activate the env and then install from requirements.
3. flask run to start the server
4. check route /api/ping
5. check route /api/posts?tags={tagName}&sortby={sortby}&direction={direction}
6. Added cache using expiredDict Module and used Postman, network and performance.py to check the response time
7. you can run the unit tests using command : python -m unittest discover . -v
