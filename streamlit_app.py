import streamlit as st

st.title('🎈 Machine Learning App')
st.info('This is a Machine learning Model')
with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

