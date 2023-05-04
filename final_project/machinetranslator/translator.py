"""This module is used to translate input text between English and French"""
import json
import os
from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an instance of IBM Watson Language translator:
authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version = '2023-05-04',
    authenticator = authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """This method translates a string input from English to French"""
    try:
        translation =  language_translator.translate(
            text= english_text,
            model_id="en-fr"
        ).get_result()

        return translation["translations"][0]["translation"]

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def french_to_english(french_text):
    """This method translates a string input from French to English"""
    try:
        translation = language_translator.translate(
            text= french_text,
            model_id="fr-en"
        ).get_result()

        return translation["translations"][0]["translation"]

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
