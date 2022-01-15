#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests # this import the required
from pprint import pprint
API_Key = "6bd416463a98ac853b7768babd51e339"
location = input("Enter Your Desired Location: ")
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
pprint(weather_data)


# In[5]:


from pprint import pprint
pprint(weather_data)


# In[ ]:




