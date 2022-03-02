import unittest
from controller.utils import (
    get_unique_posts,
    validate_parameters,
    sort_results,
)

# created two random lists of dictionaries to test
lst1 = [
    {
        "author": "Jon Abbott",
        "authorId": 4,
        "id": 95,
        "likes": 985,
        "popularity": 0.42,
        "reads": 55875,
        "tags": ["politics", "tech", "health", "history"],
    },
    {
        "author": "Jaden Bryant",
        "authorId": 3,
        "id": 18,
        "likes": 983,
        "popularity": 0.09,
        "reads": 33952,
        "tags": ["tech", "history"],
    },
    {
        "author": "Tia Roberson",
        "authorId": 2,
        "id": 59,
        "likes": 971,
        "popularity": 0.21,
        "reads": 36154,
        "tags": ["politics", "tech"],
    },
]

lst2 = [
    {
        "author": "Jaden Bryant",
        "authorId": 3,
        "id": 18,
        "likes": 983,
        "popularity": 0.09,
        "reads": 33952,
        "tags": ["tech", "history"],
    },
    {
        "author": "Zackery Turner",
        "authorId": 12,
        "id": 2,
        "likes": 469,
        "popularity": 0.68,
        "reads": 90406,
        "tags": ["startups", "tech", "history"],
    },
]


class fetchDate(unittest.TestCase):

    # tests when tag not provided
    def test_get_all_posts_tag_not_provided(self):
        with self.assertRaises(ValueError) as err:
            validate_parameters("", "id", "asc")

    # tests when tag  provided
    def test_get_all_posts_tag_provided(self):
        actual = validate_parameters("tech", "id", "asc")
        expected = True
        assert actual == expected

    # tests when invalid sortby provided
    def test_get_all_posts_invalid_sortBy(self):
        with self.assertRaises(ValueError) as err:
            validate_parameters("tech", "person", "asc")

    # tests when valid sortby provided
    def test_get_all_posts_valid_sortBy(self):
        actual = validate_parameters("tech", "likes", "desc")
        expected = True
        assert actual == expected

    # tests when invalid direction provided
    def test_get_all_posts_invalid_direction(self):
        with self.assertRaises(ValueError) as err:
            validate_parameters("tech", "id", "long")

    # tests when valid sortby provided
    def test_get_all_posts_valid_direction(self):
        actual = validate_parameters("tech", "likes", "desc")
        expected = True
        assert actual == expected

    # tests if we get unique posts from list of all posts.
    def test_get_unique_posts(self):
        all_posts = [lst1, lst2]
        actual_unique_posts = get_unique_posts(all_posts)

        expected_unique_posts = [
            {
                "author": "Jon Abbott",
                "authorId": 4,
                "id": 95,
                "likes": 985,
                "popularity": 0.42,
                "reads": 55875,
                "tags": ["politics", "tech", "health", "history"],
            },
            {
                "author": "Jaden Bryant",
                "authorId": 3,
                "id": 18,
                "likes": 983,
                "popularity": 0.09,
                "reads": 33952,
                "tags": ["tech", "history"],
            },
            {
                "author": "Tia Roberson",
                "authorId": 2,
                "id": 59,
                "likes": 971,
                "popularity": 0.21,
                "reads": 36154,
                "tags": ["politics", "tech"],
            },
            {
                "author": "Zackery Turner",
                "authorId": 12,
                "id": 2,
                "likes": 469,
                "popularity": 0.68,
                "reads": 90406,
                "tags": ["startups", "tech", "history"],
            },
        ]

        assert len(actual_unique_posts) == len(expected_unique_posts)
        assert actual_unique_posts == expected_unique_posts

    # tests if the results are correctlly sorted for descending order
    def test_sort_results_desc(self):
        actual_sorted = sort_results(lst1, "id", "desc")
        expected_sorted = [
            {
                "author": "Jon Abbott",
                "authorId": 4,
                "id": 95,
                "likes": 985,
                "popularity": 0.42,
                "reads": 55875,
                "tags": ["politics", "tech", "health", "history"],
            },
            {
                "author": "Tia Roberson",
                "authorId": 2,
                "id": 59,
                "likes": 971,
                "popularity": 0.21,
                "reads": 36154,
                "tags": ["politics", "tech"],
            },
            {
                "author": "Jaden Bryant",
                "authorId": 3,
                "id": 18,
                "likes": 983,
                "popularity": 0.09,
                "reads": 33952,
                "tags": ["tech", "history"],
            },
        ]
        assert actual_sorted == expected_sorted

    # tests if the results are correctlly sorted for ascending order
    def test_sort_results_asc(self):
        actual_sorted = sort_results(lst1, "id", "asc")
        expected_sorted = [
            {
                "author": "Jaden Bryant",
                "authorId": 3,
                "id": 18,
                "likes": 983,
                "popularity": 0.09,
                "reads": 33952,
                "tags": ["tech", "history"],
            },
            {
                "author": "Tia Roberson",
                "authorId": 2,
                "id": 59,
                "likes": 971,
                "popularity": 0.21,
                "reads": 36154,
                "tags": ["politics", "tech"],
            },
            {
                "author": "Jon Abbott",
                "authorId": 4,
                "id": 95,
                "likes": 985,
                "popularity": 0.42,
                "reads": 55875,
                "tags": ["politics", "tech", "health", "history"],
            },
        ]
        assert actual_sorted == expected_sorted


if __name__ == "__main__":
    unittest.main()
