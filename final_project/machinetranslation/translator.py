
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikeys']
url = os.environ['url']

authenticator = IAMAuthenticator('7WSe0rM-jlGWTB8Bp3NOe51IPejtQr4aLgYwjEkNRGhh')
language_translator = LanguageTranslatorV3(
    version='2018-09-05',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f8e570d5-a158-4bf4-ac99-114d90263509')
def english_to_french(englishText):

    if len(englishText) != 0:
        lang_dict = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
        word_list = lang_dict['translations']
        word_dict = word_list[0]
        frenchText = word_dict['translation']
    else:
        frenchText = None
    return frenchText


def french_to_english(frenchText):

    if len(frenchText) != 0:
        lang_dict = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
        word_list = lang_dict['translations']
        word_dict = word_list[0]
        englishText = word_dict['translation']
    else:
        englishText = None
    return englishText