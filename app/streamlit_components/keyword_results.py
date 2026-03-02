import streamlit as st
from urllib.parse import quote_plus
from .google_result import get_google_results
from .app_utils import scrapingbee_api_key_input


@st.fragment
def search_trigger():
    with st.container(border=True):
        st.header("SEO keywords", divider="gray")
        chosen_keywords = st.pills(
            label="Generated Keywords :material/key:",
            default=st.session_state['keywords'][:10],
            options=st.session_state['keywords'],
            selection_mode="multi",
            key="keyword_pills"
        )
        st.markdown(f"Your selected options: {chosen_keywords}.")

        if chosen_keywords:
            keywords_str = ", ".join(chosen_keywords)
            encoded_query = quote_plus(keywords_str) + ' -filetype:pdf'

            col1, col2 = st.columns(spec=2, vertical_alignment="top")

            with col1:
                st.link_button("Search in browser", f"https://www.google.com/search?q={encoded_query}")

            with col2:
                scrapingbee_api_key = scrapingbee_api_key_input()
            if col2.button("Search with Scrapingbee", "primary"):
                if scrapingbee_api_key:
                    get_google_results(chosen_keywords, scrapingbee_api_key)
                else:
                    st.warning('Can\'t obtain links without Scrapingbee API key! Use "Search in browser" button instead.')
        else:
            st.warning('Choose at least one keyword to search for results.')
