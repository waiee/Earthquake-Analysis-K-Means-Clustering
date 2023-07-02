import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pydeck as pdk
import folium as folium
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Earthquake Clustering Analysis",
                   page_icon=":bar_chart:",
                   layout="wide")

def home():
    import streamlit as st
     # ----- HEADER AND OBJECTIVES ----- #
    st.markdown("")
    st.text("Prepared by Waiee Zainol")
    
    df = pd.read_excel(
        io='Significant_Earthquakes.xlsx',
        engine="openpyxl", 
        usecols='B:R',
        nrows=1000,
    )

    st.header("Dataset")
    st.write("For this clustering analysis, we will be using  “Significant_Earthquakes.csv” as our main dataset.")
    st.dataframe(df)

    st.header("Objectives")
    st.write(
        """ 
        1. To identify patterns in earthquake occurrences over time. 
            
        2. To identify areas and locations with a high risk of earthquake occurrences. 
            
        3. To provide insights and recommendations for earthquake preparedness and risk management measures in the identified regions. 
        """
    )

    # ----- BASEMAP ----- #
    st.header("Global Earthquakes with Magnitude above 5 since 1900")
    df2 = pd.read_csv('Significant_Earthquakes.csv', 
                    usecols=['latitude', 'longitude', 'mag'])
    df2.columns = ['latitude', 'longitude', 'mag']
    st.map(df2)

    st.write(
        """
        This map displays every earthquake that has occured around the globe with a magnitude of 5 or above since 1900. 
        Each point on the map represent the location of the earthquake which is plotted based on their epicenter coordinates. 
        The map clearly shows that earthquakes are not evenly distributed around the world and follow a specific pattern, with regions like the Pacific Ring of Fire and the Himalayas experiencing more frequent and severe earthquakes.
        """
    )

    # ----- LINE CHART by Year ----- #

    st.header("Earthquake Occurences by Year")
    df3 = pd.read_csv('df2.csv')
    earthquake_counts = df3['year'].value_counts().sort_index()

    # Create a line chart
    chart_data = pd.DataFrame({'Year': earthquake_counts.index, 'Occurrences': earthquake_counts.values})
    st.line_chart(chart_data.set_index('Year'))

    st.write(
        """
        Graph above represents the Earthquake Occurrences by Year. Based on the graph, we can observe that the frequency of earthquakes has been increasing since the early 1900s, which could be due to better detection technology and population growth in seismically active areas. 
        We also can observe that earthquake occurrences are at peak from the year 2000 and above.
        """
    )


    # ----- HISTOGRAM by Month ----- #
    st.header("Earthquake Occurences by Month")
    earthquakes_by_month = df3['month'].value_counts().sort_index()

    # Create a bar chart
    chart_data = pd.DataFrame({'Month': earthquakes_by_month.index, 'Occurrences': earthquakes_by_month.values})
    st.bar_chart(chart_data.set_index('Month'))

    st.write(
        """
        Graph above represents the Earthquake Occurrences by Month. Based on the graph, we can observe that there is no obvious pattern in frequency of the earthquakes based on months. The highest amount of earthquake occurrences is in March since 1900. 
        Meanwhile, the lowest amount of earthquake occurrences is in February. Overall, the amount of earthquakes is distributed and occurred with quite a balanced amount.
        """
    )

    # ----- DENSITY Distribution ----- #
    st.header("Density Distribution of Earthquake Magnitude")


    hist_data, bin_edges = np.histogram(df2['mag'], bins=np.arange(df2['mag'].min(), df2['mag'].max() + 0.1, 0.1), density=True)
    hist_df = pd.DataFrame({'bin_edges': bin_edges[:-1], 'counts': hist_data})
    st.bar_chart(hist_df.set_index('bin_edges'))


    kde = sns.kdeplot(df2['mag'], color='red', legend=False)
    kde_data = kde.get_lines()[0].get_data()
    kde_df = pd.DataFrame({'mag': kde_data[0], 'density': kde_data[1]})
    st.line_chart(kde_df.set_index('mag'))

    st.write(
        """
        This plot shows the density distribution of earthquake magnitudes since 1900. The distribution is highly skewed to the left, indicating that the majority of earthquakes had a magnitude closer to 5, while only a few are very strong. 
        The plot also reveals that the distribution follows a logarithmic scale, which means that an increase in magnitude by one unit corresponds to a ten-fold increase in the strength of the earthquake. The distribution curve helps us understand the frequency and severity of earthquakes around the world.
        """
    )

    # ----- Clustering Plot ----- #

    # Create the scatterplot using Seaborn
    st.header("K-Means Clustering Result")
    newdf = pd.read_csv("newdf.csv")

    # Create the scatter plot using Plotly
    fig = px.scatter(newdf, x="latitude", y="longitude", color="clusters",
                    labels={"latitude": "Latitude", "longitude": "Longitude"})

    # Display the plot using Streamlit
    fig.update_layout(width=1200, height=600)
    st.plotly_chart(fig)
    st.write(
        """
        Both plots above represent Earthquake Clustering analysis which consist of latitude and longitude after pre-processed the data and applied K-Means Clustering. Based on the figures above, we can observe that the majority of points are well-clustered and distinct, indicating that the clustering algorithm has successfully identified patterns in the data. 
        However, there are a few points that appear to be overlapped with each other, potentially indicating some level of ambiguity or similarity between those data points. It also indicates there is a possibility of outliers or noisy data points.
        """
    )

    # ----- Clustered Map ----- #
    st.header("Clustered Basemap")
    import streamlit as st

    image_path = "C:\\Users\\user\\Downloads\\projects\\data science assignment\\image_2023-07-02_20-40-03.png"

    st.image(image_path, caption='Clustered Basemap', use_column_width=True)

    # Filter the DataFrame based on cluster label values 0 and 1
    # filtered_df = newdf[newdf['clusters'].isin([0, 1])]

    # # Create scatter plot
    # fig, ax = plt.subplots()
    # ax.scatter(filtered_df['longitude'], filtered_df['latitude'], c=filtered_df['clusters'], cmap='Set1')
    # ax.set_xlabel('Longitude')
    # ax.set_ylabel('Latitude')
    # ax.set_title('Cluster Plot')

    # # Display the plot
    # st.pyplot(fig)


    st.write(
        """ 
        This clustered map displays every earthquake that has occured around the globe since 1900. Each point on the map represents the location (latitude and longitude) of the earthquake which is plotted based on their epicenter coordinates. From this figure, we can identify areas and locations with a high risk of earthquake occurrences. 
        The map clearly shows that earthquakes are clustered into two major groups. Both clusters label have different characteristics which we can measure their differences by magnitude and depth. The red color indicates high risk location of earthquake occurrences while blue color indicates low risk location of earthquake occurrences. 
        """
        )

    # ----- Final dataframe ----- #
    st.header("Final Dataframe")
    st.dataframe(newdf)
    st.write(
        """
        Through this clustering analysis, the identified regions have been categorized into clusters that indicate the level of earthquake risk. This classification provides valuable insights into the spatial distribution of earthquake occurrences and helps prioritize risk management efforts.
        
        Given the identified high-risk areas, it is recommended to review and update building codes and regulations. Implementing stricter standards for construction and ensuring compliance through inspections can significantly improve the structural integrity of buildings, reducing the potential impact of earthquakes.
        
        By establishing and expanding early warning systems enables residents to receive advance notice of impending earthquakes. This, coupled with enhanced emergency response capabilities, such as drills and training for first responders, ensures a rapid and effective response during seismic events.Critical infrastructure, including hospitals, schools, and transportation networks, should undergo regular seismic vulnerability assessments. Identifying potential vulnerabilities and implementing mitigation measures enhances the resilience of key infrastructure components.
        
        Furthermore, effective communication and coordination among relevant stakeholders are vital for successful earthquake preparedness and risk management. Collaboration with government agencies, emergency management organizations, community groups, and businesses ensures a cohesive approach to address earthquake risks in the identified regions.
        """
    )

def dataanalysis():
    # ----- BASEMAP ----- #
    st.header("Global Earthquakes with Magnitude above 5 since 1900")
    df2 = pd.read_csv('Significant_Earthquakes.csv', 
                    usecols=['latitude', 'longitude', 'mag'])
    df2.columns = ['latitude', 'longitude', 'mag']
    st.map(df2)

    st.write(
        """
        This map displays every earthquake that has occured around the globe with a magnitude of 5 or above since 1900. 
        Each point on the map represent the location of the earthquake which is plotted based on their epicenter coordinates. 
        The map clearly shows that earthquakes are not evenly distributed around the world and follow a specific pattern, with regions like the Pacific Ring of Fire and the Himalayas experiencing more frequent and severe earthquakes.
        """
    )

    # ----- LINE CHART by Year ----- #

    st.header("Earthquake Occurences by Year")
    df3 = pd.read_csv('df2.csv')
    earthquake_counts = df3['year'].value_counts().sort_index()

    # Create a line chart
    chart_data = pd.DataFrame({'Year': earthquake_counts.index, 'Occurrences': earthquake_counts.values})
    st.line_chart(chart_data.set_index('Year'))

    st.write(
        """
        Graph above represents the Earthquake Occurrences by Year. Based on the graph, we can observe that the frequency of earthquakes has been increasing since the early 1900s, which could be due to better detection technology and population growth in seismically active areas. 
        We also can observe that earthquake occurrences are at peak from the year 2000 and above.
        """
    )


    # ----- HISTOGRAM by Month ----- #
    st.header("Earthquake Occurences by Month")
    earthquakes_by_month = df3['month'].value_counts().sort_index()

    # Create a bar chart
    chart_data = pd.DataFrame({'Month': earthquakes_by_month.index, 'Occurrences': earthquakes_by_month.values})
    st.bar_chart(chart_data.set_index('Month'))

    st.write(
        """
        Graph above represents the Earthquake Occurrences by Month. Based on the graph, we can observe that there is no obvious pattern in frequency of the earthquakes based on months. The highest amount of earthquake occurrences is in March since 1900. 
        Meanwhile, the lowest amount of earthquake occurrences is in February. Overall, the amount of earthquakes is distributed and occurred with quite a balanced amount.
        """
    )

    # ----- DENSITY Distribution ----- #
    st.header("Density Distribution of Earthquake Magnitude")


    hist_data, bin_edges = np.histogram(df2['mag'], bins=np.arange(df2['mag'].min(), df2['mag'].max() + 0.1, 0.1), density=True)
    hist_df = pd.DataFrame({'bin_edges': bin_edges[:-1], 'counts': hist_data})
    st.bar_chart(hist_df.set_index('bin_edges'))


    kde = sns.kdeplot(df2['mag'], color='red', legend=False)
    kde_data = kde.get_lines()[0].get_data()
    kde_df = pd.DataFrame({'mag': kde_data[0], 'density': kde_data[1]})
    st.line_chart(kde_df.set_index('mag'))

    st.write(
        """
        This plot shows the density distribution of earthquake magnitudes since 1900. The distribution is highly skewed to the left, indicating that the majority of earthquakes had a magnitude closer to 5, while only a few are very strong. 
        The plot also reveals that the distribution follows a logarithmic scale, which means that an increase in magnitude by one unit corresponds to a ten-fold increase in the strength of the earthquake. The distribution curve helps us understand the frequency and severity of earthquakes around the world.
        """
    )


# ----- SIDEBAR ----- #
with st.sidebar:
    selected = st.selectbox(
        "Menu",
        options=["Home", "Data Analysis", "Method", "About"],
        index=0,
    )

if selected == "Home":
    st.title("Earthquake Analysis: K-Means Clustering :bar_chart:")
    home()

elif selected == "Data Analysis":
   st.title("Exploratory Data Analysis")
   dataanalysis()

elif selected == "Method":
    st.write("this is for method")

elif selected == "About":
    st.write("Hi, I am Waiee.")

