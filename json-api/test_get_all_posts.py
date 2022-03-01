import unittest
from wsgiref import validate
from controller.utils import get_unique_posts, get_all_posts, validate_function, sort_results

lst1 = [{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},
            {"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
            {"author":"Tia Roberson","authorId":2,"id":59,"likes":971,"popularity":0.21,"reads":36154,"tags":["politics","tech"]}
            ]

lst2 = [{"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
        {"author":"Zackery Turner","authorId":12,"id":2,"likes":469,"popularity":0.68,"reads":90406,"tags":["startups","tech","history"]}
        ]

class fetchDate(unittest.TestCase):


    def test_get_all_posts_tag_not_provided(self):
        with self.assertRaises(ValueError) as err:
            validate_function("", 'id', 'asc')
    
    def test_get_all_posts_tag_provided(self):
        actual = validate_function("tech", 'id', 'asc')
        expected = True
        assert(actual == expected)


    def test_get_all_posts_invalid_sortBy(self):
        with self.assertRaises(ValueError) as err:
            validate_function("tech", 'person', 'asc')
    

    def test_get_all_posts_valid_sortBy(self):
        actual = validate_function("tech", "likes", 'desc')
        expected = True
        assert(actual == expected)

    def test_get_all_posts_invalid_direction(self):
        with self.assertRaises(ValueError) as err:
            validate_function("tech", "id", "long")

    def test_get_all_posts_valid_direction(self):
        actual = validate_function("tech", "likes", "desc")
        expected = True
        assert(actual == expected)

   
    def test_get_unique_posts_by_tags(self):
        all_posts= [lst1, lst2]
        actual_unique_posts = get_unique_posts(all_posts)

        expected_unique_posts = [{'author': 'Jon Abbott', 'authorId': 4, 'id': 95, 'likes': 985, 'popularity': 0.42, 'reads': 55875, 'tags': ['politics', 'tech', 'health', 'history']}, 
        {'author': 'Jaden Bryant', 'authorId': 3, 'id': 18, 'likes': 983, 'popularity': 0.09, 'reads': 33952, 'tags': ['tech', 'history']}, 
        {'author': 'Tia Roberson', 'authorId': 2, 'id': 59, 'likes': 971, 'popularity': 0.21, 'reads': 36154, 'tags': ['politics', 'tech']}, 
        {'author': 'Zackery Turner', 'authorId': 12, 'id': 2, 'likes': 469, 'popularity': 0.68, 'reads': 90406, 'tags': ['startups', 'tech', 'history']}]

        assert(len(actual_unique_posts) == len(expected_unique_posts))
        assert(actual_unique_posts == expected_unique_posts)
    
    def test_sort_results_desc(self):
        actual_sorted = sort_results(lst1, "id", "desc")
        expected_sorted = [{"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},
            {"author":"Tia Roberson","authorId":2,"id":59,"likes":971,"popularity":0.21,"reads":36154,"tags":["politics","tech"]},
            {"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
            ]
        assert(actual_sorted==expected_sorted)

    def test_sort_results_asc(self):
        actual_sorted = sort_results(lst1, "id", "asc")
        expected_sorted = [{"author":"Jaden Bryant","authorId":3,"id":18,"likes":983,"popularity":0.09,"reads":33952,"tags":["tech","history"]},
             {"author":"Tia Roberson","authorId":2,"id":59,"likes":971,"popularity":0.21,"reads":36154,"tags":["politics","tech"]},
             {"author":"Jon Abbott","authorId":4,"id":95,"likes":985,"popularity":0.42,"reads":55875,"tags":["politics","tech","health","history"]},
            ]
        assert(actual_sorted==expected_sorted)

if __name__ == '__main__':
    unittest.main()



     

