import requests
import pandas as pd
import streamlit as st


def get_google_results(query, scrapingbee_api_key):
    try:
        response = requests.get(
            url='https://app.scrapingbee.com/api/v1/google',
            params={
                'api_key': f'{scrapingbee_api_key}',
                'search': f"{query}",
                'language': 'en'
            },
        )

        data = response.json()
        urls = [item["url"] for item in data["organic_results"]]

        st.subheader("Table of results", divider="gray")
        data_df = pd.DataFrame({"urls": urls})
        data_df.index = data_df.index + 1
        st.data_editor(
            data_df,
            column_config={
                "urls": st.column_config.LinkColumn(
                    "Google Search result links"
                )
            }
        )
    except:
        st.warning('Can\'t obtain links with Scrapingbee. Try again or use "Search in browser" button instead.')
        return
