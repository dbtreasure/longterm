import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Long Term Management", layout="wide")

# Create a title for the landing page
st.title("Long Term Management")

# Add a brief description of the business
st.markdown(
    """
    Long Term Management is a professional agency dedicated to representing software developers in their career pursuits. 
    We are currently under development and will be launching soon to provide top-notch services that ensure the long-term success of our clients. 
    """
)

# Add a "coming soon" message
st.subheader("Coming Soon")
st.markdown(
    """
    We're working hard to build a platform that meets the needs of software developers and helps them find the perfect job opportunities.
    Please check back in the future for updates and exciting news about our services.
    """
)

# Add a "contact us" section
st.subheader("Contact Us")
st.markdown(
    """
    If you have any questions or would like to learn more about Long Term Management, please feel free to reach out to us at [info@longtermmanagement.com](mailto:info@longtermmanagement.com).
    """
)

# Run the app
if __name__ == "__main__":
    st.markdown("---")
    st.markdown("© 2023 Long Term Management. All rights reserved.")
