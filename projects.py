import streamlit as st
from PIL import Image

def projects():
    # Custom CSS for inline skill tags
    st.markdown("""
    <style>
    .skill-tag {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background-color: #ededed;
        border-radius: 25px;
        padding: 5px 10px;
        margin-right: 5px;
        margin-bottom: 5px;
        font-size: 12px;
    }
    .skills-container {
        line-height: 2.5;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Example project with skill tags
    project = {
        'title': 'Employee Performance Dashboard Development',
        'date': 'January 2024 - Present',
        'skills': ['OTBI','BI Publisher'],
        'image_path': 'assets/project_1.jpg'  # Update with the correct path
    }
    project_2={
        'title': 'Deciphering the Impact of Hybrid Teaching : Delving into the Crossroads of Intrinsic and Extrinsic Student Motivations',
        'date': 'June 2023 - December 2023',
        'skills': ['Python','R','Data cleaning','Data exploration','Data visualization','Statistical modeling','Machine learning','Streamlit'],
        'image_path': 'assets/latrobe.png'  # Update with the correct path
    }
    project_3={
        'title': 'News classification using PyTorch',
        'date': 'June 2023 - December 2023',
        'skills': ['Python','Deep Learning'],
        'image_path': 'assets/news.jpg'  # Update with the correct path
    }
    project_4={
        'title': 'American University Attendance Risk Prediction',
        'date': 'June 2023 - December 2023',
        'skills': ['Python','Data cleaning','Data exploration','Data visualization','Machine Learning'],
        'image_path': 'assets/americanuni.jpg'  # Update with the correct path
    }
    project_5={
        'title': 'Aspiring minds employability Exploratory Data Analysis',
        'date': 'June 2023 - December 2023',
        'skills': ['Python','R','Data cleaning','Data exploration','Data visualization','Statistical modeling','Machine learning'],
        'image_path': 'assets/amcat.png'  # Update with the correct path
    }
    project_6={
        'title': 'Flipkart Webscraping and Exploratory Data Analysis',
        'date': 'June 2023 - December 2023',
        'skills': ['Python','R','Data cleaning','Data exploration','Data visualization'],
        'image_path': 'assets/flipkart.png'  # Update with the correct path
    }

    st.title('Projects')
    with st.container(border=True):
        image = Image.open(project['image_path'])
        st.image(image, use_column_width=True)
        st.markdown(f"### <center><b style='font-size:15px;font-family:courier new;padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #87c85f, #11678f);'> {project['title']}</b></center>",unsafe_allow_html=True)
        # Render skill tags side by side
        skill_tags_html = ''.join(f'<span class="skill-tag">{skill}</span>' for skill in project['skills'])
        st.markdown(f'<div class="skills-container">{skill_tags_html}</div>', unsafe_allow_html=True)
        st.markdown(f"**Date**: {project['date']}")
        st.markdown("""
        - <b style='font-family:courier new;font-size:15px;'>Spearheaded the development of the Employee Performance Dashboard at Sprezza Solutions Pty Ltd, overseeing the project from HR requirement gathering to design and implementation.</b>
        - <b style='font-family:courier new;font-size:15px;'>Provided HR managers with a real-time, insightful dashboard, improving strategic decision-making and HR efficiency</b>
        """, unsafe_allow_html=True)
        # Add a link to the project's code here if needed
    with st.container(border=True):
        image = Image.open(project_2['image_path'])
        st.image(image, use_column_width=True)
        st.markdown(f"### <b style='font-size:20px;font-family:courier new;'><a href='https://github.com/angad08/Deciphering-the-Impact-of-Hybrid-Teaching-on-student-motivation' style='padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'> {project_2['title']}</a></b>",unsafe_allow_html=True)
        # Render skill tags side by side
        skill_tags_html = ''.join(f'<span class="skill-tag">{skill}</span>' for skill in project_2['skills'])
        st.markdown(f'<div class="skills-container">{skill_tags_html}</div>', unsafe_allow_html=True)
        st.markdown(f"**Date**: {project_2['date']}")
        st.markdown("""
        - <b style='font-family:courier new;font-size:15px;'>Published the research paper titled "Deciphering the Impact of Hybrid Teaching," receiving accolades from esteemed PhD professors and the Vice Chancellor at La Trobe University.</b>
        - <b style='font-family:courier new;font-size:15px;'>Recipient of the prestigious "Golden Key Academic Excellence Award 2022" by the Golden Key International Honour Society - Asia Pacific, recognizing outstanding academic achievement.</b>
        - <b style='font-family:courier new;font-size:15px;'>Graduated with distinction as one of the top 5 performers in the Master of Data Science program at La Trobe University, showcasing exceptional academic prowess.</b>
        """, unsafe_allow_html=True)

        # Add a link to the project's code here if needed
    with st.container(border=True):
        image = Image.open(project_3['image_path'])
        st.image(image, use_column_width=True)
        st.markdown(f"### <center><b style='font-size:20px;font-family:courier new;'><a href='https://colab.research.google.com/drive/1VBLtd8XAnda6Yf8shM6xh0QjQ1Hn6Kyd?usp=sharing' style='padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #87c85f, #11678f);'> {project_3['title']}</a></b></center>",unsafe_allow_html=True)
        # Render skill tags side by side
        skill_tags_html = ''.join(f'<span class="skill-tag">{skill}</span>' for skill in project_3['skills'])
        st.markdown(f'<div class="skills-container">{skill_tags_html}</div>', unsafe_allow_html=True)
        st.markdown(f"**Date**: {project_3['date']}")
        st.markdown("""
        - <b style='font-family:courier new;font-size:15px;'>Developed PyTorchNewsClassifier, utilizing PyTorch framework to accurately categorize news articles into Sports, World, Business, and Science Tech categories.</b>
        - <b style='font-family:courier new;font-size:15px;'>Achieved a commendable 77% accuracy in classifying news articles, demonstrating the effectiveness of the model trained on a diverse dataset.</b>
        - <b style='font-family:courier new;font-size:15px;'>Enabled seamless integration with recommendation systems, enhancing personalized news delivery by providing users with tailored content based on their preferences.</b>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        image = Image.open(project_4['image_path'])
        st.image(image, use_column_width=True)
        st.markdown(f"### <center><b style='font-size:20px;font-family:courier new;'><a href='https://www.kaggle.com/code/angadk268/american-university-risk-assesment' style='padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'> {project_4['title']}</a></b></center>",unsafe_allow_html=True)
        # Render skill tags side by side
        skill_tags_html = ''.join(f'<span class="skill-tag">{skill}</span>' for skill in project_4['skills'])
        st.markdown(f'<div class="skills-container">{skill_tags_html}</div>', unsafe_allow_html=True)
        st.markdown(f"**Date**: {project_4['date']}")
        st.markdown("""
        - <b style='font-family:courier new;font-size:15px;'>Developed a Python-based neural network classifier to predict student attendance risks at a selective university.</b>
        - <b style='font-family:courier new;font-size:15px;'>Analyzed academic performance data to identify at-risk students for targeted support.</b>
        - <b style='font-family:courier new;font-size:15px;'>Incorporated variables such as grade points per unit, overall GPA, instructor ID, term, high school GPA, and sex for a comprehensive risk assessment.</b>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        image = Image.open(project_5['image_path'])
        st.image(image, use_column_width=True)
        st.markdown(f"### <center><b style='font-size:20px;font-family:courier new;'><a href='https://github.com/angad08/ADULT_INCOME_EDA_ML' style='padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #87c85f, #11678f);'> {project_5['title']}</a></b></center>",unsafe_allow_html=True)
        # Render skill tags side by side
        skill_tags_html = ''.join(f'<span class="skill-tag">{skill}</span>' for skill in project_5['skills'])
        st.markdown(f'<div class="skills-container">{skill_tags_html}</div>', unsafe_allow_html=True)
        st.markdown(f"**Date**: {project_5['date']}")
        st.markdown("""
        - <b style='font-family:courier new;font-size:15px;'>Conducted an exploratory data analysis to assess the accuracy of a 2019 Times of India article on Computer Science Engineering graduate salaries, examining the interplay between gender and field specialization.</b>
        - <b style='font-family:courier new;font-size:15px;'>Analyzed AMCAT aspirants' data to determine the top 20 professions by salary, providing detailed insights into salary trends, domain, state, experience, gender, and age, with a focused study on the second most popular profession among candidates.</b>
        """, unsafe_allow_html=True)

    with st.container(border=True):
        image = Image.open(project_6['image_path'])
        st.image(image, use_column_width=True)
        st.markdown(f"### <center><b style='font-size:15px;font-family:courier new;padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'> {project_6['title']}</b></center>",unsafe_allow_html=True)
        # Render skill tags side by side
        skill_tags_html = ''.join(f'<span class="skill-tag">{skill}</span>' for skill in project_6['skills'])
        st.markdown(f'<div class="skills-container">{skill_tags_html}</div>', unsafe_allow_html=True)
        st.markdown(f"**Date**: {project_6['date']}")
        st.markdown("""
        - <b style='font-family:courier new;font-size:15px;'>Recommended three high-rated, affordable laptop brands suitable for everyday use or gaming.</b>
        - <b style='font-family:courier new;font-size:15px;'>Simplified decision-making for users by aligning recommendations with the latest Flipkart trends and customer needs.</b>
        """, unsafe_allow_html=True)

        # Add a link to the project's code here if needed    # Add a link to the project's code here if needed  # Add a link to the project's code here if needed

if __name__ == "__main__":
    projects()