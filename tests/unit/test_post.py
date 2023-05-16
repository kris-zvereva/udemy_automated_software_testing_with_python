from unittest import TestCase
from post import Post


# when we create a Post object, the correct properties get set on it
class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test Title', 'Test Content')

        self.assertEqual('Test Title', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test Title', 'Test Content')
        expected = {
            'title': 'Test Title',
            'content': 'Test Content',
        }

        self.assertDictEqual(expected, p.json())



