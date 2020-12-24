import streamlit as st
import os
import requests
import urllib.parse

st.title('Wolfram to the rescue')

st.write('Simply amazing Wolfram Alpha Engine can help you to solve many of the scientific \
    tasks one will encounter in the college and university. Use it wisely \
    besides providing the right answer it shows also the calculations steps. \
    Enjoy the journey too.  Some of the options:')

st.markdown("- solve 2x + 3 = 11")
st.markdown("- solve y' = y^2 x")
st.markdown('- area of a circle with radius 2')
st.markdown('- equation of line through (2, 5), (4, 1)')
st.markdown("- is 73 prime?")

st.markdown("[More examples from Wolfram](https://www.wolframalpha.com/examples/pro-features/step-by-step-solutions/)")

equation = st.text_input("Enter the task you are trying to solve:", "")

pic = ''

if equation != '':
    query = urllib.parse.quote_plus(f"{equation}")
    query_url = f"http://api.wolframalpha.com/v2/query?" \
                f"appid={os.environ['WOLFRAM_API_KEY']}" \
                f"&input={query}" \
                f"&podstate=Result__Step-by-step+solution" \
                "&format=image" \
                f"&output=json"

    r = requests.get(query_url).json()

    for i in r["queryresult"]["pods"]:
        for i2 in i['subpods']:
            if i2['title'] == 'Possible intermediate steps':
                pic = i2['img']['src']

# st.write(pic)
if pic != '':
    st.image(pic, width=300)
