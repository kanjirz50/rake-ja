import string

from itertools import chain, groupby
from rake_nltk import Rake, Metric


class JapaneseRake(Rake):
    def __init__(
        self,
        stopwords=None,
        punctuations=None,
        ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO,
        max_length=100000,
        min_length=1,
    ):
        if isinstance(ranking_metric, Metric):
            self.metric = ranking_metric
        else:
            self.metric = Metric.DEGREE_TO_FREQUENCY_RATIO

        self.stopwords = stopwords
        if self.stopwords is None:
            self.stopwords = "か な において にとって について する これら から と も が は て で に を は し た の ない よう いる という により 以外 それほど ある 未だ さ れ および として といった られ この ため こ たち ・ ご覧".split()

        self.punctuations = punctuations
        if self.punctuations is None:
            self.punctuations = string.punctuation + "。、"

        self.to_ignore = set(chain(self.stopwords, self.punctuations))

        self.min_length = min_length
        self.max_length = max_length

        self.frequency_dist = None
        self.degree = None
        self.rank_list = None
        self.ranked_phrases = None

    def extract_keywords_from_text(self, text):
        sentences = [list(g) for k, g in groupby(text, lambda x: x.surface not in set(["!", "。"]))]
        self.extract_keywords_from_sentences(sentences)

    def _generate_phrases(self, tokens_of_sentences):
        phrase_list = set()
        # Create contender phrases from sentences.
        for tokens in tokens_of_sentences:
            phrase_list.update(self._get_phrase_list_from_words(tokens))
        return phrase_list

    def _group_tokens_to_str(self, group):
        return tuple([token.surface for token in group])

    def _get_phrase_list_from_words(self, word_list):
        groups = groupby(word_list, lambda x: self._is_ignore(x))
        phrases = [self._group_tokens_to_str(group[1]) for group in groups if group[0]]
        return list(
            filter(
                lambda x: self.min_length <= len(x) <= self.max_length, phrases
            )
        )

    def _is_ignore(self, token):
        if token.surface in self.to_ignore:
            return False
        if token.pos_s2 == "助数詞":
            return False
        if token.pos == "名詞" and token.pos_s1 not in set(["代名詞", "非自立", "形容動詞語幹"]):
            return True
        if token.pos == "動詞" and token.pos_s1 == "自立" and token.form == "連用形":
            return True
        return False
