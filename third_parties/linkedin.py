import os
import requests
import json

def scrpae_linkedin_profile(linkedin_profile_url:str):
    """

    :param linkedin_profile_url:
    :return: String of the linkedin profile scraped from the URl
    """
    pass

    gist_response=requests.get("https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json")
    data= gist_response.json()

    data={
        k:v
        for k, v in data.items()
            if v not in ([], "", "",None) and k not in ['people_also_viewed','certifications']
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop('profile_pc_url')


    return data