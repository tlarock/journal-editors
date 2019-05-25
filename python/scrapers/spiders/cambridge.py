"""Cambridge journals' editorial boards scrapper."""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from taukit.webscraping.spidercls import TauSpiderMixin
from taukit.webscraping.selectors import CSS
from ..items import EditorItemLoader


class CambridgeEditorItemLoader(EditorItemLoader):
    """Cambridge editor item loader."""
    publisher = 'Cambridge'

    container_sel = CSS("body")
    journal_sel = CSS("section.banner h1.title::text")
    editors_sel = CSS("div.editorial-position")


class CambridgeEditorsSpider(TauSpiderMixin, CrawlSpider):
    """Cambridge Editors spider."""
    name = 'cambridge'
    item_loader = CambridgeEditorItemLoader
    start_urls = ['https://www.cambridge.org/core/what-we-publish/journals']
    allowed_domains = ['cambridge.org']

    # pylint: disable=bad-continuation
    rules = (
        Rule(LinkExtractor(
            allow='cambridge.org',
            restrict_css="li.product-list-entry a.title"
        ), follow=True),
        Rule(LinkExtractor(
            allow='cambridge.org',
            restrict_css="div.details li > a.blue"
        ), follow=True, callback='parse_editors')
    )

    def parse_editors(self, response):
        item = self.parse_item(response)
        return item
