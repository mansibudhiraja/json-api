import urllib.request, json

dct = {"posts": [{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},
            {"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
            {"author":"Tia Roberson","authorId":2,"id":59,"likes":971,"popularity":0.21,"reads":36154,"tags":["politics","tech"]},
            {"author":"Ahmad Dunn","authorId":7,"id":45,"likes":31,"popularity":0.89,"reads":63432,"tags":["science","history"]},
            {"author":"Adalyn Blevins","authorId":11,"id":89,"likes":251,"popularity":0.6,"reads":75503,"tags":["politics","startups","tech","history"]},
            {"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history, duplicate"]}
            ]}

# def get_all_posts_by_tagname(tagname):
#     url = "https://api.hatchways.io/assessment/blog/posts?tag={}".format(tagname)
#     response = urllib.request.urlopen(url)
#     data = response.read()
#     all_posts = json.loads(data)
#     return all_posts

def get_unique_posts_by_tags(tags):
    all_tags = tags.split(',')
    post_dict={}
    for tag_name in all_tags:
        #complete_list = get_all_posts_by_tagname(tag_name)
        for post in dct["posts"]:
            if post["id"] not in post_dict:
                post_dict[post["id"]] = post

    return post_dict




def get_all_posts(parameters_dict):
    tags = parameters_dict.args.get("tag")
    sortBy = parameters_dict.args.get("sortBy")
    direction=parameters_dict.args.get("direction")


    validsortBy = ['id', 'author', 'authorID', 'likes', 'popularity', 'reads', 'tags', None]
    validDirections = ['asc', 'desc', None]

    if len(tags) == 0:
        raise ValueError("Tags parameter is required")

    if direction not in validDirections:
        raise ValueError("Direction parameter is invalid")
    
    if sortBy not in validsortBy:
        raise ValueError("sortBy parameter is invalid")

    all_unique_posts = get_unique_posts_by_tags(tags)

    if sortBy == 'desc':
         = sorted(all_unique_posts)


   




    

    

    
    
    
