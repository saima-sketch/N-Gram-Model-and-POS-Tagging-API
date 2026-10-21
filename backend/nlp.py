
import nltk

def ensure_nltk_data():
    resources = [
        ("tokenizers/punkt_tab", "punkt_tab"),
        ("taggers/averaged_perceptron_tagger_eng",
         "averaged_perceptron_tagger_eng"),
    ]

    for resource_path, package in resources:
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(package, quiet=True)


ensure_nltk_data()


def perform_pos_tagging(text):
    tokens = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)

    descriptions = {
        "NN": "Noun",
        "NNS": "Plural Noun",
        "NNP": "Proper Noun",
        "NNPS": "Plural Proper Noun",
        "VB": "Verb",
        "VBD": "Past Tense Verb",
        "VBG": "Gerund / Present Participle",
        "VBN": "Past Participle",
        "VBP": "Present Verb",
        "VBZ": "Third-Person Singular Verb",
        "JJ": "Adjective",
        "JJR": "Comparative Adjective",
        "JJS": "Superlative Adjective",
        "RB": "Adverb",
        "RBR": "Comparative Adverb",
        "RBS": "Superlative Adverb",
        "PRP": "Personal Pronoun",
        "PRP$": "Possessive Pronoun",
        "DT": "Determiner",
        "IN": "Preposition / Subordinating Conjunction",
        "CC": "Coordinating Conjunction",
        "CD": "Cardinal Number",
        "MD": "Modal Verb",
        "TO": "To",
        "RP": "Particle",
        "UH": "Interjection",
        "WDT": "Wh-Determiner",
        "WP": "Wh-Pronoun",
        "WRB": "Wh-Adverb",
        ".": "Punctuation",
        ",": "Comma",
        ":": "Colon",
        "POS": "Possessive Ending",
        "EX": "Existential There",
        "SYM": "Symbol",
    }

    results = []

    for word, tag in tagged_words:
        results.append({
            "word": word,
            "tag": tag,
            "description": descriptions.get(tag, "Other")
        })

    return {
        "input_text": text,
        "tokens": tokens,
        "results": results
    }
