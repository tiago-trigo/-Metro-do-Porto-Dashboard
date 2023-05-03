import streamlit as st

st.set_page_config(page_title = "Metro do Porto Dashboard", layout = "wide")

st.markdown(
    """
    <h1 style="text-align: center; padding: 5px;">Metro do Porto Operational Indicators Dashboard</h1>
    <h4 style="text-align: center; padding-top: 5px; padding-bottom:20px;">🚇🚈🚊</h4>
    <p style="text-align: center; padding-top: 5px; padding-bottom:20px;"><i>Making transit data acessible to everyone</i></p>
    """,
    unsafe_allow_html=True,
)
with st.expander("What does this dashboard represent?"):
    st.markdown(
        """
        - This Dashboard showcases the perfomance and operational indicators of **Porto's Light Rail System**.
        
        - The objective of such data visualizations is to make the not so organized data **acessible to everyone**, even those with less data knowledge.
        """
    )

with st.expander("From where was the data obtained?"):
    st.markdown(
        """
        - All the data showcased here was obtained from the Excel sheets provided by **Metro do Porto**, on their own [website](https://www.metrodoporto.pt/pages/677)
        
        - Although data from several years is provided, I only added the last two pre-covid years. I'll do my best to add more data in the future.
        """
    )

with st.expander("How is the dashboard organized?"):
    st.markdown(
        """
        This dashboard is organized in 3 diferent pages, with several data in each of them:

        - **🏠 Homepage**: The page your are right now. This page gives some brief information and guidance on the data used

        - **🚉 Data by track section**: This page showcases data refering to the trip between two consecutive stations.

        - **🥇 Top 10s**: This page showcases upper and bottom top 10 track sections for various metrics.

        """
    )

with st.expander("What does each indicator mean?"):
    st.markdown(
        """
        **🚉 Data by track section.**:
        - **Monthly average occupancy**: The average vehicle occupancy in a certain month for a given track section (percentage);
        - **Total number of passagers**: The total number of passagers that passed through a given track section in a certain month (absolute value);
        - **Total number of train movements**: The total number of trains that passed through a given track section in a certain month (absolute value);
        - **Occupancy rate by hour**: The average vehicle occupancy in a certain month for a given track section in function of the hour of the day (percentage);
        - **Train movements by type of train**: The number of trains that passed through a given track section in a certain month in function of the hour of the day categorized by the type of train (absolute value);
        - **Occupancy Rate (from A to B)**: The average vehicle occupancy in a certain month for a given track section (direction A to B) in function of the hour of the day (percentage)
        
        
        **🥇 Top 10s**:
        - **Vehicle occupancy (monthly average)**: Average vehicle occupancy during a given month on a given track section;
        - **Vehicle occupancy (morning peak)**: Average vehicle occupancy during a given month for the morning peak hour (8h-9h) on a given track section;
        - **Vehicle occupancy (evening peak)**: Average vehicle occupancy during a given month for the evening peak hour (18h-19h) on a given track section;
        - **Passager load (monthly average)**: Total number of passagers that passed through a given track section during a given month;
        - **Passager load (morning average)**: Total number of passagers that passed through a given track section during a given month for the morning peak hour (8h-9h);
        - **Passager load (evening average)**: Total number of passagers that passed through a given track section during a given month for the evening peak hour (18h-19h);
        """
    )
