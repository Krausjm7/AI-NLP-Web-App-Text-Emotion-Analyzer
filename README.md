# AI-NLP-Web-App-Text-Emotion-Analyzer

This is a web application I developed to perform sentiment analysis on text, leveraging an AI NLP Model. It provides a simple, interactive interface where users can input text and receive an immediate sentiment classification (positive, negative, or neutral) along with a confidence score.

## Business Purpose
The primary business purpose of this application is to enable quick and efficient **sentiment analysis** of textual data. This can be invaluable for:

* **Customer Feedback Analysis**: Understanding the general sentiment in customer reviews, support tickets, or social media mentions to gauge satisfaction and identify areas for improvement.

* **Brand Monitoring**: Tracking public perception of a brand, product, or service over time.

* **Market Research**: Gaining insights into opinions and attitudes towards specific topics or trends.

* **Content Moderation**: Identifying potentially harmful or negative content in user-generated text.

By automating sentiment detection, this tool helps businesses and individuals quickly extract meaningful insights from large volumes of unstructured text data, facilitating better decision-making and more targeted actions.

## Technical Stack
My project is built using a combination of Python for the backend logic and a pre-trained AI model for natural language processing.

* **Python 3.11**: The core programming language for the application logic.

* **Flask**: A lightweight Python web framework used to build the web interface and handle HTTP requests and responses.

* **IBM Watson Natural Language Processing (NLP) Library for Embed (BERT Sentiment Analysis)**: This is the powerful AI engine behind the sentiment analysis. I interact with this pre-deployed service via HTTP POST requests to analyze the text.

* **`requests` library**: Used in Python to make HTTP requests to the Watson NLP service.

* **`json` library**: Utilized for parsing the JSON responses received from the AI service.

* **`unittest` framework**: Employed for unit testing the sentiment analysis function, ensuring its accuracy and reliability.

* **`Pylint`**: Used for static code analysis to ensure adherence to PEP 8 style guidelines and maintain high code quality.

* **HTML/CSS/JavaScript**: A simple front-end provides the user interface for text input and displaying results.

## How to Clone and Run This Project
To get a local copy of this project up and running, follow these steps:

### Prerequisites
* Git installed on your system.

* Python 3.11 installed.

* `pip` (Python package installer).

### Cloning the Repository
1.  **Open your terminal or command prompt.**

2.  **Navigate to the directory** where you want to store the project.

3.  **Clone the repository** using the following command:

    ```bash
    git clone [https://github.com/Krausjm7/AI-NLP-Web-App-Text-Emotion-Analyzer.git](https://github.com/Krausjm7/AI-NLP-Web-App-Text-Emotion-Analyzer.git)

    ```

4.  **Change into the project directory**:

    ```bash
    cd AI-NLP-Web-App-Text-Emotion-Analyzer

    ```

### Setting Up the Environment and Running the Application

1.  **Install the required Python libraries**:

    ```bash
    python3.11 -m pip install requests flask pylint

    ```

2.  **Run the Flask application**:

    ```bash
    python3.11 server.py

    ```

    You will see output indicating that the Flask development server has started, typically on `http://0.0.0.0:5000`.

3.  **Access the web application**:
    Open your web browser and go to `http://localhost:5000`. If you are running this in a cloud environment like Skills Network Labs, you might need to use a "Launch Application" button or similar mechanism provided by the environment, specifying port `5000`.

4.  **Interact with the app**:
    Enter text into the input field and click "Run Sentiment Analysis" to see the sentiment results.

### Running Unit Tests (Optional)

To verify the core sentiment analysis logic, you can run the unit tests:

1.  **Ensure you are in the `AI-NLP-Web-App-Text-Emotion-Analyzer` directory.**

2.  **Execute the test file**:

    ```bash
    python3.11 test_sentiment_analysis.py

    ```

    You should see output indicating that the tests passed.
