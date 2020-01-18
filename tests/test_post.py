import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
   def setUp(self):
        self.user_cate = User(first_name = "Cate",
                                last_name = "Nduku",
                                username = "Cateh",
                                password = "cate123",
                                email = "ccayreen24@gmail.com")
        self.new_post = Post(post_title = "Fashion",
                            post_content = "Hello",
                            user_id = self.user_cate.id)
        self.new_comment = Comment(comment = "Nice",
                                    post_id = self.new_post.id,
                                    user_id = self.user_cate.id)

   def test_instance(self):
        self.assertTrue(isinstance(self.user_cate, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))