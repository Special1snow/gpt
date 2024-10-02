
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = 'AI를 활용한 HR솔루션 기능요건정의 (SKGC).xlsx'
xls = pd.ExcelFile(file_path)

df_skillset = pd.read_excel(xls, '직무별SkillSet')
df_self_review = pd.read_excel(xls, 'Self Review')
df_education_db = pd.read_excel(xls, '교육DB')

# Dashboard title
st.title('HR Dashboard with AI-Powered Insights')

# Sidebar for selecting sheets to display
option = st.sidebar.selectbox(
    'Which data would you like to explore?',
    ('직무별SkillSet', 'Self Review', '교육DB')
)

if option == '직무별SkillSet':
    st.header('직무별SkillSet')
    
    st.write("Skillset data across various departments.")
    
    # Display dataframe
    st.dataframe(df_skillset)
    
    # Heatmap of skill proficiency across departments
    st.subheader('Skill Proficiency Heatmap')
    plt.figure(figsize=(10,6))
    sns.heatmap(df_skillset.iloc[:, 2:], annot=True, cmap="coolwarm", fmt=".1f")
    st.pyplot(plt)

elif option == 'Self Review':
    st.header('Self Review')
    
    st.write("Self review and skill assessment comparison.")
    
    # Display dataframe
    st.dataframe(df_self_review)
    
    # Bar chart: Self review scores vs average department score
    st.subheader('Self Review Scores Comparison')
    fig, ax = plt.subplots()
    df_self_review['Self Review'].plot(kind='bar', ax=ax, color='skyblue', label='Self Review')
    df_self_review['환산점수'].plot(kind='bar', ax=ax, color='orange', alpha=0.5, label='Converted Score')
    ax.legend()
    st.pyplot(fig)

elif option == '교육DB':
    st.header('교육DB')
    
    st.write("Training and education data overview.")
    
    # Display dataframe
    st.dataframe(df_education_db)
    
    # Bar chart of educational costs across departments
    st.subheader('Educational Costs by Department')
    df_education_db_filtered = df_education_db[df_education_db['비용(만원)'] > 0]
    fig, ax = plt.subplots()
    df_education_db_filtered.groupby('사업부')['비용(만원)'].sum().plot(kind='bar', ax=ax, color='green')
    ax.set_ylabel('Cost (만원)')
    st.pyplot(fig)
    
# Footer
st.write("Dashboard created with Streamlit.")
