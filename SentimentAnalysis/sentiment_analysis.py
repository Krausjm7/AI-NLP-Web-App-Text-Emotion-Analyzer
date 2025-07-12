"""
This module provides a function to analyze the sentiment of text
using the Watson NLP BERT Sentiment Analysis service.
It handles various response scenarios including valid sentiment,
invalid input leading to a 500 error, and other request/parsing errors.
"""
import requests
import json

def sentiment_analyzer(text_to_analyze):
    """
    Analyzes the sentiment of the given text using the Watson NLP BERT
    Sentiment Analysis function.

    Args:
        text_to_analyze (str): The text string to be analyzed for sentiment.

    Returns:
        dict: A dictionary containing the sentiment 'label' and 'score'.
              Returns {'label': None, 'score': None} for unprocessable input
              (e.g., when the service returns a 500 status code for invalid text).
              Returns {'error': ...} for other network, JSON decoding, or
              unexpected structural issues.
    """
    url = ('https://sn-watson-sentiment-bert.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/SentimentPredict')
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, json=myobj, headers=headers)

        # If the response status code is 500, set label and score to None
        if response.status_code == 500:
            return {'label': None, 'score': None}

        # For other non-200 successful statuses (e.g., 204 No Content) or actual errors (like 4xx),
        # raise an HTTPError that will be caught by the except block below.
        response.raise_for_status()

        # Parse the JSON response from the API
        formatted_response = json.loads(response.text)

        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']

        # Return a dictionary with the extracted label and score
        return {'label': label, 'score': score}

    except requests.exceptions.RequestException as e:
        # Handles network-related errors (e.g., connection refused, timeout)
        # or HTTP errors from raise_for_status()
        return {"error": f"Network or request error: {e}"}
    except json.JSONDecodeError as e:
        # Handles cases where the response is not valid JSON
        # Include response.text for debugging purposes
        return {"error": f"JSON decoding error: {e}. Response text: {response.text}"}
    except KeyError as e:
        # Handles cases where expected keys are missing from the JSON response
        # This means the API response structure was unexpected
        return {"error": f"Missing key in JSON response: {e}. Full response: {formatted_response}"}
    except Exception as e:
        # Catches any other unexpected errors
        return {"error": f"An unexpected error occurred: {e}"}