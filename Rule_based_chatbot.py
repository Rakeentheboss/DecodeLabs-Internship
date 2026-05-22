#make a rule based chatbot
#continuous while command for input loop
#Handle cases and white spaces
#Dictionary with 5+ intents
#clean break command
# use if else logic to respond to user input




import re
import random
import streamlit as st



# Define a dictionary of intents and responses
intents = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "help": ["I can help you with currency related queries. What do you need assistance with?"],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?"],
    "currency of United States": ["The currency of the United States is the US Dollar (USD)."],
    "currency of United Kingdom": ["The currency of the United Kingdom is the British Pound (GBP)."],
    "currency of Japan": ["The currency of Japan is the Japanese Yen (JPY)."],
    "currency of European Union": ["The currency of the European Union is the Euro (EUR)."],
    "currency of India": ["The currency of India is the Indian Rupee (INR)."],
    "currency of China": ["The currency of China is the Chinese Yuan (CNY)."],
    "exchange_rate of USD and EUR": ["The current exchange rate for USD to EUR is 0.85."],
    "exchange_rate of GBP and USD": ["The current exchange rate for GBP to USD is 1.39."],
    "exchange_rate of JPY and USD": ["The current exchange rate for JPY to USD is 0.0091."],
    "exchange_rate of EUR and USD": ["The current exchange rate for EUR to USD is 1.18."],
    "exchange_rate of INR and USD": ["The current exchange rate for INR to USD is 0.013."],
    "exchange_rate of CNY and USD": ["The current exchange rate for CNY to USD is 0.15."],
    "exchange_rate of USD and GBP": ["The current exchange rate for USD to GBP is 0.72."]
}


# use re to clean user input
#use if-else loop to match user input to intents
#integrate streamlit

def get_intent(user_input):
    #The, what and other common words can be ignored in the user input to improve intent matching

    st.user_input = user_input.lower().strip()
    # keep conjunctions 'and' and 'to' because they matter for exchange-rate queries
    user_input = re.sub(r'\b(the|what|is|are|of|in|for|on|with|a|an)\b', '', st.user_input)
    while(True):
        if re.search(r'\b(hi|hello|hey)\b', st.user_input):
            return "greeting"
        elif re.search(r'\b(bye|goodbye|see you)\b', st.user_input):
            return "goodbye"
        elif re.search(r'\b(thanks|thank you)\b', st.user_input):
            return "thanks"
        elif re.search(r'\b(help|assist|support)\b', st.user_input):
            return "help"
        elif re.search(r'\bcurrency of (united states|usa|us)\b', st.user_input):
            return "currency of United States"
        elif re.search(r'\bcurrency of (united kingdom|uk|britain)\b', st.user_input):
            return "currency of United Kingdom"
        elif re.search(r'\bcurrency of japan\b', st.user_input):
            return "currency of Japan"
        elif re.search(r'\bcurrency of european union\b', st.user_input):
            return "currency of European Union"
        elif re.search(r'\bcurrency of india\b', st.user_input):
            return "currency of India"
        elif re.search(r'\bcurrency of china\b', st.user_input):
            return "currency of China"
        
        #avoid prepositions and conjunctions in exchange rate queries to improve intent matching

        # accept both 'and' and 'to', and allow optional 'of' after 'exchange rate'
        elif re.search(r"\bexchange rate(?: of)? (?:usd|dollar) (?:and|to) (?:eur|euro)\b", st.user_input):
            return "exchange_rate of USD and EUR"   
        elif re.search(r"\bexchange rate(?: of)? (?:gbp|pound) (?:and|to) (?:usd|dollar)\b", st.user_input):
            return "exchange_rate of GBP and USD"
        elif re.search(r"\bexchange rate(?: of)? (?:jpy|yen) (?:and|to) (?:usd|dollar)\b", st.user_input):
            return "exchange_rate of JPY and USD"
        elif re.search(r"\bexchange rate(?: of)? (?:eur|euro) (?:and|to) (?:usd|dollar)\b", st.user_input):
            return "exchange_rate of EUR and USD"
        elif re.search(r"\bexchange rate(?: of)? (?:inr|rupee) (?:and|to) (?:usd|dollar)\b", st.user_input):
            return "exchange_rate of INR and USD"
        elif re.search(r"\bexchange rate(?: of)? (?:cny|yuan) (?:and|to) (?:usd|dollar)\b", st.user_input):
            return "exchange_rate of CNY and USD"
        elif re.search(r"\bexchange rate(?: of)? (?:usd|dollar) (?:and|to) (?:gbp|pound)\b", st.user_input):
            return "exchange_rate of USD and GBP"
        else:
            return "I am sorry I don't understand that. Please try asking in a different way or type 'help' for assistance."
        

def get_response(intent):
    if intent in intents:
        return random.choice(intents[intent])
    else:
        return random.choice(intents["default"])
    
def main():
    st.title("Rule-Based Chatbot")
    st.write("Ask me about currency and exchange rates!")
    st.write("Type 'exit' to end the conversation.")
    st.write("I mainly work with currency of United States, United Kingdom, Japan, European Union, India, China and exchange rates between USD, EUR, GBP, JPY, INR and CNY.")

    user_input = st.text_input("You: ")
    if user_input:
        intent = get_intent(user_input)
        response = get_response(intent)
        st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    main()          