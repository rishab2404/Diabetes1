# Show complete dataset and summary in 'diabetes_home.py'
# Import the streamlit modules.
import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):
    # Set the title to the home page contents.
    st.title("Early Diabetes Prediction Web App")
    # Provide a brief description for the web app.
    st.write("""Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.
There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.
This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.""")


    # Add the 'beta_expander' to view full dataset 
    st.header("View Data")
    with st.beta_expander("Press To view Data"):
      st.dataframe(diabetes_df)
    


    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
    b1,b2,b3 = st.beta_columns(3)
    with b1:
      if st.checkbox("Show Column Names"):
        st.write(diabetes_df.columns)


    # Add a checkbox in the second column. Display the column data-types of 'diabetes_df' on the click of checkbox.
    with b2:
      if st.checkbox("Show data types"):
        cols_name = st.selectbox("Select Column for data-type",list(diabetes_df.columns))
        st.text(diabetes_df[cols_name].dtype)


    # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
    with b3:
      if st.checkbox("Show column data"):
        column = st.selectbox("Select Column",(diabetes_df.columns))
        st.write(diabetes_df[column])
