import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

# st.title("Hello World APP")

# st.header('st.button')

# if st.button('Say hello'):
#     st.write('Why Hello there')
# else:
#     st.write('Bye')

## day 5

import numpy as np
import pandas as pd 
import altair as alt 


# st.header('st.write')
# st.write('Hello, *World* :sunglasses:')

# st.write(124)

# df = pd.DataFrame({
#     'first column: ' : [1,24,4],
#     'second column: ' : [2,4,6]
# })
# st.write(df)

# df2 = pd.DataFrame(
#     np.random.rand(200,3),
#     columns=['a','b','c']
# )

# c = alt.Chart(df2).mark_circle().encode(
#     x = 'a' , y='b' , size = 'c' , color = 'c' , tooltip=['a','b','c']
# )

# st.write(c)

# st.markdown('Hello from the other world')
# st.header('Hello from the star')
# st.subheader('Hello from the moon')
# st.caption('Hi all')
# st.text('Basic')
# st.latex('My latex line')
# st.code('x=4')

# day 6
# deploy in GitHub

# day 7 
# deploy app in cloud community

# day 8

from datetime import datetime, time

# st.header('st.slider')

# age = st.slider('How old are you?' , 1 ,130,25)

# st.write('I am ' , age)

# values = st.slider(
#     'select a range',
#     0.0 , 100.0,(25.0,75.0))

# st.write('values selected ', values)


# app = st.slider(
#     'set appointment ',
#     value=(time(11,30), time(12,45))
# )

# st.write(' Your schedual is ' , app)

# st_time = st.slider(
#     'when do you start ?',
#     value = datetime(2020,1,1,9,30),
#     format="MM/DD/YY - hh:mm"
# )

# st.write(st_time)

# color = st.select_slider(
#     "Select a color of the rainbow",
#     options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
# st.write("My favorite color is", color)

# start_color, end_color = st.select_slider(
#     "Select a range of color wavelength",
#     options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
#     value=("red", "blue"))
# st.write("You selected wavelengths between", start_color, "and", end_color)

# day 9

# st.write('line chart')

# chart_data = pd.DataFrame(
#     np.random.rand(20,3),
#     columns = ['a','b','c'],
# )

# st.line_chart(chart_data)

# day 10


# st.write('st.selectbox')

# opt = st.selectbox('whats fav color', 
#                    ('Blue' , 'Red' , 'Green'),
#                    index=None)

# st.write('your color is ' , opt)

# if 'visibility' not in st.session_state:
#     st.session_state.visibility = 'visible'
#     st.session_state.disabled = False

# col1 , col2 = st.columns(2)

# with col1 :
#     st.checkbox ('Disable select box widget' , key = 'disabled')
#     st.radio('set selectbox label visibility :thumbsup:',
#              key='visibilty',
#              options=['visible', 'hidden', 'collapsed'])


# with col2 :
#     options = st.selectbox("How to be contacted",
#                            ('mobile','Email','home'),
#                            label_visibility=st.session_state.visibility,
#                            disabled=st.session_state.disabled
#                            )




# day 11

# st.header('st.multiselect')

# options = st.multiselect(
#     'what is ur fav color',
#     ['Green', 'yellow', 'Blue','Red'],
#     ['Red','Blue']

# )

# st.write('you selected :')
# for i in options:
#     st.write(i) 



# day 12

# st.header('st.checkbox')

# st.write('What do you want to order ')

# ic = st.checkbox('Ice Cream')
# coff = st.checkbox('Coffee')
# cola = st.checkbox('Cola')

# if ic :
#     st.write(':icecream:')
# if coff:
#     st.write(':coffee:')
# if cola:
#     st.write(':beer:')



# day 13
#Spin up a cloud development environment


# day 14
# Streamlit component 

# from ydata_profiling import ProfileReport

# from streamlit_pandas_profiling import st_profile_report

# st.header('pandas profiling')

# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')


# pr = df.profile_report()

# st_profile_report(pr)



# day 15

# st.header('st.latex')

# st.latex(r''''
#          a +ar + a r^3 + \cdots + a r^{n-1} = 
#          \sum_{k=0}^{n-1} ar^k =
#          a \left(\frac{1-r^{n}}{1-r}\right)
         
#           ''')

# day 16
# customize the theme of streamlit 

# st.write('Customize theme')

# st.code("""
#     [theme]
#         primaryColor ="#F39C12"
#         backgroundColor = "#2E86C1"
#         secondryBackgroundColor = "#AED6F1"
#         textyColor = "#FFFFFF"
#         font = "monospace"
#  """)

# numb = st.sidebar.slider('select number ', 0,14,5)

# st.write('selected num ' ,numb)


# day 17

# st.header('st.secrets')

# new_var = st.secrets['message']
# st.write(new_var)

# day 18

# st.header('st.file_uploader')

# st.subheader('csv')

# uploaded_file = st.file_uploader("Choose a file ")

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.subheader('DataFrame')
#     st.write(df)
#     st.subheader('Descriptive Statistics')
#     st.write(df.describe())
# else:
#     st.info(':thumbsup: UPload CSV file')


# fileas= st.file_uploader('Choose multi files ' , accept_multiple_files=True)

# for files in fileas:
#     st.write("filename : ", files.name) 
   

# day 19


# st.set_page_config(layout="wide")

# st.title("How to layout streamlit")


# with st.expander('About this app'):
#     st.write('This is app shows how you layout streamlit ')
#     st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)



# st.sidebar.header('Input')

# userName = st.sidebar.text_input('Whats ur name')
# userEmoji = st.sidebar.selectbox('choose emoji' , ['','😂','❤️','👍'])
# userFood = st.sidebar.selectbox('Whats ur fav food' , ['','Tom Yum', 'Biryani','Pasta'])


# st.header('Output')

# col1 , col2 , col3 = st.columns(3)

# with col1:
#     if userName != '':
#         st.write('Hello ' , userName)
#     else:
#         st.warning('Enter your name')

# with col2 :
#     if userEmoji != '':
#         st.write(userEmoji , " is ur fav **Emoji**")
#     else:
#         st.write('Please choose ur fav *Emoji*')

# with col3: 
#     if userFood != '':
#         st.write(userFood , ' is ur fav **food**')
#     else:
#         st.write ("Choose ur fav foods")


# ## testing modals ## #


# @st.experimental_dialog("cast your vote")
# def vote(str):
#     st.write('why is ' , str , ' ur fav?')
#     res = st.text_input('Beacuse .... ')
#     if st.button("Submit"):
#         st.session_state.vote = {'item':str, 'reason':res}
#         st.rerun()

# if "vote" not in st.session_state:
#     st.write("Vote for your fav")
#     if st.button("A"):
#         vote('A')
#     if st.button("B"):
#         vote('B')
# else:
#     f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"


# day 20



































