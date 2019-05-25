"""Item classes."""
from datetime import datetime
from scrapy import Field
from scrapy.loader.processors import Compose, Join, MapCompose, TakeFirst
from taukit.webscraping.itemcls import Item, ItemLoader
from taukit.utils import make_hash, parse_date
from taukit.webscraping.utils import strip, normalize_web_content, get_url_domain


class EditorsItem(Item):
    """Generic editors item.

    Attributes
    ----------
    """
    hash_id = Field()
    url = Field()
    final_url = Field()
    scraped_at = Field()
    publisher = Field()
    journal = Field()
    editors = Field()


class EditorItemLoader(ItemLoader):
    """Generic editor item loader."""
    publisher = None
    default_item_class = EditorsItem
    # Input processors
    default_input_processor = MapCompose(
        lambda x: normalize_web_content(x, replace=(("\xa0", " "), )),
        strip
    )
    editors_in = MapCompose(strip)
    # Output processors
    editors_out = MapCompose()

    def add_data(self, data):
        self.data = data

    def load_item(self):
        item = super().load_item()
        item['scraped_at'] = datetime.now()
        item['publisher'] = self.publisher
        # item['hash_id'] = make_hash(item['publisher'] + item['journal'])
        return item
