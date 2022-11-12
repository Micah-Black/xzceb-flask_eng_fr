"""Translator App"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = '2018-05-01'

language_translator = LanguageTranslatorV3 (apikey, url, version)
language_translator.list_identifiable_languages().get_result()
def english_to_french(english_text):
    """English To French Command"""
    english_text = input("Hello")
    french_text = language_translator.translate(text = english_text, model_id = 'en-fr')
    return french_text

def french_to_english(french_text):
    """French To English Command"""
    french_text = input("Bonjour")
    english_text = language_translator.translate(text = french_text, model_id = 'fr-en')
    return english_text
