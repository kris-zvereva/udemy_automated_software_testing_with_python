from unittest import TestCase
from blog import Blog


# checks how to separate classes work together
class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test Title', 'Cool Author')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json_no_posts(self):
        b = Blog('Test Title', 'Cool Author')
        expected = {
            'title': 'Test Title',
            'author': 'Cool Author',
            'posts': []
        }

        self.assertDictEqual(b.json(), expected)

    def test_json(self):
        b = Blog('Test Title', 'Cool Author')
        b.create_post('Test Post', 'Test Content')
        expected = {
            'title': 'Test Title',
            'author': 'Cool Author',
            'posts': [{
                'title': 'Test Post',
                'content': 'Test Content',
                }]
        }

        self.assertDictEqual(b.json(), expected)

