import unittest
from app_news import  models 

Articles = models.Articles
Categories = models.Categories
News_Source = models.News_Source
All_news_sources = models.All_news_sources

class AllClassesTest(unittest.TestCase):
    def setUp(self):
        '''
        The setup method will run before each test case
        '''

        self.new_article = Articles('John Smith','A new Beginning','mini description','www.lemmy\'s blog','https/imagelink','2022/05/05', 'More content')
        self.new_category = Categories('Lemmy Mwaura', 'A wonderful Story', 'mini description', 'www.lemmy.com', 'https/lemmy/profile','2022/05/05', 'More content')
        self.new_news_source = News_Source('BBC News','Most up to date coverage','mini desc','www.bbcnews.com/article','https/bbcnews/image','2022/05/05','More content')
        self.all_news_sources = All_news_sources('lemmys-news', 'Lemmys News', 'Mini desc', 'www.emmysnews.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
        self.assertTrue(isinstance(self.new_category,Categories))
        self.assertTrue(isinstance(self.new_news_source,News_Source))
        self.assertTrue(isinstance(self.all_news_sources,All_news_sources))
