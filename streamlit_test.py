import streamlit as st
import pandas as pd

st.title("Sales Report")

q1_sales = {
    'January': 100,
    'February': 110,
    'March': 115
}

q2_sales = {
    'April': 150,
    'May': 200,
    'June': 250
}

q1_df = pd.DataFrame(q1_sales.items(),columns = ['Month', 'Amount'])
q2_df = pd.DataFrame(q2_sales.items(),columns = ['Month', 'Amount'])


section = st.sidebar.radio('Which section?', ('Text', 'Charts', 'Widgets', 'More Widgets'))

if section == 'Text':
    st.header("Q1 Results")
    st.write('January was the start of the year')
    st.write(q1_sales)
    st.header('Q2 Results')
    st.write('Q2 had better results')
    st.table(q2_df)
    st.dataframe(q2_df)


elif section == 'Charts':
    st.line_chart(q2_df)
    st.area_chart(q2_df)
    st.bar_chart([q1_sales.values(), q2_sales.values()])


elif section == 'Widgets':
    if st.button('Show Q2 Data'):
        st.table(q2_df)
    else:
        st.table(q1_df)

    if st.checkbox('Show Q2 Data'):
        st.line_chart(q2_df)
    else:
        st.line_chart(q1_df)

    quarter = st.radio('Which quarter?', ('Q1', 'Q2'))
    if quarter == 'Q1':
        st.line_chart(q1_df)
    elif quarter == 'Q2':
        st.line_chart(q2_df)

    selected_quarter = st.selectbox('Which quarter?', ('Q1', 'Q2'))
    if selected_quarter == 'Q1':
        st.area_chart(q1_df)
    elif selected_quarter == 'Q2':
        st.area_chart(q2_df)

elif section == 'More Widgets':
    st.write(st.slider('Which quarters?', 1,4, (1,2)))
    st.write(st.multiselect('Choose quarters', ['Q1', 'Q2', 'Q3', 'Q4']))
    st.write(st.number_input('Which quarter?', 1,4))
















