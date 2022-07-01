from tech_news.database import search_news
from datetime import datetime


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
# https://docs.python.org/3/library/datetime.html
def format_date(date):
    datetime.fromisoformat(date)
    months = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro",
    }

    year, month = date[0:4], date[5:7]
    day = date[8:10] if date[8] != "0" else date[9:10]

    date_formated = f"{day} de {months[month]} de {year}"

    return date_formated


def search_by_date(date):
    try:
        date_formated = format_date(date)
        news = search_news({"timestamp": {"$regex": date_formated}})
        news_list = []

        for one_news in news:
            news_list.append((one_news["title"], one_news["url"]))

        return news_list
    except ValueError:
        raise ValueError("Data inválida")


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
