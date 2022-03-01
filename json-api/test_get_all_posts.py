import unittest
from controller.utils import get_unique_posts

lst1 = [{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},
            {"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
            {"author":"Tia Roberson","authorId":2,"id":59,"likes":971,"popularity":0.21,"reads":36154,"tags":["politics","tech"]}
            ]

lst2 = [{"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
        {"author":"Zackery Turner","authorId":12,"id":2,"likes":469,"popularity":0.68,"reads":90406,"tags":["startups","tech","history"]}
        ]

class fetchDate(unittest.TestCase):

   

    # def get_all_posts_tag_not_provided(self):
    #     # get_all_posts("", 'id')


    # def get_all_posts_tag_provided(self):
    #     # get_al_posts("abcd", )

    # def get_all_posts_invalid_sortBy(self):

    # def get_all_posts_valid_sortBy(self):


    # def get_all_posts_invalid_direction(self):

    # def get_all_posts_valid_direction(self):

   
        
    def test_get_unique_posts_by_tags(self):
        all_posts= [lst1, lst2]
        actual_unique_posts = get_unique_posts(all_posts)

        expected_unique_posts = [{'author': 'Jon Abbott', 'authorId': 4, 'id': 95, 'likes': 985, 'popularity': 0.42, 'reads': 55875, 'tags': ['politics', 'tech', 'health', 'history']}, 
        {'author': 'Jaden Bryant', 'authorId': 3, 'id': 18, 'likes': 983, 'popularity': 0.09, 'reads': 33952, 'tags': ['tech', 'history']}, 
        {'author': 'Tia Roberson', 'authorId': 2, 'id': 59, 'likes': 971, 'popularity': 0.21, 'reads': 36154, 'tags': ['politics', 'tech']}, 
        {'author': 'Zackery Turner', 'authorId': 12, 'id': 2, 'likes': 469, 'popularity': 0.68, 'reads': 90406, 'tags': ['startups', 'tech', 'history']}]

        assert(len(actual_unique_posts) == len(expected_unique_posts))
        assert(actual_unique_posts == expected_unique_posts)
    


if __name__ == '__main__':
    unittest.main()



     

