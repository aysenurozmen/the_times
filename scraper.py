from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from dateutil import parser
from article_element import ArticleElement
from selenium.webdriver.remote.webelement import WebElement
from database_manager import DatabaseManager

from links import *

account_email = ''
account_password = ''


class Browser:
    browser, service = None, None

    # Initialize the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)
        time.sleep(3)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(0.5)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(0.5)

    def login_to_the_times(self, email: str, password: str):
        self.open_page('https://login.thetimes.co.uk?gotoUrl=https://www.thetimes.co.uk')
        self.add_input(by=By.ID, value='1-email', text=email)
        self.add_input(by=By.NAME, value='password', text=password)
        self.click_button(by=By.CLASS_NAME, value='auth0-lock-submit')

    def get_article_links(self, section: str, subsection: str, url: str):

        # Go to page to get the article links
        self.open_page(url)

        article_elements = []
        all_links = self.browser.find_elements(By.XPATH, "//a[@href]")
        for link in all_links:
            if '/article/' in link.get_attribute("href"):  # and link.get_attribute("href") not in article_links:
                if len(article_elements) == 0 or article_elements[-1].link != link.get_attribute("href"):
                    # Article section and link
                    article_element = ArticleElement(section=section, subsection=subsection,
                                                     link=link.get_attribute("href"))
                    article_elements.append(article_element)

        return article_elements

    def scrape_article(self, article_element: ArticleElement):

        # Go to article page via link
        self.open_page(article_element.link)

        # Title
        article_element.title = self.browser.find_element(By.TAG_NAME, "h1").text

        # Text
        article_paragraphs = self.browser.find_elements(By.XPATH,
                                                        "//p[@class='responsive__Paragraph-sc-1pktst5-0 gaEeqC']")
        article_element.text = get_article_text(article_paragraphs)

        # Date and Time
        time_tag = self.browser.find_element(By.XPATH, "//article[@id='article-main']//time")
        article_datetime = parser.parse(time_tag.get_attribute("datetime"))
        article_element.datetime = article_datetime

        # TODO Author
        authors = []
        article_element.authors = authors

        return article_element


def get_article_text(paragraphs: list[WebElement]):
    article_content = ''
    first_paragraph = True
    for p in paragraphs:
        if p.text != '':
            if first_paragraph:
                article_content += p.text.replace('\n', '')
                first_paragraph = False
            else:
                article_content += p.text.replace('\n', ' ')
        else:
            if first_paragraph:
                article_content += p.get_attribute("innerText").replace('\n', '')
                first_paragraph = False
            else:
                article_content += p.get_attribute("innerText").replace('\n', ' ')
        article_content += ' '
    return article_content


def article_cannot_be_scraped(article_section: str, article_subsection: str, article_link: str,
                              article_page_index: str):
    with open('articles/articles_cannot_be_scraped.txt', 'a') as f:
        f.write(
            article_section + ', ' + article_subsection + ', ' + article_link + ', Page Index: ' + article_page_index)
        f.write('\n')
        f.close()


if __name__ == '__main__':

    # Set the browser
    browser = Browser('drivers/chromedriver.exe')

    # Login to The Times
    browser.login_to_the_times(account_email, account_password)

    time.sleep(2)

    page_index = 3
    while page_index != 5:

        # Get article links from page
        articles = browser.get_article_links(LifeAndStyle.SECTION.value, LifeAndStyle.DRIVING.value,
                                             LifeAndStyle.DRIVING_URL.value + str(page_index))

        # Scrape articles from links
        for article in articles:

            existing_article = DatabaseManager.find_article(section=article.section, subsection=article.subsection,
                                                            link=article.link)

            # If article is not already in the db of same section
            if existing_article is None:
                try:
                    browser.scrape_article(article)
                    DatabaseManager.write_article_to_db(article_to_write=article)
                except:
                    try:
                        browser.scrape_article(article)
                        DatabaseManager.write_article_to_db(article_to_write=article)
                    except:
                        article_cannot_be_scraped(article_section=article.section,
                                                  article_subsection=article.subsection, article_link=article.link,
                                                  article_page_index=str(page_index))

        # Go to next page
        page_index += 1

    time.sleep(2)

    # browser.close_browser()
