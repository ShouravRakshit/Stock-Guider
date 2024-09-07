import streamlit as st
from app_pages import home, stock_analysis, news, about, fun

# Set up page config
st.set_page_config(page_title="Stock Price App", layout="wide")

# Custom CSS for gradient background and other styles
def set_custom_style():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #1a1a2e, #16213e, #0f3460);
        background-attachment: fixed;
    }
                
    .stButton > button {
        height: 3rem;
        padding: 0 1.5rem;
        background-color: rgba(47, 57, 77, 0.7) !important;
        color: white !important;
        font-size: 1rem;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        justify-content: center;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #1F316F, #4158A6, #4158A6, #1F316F);
        z-index: -1;
        filter: blur(5px);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .stButton > button:hover::before {
        opacity: 1;
    }
    .stButton > button:active, .stButton > button:focus {
        transform: scale(0.98);
        color: white !important;
    }
    .stButton > button:active::before, .stButton > button:focus::before {
        opacity: 1;
        filter: blur(3px);
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: linear-gradient(55deg, #102C57, #4158A6, #4158A6, #102C57);
        color: white;
        text-align: center;
        padding: 12px 0px;
    }
    .footer p {
        margin: 0;
        font-size: 1.2rem;
    }
    .footer a {
        color: white;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
                      
     @media (max-width: 768px) {
         .nav-container {
             flex-direction: column;
         }
         .stButton > button {
            width: 100%;
            margin-bottom: 0.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Navbar styling and links
def display_navbar():
    
    # Create columns for navigation buttons
    col1, col2, col3, col4, col5 = st.columns([1, 1,1, 1, 1])

    # Create button-based navigation
    with col1:
        if st.button("Home"):
            st.session_state["page"] = "home"
    with col2:
        if st.button("Stock Analysis"):
            st.session_state["page"] = "stock_analysis"
    with col3:
        if st.button("Stock News"):
            st.session_state["page"] = "news"
    with col4:
        if st.button("About"):
            st.session_state["page"] = "about"
    
    with col5:
        if st.button("Fun"):
            st.session_state["page"] = "fun"
    
    st.markdown('</div>', unsafe_allow_html=True)


# Main function to handle page routing
def main():
    # Set custom style
    set_custom_style()

    # Initialize session state for the page
    if "page" not in st.session_state:
        st.session_state["page"] = "home"

    display_navbar()

    st.title("Stock Price App")
    

    # Route to the correct page based on session state
    page = st.session_state["page"]

    if page == "home":
        home.show_home_page()
    elif page == "stock_analysis":
        stock_analysis.show_stock_analysis_page()
    elif page == "news":
        news.show_news_page()
    elif page == "about":
        about.show_about_page()
    elif page == "fun":
        fun.show_fun_page()
    else:
        home.show_home_page()

    # Footer
    st.markdown("""
        <div class="footer">
            <p>Developed by Shourav Rakshit Ivan | <a href="https://github.com/ShouravRakshit">GitHub</a>
               | <a href="https://www.linkedin.com/in/shourav-rakshit-ivan-7308a6177/">Linkedin</a> </p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()


