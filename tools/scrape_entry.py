from typing import Callable
import requests
import pyquery
import normality 
from markdownify import markdownify as md


def scrape_entry(entry_id: str, on_exception: Callable) -> str:
    try:
        url = f'https://plato.stanford.edu/entries/{entry_id}'
        document = pyquery.PyQuery(requests.get(url).text)
        html = document.find('#main-text').html()
        markdown = md(html, heading_style='ATX', strip=['a'])
        markdown = normality.ascii_text(markdown)

        return markdown
    except Exception as e:
        on_exception(e)
