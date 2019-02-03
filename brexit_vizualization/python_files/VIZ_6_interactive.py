
# coding: utf-8

# In[5]:


#https://www.kaggle.com/kanncaa1/plotly-tutorial-for-beginners
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# plotly
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
# matplotlib
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[8]:


#iplot([{"x": [1, 2, 3], "y": [3, 1, 6]}])
df = pd.read_csv("data\uk_econcomic.csv")
df.info()


# In[14]:


# import graph objects as "go"
import plotly.graph_objs as go

# Creating trace1
trace1 = go.Scatter(
                    x = df['Year'],
                    y = df['GDP growth (annual %)'],
                    mode = "lines+markers",
                    name = "GDP growth (annual %)",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)')
                    )
# Creating trace2
trace2 = go.Scatter(
                    x = df['Year'],
                    y = df['Population growth (annual %)'],
                    mode = "lines+markers",
                    name = "Population growth (annual %)",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)')
                    )
data = [trace1, trace2]
layout = dict(title = 'Annual GDP growth and Population Since Joining The EU',
              xaxis= dict(title= 'Year',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Percentage',ticklen= 5,zeroline= True)
             )
fig = dict(data = data, layout = layout)
iplot(fig)


# In[18]:


# import graph objects as "go"
import plotly.graph_objs as go

# Creating trace1
trace1 = go.Scatter(
                    x = df['Year'],
                    y = df['Merchandise exports (current US$)'],
                    mode = "lines",
                    name = "Merchandise exports",
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)')
                    )
# Creating trace2
trace2 = go.Scatter(
                    x = df['Year'],
                    y = df['Merchandise imports (current US$)'],
                    mode = "lines",
                    name = "Merchandise imports",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)')
                    )
data = [trace1, trace2]
layout = dict(title = 'Merchandise Exports Vs Merchandise Imports',
              xaxis= dict(title= 'Year',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'current US$',ticklen= 5,zeroline= True)
             )
fig = dict(data = data, layout = layout)
iplot(fig)

