from ..write_text import write_text


def parse_item_category(json, origin):
    if "name" in json:
        write_text(json["name"], origin, comment="Item category name")
