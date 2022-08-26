import pickle
import streamlit as st
wine_model=pickle.load(open('wine_pickle_file','rb'))
st.title('wine Predicton Using ML')
col1,col2,col3 =st.columns(3)
with col1:
    fixed_acidity=st.text_input('Number of  fixed acidity')
with col2:
   volatile_acidity=st.text_input('Number of volatile acidity')
with col3:
    citric_acid=st.text_input('Number of citric acid')
with col1:
    residual_sugar=st.text_input('Number of residual sugar')
with col2:
    chlorides=st.text_input('Number of chlorides')
with col3:
    free_sulphur_dioxide=st.text_input('Number of free sulphur dioxide')
with col1:
    total_sulphur_dioxide=st.text_input('Number of total sulphur dioxide')
with col2:
    density=st.text_input('Number of density')
with col3:
    ph=st.text_input('Nmuber of ph')
with col1:
    sulphates=st.text_input('Number of sulphates')
with col2:
    alcohol=st.text_input('Number of alcohol')
wine_prediction = ''
if st.button('wine Test Result'):
    wine_prediction = wine_model.predict(
        [[fixed_acidity, volatile_acidity ,citric_acid, residual_sugar, chlorides, free_sulphur_dioxide, total_sulphur_dioxide, density, ph, sulphates, alcohol]])

    if (wine_prediction[0] == 1):
        wine_prediction = 'Good Quality Wine'
    else:
        wine_prediction = 'Bad Quality Wine'
st.success(wine_prediction) 
