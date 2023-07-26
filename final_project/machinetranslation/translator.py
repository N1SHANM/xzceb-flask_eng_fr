"""import translator"""
from deep_translator import MyMemoryTranslator
def englishtofrench(englishtext):
    """englishtofrench function translates english to french"""
    trans=MyMemoryTranslator(source='en-GB',target='fr-FR')
    frenchtext=trans.translate(englishtext)
    return frenchtext
def frenchtoenglish(frenchtext):
    """frenchtoenglish function translates french to english"""
    trans=MyMemoryTranslator(source='fr-FR',target='en-GB')
    englishtext=trans.translate(frenchtext)
    return englishtext
