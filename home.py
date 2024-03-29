import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from io import BytesIO
import time
from projects import projects
from experience import experience
from contact import contact
from recomm import recommendations
def app():
    with st.sidebar:
        selected_page = option_menu(
            menu_title="Main Menu",
            options=["Home", "Projects", "Experience","Recommendations","Contact",],
        )
    # Custom CSS for circular image and FontAwesome icons
    st.markdown("""
    <style>
    .metric-container {
        padding: 10px 0;
        text-align: center; /* Center align metric containers */
    }
    .metric-title {
        color: #333;
        margin-bottom: 5px;
        font-weight: bold;
    }
    .metric-number {
        color: #FF4C4C;
        font-weight: bold;
        font-size: 2.5em; /* Larger font size for the numbers */
    }
    /* Responsive design adjustments */
    @media (max-width: 768px) {
        .metric-title, .metric-number {
            font-size: 1.5em; /* Smaller font size for mobile devices */
        }
    }
    .circular-image {
        border-radius: 50%;
        overflow: hidden;
        background: #fff;
        box-shadow: 0 0 30px 0px rgba(131, 198, 231, 0.85);
        width: 150px;
        height: 150px;
        border: 1px solid #000;
        margin: 0 auto;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    .circular-image img {
        display: block;
        margin: auto;
        width: 150px;
        height: 150px;
        object-fit: cover; /* Ensures the image is not stretched */
    }
    .gradient-text {
        font-size: 27px;
        background: linear-gradient(to right, #1a155d,#5651a0);
        -webkit-background-clip: text;
        color: transparent;
        display: inline;
    }
    .gradient-text-subheader {
        font-size: 27px;
        background: linear-gradient(to right, #2f329b, #f55555);
        -webkit-background-clip: text;
        color: transparent;
        display: inline;
    }
    .gradient-text-header {
        font-size: 27px;
        background: linear-gradient(to right, #000000, #49ff01);
        -webkit-background-clip: text;
        color: transparent;
        display: inline;
    }
    .aboutme-header {
    font-size: 27px;
    font-family: 'Courier New', Courier, monospace;
    background-color: #f0f0f0; /* Light grey background */
    padding: 10px;
    border-radius: 8px;
}
    </style>
    """, unsafe_allow_html=True)

    if selected_page == "Home":
        # Layout with columns
        col1, col2,col3 = st.columns(3)
        # Profile photo (Make sure the path to your image is correct)
        with col2:
            image = Image.open('assets/dp.jpg')
            st.markdown(f'<div class="circular-image"><img src="data:image/jpeg;base64,{image_to_base64(image)}"/></div>', unsafe_allow_html=True)
        # Personal details
        st.markdown("<div style='text-align:center;'><b style='font-size:27px;font-family:courier new;'>Hello, I'm <span class='gradient-text-subheader'>Angad</span>,a <span class='gradient-text-subheader'>Data Scientist</span> fueled by an intrinsic drive to decode the data maze. By refining our analytical strategies and deciphering the hidden messages within, I unearth actionable insights that not only shape today's decisions but also pave the way for tomorrow's breakthroughs.</div><br>", unsafe_allow_html=True)
        # st.markdown("<b>🎂 26 August 1996</b>", unsafe_allow_html=True)
        col1,col2=st.columns(2)
        # About me
        with col1:
            with st.container(border=True):
                st.markdown("<b style='font-size:15px;font-family:courier new;padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'>ABOUT ME</b>", unsafe_allow_html=True)
                st.markdown("<b style='font-family:courier new;font-size:15px;'>As an intrinsic data enthusiast, my journey through the realms of analytics, artificial intelligence, and machine learning has been both profound and fulfilling. Graduating with a Master of Data Science from La Trobe University, I've cultivated a robust skill set that spans across Python, R, and various machine learning frameworks. My academic endeavors have not only honed my technical abilities but also highlighted my penchant for pushing the boundaries of data-driven insights. With a solid foundation in statistical analysis, data visualization, and model development, I am driven by the challenge of transforming complex datasets into actionable intelligence. Beyond the technical, my journey is fueled by a relentless pursuit of knowledge and a deep-seated belief in the power of data to inform and inspire. My skills in programming, coupled with a strategic approach to problem-solving, embody my dedication to excellence in the data science field.</b>",unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<b style='font-size:15px;font-family:courier new;padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'>ACHEIVEMENTS</b>",unsafe_allow_html=True)
                st.markdown("""
                - <b style='font-family:courier new;font-size:15px;'>Authored the paper "Deciphering the Impact of Hybrid Teaching," earning acclaim from PhD professors and the Vice Chancellor at La Trobe University.</b>
                - <b style='font-family:courier new;font-size:15px;'>Awarded the "Golden Key Academic Excellence Award 2022" by the Golden Key International Honour Society - Asia Pacific.</b>
                - <b style='font-family:courier new;font-size:15px;'>Graduated among the top 5 highest academic performers with a Master of Data Science from La Trobe University.</b>
                """, unsafe_allow_html=True)
        
            
            with st.container(border=True):    
                metric_col1, metric_col2 = st.columns(2)
                project_count_placeholder = metric_col1.empty()  # Placeholder for total projects
                lines_of_code_placeholder = metric_col2.empty()  # Placeholder for lines of code              
                for num in range(1, 9):  # Assuming you want to show 8+ projects
                    project_count_placeholder.markdown(f"""<b style='font-size:27px;font-family:courier new;'><center>TOTAL PROJECTS</center></b><div class="metric-number"><center>{num}+</center></div>""", unsafe_allow_html=True)
                    
                for num in range(1, 108):
                    lines_of_code_placeholder.markdown(f"""<b style='font-size:27px;font-family:courier new;'><center>LINES OF CODE</center> </b></div>
                        <div class="metric-number"><center>{num}+</center></div>
                        <br><br><br>
                    </div>
                    """, unsafe_allow_html=True)
    if selected_page == "Projects":
        projects()
    if selected_page == "Experience":
        experience()
    if selected_page == "Contact":
        contact()
    if selected_page == "Recommendations":
        recommendations()
        
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

if __name__ == "__main__":
    try:
        st.set_page_config(page_title="Home - My Data Science Portfolio", layout="wide")
        app()
    except Exception as e:
        app()
