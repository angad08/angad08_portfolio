import streamlit as st

def experience():
    st.title('Professional Experience')

    def display_job(title, company, duration, location, bullet_points):
        with st.container(border=True):
            left, right = st.columns([3, 1])
            with left:
                st.markdown(f"**<b style='padding: 5px 10px; text-align: center; display: inline-block; border-radius: 5px; text-decoration: none; color: white; background-image: linear-gradient(to right, #87c85f, #11678f);'>{title}</b> @ <b style='padding: 5px 10px; text-align: center; display: inline-block; border-radius: 5px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'>{company}</b>**",unsafe_allow_html=True)
                st.markdown(f"_{location}_")
                for point in bullet_points:
                    st.markdown(f"- {point}")
            with right:
                st.markdown(f"<h6>&nbsp;{duration}</h6>", unsafe_allow_html=True)
            

    display_job(
        "HCM Reporting analyst",
        "Sprezza Solutions Pty Ltd",
        "Nov 2023 – present",
        "Bundoora, Australia",
        [
            "Developed Reports and Dashboards Using Oracle Transactional Business Intelligence (OTBI) and BI Publisher",
            "Conducted Analysis of HR Data for Insights on Employee Performance, Turnover, and Recruitment",
            "Played a Key Role in Automating Reports, Improving Time Efficiency and Data Accuracy"
        ]
    )

    display_job(
        "Data Analyst",
        "Latrobe University",
        "Jun 2023 – Nov 2023",
        "Bundoora, Australia",
        [
            "Analyzed student performance in hybrid learning to assess the impact of motivation on engagement and success, to enhance teaching methods.",
            "Utilized statistical methods including Linear, Logistic, and Decision Tree",
            "Conducted statistical analyses and hypothesis testing focusing on data privacy and ethics."
        ]
    )

    display_job(
        "Data Analyst Intern",
        "Innomatics Reserch Labs",
        "May 2021 – Jan 2022",
        "Mumbai, India",
        [
            "Analyzed data to extract key insights for data-driven decision-making, significantly contributing to the strategic planning process.",
            "Developed and fine-tuned machine learning models for deployment in a Streamlit web application hosted on Heroku, enhancing accessibility and user interaction"
        ]
    )
    display_job(
        "Software Engineer Support Analyst",
        "FIS Global",
        "Aug 2021 – Mar 2022",
        "Mumbai, India",
        [
            "Analyzed logs to troubleshoot issues of the File Change Event (FCE) component, transactions, and ATS server setup.",
            "Tested and configured the FCE component; managed Request.xml file submissions to the ATS server.",
            "Handled server configurations and setups."
        ]
    )

if __name__ == "__main__":
    experience()
