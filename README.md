# Rule-Based Chatbot

A simple rule-based chatbot implemented in Python using regular expressions. The bot answers questions about country currencies and some predefined exchange rates. It can be run with Streamlit for a minimal web UI.

## Features

- Recognizes greetings, goodbyes, thanks, and help requests.
- Returns currency information for: United States, United Kingdom, Japan, European Union, India, China.
- Returns hard-coded exchange rates between USD, EUR, GBP, JPY, INR, and CNY.
- Simple intent matching using regular expressions in `Rule_based_chatbot.py`.

## Requirements

- Python 3.8+
- `streamlit` (for the UI)

## Installation


pip install streamlit


## Running the chatbot



You can run the app directly at
https://rakeentheboss-decodelabs-internship-rule-based-chatbot-sgqmcp.streamlit.app/

Type queries like:

- "What is the currency of Japan?"
- "Exchange rate USD to EUR"
- "exchange rate of gbp and usd"

**Dont try to run using command prompt as the API keys are not embedded in the code for security reasons**

## Extending intents

Open `Rule_based_chatbot.py` and modify the `intents` dictionary to add responses, and update the `get_intent()` regexes to recognize new phrases.

## Troubleshooting

- If exchange-rate queries don't match, avoid stripping conjunctions like `and`/`to` — the code already preserves those for matching.
- For a dynamic exchange-rate lookup, replace the hard-coded values with an API call (e.g., exchangeratesapi.io or another provider).

## License

This project is provided as-is for learning and experimentation.
