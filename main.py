import requests
import streamlit as st
import json

def main():

    class TextInput:
        def __init__(self, text, temperature, length):
            self.text = text
            self.temperature = temperature
            self.length = length

    st.title('Borgesian')
    st.image('tower_of_babel.jpg')
    st.write('Write a prompt in Russian, and the GPT-based model will follow up with a Borgesian text provided via API.')
    st.write('Define the parameters of generation:')
    temperature = st.slider('Temperature', value = 1.5, min_value = 1.0, max_value = 5.0, step = 0.1)
    length = st.slider('Length', value = 50, min_value = 20, max_value = 250, step = 1)
    user_input = st.text_area("Enter your text:")
    input = {
    "text": user_input,
    "temperature": temperature,
    "length": length
    }
        
    if st.button("Send"):
        if user_input:
            res = requests.post(st.secrets["generate"], json=input)
            data = json.loads(res.content)
            generated_text = data.get('generated', '')
            st.write(generated_text)
        else:
            st.warning("Please enter some text.")

if __name__ == '__main__':
    main()
