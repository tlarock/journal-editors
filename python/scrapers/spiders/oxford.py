"""Oxford journals' editorial boards scrapper."""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import Compose, TakeFirst, MapCompose
from taukit.webscraping.spidercls import TauSpiderMixin
from taukit.webscraping.selectors import CSS
from ..items import EditorItemLoader


class OxfordEditorItemLoader(EditorItemLoader):
    """Oxford editor item loader."""
    publisher = 'Oxford'

    container_sel = CSS("html")
    journal_sel = CSS("head > title::text")
    editors_sel = CSS("div#ContentColumn")
    # Input processors
    journal_in = MapCompose()
    # Output processors
    journal_out = Compose(
        TakeFirst(),
        lambda x: x.split("|")[1].strip()
    )
    editors_out = TakeFirst()


class OxfordEditorsSpider(TauSpiderMixin, CrawlSpider):
    """Oxford Editors spider."""
    name = 'oxford'
    item_loader = OxfordEditorItemLoader
    start_urls = ['https://academic.oup.com/journals/pages/journals_a_to_z']
    allowed_domains = ['oup.com']

    # pylint: disable=bad-continuation
    rules = (
        Rule(LinkExtractor(
            allow='oup.com',
            restrict_css="div#ContentColumn p > a"
        ), follow=True),
        Rule(LinkExtractor(
            allow=('oup.com/.*?/Editorial_Board'),
            restrict_css="nav.navbar-menu ul.site-menu > li.site-menu-item"
        ), follow=True, callback='parse_editors')
    )

    def parse_editors(self, response):
        item = self.parse_item(response)
        return item
