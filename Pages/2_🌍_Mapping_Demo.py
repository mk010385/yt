from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import seaborn as sns
import altair as alt
api_key = "AIzaSyANpzCVkmvylEAvr-QjryM1cg9uWaU78Tc"  # Replace with your actual API key
channel_id = "UCNdY5AsfPZqsCO8IxkAuSyQ"  # Example: T-Series channel ID

youtube = build('youtube', 'v3', developerKey=api_key)
def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_id
    )
    response = request.execute()
    data = dict(Channel_name = response['items'][0]['snippet']['title'],
               Subscriber = response['items'][0]['statistics']['subscriberCount'],
               Views = response['items'][0]['statistics']['viewCount'],
               Total_videos = response['items'][0]['statistics']['videoCount'])
    return data

channel_stats = get_channel_stats(youtube, channel_id)
channel_data = pd.DataFrame(channel_stats,index=[0])
channel_data 

channel_data['Subscriber'] = channel_data['Subscriber'].astype('int64')
channel_data['Views'] = channel_data['Views'].astype('int64')
channel_data['Total_videos'] = channel_data['Total_videos'].astype('int64')
# channel_data['Country'] = channel_data['Country'].astype('str')


chart =alt.Chart(channel_data ).mark_circle().encode(

   x='Subscriber' ,y='Views',tooltip = ['Subscriber','Views']
)
st.altair_chart(chart,use_container_width=True)


# # Assuming you have the 'channel_data' DataFrame

# ax = sns.barplot(x='Subscriber', y='Views', data=channel_data)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="right")  # Rotate x-axis labels
# plt.tight_layout()  # Adjust layout to prevent label cutoff
# st.line_chart(channel_data)



st.bar_chart(
    channel_data ,
    x='Subscriber',
    y='Views',
    color='#ffaa00'
)

fig, ax = plt.subplots()
ax.hist(channel_data, bins=20,x="Subscriber",y="Views")

st.pyplot(fig)
