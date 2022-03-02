import json
import urllib.request
import concurrent.futures
import time

from expiringdict import ExpiringDict

# Responsible for supplying data for an API request
# Returns cached value when available
class ApiClient:
    def __init__(self, max_len, max_age_seconds) -> None:
        self.cache = ExpiringDict(max_len, max_age_seconds)

    def fetch_posts_by_tagname_from_external_api(self, tagname)->list:
        cached_result = self.cache.get(tagname)
        if cached_result:
            return cached_result

        url = "https://api.hatchways.io/assessment/blog/posts?tag={}".format(tagname)
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        all_posts = data["posts"]
        self.cache[tagname] = all_posts
        return all_posts

    # return all posts obtained from api calls and includes duplicates as well.
    # added threading for the list of tags
    def get_all_posts_by_tags(self, tags) -> list:
        all_tags = tags.split(",")
        all_posts = []
        
        t1=time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = [executor.submit(self.fetch_posts_by_tagname_from_external_api, tagname) for tagname in all_tags]

            for f in concurrent.futures.as_completed(results):
                all_posts.append(f.result())

        t2=time.perf_counter()
        print(f'Finished in {t2-t1} seconds')
        return all_posts




    