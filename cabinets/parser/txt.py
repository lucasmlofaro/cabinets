from cabinets.parser import register_extensions, Parser


@register_extensions('txt')
class PlainTextParser(Parser):

    @classmethod
    def load_content(cls, content):
        return content.decode()

    @classmethod
    def dump_content(cls, data, encoding='utf-8'):
        return bytes(data, encoding=encoding)
