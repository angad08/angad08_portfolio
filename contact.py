import streamlit as st

def contact():
    st.title('Get in Touch')

    # Define a row with multiple columns
    # Adding extra columns on the sides for additional control over spacing
    col1, col2, col3, col4, col5, col6,col7 = st.columns([1, 1, 1, 1, 1, 1,1])

    with col1:
        st.markdown(
            "<a href='mailto:angadkadam08@gmail.com' target='_blank'>"
            "<img src='https://img.icons8.com/color/48/000000/gmail-new.png' "
            "style='vertical-align: middle;' alt='Gmail icon'></a>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            "<a href='https://www.linkedin.com/in/angad-kadam-03b606159' target='_blank'>"
            "<img src='https://img.icons8.com/fluent/48/000000/linkedin.png' "
            "style='vertical-align: middle;' alt='LinkedIn icon'></a>",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            "<a href='https://github.com/angad08' target='_blank'>"
            "<img src='https://img.icons8.com/ios-filled/50/000000/github.png' "
            "style='vertical-align: left;' alt='GitHub icon'></a>",
            unsafe_allow_html=True
        )
    # Empty columns col1 and col6 help center the icons
    # Columns col2, col3, and col4 contain the icons

if __name__ == "__main__":
    contact()
