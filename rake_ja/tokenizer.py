import MeCab
from collections import namedtuple


Morpheme = namedtuple("Morpheme", "surface pos pos_s1 pos_s2 pos_s3 conj form")


class Tokenizer:
    def __init__(self, **kwargs):
        self.__mecab = MeCab.Tagger(**kwargs)
        self.__mecab.parse("Initialize parse.")

    def tokenize(self, text):
        return [m for m in self.__iter_morpheme(text)]

    def __iter_morpheme(self, text):
        node = self.__mecab.parseToNode(text)
        node = node.next
        while node.next:
            surface = node.surface
            features = node.feature.split(",")

            yield Morpheme(surface, *features[:6])

            node = node.next
