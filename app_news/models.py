class Articles():
    def __init__(self, author, title, description, url, urltoImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urltoImage = urltoImage
        self.publishedAt = publishedAt
        self.content = content

class Categories():
    def __init__(self, author, title, description, url, urltoImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urltoImage = urltoImage
        self.publishedAt = publishedAt
        self.content = content
       
class News_Source():
    def __init__(self, author, title, description, url, urltoImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urltoImage = urltoImage
        self.publishedAt = publishedAt
        self.content = content

class All_news_sources():
    def __init__(self, news_id, name, description, url):
        self.news_id = news_id
        self.name = name
        self.description = description
        self.url = url
       
