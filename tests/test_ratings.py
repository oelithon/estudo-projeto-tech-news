from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.database import db
from tests.news import (
    NEWS,
    EXPECTED_NEWS,
    EXPECTED_NEWS_REQ11,
    EXPECTED_NEWS_REQ11_2,
)


# Req.10
def test_listar_as_top_cinco_noticias():
    db.news.delete_many({})

    # é possível buscar as cinco top 5 notícias
    db.news.insert_many(NEWS)
    assert top_5_news() == [EXPECTED_NEWS[i] for i in [8, 7, 9, 1, 0]]

    # caso houver menos de 5 notícias, serão retornadas quantas houverem
    db.news.delete_many({})
    db.news.insert_many(NEWS[:3])
    assert top_5_news() == [EXPECTED_NEWS[i] for i in [1, 0, 2]]

    # retornar vazio caso nao exista noticias
    db.news.delete_many({})
    assert top_5_news() == []


# Req.11
def test_listar_as_top_cinco_categorias():
    db.news.delete_many({})

    # é possível buscar as cinco top 5 categorias
    db.news.insert_many(NEWS)
    assert top_5_categories() in EXPECTED_NEWS_REQ11

    # caso houver menos de 5 categorias, serão retornadas quantas houverem
    db.news.delete_many({})
    db.news.insert_many(NEWS[:-1])

    assert top_5_categories() in EXPECTED_NEWS_REQ11_2

    # buscar top categorias retornar vazio caso nao exista noticias
    db.news.delete_many({})
    assert top_5_categories() == []
