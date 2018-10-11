# rake-ja
Rapid Automatic Keyword Extraction algorithm for Japanese.

This module builds on [rake-nltk](https://github.com/csurfer/rake-nltk).


## Setup

```sh
$ git clone https://github.com/kanjirz50/rake-ja.git
$ cd rake-ja
$ python setup.py install
```

## Quick start

```python
>>> from rake_ja import JapaneseRake, Tokenizer
>>> tok = Tokenizer()
>>> ja_rake = JapaneseRake()
>>> # Wikipediaの記事から引用
>>> text = """「人工知能」という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。
現在では、記号処理を用いた知能の記述を主体とする情報処理や研究でのアプローチという意味あいでも使われている。
日常語としての「人工知能」という呼び名は非常に曖昧なものになっており、多少気の利いた家庭用電気機械器具の制御システムやゲームソフトの思考ルーチンなどがこう呼ばれることもある。"""
>>> tokens = tok.tokenize(text)
>>> ja_rake.extract_keywords_from_text(tokens)
>>> ja_rake.get_ranked_phrases_with_scores()
[(25.0, '家庭 用 電気 機械 器具'),
 (9.0, 'ダート マス 会議'),
 (4.0, '記号 処理'),
 (4.0, '日常 語'),
 (4.0, '思考 ルーチン'),
 (4.0, '制御 システム'),
 (4.0, 'ゲーム ソフト'),
 (3.5, '人工 知能'),
 (1.5, '知能'),
 (1.0, '記述'),
 (1.0, '研究'),
 (1.0, '用い'),
 (1.0, '現在'),
 (1.0, '気'),
 (1.0, '意味あい'),
 (1.0, '情報処理'),
 (1.0, '命名'),
 (1.0, '呼び名'),
 (1.0, '名前'),
 (1.0, '主体'),
 (1.0, 'マッカーシー'),
 (1.0, 'ジョン'),
 (1.0, 'アプローチ'),
 (1.0, '1956')]
```
