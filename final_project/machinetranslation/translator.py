from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    The method translate input as English text the output is a French text
    """
    french_text = MyMemoryTranslator(source='en',target='fr').translate(english_text)
    print(french_text)
    #write the code here
    return french_text

def french_to_english(french_text):
    """
    The method translate input as French text the output is a English text
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    #write the code here
    return english_text
