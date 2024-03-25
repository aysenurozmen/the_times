import datetime

from pymongo import MongoClient

from article_element import ArticleElement


class DatabaseManager:
    cluster = "mongodb://localhost:27017"
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(cluster)

    articles_collection = client.idp.articles_with_subtitles

    @staticmethod
    def get_articles_collection_from_db():
        # Create the database for our example (we will use the same database throughout the tutorial
        return DatabaseManager.articles_collection

    @staticmethod
    def write_article_to_db(article_to_write: ArticleElement):
        # Write articles to the database
        article_dict = article_to_write.to_dict()
        result = DatabaseManager.articles_collection.insert_one(article_dict)

    @staticmethod
    def find_article(section: str, subsection: str, link: str):
        return DatabaseManager.articles_collection.find_one({'section': section, 'subsection':subsection, 'link': link})

    @staticmethod
    def get_articles_by_section(section: str, subsection: str):
        return DatabaseManager.articles_collection.find({'section': section, 'subsection': subsection})

    # TODO get articles by month

    @staticmethod
    def get_articles_by_section_and_month(section: str, subsection: str, month: int):
        articles_by_section = DatabaseManager.get_articles_by_section(section=section, subsection=subsection)
        articles_by_section_and_month = []

        for article_dict in articles_by_section:
            article = ArticleElement.from_dict(article_dict)
            if article.datetime.month == month:
                articles_by_section_and_month.append(article)

        return articles_by_section_and_month

    @staticmethod
    def delete_articles_by_subsection(subsection: str):
        DatabaseManager.articles_collection.deleteMany({"subsection": subsection})

    @staticmethod
    def delete_articles_by_year(year: int):
        pass
        # TODO
        #DatabaseManager.articles_collection.deleteMany({ "datetime" : { $year: year }} )
        # { $year: new Date("2016-01-01")} -> returns 2016