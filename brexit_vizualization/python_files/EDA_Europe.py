
# coding: utf-8

# Select the EU countries and check how they performed over the years for population, GDP, consumer index, price index etc..
# 
# Was UK bad compared to other countries?

# In[1]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import warnings
get_ipython().magic("config InlineBackend.figure_format = 'png' #set 'png' here when working on notebook")
warnings.filterwarnings('ignore') 

# Set some parameters to get good visuals - style to ggplot and size to 15,10

pd.set_option('display.width',170, 'display.max_rows',200, 'display.max_columns',300)


# In[2]:


df = pd.read_csv(r"data\WDI_csv\WDIData.csv")


# In[3]:


df.columns


# In[4]:


df = df.drop(['Country Code','Indicator Code'], 1)


# ###### Selecting United Kingdom, other countries in eu

# In[5]:


df[df['Country Name'] == "Lithuania"]


# In[6]:


df = df[df['Country Name'].isin([
    "Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France",
"Germany",
"Greece",
"Hungary",
"Ireland",
"Italy",
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",
"Sweden",
"United Kingdom"
])]


# In[7]:


df['Country Name'].nunique()


# In[8]:


#df.head()


# In[9]:


#Not null values for the column
# Selected 2015 because the brexit happened in 2016 
dfi2 = df[df['2015'].notnull()]


# In[10]:


dfi2.to_csv("europe_uk.csv")


# In[11]:


#dfi2.head()


# In[12]:


dfgdp_percentage = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='GDP growth (annual %)']
dfgdp_percentage = dfgdp_percentage.drop('Indicator Name', 1)

# dfgdp_percentage = dfgdp_percentage.T.reset_index()
# dfgdp_percentage.columns = dfgdp_percentage.iloc[0]
# #dfgdp_percentage.drop(dfgdp_percentage.index[0])
# dfgdp_percentage = dfgdp_percentage.iloc[1:]
# dfgdp_percentage = dfgdp_percentage.rename(columns={ dfgdp_percentage.columns[0]: "Year" })
# dfgdp_percentage["Year"] = dfgdp_percentage.Year.astype(int)
# dfgdp_percentage.iloc[:,1:] = dfgdp_percentage.iloc[:,1:].astype(float)
# #dfgdp_percentage


# In[13]:


dfgdp_percentage.columns
# Longitude and Latitue of countries
#https://developers.google.com/public-data/docs/canonical/countries_csv


# In[14]:


dfinf_percentage = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='Inflation, GDP deflator (annual %)']
dfinf_percentage = dfinf_percentage.drop('Indicator Name', 1)

dfinf_percentage = dfinf_percentage.T.reset_index()
dfinf_percentage.columns = dfinf_percentage.iloc[0]
#dfgdp_percentage.drop(dfgdp_percentage.index[0])
dfinf_percentage = dfinf_percentage.iloc[1:]
dfinf_percentage = dfinf_percentage.rename(columns={ dfinf_percentage.columns[0]: "Year" })
dfinf_percentage["Year"] = dfinf_percentage.Year.astype(int)
dfinf_percentage.iloc[:,1:] = dfinf_percentage.iloc[:,1:].astype(float)
#dfgdp_percentage


# In[15]:


dfp_percentage = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='Population growth (annual %)']
dfp_percentage = dfp_percentage.drop('Indicator Name', 1)

dfp_percentage = dfp_percentage.T.reset_index()
dfp_percentage.columns = dfp_percentage.iloc[0]
#dfgdp_percentage.drop(dfgdp_percentage.index[0])
dfp_percentage = dfp_percentage.iloc[1:]
dfp_percentage = dfp_percentage.rename(columns={ dfp_percentage.columns[0]: "Year" })
dfp_percentage["Year"] = dfp_percentage.Year.astype(int)
dfp_percentage.iloc[:,1:] = dfp_percentage.iloc[:,1:].astype(float)
#dfp_percentage


# In[16]:


dfc_percentage = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='Consumer price index (2010 = 100)']
dfc_percentage = dfc_percentage.drop('Indicator Name', 1)

dfc_percentage = dfc_percentage.T.reset_index()
dfc_percentage.columns = dfc_percentage.iloc[0]
#dfgdp_percentage.drop(dfgdp_percentage.index[0])
dfc_percentage = dfc_percentage.iloc[1:]
dfc_percentage = dfc_percentage.rename(columns={ dfc_percentage.columns[0]: "Year" })
dfc_percentage["Year"] = dfc_percentage.Year.astype(int)
dfc_percentage.iloc[:,1:] = dfc_percentage.iloc[:,1:].astype(float)
dfp_percentage


# In[18]:


#http://www.physics.nyu.edu/pine/pymanual/html/chap5/chap5_plot.html
#sns.pointplot( x = 'Austria',y = 'Year',data = dfgdp_percentage.tail(11))


# In[19]:


import matplotlib.style as style
style.use('ggplot')
sns.set_color_codes("deep")
sns.despine()
#https://en.wikipedia.org/wiki/Financial_and_social_rankings_of_sovereign_states_in_Europe
f, (ax1, ax2) = plt.subplots(1,2, sharey =True, gridspec_kw = {'wspace':0.1, 'hspace':0})
   
fte_graph = dfgdp_percentage.tail(12).plot(x = 'Year', y = ["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France", #3
"Germany", #1
"Greece",
"Hungary",
"Ireland",
"Italy", #4
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",#5
"Sweden", #2
"United Kingdom"], figsize = (20,8),color =['#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#0000FF','#000000',
                                            '#D3D3D3','#D3D3D3','#D3D3D3','#008000','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3',
                                            '#FFDF00','#D3D3D3','#FF6347'], ax = ax1)


fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 9)
# Customizing the tick labels of the y-axis 
# fte_graph.set_ylim(0,25)
# # Generate a bolded horizontal line at y = 0 

fte_graph.get_xaxis().get_major_formatter().set_useOffset(False)
# # Add an extra vertical line by tweaking the range of the x-axis
#fte_graph.set_xlim(left = 1, right = 2017)
#plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
#plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)

# # Remove the plot frame lines. They are unnecessary here.
fte_graph.spines['top'].set_visible(False)
fte_graph.spines['bottom'].set_visible(False)
fte_graph.spines['right'].set_visible(False)
fte_graph.spines['left'].set_visible(False)

# # Remove the tick marks; they are unnecessary with the tick lines we just
# # plotted.
fte_graph.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)

# fte_graph.text(x = 2009, y = 26.0, s = "Annual GDP Growth",
#                 fontsize = 15, weight = 'bold', alpha = .75)
fte_graph.set_xlabel('Year',fontsize=12, weight = 'bold', alpha = .75)

fte_graph.yaxis.set_major_formatter(plt.FuncFormatter('{}%'.format))
#fte_graph.legend([]) 
fte_graph.set_title("Annual GDP Growth" , fontsize=15)
fte_graph.legend(labels=["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France",
"Germany",
"Greece",
"Hungary",
"Ireland",
"Italy",
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",
"Sweden",
"United Kingdom"],frameon=False,ncol= 4,fontsize= 8,loc='upper left').get_frame().set_edgecolor('red') 
#skip every one x-tick for cleanliness

fte_graph_1 = dfinf_percentage.tail(12).plot(x = 'Year', y = ["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France", #3
"Germany", #1
"Greece",
"Hungary",
"Ireland",
"Italy", #4
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",#5
"Sweden", #2
"United Kingdom"], figsize = (20,8),color =['#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#0000FF','#000000',
                                            '#D3D3D3','#D3D3D3','#D3D3D3','#008000','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3',
                                            '#FFDF00','#D3D3D3','#FF6347'], ax = ax2)


fte_graph_1.tick_params(axis = 'both', which = 'major', labelsize = 9)
# Customizing the tick labels of the y-axis 
# fte_graph.set_ylim(0,25)
# # Generate a bolded horizontal line at y = 0 

fte_graph_1.get_xaxis().get_major_formatter().set_useOffset(False)
# # Add an extra vertical line by tweaking the range of the x-axis
#fte_graph.set_xlim(left = 1, right = 2017)
#plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
#plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)

# # Remove the plot frame lines. They are unnecessary here.
fte_graph_1.spines['top'].set_visible(False)
fte_graph_1.spines['bottom'].set_visible(False)
fte_graph_1.spines['right'].set_visible(False)
fte_graph_1.spines['left'].set_visible(False)

# # Remove the tick marks; they are unnecessary with the tick lines we just
# # plotted.
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)

# fte_graph_1.text(x = 2009, y = 26.0, s = "Annual Inflation ",
#                 fontsize = 15, weight = 'bold', alpha = .75)
fte_graph_1.set_xlabel('Year',fontsize=12, weight = 'bold', alpha = .75)
fte_graph_1.legend([])
# fte_graph_1.legend(labels=["Austria",
# "Belgium",
# "Bulgaria",
# "Croatia",
# "Cyprus",
# "Czech Republic",
# "Denmark",
# "Estonia",
# "Finland",
# "France",
# "Germany",
# "Greece",
# "Hungary",
# "Ireland",
# "Italy",
# "Latvia",
# "Lithuania",
# "Luxembourg",
# "Malta",
# "Netherlands",
# "Poland",
# "Portugal",
# "Romania",
# "Slovak Republic",
# "Slovenia",
# "Spain",
# "Sweden",
# "United Kingdom"],frameon=False,ncol= 4,fontsize= 8,loc='upper right').get_frame().set_edgecolor('red') 
fte_graph_1.set_title("Annual Inflation" , fontsize=15)
plt.tight_layout
plt.savefig("euGDP-Inflation.png", bbox_inches="tight")


# In[23]:


df2 = df[df['Country Name'].isin([
"France",
"Germany",
"Italy",
"Spain",
"United Kingdom"
])]
df3 = df2[df2['2015'].notnull()]


# In[24]:


dfgdp_percentage = df3[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][df3['Indicator Name'] =='GDP growth (annual %)']
dfgdp_percentage = dfgdp_percentage.drop('Indicator Name', 1)

dfgdp_percentage = dfgdp_percentage.T.reset_index()
dfgdp_percentage.columns = dfgdp_percentage.iloc[0]
#dfgdp_percentage.drop(dfgdp_percentage.index[0])
dfgdp_percentage = dfgdp_percentage.iloc[1:]
dfgdp_percentage = dfgdp_percentage.rename(columns={ dfgdp_percentage.columns[0]: "Year" })
dfgdp_percentage["Year"] = dfgdp_percentage.Year.astype(int)
dfgdp_percentage.iloc[:,1:] = dfgdp_percentage.iloc[:,1:].astype(float)


# In[25]:


dfinf_percentage = df3[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][df3['Indicator Name'] =='Inflation, GDP deflator (annual %)']
dfinf_percentage = dfinf_percentage.drop('Indicator Name', 1)

dfinf_percentage = dfinf_percentage.T.reset_index()
dfinf_percentage.columns = dfinf_percentage.iloc[0]
#dfgdp_percentage.drop(dfgdp_percentage.index[0])
dfinf_percentage = dfinf_percentage.iloc[1:]
dfinf_percentage = dfinf_percentage.rename(columns={ dfinf_percentage.columns[0]: "Year" })
dfinf_percentage["Year"] = dfinf_percentage.Year.astype(int)
dfinf_percentage.iloc[:,1:] = dfinf_percentage.iloc[:,1:].astype(float)
#dfgdp_percentage


# In[32]:


import matplotlib.style as style
style.use('ggplot')
sns.set_color_codes("deep")
sns.despine()
#https://en.wikipedia.org/wiki/Financial_and_social_rankings_of_sovereign_states_in_Europe
f, (ax1, ax2) = plt.subplots(1,2, sharey =True, gridspec_kw = {'wspace':0.1, 'hspace':0})
   
fte_graph = dfgdp_percentage.tail(12).plot(x = 'Year', y =[ 
"France", #3
"Germany", #1
"Italy", #4
"Spain",#5
"United Kingdom"], figsize = (20,8),color =['#0000FF','#000000',
                                            '#008000',
                                            '#FFDF00','#FF6347'], ax = ax1)


fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 15)
# Customizing the tick labels of the y-axis 
# fte_graph.set_ylim(0,25)
# # Generate a bolded horizontal line at y = 0 

fte_graph.get_xaxis().get_major_formatter().set_useOffset(False)
# # Add an extra vertical line by tweaking the range of the x-axis
#fte_graph.set_xlim(left = 1, right = 2017)
#plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
#plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)

# # Remove the plot frame lines. They are unnecessary here.
fte_graph.spines['top'].set_visible(False)
fte_graph.spines['bottom'].set_visible(False)
fte_graph.spines['right'].set_visible(False)
fte_graph.spines['left'].set_visible(False)

# # Remove the tick marks; they are unnecessary with the tick lines we just
# # plotted.
fte_graph.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)

# fte_graph.text(x = 2009, y = 26.0, s = "Annual GDP Growth",
#                 fontsize = 15, weight = 'bold', alpha = .75)
fte_graph.set_xlabel('Year',fontsize=15, weight = 'bold')

fte_graph.yaxis.set_major_formatter(plt.FuncFormatter('{}%'.format))
#fte_graph.legend([]) 
fte_graph.set_title("Annual GDP Growth" , fontsize=15)
fte_graph.legend(labels=[
"France",
"Germany",
"Italy",
"Spain",
"United Kingdom"],frameon=False,fontsize= 10,ncol =2,loc='lower right').get_frame().set_edgecolor('red') 
#skip every one x-tick for cleanliness

fte_graph_1 = dfinf_percentage.tail(12).plot(x = 'Year', y = ["France", #3
"Germany", #1
"Italy", #4
"Spain",#5
"United Kingdom"], figsize = (20,8),color =['#0000FF','#000000',
                                            '#008000',
                                            '#FFDF00','#FF6347'], ax = ax2)


fte_graph_1.tick_params(axis = 'both', which = 'major', labelsize = 15)
# Customizing the tick labels of the y-axis 
# fte_graph.set_ylim(0,25)
# # Generate a bolded horizontal line at y = 0 

fte_graph_1.get_xaxis().get_major_formatter().set_useOffset(False)
# # Add an extra vertical line by tweaking the range of the x-axis
#fte_graph.set_xlim(left = 1, right = 2017)
#plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
#plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)

# # Remove the plot frame lines. They are unnecessary here.
fte_graph_1.spines['top'].set_visible(False)
fte_graph_1.spines['bottom'].set_visible(False)
fte_graph_1.spines['right'].set_visible(False)
fte_graph_1.spines['left'].set_visible(False)

# # Remove the tick marks; they are unnecessary with the tick lines we just
# # plotted.
plt.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)

# fte_graph_1.text(x = 2009, y = 26.0, s = "Annual Inflation ",
#                 fontsize = 15, weight = 'bold', alpha = .75)
fte_graph_1.set_xlabel('Year',fontsize=15, weight = 'bold')
fte_graph_1.legend([])
# fte_graph_1.legend(labels=["Austria",
# "Belgium",
# "Bulgaria",
# "Croatia",
# "Cyprus",
# "Czech Republic",
# "Denmark",
# "Estonia",
# "Finland",
# "France",
# "Germany",
# "Greece",
# "Hungary",
# "Ireland",
# "Italy",
# "Latvia",
# "Lithuania",
# "Luxembourg",
# "Malta",
# "Netherlands",
# "Poland",
# "Portugal",
# "Romania",
# "Slovak Republic",
# "Slovenia",
# "Spain",
# "Sweden",
# "United Kingdom"],frameon=False,ncol= 4,fontsize= 8,loc='upper right').get_frame().set_edgecolor('red') 
fte_graph_1.set_title("Annual Inflation" , fontsize=15)
plt.tight_layout
plt.savefig("eu-gdp.png", bbox_inches="tight")


# In[33]:


import matplotlib.style as style
style.use('seaborn-white')
sns.set_color_codes("deep")
sns.despine()
#https://en.wikipedia.org/wiki/Financial_and_social_rankings_of_sovereign_states_in_Europe
#f, (ax) = plt.subplots(1,2, sharey =True, gridspec_kw = {'wspace':0.1, 'hspace':0})
   
fte_graph = dfp_percentage.tail(12).plot(x = 'Year', y = ["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France", #3
"Germany", #1
"Greece",
"Hungary",
"Ireland",
"Italy", #4
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",#5
"Sweden", #2
"United Kingdom"], figsize = (12,8))
                                                          #,color =['#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#0000FF','#000000',
#                                             '#D3D3D3','#D3D3D3','#D3D3D3','#008000','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3',
#                                             '#FFDF00','#D3D3D3','#FF6347'])


fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 9)
# Customizing the tick labels of the y-axis 
# fte_graph.set_ylim(0,25)
# # Generate a bolded horizontal line at y = 0 

fte_graph.get_xaxis().get_major_formatter().set_useOffset(False)
# # Add an extra vertical line by tweaking the range of the x-axis
#fte_graph.set_xlim(left = 1, right = 2017)
#plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
#plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)

# # Remove the plot frame lines. They are unnecessary here.
fte_graph.spines['top'].set_visible(False)
fte_graph.spines['bottom'].set_visible(False)
fte_graph.spines['right'].set_visible(False)
fte_graph.spines['left'].set_visible(False)

# # Remove the tick marks; they are unnecessary with the tick lines we just
# # plotted.
fte_graph.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)

# fte_graph.text(x = 2009, y = 26.0, s = "Annual GDP Growth",
#                 fontsize = 15, weight = 'bold', alpha = .75)
fte_graph.set_xlabel('Year',fontsize=12, weight = 'bold', alpha = .75)

fte_graph.yaxis.set_major_formatter(plt.FuncFormatter('{}%'.format))
#fte_graph.legend([]) 
fte_graph.set_title("Annual GDP Growth" , fontsize=15)
fte_graph.legend(labels=["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France",
"Germany",
"Greece",
"Hungary",
"Ireland",
"Italy",
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",
"Sweden",
"United Kingdom"],frameon=False,ncol= 1,fontsize= 12,bbox_to_anchor=(1.10, 1)).get_frame().set_edgecolor('red') 
#skip every one x-tick for cleanliness


plt.tight_layout
plt.savefig("eu-population.png", bbox_inches="tight")


# In[37]:


import matplotlib.style as style
style.use('seaborn-white')
sns.set_color_codes("deep")
sns.despine()
#https://en.wikipedia.org/wiki/Financial_and_social_rankings_of_sovereign_states_in_Europe
#f, (ax) = plt.subplots(1,2, sharey =True, gridspec_kw = {'wspace':0.1, 'hspace':0})
   
fte_graph = dfc_percentage.tail(12).plot(x = 'Year', y = ["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France", #3
"Germany", #1
"Greece",
"Hungary",
"Ireland",
"Italy", #4
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",#5
"Sweden", #2
"United Kingdom"], figsize = (12,8),color =['#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#0000FF','#000000',
                                            '#D3D3D3','#D3D3D3','#D3D3D3','#008000','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3','#D3D3D3',
                                             '#FFDF00','#D3D3D3','#FF6347'])


#fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 9)
# Customizing the tick labels of the y-axis 
# fte_graph.set_ylim(0,25)
# # Generate a bolded horizontal line at y = 0 

fte_graph.get_xaxis().get_major_formatter().set_useOffset(False)
# # Add an extra vertical line by tweaking the range of the x-axis
#fte_graph.set_xlim(left = 1, right = 2017)
#plt.grid(True, 'major', 'y', ls='--', lw=.5, c='k', alpha=.3)
#plt.grid(True, 'major', 'x', ls='--', lw=.5, c='k', alpha=.3)

# # Remove the plot frame lines. They are unnecessary here.
fte_graph.spines['top'].set_visible(False)
fte_graph.spines['bottom'].set_visible(False)
fte_graph.spines['right'].set_visible(False)
fte_graph.spines['left'].set_visible(False)

# # Remove the tick marks; they are unnecessary with the tick lines we just
# # plotted.
fte_graph.tick_params(axis='both', which='both', bottom=False, top=False,
                labelbottom=True, left=False, right=False, labelleft=True)

# fte_graph.text(x = 2009, y = 26.0, s = "Annual GDP Growth",
#                 fontsize = 15, weight = 'bold', alpha = .75)
fte_graph.set_xlabel('Year',fontsize=15, weight = 'bold')

fte_graph.tick_params(axis = 'both', which = 'major', labelsize = 12)

fte_graph.yaxis.set_major_formatter(plt.FuncFormatter('{}'.format))
#fte_graph.legend([]) 
fte_graph.set_title("Consumer price index (2010 = 100)" , fontsize=15)
fte_graph.legend(labels=["Austria",
"Belgium",
"Bulgaria",
"Croatia",
"Cyprus",
"Czech Republic",
"Denmark",
"Estonia",
"Finland",
"France",
"Germany",
"Greece",
"Hungary",
"Ireland",
"Italy",
"Latvia",
"Lithuania",
"Luxembourg",
"Malta",
"Netherlands",
"Poland",
"Portugal",
"Romania",
"Slovak Republic",
"Slovenia",
"Spain",
"Sweden",
"United Kingdom"],frameon=False,ncol= 1,fontsize= 12,bbox_to_anchor=(1.02, 1)).get_frame().set_edgecolor('red') 
#skip every one x-tick for cleanliness


plt.tight_layout
plt.savefig("eu_consumer_index.png", bbox_inches="tight")


# In[16]:


ax = dfgdp_percentage.tail(5).plot(kind="scatter", x="Year",y="Austria",s =20, edgecolors="grey", linewidth=2,c='#e6194b', label="Austria")
dfgdp_percentage.tail(5).plot(kind="scatter", x="Year",y="Belgium",s =20,ax =ax, edgecolors="grey", linewidth=2,c = '#3cb44b', label="Belgium")
dfgdp_percentage.tail(5).plot(kind="scatter", x="Year",y="Bulgaria",s =20,ax=ax, edgecolors="grey", linewidth=2,c ='#ffe119', label="Bulgaria")
ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))


# In[16]:


ax = dfgdp_percentage.tail(5).plot(kind="scatter", x="Year",y="Austria",s =20, edgecolors="grey", linewidth=2,c='#e6194b', label="Austria")
dfgdp_percentage.tail(5).plot(kind="scatter", x="Year",y="Belgium",s =20,ax =ax, edgecolors="grey", linewidth=2,c = '#3cb44b', label="Belgium")
dfgdp_percentage.tail(5).plot(kind="scatter", x="Year",y="Bulgaria",s =20,ax=ax, edgecolors="grey", linewidth=2,c ='#ffe119', label="Bulgaria")
ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))


# In[69]:


plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()


# In[72]:





# In[28]:


sns.scatterplot(x="Year", y='Austria', data=dfgdp_percentage)


# In[23]:


sns.set(style="whitegrid")
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(30, 4))

# Plot the total crashes
sns.set_color_codes("deep")
sns.scatterplot(x="Year", y='Austria', data=dfgdp_percentage, color="r")
#sns.despine()
plt.title('Total GDP in UK ', fontsize= 15)
plt.xlabel('Year', fontsize= 15)
plt.ylabel('GDP (current US$)', fontsize= 15)
plt.show()


# In[ ]:


sns.set(style="whitegrid")
# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(30, 4))

# Plot the total crashes
sns.set_color_codes("deep")
sns.lineplot(x="Country Name", y='GDP growth (annual %)', data=dfgdp_percentage, color="r")
#sns.despine()
plt.title('Total GDP in UK ', fontsize= 15)
plt.xlabel('Year', fontsize= 15)
plt.ylabel('GDP (current US$)', fontsize= 15)
plt.show()


# ###### Need to reformat all of the cells as above

# In[ ]:


dfgdp_percapita_percentage = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='GDP per capita growth (annual %)']


# In[ ]:


dfgdp = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='GDP (current US$)']


# In[ ]:


df_inflation = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='Inflation, GDP deflator (annual %)']


# In[ ]:


df_cpi = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] =='Consumer price index (2010 = 100)']


# In[ ]:


df_population = dfi2[['Country Name','Indicator Name','1973', '1974', '1975',
       '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017']][dfi2['Indicator Name'] == 'Population growth (annual %)']


# In[ ]:


#Select from 1973
# dfeu = dfeu[['Country Name', 'Indicator Name', '1973', '1974', '1975',
#        '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
#        '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
#        '2016', '2017']]


# In[ ]:


# dfeu = dfi2[dfi2['Indicator Name'].isin(['GDP (current US$)',
#  'GDP per capita (current US$)',
 
#  'GDP growth (annual %)', 
#  'GDP per capita growth (annual %)',
# 'Inflation, GDP deflator (annual %)',
#    'Consumer price index (2010 = 100)',
#     'Population growth (annual %)'])].groupby(['Country Name','Indicator Name']).mean().reset_index()


# In[ ]:


# #Select the row with Total population , select only the years data, transpose the data and reset the index
# dfi2[dfi2['Indicator Name'].isin(['GDP (current US$)',
#  'GDP per capita (current US$)',
 
#  'GDP growth (annual %)', 
#  'GDP per capita growth (annual %)'])].iloc[:,1:60].T.reset_index()

