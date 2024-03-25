from datetime import datetime


class ArticleElement:

    def __init__(self, title='', date=datetime.now(), section='', subsection='', authors=[], text='', link=''):
        self.title = title
        self.datetime = date
        self.section = section
        self.subsection = subsection
        self.authors = authors
        self.text = text
        self.link = link

    def __str__(self):
        return 'Title: ' + self.title + '\n' + 'Date: ' + self.datetime.strftime(
            "%d/%m/%Y, %H:%M:%S") + '\n' + 'Section: ' + self.section + '\n' + 'Subsection: ' + self.subsection + '\n' + 'Author: ' + str(
            self.authors) + '\n' + 'Text: ' + self.text + '\n' + 'Link: ' + self.link

    def to_dict(self):
        article_dict = {
            "title": self.title,
            "datetime": self.datetime,
            "section": self.section,
            "subsection": self.subsection,
            "authors": self.authors,
            "text": self.text,
            "link": self.link
        }
        return article_dict

    @staticmethod
    def from_dict(article_dict: dict):

        article = None

        if article_dict is not None:
            title = article_dict.get('title')
            date = article_dict.get('datetime')
            section = article_dict.get('section')
            subsection = article_dict.get('subsection')
            authors = article_dict.get('authors')
            text = article_dict.get('text')
            link = article_dict.get('link')
            article = ArticleElement(title=title, date=date, section=section, subsection=subsection, authors=authors, text=text, link=link)

        return article
