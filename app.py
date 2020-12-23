import streamlit as st
import os
import requests
import urllib.parse

st.title('Wolfram to the rescue')

st.write('Simply amazing Wolfram Alpha Engine can help you to solve many of the scientific \
    tasks one will encounter in the college and university. Use it wisely \
    besides providing the right answer it shows also the calculations steps. \
    Enjoy the journey too.  Some of the options:')

st.markdown('- area of a circle with radius 2')
st.markdown('- equation of line through (2, 5), (4, 1)')
st.markdown("- 2x + 3 = 11")
st.markdown("- glucose + oxygen -> water + carbon dioxide")
st.markdown("- is 73 prime?")

equation = st.text_input("Enter the task you are trying to solve:", "y' = y^2 x")

query = urllib.parse.quote_plus(f"solve {equation}")
query_url = f"http://api.wolframalpha.com/v2/query?" \
            f"appid={os.environ['WOLFRAM_API_KEY']}" \
            f"&input={query}" \
            f"&scanner=Solve" \
            f"&podstate=Result__Step-by-step+solution" \
            "&format=image" \
            f"&output=json"

r = requests.get(query_url).json()

# st.write(r)

pic = r["queryresult"]["pods"][0]["subpods"][1]['img']['src']
st.image(pic, width=300)
