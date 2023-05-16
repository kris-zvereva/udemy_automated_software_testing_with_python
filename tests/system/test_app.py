from unittest import TestCase
from unittest.mock import patch # using that we can change the function and make it do smt different
import app
from blog import Blog
from post import Post

# test creates a new blog object, sets app.blogs to be a dict that contains a single blog,
# and patches the built-in print func (print func itself was not called)


class AppTest(TestCase):
    #setUp is a func you can define inside a testcase and run before each test
    def setUp(self):
        blog = Blog('Test Title', 'Cool Author')
        app.blogs = {'Test Title': blog} # created a new Blog object and mapped blog name to blog object

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()

            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test', 'Test Author', 'q')
            app.menu()

            self.assertIsNotNone(app.blogs['Test'])

    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'q')
                app.menu()

                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', 'Test', 'q')
                app.menu()

                mocked_ask_read_blog.assert_called()

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'Test', 'New Post', 'New Content', 'q')
                app.menu()

                mocked_ask_create_post.assert_called()

    def test_print_blogs(self):
        # patching the print function as mocked_print
        with patch('builtins.print') as mocked_print:
            # call a func that will print
            app.print_blogs()
            # replaced the print func with a mock // assert that it has been called with this value
            mocked_print.assert_called_with('- Test Title by Cool Author, 0 posts')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Author')

            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))
            self.assertEqual(app.blogs.get('Test').title, 'Test')
            self.assertEqual(app.blogs.get('Test').author, 'Author')

    # checking if ask_read_blog calls print_posts
    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test Title'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs['Test Title'])

    def test_print_posts(self):
        blog = app.blogs['Test Title']
        blog.create_post('Post title', 'Post content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Test Title', 'Test Content')
        expected_print = '\n---Test Title---\n    \nTest Content\n    \n'
        with patch('builtins.print') as mocked_print_post:
            app.print_post(post)
            mocked_print_post.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = app.blogs['Test Title']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Title', 'Test', 'Post Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, 'Test')
            self.assertEqual(blog.posts[0].content, 'Post Content')

