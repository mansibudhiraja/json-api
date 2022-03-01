from enum import unique
import urllib.request, json

dct1 = {"posts": [{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},
            {"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
            {"author":"Tia Roberson","authorId":2,"id":59,"likes":971,"popularity":0.21,"reads":36154,"tags":["politics","tech"]},
            ]}

dct2 = {"posts": [
        {"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
        {"author":"Zackery Turner","authorId":12,"id":2,"likes":469,"popularity":0.68,"reads":90406,"tags":["startups","tech","history"]}
        ]}

# def get_all_posts_by_tagname(tagname):
#     url = "https://api.hatchways.io/assessment/blog/posts?tag={}".format(tagname)
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     all_posts = json.loads(data)
#     return all_posts

#this function validates the parameters
def validate_function(tags, sortBy, direction):
    validsortBy = ['id', 'author', 'authorID', 'likes', 'popularity', 'reads', 'tags', None]
    validDirections = ['asc', 'desc', None]

    if not tags or len(tags) == 0:
        raise ValueError("Tags parameter is required")

    if sortBy not in validsortBy:
        raise ValueError("sortBy parameter is invalid")
        
    if direction not in validDirections:
        raise ValueError("Direction parameter is invalid")
    
    return True

#this function makes the api call and return all posts and includes duplicates as well.
def get_all_posts_by_tags(tags):
    all_tags = tags.split(',')
    all_posts = []
    
    for tag in all_tags:
        #complete_list = get_all_posts_by_tagname(tag_name)
        all_posts.append(dct1["posts"])
        all_posts.append(dct2["posts"])
    return all_posts
    
#this function returns all unique posts by using a map.
def get_unique_posts(all_posts)-> list:
    unique_posts={}
    for post in all_posts:
        for sub_post in post:
            if sub_post["id"] not in unique_posts:
                unique_posts[sub_post["id"]] = sub_post
    return list(unique_posts.values())

#this function returns sorted posts basis sortby and direction parameters
def sort_results(posts, sortBy, direction) -> list:

    if direction == 'desc':
        return sorted(posts, key= lambda x: x[sortBy], reverse=True)
    else:
        return sorted(posts, key= lambda x: x[sortBy])

# this is the function called from routes.py and returns the unique posts basis tag, sortby and direction.
def get_all_posts(tags, sortBy, direction="asc") -> list:

    if validate_function(tags, sortBy, direction):
        all_posts = get_all_posts_by_tags(tags)
        all_unique_posts = get_unique_posts(all_posts)

        if sortBy:
            final_posts = sort_results(all_unique_posts, sortBy, direction)
        else:
            final_posts = all_unique_posts
        
        return final_posts

    




        


   




    

    

    
    
    
