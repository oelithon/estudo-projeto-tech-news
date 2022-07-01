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
    news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news_list = []

    for one_news in news:
        news_list.append((one_news["title"], one_news["url"]))

    return news_list


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    news_list = []

    for one_news in news:
        news_list.append((one_news["title"], one_news["url"]))

    return news_list
