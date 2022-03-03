import json
import urllib.request
from expiringdict import ExpiringDict

# Responsible for supplying data for an API request
# Returns
class ApiClient:
    def __init__(self, max_len, max_age_seconds) -> None:
        self.cache = ExpiringDict(max_len, max_age_seconds)

    def fetch_posts_by_tagname_from_external_api(self, tagname) -> dict:
        
        cached_result = self.cache.get(tagname)
        if cached_result:
            return cached_result

        url = "https://api.hatchways.io/assessment/blog/posts?tag={}".format(tagname)
        response = urllib.request.urlopen(url)
        data = response.read()
        all_posts = json.loads(data)
        self.cache[tagname] = all_posts
        
        return all_posts

