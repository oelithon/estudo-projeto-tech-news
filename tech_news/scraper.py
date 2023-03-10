import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
# https://app.betrybe.com/course/computer-science/redes-e-raspagem-de-dados/raspagem-de-dados/ab38ab4e-bdbd-4984-8987-1abf32d85f26/conteudos/726e3190-54a2-4c75-9c93-02eaf6f5367b/analisando-respostas/c6601d00-f015-4445-95fe-0c449f8a551c?use_case=side_bar
# https://devhints.io/css
# https://devhints.io/xpath
def scrape_novidades(html_content):
    selector = Selector(html_content)
    url_list = selector.css("h2.entry-title a::attr(href)").getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    forward_page = selector.css("a.next::attr(href)").get()
    if forward_page:
        return forward_page
    else:
        return None


# Requisito 4
def get_summary(html_content):
    selector = Selector(html_content)
    summary = selector.css("div.entry-content p:nth-child(2) *::text").getall()
    first_paragraph = ""
    for text in summary:
        first_paragraph += text
    return first_paragraph


def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url::text").get()
    comments_count = selector.css(
        "div.post-comments h5.title-block::text"
    ).get()
    summary = get_summary(html_content)
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("div.meta-category span.label::text").get()

    if comments_count:
        comments_count = comments_count.split()[0].strip()
    else:
        comments_count = 0

    newsletter = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return newsletter


# Requisito 5
def get_tech_news(amount):
    url = fetch("https://blog.betrybe.com")
    news_url_list = scrape_novidades(url)
    result = []

    while len(news_url_list) < amount:
        next_page = scrape_next_page_link(url)
        url = fetch(next_page)
        news_url_list.extend(scrape_novidades(url))

    for url_page in news_url_list[:amount]:
        news_content = fetch(url_page)
        news = scrape_noticia(news_content)
        result.append(news)

    create_news(result)
    return result
