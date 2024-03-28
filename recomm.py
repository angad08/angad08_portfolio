import streamlit as st
from PIL import Image
import base64
from io import BytesIO
st.markdown("""
    <style>
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
}
    </style>
    """, unsafe_allow_html=True)

def show_recommendation(author, profile_image_path, date, role, content, expanded=False):
    # Define a container for the recommendation
    with st.container():
        # Create a layout with image on the left and text on the right
        col1, col2 = st.columns([1, 4])
        with col1:
            try:
                # Open the image using PIL and display it with rounded corners
                image = Image.open(profile_image_path)
                st.markdown(f'<div class="circular-image"><img src="data:image/jpeg;base64,{image_to_base64_rec(image)}"/></div>', unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"Error: The image at {profile_image_path} was not found.")
        with col2:
            # Display the author's name as a header and other details as caption
            st.markdown(f"<b style='font-size:20px;font-family:courier new;padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #87c85f, #11678f);'>{author}</b>",unsafe_allow_html=True)
            st.caption(f"<b style='font-size:15px;font-family:courier new;padding: 10px 20px; text-align: center; display: inline-block; border-radius: 12px; text-decoration: none; color: white; background-image: linear-gradient(to right, #cf3732, #11678f);'>{role} | {date}</b>",unsafe_allow_html=True)
            # If the content is too long, truncate and add a link to expand
            st.write(content if expanded else content[:200] + '... [see more]')
            # Horizontal line for separation
            st.markdown("---")

def recommendations():
    st.title('Recommendations')

    # Example recommendation data
    recommendations_data = [
        {
            "author": "Mitra Jazayeri",
            "profile_image_path": "assets/Mitra.jpeg",  # Replace with the correct path to the image
            "date": "February 17, 2024",
            "role": "Lecturer at La Trobe University",
            "content": ("I am writing to recommend Angad for the position of Data Analyst at your organization."
                        "I had the pleasure of serving as Angad's supervisor during his Master of Data Science project, titled 'The Impact of Hybrid Teaching on Student Motivation, and Engagement'." 
                        "Angad’s proficiency in data analytics, and strong foundation in research methods and modelling approaches, enhances his analytical capabilities and decision-making. He proved to be an exemplary student throughout his time under my supervision."
                        "He consistently demonstrated diligence, punctuality, and meticulous attention to detail in completing each assigned task. His commitment to excellence was evident in his conscientious approach to his work, ensuring that every aspect was completed to the highest standard."
                        "One of Angad's standout attributes is his remarkable time management skills. He efficiently prioritized tasks and consistently delivered results ahead of deadlines, he demonstrated his exceptional ability to work under pressure without compromising quality."
                        "Furthermore, Angad's trustworthiness and reliability made him a valuable asset to our project team.I was particularly impressed by Angad's aptitude for learning and his quick grasp of new concepts. He approached challenges with enthusiasm and determination, consistently seeking opportunities for growth and improvement."
                        "Moreover, Angad's active participation and attentiveness during meetings underscored his strong communication skills and collaborative spirit.Angad's combination of technical proficiency, diligence, reliability, and strong work ethic make him an ideal candidate for the Data Analyst position."
                        "I have no doubt that he will excel in this role and contribute positively to your organization.Please feel free to contact me if you require any further information or clarification regarding Angad's qualifications and capabilities. Thank you for considering his application."),
            "expanded": True
        },
        {
            "author": "Andriy Olenko",
            "profile_image_path": "assets/Andriy.jpeg",  # Replace with the correct path to the image
            "date": "February 17, 2024",
            "role": "Associate Professor",
            "content": ("Angad actively participated in a project centered on the analysis of education data, where I served as one of the investigators."
                        "He consistently demonstrated keen interest in the project and delivered the required data analysis results on a weekly basis."
                        "This engagement proved invaluable for his professional development, providing him with exposure to classical statistical methods and their practical application to real-world data." 
                        "As investigators, we were pleased with Angad's contributions to the project."),
            "expanded": True
        }
        # ... Add more recommendations as needed ...
    ]

    # Display each recommendation
    for rec in recommendations_data:
        show_recommendation(**rec)
def image_to_base64_rec(image):
    buffered_r = BytesIO()
    image.save(buffered_r, format="JPEG")
    img_str_r = base64.b64encode(buffered_r.getvalue()).decode()
    return img_str_r
if __name__ == "__main__":
    recommendations()
