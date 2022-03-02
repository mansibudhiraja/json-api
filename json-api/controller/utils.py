
import urllib.request, json


def get_all_posts_by_tags(api_client, tags) -> list:
    all_tags = tags.split(",")
    all_posts = []

    for tag_name in all_tags:
        complete_list = api_client.fetch_posts_by_tagname_from_external_api(tag_name)
        all_posts.append(complete_list["posts"])
    return all_posts


# return the list of unique posts
def get_unique_posts(all_posts) -> list:
    unique_posts = {}
    for post in all_posts:
        for sub_post in post:
            if sub_post["id"] not in unique_posts:
                unique_posts[sub_post["id"]] = sub_post
    return list(unique_posts.values())


# returns sorted posts based on sortby and direction parameters
def sort_results(posts, sortBy, direction) -> list:

    if direction == "desc":
        return sorted(posts, key=lambda x: x[sortBy], reverse=True)
    else:
        return sorted(posts, key=lambda x: x[sortBy])


# validates the parameters(tags, sortby and direction)
def validate_parameters(tags, sortBy, direction) -> bool:
    validsortBy = [
        "id",
        "author",
        "authorID",
        "likes",
        "popularity",
        "reads",
        "tags",
        None,
    ]
    validDirections = ["asc", "desc", None]

    if not tags or len(tags) == 0:
        raise ValueError("Tags parameter is required")

    if sortBy not in validsortBy:
        raise ValueError("sortBy parameter is invalid")

    if direction not in validDirections:
        raise ValueError("Direction parameter is invalid")

    return True


# returns the unique posts based on the tag, sortby and direction
def get_all_posts(api_client, tags, sortBy, direction="asc") -> list:

    if validate_parameters(tags, sortBy, direction):
        all_posts = get_all_posts_by_tags(api_client, tags)
        all_unique_posts = get_unique_posts(all_posts)

        if sortBy:
            final_posts = sort_results(all_unique_posts, sortBy, direction)
        else:
            final_posts = all_unique_posts

        return final_posts
