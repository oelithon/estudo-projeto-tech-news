import requests
import time
from parsel import Selector


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
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
