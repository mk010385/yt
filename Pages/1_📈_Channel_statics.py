from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
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
