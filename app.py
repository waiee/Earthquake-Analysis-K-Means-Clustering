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

    st.header("Earthquake Occurrences by Year")
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
    st.header("Earthquake Occurrences by Month")
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

    image1 = Image.open("image/image_2023-07-02_20-40-03.png")
    st.image(image1, caption="Clustered Basemap")

    st.write(
        """ 
        This clustered map displays every earthquake that has occured around the globe since 1900. Each point on the map represents the location (latitude and longitude) of the earthquake which is plotted based on their epicenter coordinates. From this figure, we can identify areas and locations with a high risk of earthquake occurrences. 
        The map clearly shows that earthquakes are clustered into two major groups. Both clusters label have different characteristics which we can measure their differences by magnitude and depth. The red color indicates high risk location of earthquake occurrences while blue color indicates low risk location of earthquake occurrences. 
        """
        )

    # ----- Clustered Map ----- #
    st.header("Mean Magnitude and Depth")
    image2 = Image.open("image/output1.png")
    image3 = Image.open("image/output2.png")

    # Display the images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(image2, caption="Mean Magnitudes")

    with col2:
        st.image(image3, caption="Mean Depth")

    st.write(
        """
        First figure represents Comparison of Mean Magnitudes of k=2.. Based on the graph, we can observe that cluster label 1 has slightly higher mean magnitude (5.461928395135152) compared to label 0 (5.453090283336001). Moreover, second figure represents Comparison of Mean Depth of k=2. 
        Based on the graph, we can observe that cluster label 1 has higher mean depth (72.87603063277942) compared to label 0 (56.677855162478004).
        Based on the result, we can observe that cluster label 1 has higher mean magnitude and mean depth. Thus, we can conclude that cluster label 1 has higher risk of earthquake occurrences compared to label 0.
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
    # ----- Correlation Heatmap ----- #
    st.header("Correlation Heatmap")
    image4 = Image.open("image/output3.png")
    st.image(image4, caption="Correlation Heatmap")

    st.write(
            """
            Based on the heatmap above, the highest positive correlation is 0.72, between magNst and nst with brighter color. Other than that, the highest negative correlation is -0.68 between year and magError with the darkest color. 
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

    st.header("Earthquake Occurrences by Year")
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
    st.header("Earthquake Occurrences by Month")
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

    # ----- DENSITY Distribution Magnitude ----- #
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

    # ----- DENSITY Distribution Depth ----- #
    st.header("Density Distribution of Earthquake Depth")
    newdf = pd.read_csv("newdf.csv")

    # Create the histogram plot
    plt.figure(figsize=(10, 5))
    sns.histplot(data=newdf, x='depth', stat='density', kde=True)

    # Display the plot using Streamlit
    st.pyplot(plt)

    st.write(
        """
        This plot shows the density distribution of earthquake depths since 1900. The distribution is also highly skewed to the left, indicating that the majority of earthquakes occur at shallow depths, while only a few occur at deeper depths. 
        The plot reveals that most earthquakes occur within the first 100 kilometers of the Earth's crust. However, some regions, such as the Ring of Fire, experience more frequent and stronger earthquakes at greater depths. The distribution curve helps us understand the spatial and temporal patterns of earthquakes around the world.
        """
    )


def method():
    # ----- Elbow Method ----- #
    st.header("Elbow Method")
    image5 = Image.open("image/output4.png")
    image6 = Image.open("image/output5.png")

    # Display the images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(image5, caption="Elbow Method 1")

    with col2:
        st.image(image6, caption="Elbow Method 2")

    st.write(
        """
        The plot above shows the Elbow method which consists of WSS(Within-Cluster Sum of Squares) Scores and number of clusters. The goal is to find which cluster has elbow shape. 
        Based on the plot above, we can observe that the “elbow” is in range 3-4. After that, the number of clusters decreases continuously, which indicates that there is no potential “elbow” in that range. Overall, we can conclude that the optimal k(number of clusters) values is in the 3-4.
        """
    )

    # ----- Silhouette Method ----- #
    st.header("Silhouette Method")
    image7 = Image.open("image/output6.png")
    image8 = Image.open("image/output7.png")

    # Display the images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(image8, caption="Silhouette Table")

    with col2:
        st.image(image7, caption="Silhouette Scores")

    st.write(
        """
        The plot above represents Silhouette Scores for different numbers of clusters. From the plot, we can observe that k=3 has the highest silhouette score, which is 0.612689 followed by k=2 with silhouette score of 0.550902. 
        This result shows that the ideal k(number of clusters) values are between 2 and 3. Now, we can compare models using both clusters.
        """
    )

    # ----- Model Comparison ----- #
    st.header("Models Comparison")
    cimage = Image.open("image/cluster2.png")
    cimage2 = Image.open("image/cluster3.png")

    # Display the images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(cimage, caption="k=2")

    with col2:
        st.image(cimage2, caption="k=3")

    st.write(
        """
        The graph above represents clustering analysis where k=2 and clustering analysis where k=3. Based on the plot, we can observe that the first figure(k=2) has less overlapped points compared to the second figure(k=3) which indicates better performance in clustering. 
        Moreover, we can see an obvious pattern in the first figure(k=2) compared to the second figure(k=3) which shows the data is clustered well. Thus, we can conclude that the first figure(k=2) has better clustering results since it has a small amount of overlapped data points and has an obvious pattern. Since our objective is just to identify high and low risk locations for earthquake occurrences, therefore we choose k = 2 in this case. 
        Further studies are needed in future in order to obtain better and more accurate results.
        """
    )

def about():
    dp_image = Image.open("image/removebgWaiee.png")
    image_column, right_column = st.columns((1,2))
    with image_column:
        st.image(dp_image, caption="")
    with right_column:
        st.subheader("Hi, I am Waiee :wave:")
        st.title("Bachelor of Computer Science (Hons.) Data Science")
        st.write("I am passionate in Data Science, AI and Machine Learning.")

        # Define the GitHub and LinkedIn links
        github_link = "[GitHub](https://github.com/waiee)"
        linkedin_link = "[LinkedIn](https://www.linkedin.com/in/waiee-zainol-9b00461ab/)"
        
        # Display the sentence with the links
        st.markdown(f"Check out my {github_link} & {linkedin_link} for more info!")




# ----- SIDEBAR ----- #
with st.sidebar:
    selected = st.selectbox(
        "Menu",
        options=["Home", "Data Analysis", "Model Comparison", "About"],
        index=0,
    )

if selected == "Home":
    st.title("Earthquake Analysis: K-Means Clustering :bar_chart:")
    home()

elif selected == "Data Analysis":
    st.title("Exploratory Data Analysis")
    dataanalysis()

elif selected == "Model Comparison":
    st.title("Model Comparison")
    method()

elif selected == "About":
    about()

