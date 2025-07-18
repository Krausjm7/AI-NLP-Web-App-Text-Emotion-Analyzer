''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from SentimentAnalysis import sentiment_analyzer

# Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    # The 'textToAnalyze' variable name comes from mywebscript.js
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Check for errors from your sentiment_analyzer function
    if 'error' in response:
        # Return a user-friendly error message if sentiment_analyzer failed
        return f"Error analyzing sentiment: {response['error']}"

    # Extract the label and score from the response dictionary
    label = response['label']
    score = response['score']

    # Format the label (e.g., 'SENT_POSITIVE' -> 'POSITIVE') by splitting on '_'
    formatted_label = label.split('_')[1]

    # Return a formatted string with the sentiment label and score
    # Round the score for cleaner display
    return "The given text has been identified as {} with a score of {}.".format(formatted_label, round(score, 4))


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)