from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Cool Author')

        self.assertEqual('Test Title', b.title)
        self.assertEqual('Cool Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test Title', 'Cool Author')

        self.assertEqual(b.__repr__(), 'Test Title by Cool Author, 0 posts')

    def test_repr_multiple_posts(self):
        b = Blog('Test Title', 'Cool Author')
        b.posts = ['test']
        b2 = Blog('Simple Title', 'Old Author')
        b2.posts = ['test', 'one more']

        self.assertEqual(b.__repr__(), 'Test Title by Cool Author, 1 post')
        self.assertEqual(b2.__repr__(), 'Simple Title by Old Author, 2 posts')

