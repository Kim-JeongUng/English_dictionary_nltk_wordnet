import nltk
import re

nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet as wn

wd = []
print("Enlish Dictionary")
print("단어를 입력하세요. (0을 눌러 종료)")

while True:
    input_word = input()
    if input_word == '0':
        break
    wd.append(input_word)

cnt = 0;
print("----------------------------------------------------------------------")

wordnet_map = {
    "noun.": wn.NOUN,
    "verb.": wn.VERB,
    "adj.": wn.ADJ,
    "adv.": wn.ADV
}


def pos_tag_wordnet(text):
    """
        Create pos_tag with wordnet format
    """
    pos_tagged_text = nltk.pos_tag(text)

    pos_tagged_text = [
        (word, wordnet_map.get(pos_tag[0])) if pos_tag[0] in wordnet_map.keys()
        else (word, wn.NOUN)
        for (word, pos_tag) in pos_tagged_text
    ]

    return pos_tagged_text


def antonyms_for(word):
    antonyms = []
    for ss in wn.synsets(word):
        for lemma in ss.lemmas():
            any_pos_antonyms = [antonym.name() for antonym in lemma.antonyms()]
            for antonym in any_pos_antonyms:
                antonym_synsets = wn.synsets(antonym)
                if wn.ADJ not in [ss.pos() for ss in antonym_synsets]:
                    continue
                antonyms.append(antonym)
    return antonyms


for w in wd:
    try:
        word_temp = wn.synsets(w)[0]
    except:
        word_temp = ""

    cnt += 1
    print(cnt, ".", w)
    print('- Spelling and Part of Speech(철자 및 품사):', w, "(",pos_tag_wordnet(wd)[cnt - 1][1],")")
    try:
        definition = word_temp.definition()
    except:
        definition = ""
    print('- Definition(뜻) : ', definition)

    try:
        Synoymous = word_temp.lemma_names()[1]
    except:
        Synoymous = ""

    try:
        antonyms = antonyms_for(w)[0]
    except:
        antonyms = ""
    print('- Synonymous/Antonym(동의어/반의어): ', Synoymous, "/", antonyms)

    try:
        wd_example = word_temp.examples()[0]
    except:
        wd_example = ""
    print('- Example Sentence(예문) : ', wd_example, '\n')

