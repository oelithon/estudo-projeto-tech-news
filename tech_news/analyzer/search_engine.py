from tech_news.database import search_news


# Requisito 6
# https://www.mongodb.com/docs/manual/reference/operator/query/regex/
def search_by_title(title):
    news_title_search = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    result_list = list()
    for news in news_title_search:
        result_list.append((news["title"], news["url"]))

    return result_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
