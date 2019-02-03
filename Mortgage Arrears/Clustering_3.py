
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

import warnings
get_ipython().magic("config InlineBackend.figure_format = 'png' #set 'png' here when working on notebook")
warnings.filterwarnings('ignore') 

# Set some parameters to get good visuals - style to ggplot and size to 15,10
pd.set_option('display.precision',4)

pd.set_option('display.width',170, 'display.max_rows',200, 'display.max_columns',900)


# In[3]:


df = pd.read_csv("mortgage_arrears.csv")


# ##### 26 in the Republic of Ireland and 6 in Northern Ireland .
# This project is about Republic of Ireland
# ##### State

# In[4]:


#list(df.columns)


# In[5]:


#https://www.ireland.com/en-us/about-ireland/discover-ireland/ireland-counties-and-provinces/
df['Provinces'] = ['Leinster',
'Ulster',
'Munster',
'Munster',
'Ulster',
'Leinster',
'Connacht',
'Munster',
'Leinster',
'Leinster',
'Leinster',
'Connacht',
'Munster',
'Leinster',
'Leinster',
'Connacht',
'Leinster',
'Ulster',
'Leinster',
'Connacht',
'Connacht',
'Munster',
'Munster',
'Leinster',
'Leinster',
'Leinster',
'Ireland']


# ### Remove the last row  that is the country

# In[6]:


df = df.head(26)


# ###### Create new features using the difference between yearly and 5 yearly data from census

# In[7]:


#Mortgage Count
df['diff_mortgage_count_1'] = df['2012_Mortgate_Count'] - df['2011_Mortgate_Count']
df['diff_mortgage_count_2'] = df['2013_Mortgate_Count'] - df['2012_Mortgate_Count']
df['diff_mortgage_count_3'] = df['2014_Mortgate_Count'] - df['2013_Mortgate_Count']
df['diff_mortgage_count_4'] = df['2015_Mortgate_Count'] - df['2014_Mortgate_Count']
df['diff_mortgage_count_5'] = df['2016_Countof_mortgages'] - df['2015_Mortgate_Count'] # Different column name
df['diff_mortgage_count_6'] = df['2017_Mortgate_Count'] - df['2016_Countof_mortgages']


# In[8]:


df['2012_Mortgate_Count']


# In[9]:


#New House Prices
df['diff_new_house_price_1'] = df['2012_New_House_Price'] - df['2011_New_House_Price']
df['diff_new_house_price_2'] = df['2013_New_House_Price'] - df['2012_New_House_Price']
df['diff_new_house_price_3'] = df['2014_New_House_Price'] - df['2013_New_House_Price']
df['diff_new_house_price_4'] = df['2015_New_House_Price'] - df['2014_New_House_Price']
df['diff_new_house_price_5'] = df['2016_New_House_Price '] - df['2015_New_House_Price'] # Extra space in the column name
df['diff_new_house_price_6'] = df['2017_New_House_Price'] - df['2016_New_House_Price ']



# In[10]:


#Second House Prices
df['diff_secondhand_house_price_1'] = df['2012_Second_Hand_Price'] - df['2011_Second_Hand_Price']
df['diff_secondhand_house_price_2'] = df['2013_Second_Hand_Price'] - df['2012_Second_Hand_Price']
df['diff_secondhand_house_price_3'] = df['2014_Second_Hand_Price'] - df['2013_Second_Hand_Price']
df['diff_secondhand_house_price_4'] = df['2015_Second_Hand_Price'] - df['2014_Second_Hand_Price']
df['diff_secondhand_house_price_5'] = df['2016_Second_Hand_Price'] - df['2015_Second_Hand_Price']
df['diff_secondhand_house_price_6'] = df['2017_Second_Hand_Price'] - df['2016_Second_Hand_Price']


# In[11]:


#Sum House Prices
df['diff_sum_house_price_1'] = df['2012_Sum_of_Price'] - df['2011_Sum_of_Price']
df['diff_sum_house_price_2'] = df['2013_Sum_of_Price'] - df['2012_Sum_of_Price']
df['diff_sum_house_price_3'] = df['2014_Sum_of_Price'] - df['2013_Sum_of_Price']
df['diff_sum_house_price_4'] = df['2015_Sum_of_Price'] - df['2014_Sum_of_Price']
df['diff_sum_house_price_5'] = df['2016_Sum_of_Price'] - df['2015_Sum_of_Price']
df['diff_sum_house_price_6'] = df['2017_Sum_of_Price'] - df['2016_Sum_of_Price']


# In[12]:


#Average Interest Rate
df['diff_interestrate_1'] = df['2012_AVG_Interest_Rate'] - df['2011_AVG_Interest_Rate']
df['diff_interestrate_2'] = df['2013_AVG_Interest_Rate'] - df['2012_AVG_Interest_Rate']
df['diff_interestrate_3'] = df['2014_AVG_Interest_Rate'] - df['2013_AVG_Interest_Rate']
df['diff_interestrate_4'] = df['2015_AVG_Interest_Rate'] - df['2014_AVG_Interest_Rate']
df['diff_interestrate_5'] = df['2016_AVG_Interest_Rate'] - df['2015_AVG_Interest_Rate']
df['diff_interestrate_6'] = df['2017_AVG_Interest_Rate'] - df['2016_AVG_Interest_Rate']


# In[13]:


#Loan Arrears
df['diff_loanarrears_1'] = df['2012_LA_Arrears'] - df['2011_LA_Arrears']
df['diff_loanarrears_2'] = df['2013_LA_Arrears'] - df['2012_LA_Arrears']
df['diff_loanarrears_3'] = df['2014_LA_Arrears'] - df['2013_LA_Arrears']
df['diff_loanarrears_4'] = df['2015_LA_Arrears'] - df['2014_LA_Arrears']
df['diff_loanarrears_5'] = df['2016_LA_Arrears'] - df['2015_LA_Arrears']
df['diff_loanarrears_6'] = df['2017_LA_Arrears'] - df['2016_LA_Arrears']


# In[14]:


#Loans Approved
df['diff_loanapproved_1'] = df['2012_Loans Approved'] - df['2011_Loans Approved']
df['diff_loanapproved_2'] = df['2013_Loans Approved'] - df['2012_Loans Approved']
df['diff_loanapproved_3'] = df['2014_Loans Approved'] - df['2013_Loans Approved']
df['diff_loanapproved_4'] = df['2015_Loans Approved'] - df['2014_Loans Approved']
df['diff_loanapproved_5'] = df['2016_Loans_Approved'] - df['2015_Loans Approved']
df['diff_loanapproved_6'] = df['2017_Loans Approved'] - df['2016_Loans_Approved']


# In[15]:


#Loans Paid
df['diff_loanpaid_1'] = df['2012_Loans_Paid'] - df['2011_Loans_Paid']
df['diff_loanpaid_2'] = df['2013_Loans_Paid'] - df['2012_Loans_Paid']
df['diff_loanpaid_3'] = df['2014_Loans_Paid'] - df['2013_Loans_Paid']
df['diff_loanpaid_4'] = df['2015_Loans_Paid'] - df['2014_Loans_Paid']
df['diff_loanpaid_5'] = df['2016_Loans_Paid'] - df['2015_Loans_Paid']
df['diff_loanpaid_6'] = df['2017_Loans_Paid'] - df['2016_Loans_Paid']


# ###### Diversity in county according to Sex. Take a difference between the 5 years

# In[16]:



df['2011_diversity_bothsexes'] = df[['2011_African-Both sexes',
'2011_All nationalities-Both sexes',
'2011_American (US)-Both sexes', 
 '2011_Brazilian-Both sexes',
 '2011_French-Both sexes',
 '2011_German-Both sexes',
 '2011_Indian-Both sexes',
 '2011_Irish-Both sexes', 
 '2011_Italian-Both sexes',
 '2011_Latvian-Both sexes',
 '2011_Lithuanian-Both sexes', 
 '2011_Not stated, including no nationality-Both sexes', 
 '2011_Other American-Both sexes', 
 '2011_Other Asian-Both sexes', 
 '2011_Other EU28-Both sexes', 
 '2011_Other European-Both sexes',
 '2011_Other nationalities-Both sexes',
 '2011_Polish-Both sexes', 
 '2011_Romanian-Both sexes', 
 '2011_Spanish-Both sexes', 
 '2011_UK-Both sexes']].sum(axis = 1)


# In[17]:



df['2016_diversity_bothsexes'] = df[['2016_African-Both sexes',
'2016_All nationalities-Both sexes',
'2016_American (US)-Both sexes', 
 '2016_Brazilian-Both sexes',
 '2016_French-Both sexes',
 '2016_German-Both sexes',
 '2016_Indian-Both sexes',
 '2016_Irish-Both sexes', 
 '2016_Italian-Both sexes',
 '2016_Latvian-Both sexes',
 '2016_Lithuanian-Both sexes', 
 '2016_Not stated, including no nationality-Both sexes', 
 '2016_Other American-Both sexes', 
 '2016_Other Asian-Both sexes', 
 '2016_Other EU28-Both sexes', 
 '2016_Other European-Both sexes',
 '2016_Other nationalities-Both sexes',
 '2016_Polish-Both sexes', 
 '2016_Romanian-Both sexes', 
 '2016_Spanish-Both sexes', 
 '2016_UK-Both sexes']].sum(axis = 1)


# In[18]:


df['diff_diversity_bothsexes'] = df['2016_diversity_bothsexes'] - df['2011_diversity_bothsexes']


# In[19]:


#df['diff_diversity_bothsexes']


# In[20]:


df['2011_diversity_female'] = df[['2011_African-Female',
'2011_All nationalities-Female',
'2011_American (US)-Female',
'2011_Brazilian-Female',
'2011_French-Female',
'2011_German-Female',
 '2011_Indian-Female',
'2011_Irish-Female',
 '2011_Italian-Female',
 '2011_Latvian-Female',
'2011_Lithuanian-Female',
'2011_Not stated, including no nationality-Female',
'2011_Other American-Female',
 '2011_Other Asian-Female',
'2011_Other EU28-Female',
 '2011_Other European-Female',
'2011_Other nationalities-Female',
'2011_Polish-Female',
'2011_Romanian-Female',
'2011_Spanish-Female',
 '2011_UK-Female']].sum(axis = 1)


# In[21]:


df['2016_diversity_female'] = df[['2016_African-Female',
'2016_All nationalities-Female',
'2016_American (US)-Female',
'2016_Brazilian-Female',
'2016_French-Female',
'2016_German-Female',
 '2016_Indian-Female',
'2016_Irish-Female',
 '2016_Italian-Female',
 '2016_Latvian-Female',
'2016_Lithuanian-Female',
'2016_Not stated, including no nationality-Female',
'2016_Other American-Female',
 '2016_Other Asian-Female',
'2016_Other EU28-Female',
 '2016_Other European-Female',
'2016_Other nationalities-Female',
'2016_Polish-Female',
'2016_Romanian-Female',
'2016_Spanish-Female',
 '2016_UK-Female']].sum(axis = 1)


# In[22]:


df['diff_diversity_female'] = df['2016_diversity_female'] - df['2011_diversity_female']


# In[23]:


df['2011_diversity_male'] = df[[ '2011_African-Male',
'2011_All nationalities-Male',
 '2011_American (US)-Male',
 '2011_Brazilian-Male',
  '2011_French-Male',
 '2011_German-Male',
 '2011_Indian-Male',
'2011_Irish-Male',
 '2011_Italian-Male',
 '2011_Latvian-Male',
 '2011_Lithuanian-Male',
 '2011_Not stated, including no nationality-Male',
'2011_Other American-Male',
'2011_Other Asian-Male',
'2011_Other EU28-Male',
 '2011_Other European-Male',
 '2011_Other nationalities-Male',
'2011_Polish-Male',
'2011_Romanian-Male',
'2011_Spanish-Male',
 '2011_UK-Male']].sum(axis = 1)


# In[24]:


df['2016_diversity_male'] = df[[ '2016_African-Male',
'2016_All nationalities-Male',
 '2016_American (US)-Male',
 '2016_Brazilian-Male',
  '2016_French-Male',
 '2016_German-Male',
 '2016_Indian-Male',
'2016_Irish-Male',
 '2016_Italian-Male',
 '2016_Latvian-Male',
 '2016_Lithuanian-Male',
 '2016_Not stated, including no nationality-Male',
'2016_Other American-Male',
'2016_Other Asian-Male',
'2016_Other EU28-Male',
 '2016_Other European-Male',
 '2016_Other nationalities-Male',
'2016_Polish-Male',
'2016_Romanian-Male',
'2016_Spanish-Male',
 '2016_UK-Male']].sum(axis = 1)


# In[25]:


df['diff_diversity_male'] = df['2016_diversity_male'] - df['2011_diversity_male']


# In[26]:


df['diff_male_population'] = df['2016_Male_Population'] - df['2011_Male_Population']


# In[27]:


df['diff_female_population'] = df['2016_Female_Population'] - df['2011_Female_Population']


# In[28]:


df['diff_total_population'] = df['2016_Total_Population'] - df['2011_Total_Population']


# In[29]:


df['diff_migration_population'] = df['2016_Migration_Population'] - df['2011_Migration_Population']


# In[30]:


df['diff_1-14years_population'] = df['2016_1 - 14 years'] -df['2011_1 - 14 years']
df['diff_15-19years_population'] = df['2016_15 - 19 years'] -df['2011_15 - 19 years']
df['diff_20-24years_population'] = df['2016_20 - 24 years'] -df['2011_20 - 24 years']
df['diff_25-29years_population'] = df['2016_25 - 29 years'] -df['2011_25 - 29 years']
df['diff_30-34years_population'] = df['2016_30 - 34 years'] -df['2011_30 - 34 years']
df['diff_35-44years_population'] = df['2016_35 - 44 years'] -df['2011_35 - 44 years']
df['diff_45-54years_population'] = df['2016_45 - 54 years'] -df['2011_45 - 54 years']
df['diff_55-64years_population'] = df['2016_55 - 64 years'] -df['2011_55 - 64 years']
df['diff_65-74years_population'] = df['2016_65 - 74 years'] -df['2011_65 - 74 years']
df['diff_75years_over_population'] = df['2016_75 years and over'] -df['2011_75 years and over']


# In[31]:


#Employment
df['diff_employment'] = df['2016_employment'] - df['2011_employment']
df['diff_average'] = df['Average of 2016'] - df['Average of 2011']
df['diff_All persons aged 15 years and over'] = df['2016_All persons aged 15 years and over'] - df['2011_All persons aged 15 years and over']
df['diff_Employer or own account worker'] = df['2016_Employer or own account worker'] - df['2011_Employer or own account worker']
df['diff_Employee'] = df['2016_Employee'] - df['2011_Employee']
df['diff_Assisting_relative'] = df['2016_Assisting_relative'] - df['2011_Assisting_relative']
df['diff_Unemployed looking for first regular job'] = df['2016_Unemployed looking for first regular job'] - df['2011_Unemployed looking for first regular job']
df['diff_Unemployed having lost or given up previous job'] = df['2016_Unemployed having lost or given up previous job'] - df['2011_Unemployed having lost or given up previous job']
df['diff_Student'] = df['2016_Student'] - df['2011_Student']
df['diff_Looking after home/family'] = df['2016_Looking after home/family'] - df['2011_Looking after home/family']
df['diff_Retired'] = df['2016_Retired'] - df['2011_Retired']
df['diff_Unable to work due to permanent sickness or disability'] = df['2016_Unable to work due to permanent sickness or disability'] - df['2011_Unable to work due to permanent sickness or disability']
df['diff_Other economic status'] = df['2016_Other economic status'] - df['2011_Other economic status']


# In[32]:


#martital Status
df['diff_Married_First_Marriage'] = df['2016_Married_First_Marriage'] - df['2011_Married_First_Marriage']
df['diff_divorced'] = df['2016_Divorsed'] - df['2011_Divorsed']
df['diff_Same_Sex_Civil Partners'] = df['2016_Same_Sex_Civil Partners'] - df['2011_Same_Sex_Civil Partners']
df['diff_Remarried'] = df['2016_Remarried'] - df['2011_Remarried']
df['diff_Seperated'] = df['2016_Seperated'] - df['2011_Seperated']
df['diff_Single'] = df['2016_Single'] - df['2011_Single']
df['diff_Widowed'] = df['2016_Widowed'] - df['2011_Widowed']
df['diff_Remarried'] = df['2016_Remarried'] - df['2011_Remarried']



# In[33]:


#Commmuter Information
df['diff_all_depature_timeAll_Persons'] = df['2016_all_depature_timeAll_Persons'] - df['2011_all_depature_timeAll_Persons']
df['diff_all_depature_time_Children at school aged between 5 and 12 years'] = df['2016_all_depature_time_Children at school aged between 5 and 12 years'] - df['2011_all_depature_time_Children at school aged between 5 and 12 years']
df['diff_all_depature_time_Students at school or college aged between 13 and 18 years'] = df['2016_all_depature_time_Students at school or college aged between 13 and 18 years'] - df['2011_all_depature_time_Students at school or college aged between 13 and 18 years']
df['diff_all_depature_time_Students at school or college aged 19 years and over'] = df['2016_all_depature_time_Students at school or college aged 19 years and over'] - df['2011_all_depature_time_Students at school or college aged 19 years and over']
df['diff_all_depature_time_Population aged 15 years and over at work'] = df['2016_all_depature_time_Population aged 15 years and over at work'] - df['2011_all_depature_time_Population aged 15 years and over at work']


# In[34]:


#Type of house
df['diff_AllPrivate'] = df['2016_AllPrivate'] - df['2011_AllPrivate']


# In[35]:


#df


# In[36]:


df.shape


# In[37]:


df['2012_Employees'] = df['2012_Employees'].apply(lambda x: float(x.replace(',', '')))
df['2013_Employees'] = df['2013_Employees'].apply(lambda x: float(x.replace(',', '')))
df['2014_Employees'] = df['2014_Employees'].apply(lambda x: float(x.replace(',', '')))
df['2015_Employees'] = df['2015_Employees'].apply(lambda x: float(x.replace(',', '')))
df['2016_Employees'] = df['2016_Employees'].apply(lambda x: float(x.replace(',', '')))


# In[38]:


#list(train.columns)


# In[39]:


df['sum_forced_possesion'] = df['2011_Forced'] + df['2012_Forced'] + df['2014_Forced'] + df['2015_Forced'] + df['2016_Forced']


# In[40]:


df['sum_voluntary_possesion'] = df['2011_Voluntary'] + df['2012_Voluntary'] + df['2014_Voluntary'] + df['2015_Voluntary']


# In[41]:


df['sum_societal'] = df[['diff_employment',
 'diff_Married_First_Marriage',
 'diff_divorced',
 'diff_Same_Sex_Civil Partners',
 'diff_Remarried',
 'diff_Seperated',
 'diff_Single',
 'diff_Widowed']].sum(axis =1)


# In[42]:


df['sum_population'] = df[['diff_male_population',
 'diff_female_population',
 'diff_total_population',
 'diff_migration_population']].sum(axis =1)


# In[43]:


df['sum_commuter'] = df[['diff_all_depature_timeAll_Persons',
 'diff_all_depature_time_Children at school aged between 5 and 12 years',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years',
 'diff_all_depature_time_Students at school or college aged 19 years and over',
 'diff_all_depature_time_Population aged 15 years and over at work']].sum(axis =1)


# In[44]:


df['ratio_commuter_population'] = df['sum_commuter'] / df['sum_population']


# In[45]:


df['total__diff_loanarrears'] = df[['diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
 'diff_loanarrears_4',
 'diff_loanarrears_5',
 'diff_loanarrears_6']].sum(axis=1)


# In[46]:


df['total_diff_mortgage_count'] = df[['diff_mortgage_count_1',
 'diff_mortgage_count_2',
 'diff_mortgage_count_3',
 'diff_mortgage_count_4',
 'diff_mortgage_count_5',
 'diff_mortgage_count_6']].sum(axis=1)


# In[47]:


#list(df.columns)


# In[48]:


train = df[['County',
'total__diff_loanarrears',
'total_diff_mortgage_count',
# 'diff_male_population',
'sum_societal',
'sum_population',
'sum_commuter',
 #'ratio_commuter_population',
 #'2011_Forced',
# '2011_Voluntary',
# '2012_Forced',
# '2012_Voluntary',
# '2013_Forced',
 #'2013_Voluntary',
 #'2014_Forced',
 #'2014_Voluntary',
 #'2015_Forced',
 #'2015_Voluntary',
# '2016_Forced',
#  '2015_LA_Arrears',
#  '2016_LA_Arrears',
 'sum_forced_possesion',
 'sum_voluntary_possesion'
            ]]
train = train.set_index('County')


# Python's sklearn machine learning library comes with a PCA implementation. This implementation uses the scipy.linalg implementation of the singular value decomposition. It only works for dense arrays (see numPy dense arrays or sparse array PCA if you are using sparse arrays) and is not scalable to large dimensional data. 

# In[49]:


train.columns


# In[50]:


#https://github.com/jadianes/data-science-your-way/blob/master/03-dimensionality-reduction-and-clustering/dimensionality-reduction-clustering-python.ipynb
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(train)


# In[51]:


existing_2d = pca.transform(train)


# In[52]:


existing_df_2d = pd.DataFrame(existing_2d)
existing_df_2d.index = train.index
existing_df_2d.columns = ['PC1','PC2']
#existing_df_2d.set_index(train.index)
#existing_df_2d.to_csv('pca_county.csv')


# In[53]:


print(pca.explained_variance_ratio_)


# We see that the first PC already explains almost 99.4% of the variance, while the second one accounts for another .002% for a total of almost 99.4% between the two of them.

# In[54]:


get_ipython().magic('matplotlib inline')

ax = existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', figsize=(15,5))

for i, country in enumerate(train.index):
    ax.annotate(country, (existing_df_2d.iloc[i].PC2, existing_df_2d.iloc[i].PC1))
plt.title("PCA (All Counties)")
plt.tight_layout()
#plt.show()
plt.savefig("pca_dublin")


# #### Look more for in the grouped together counties

# In[55]:


existing_df_2d.index


# In[57]:


bad_df = existing_df_2d.index.isin(['Carlow', 'Cavan', 'Clare', 'Donegal', 'Kerry', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo',
       'Meath', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Waterford', 'Wicklow'])

existing_df_3d = existing_df_2d[bad_df]

ax = existing_df_3d.plot(kind='scatter', x='PC2', y='PC1', figsize=(15,5))

for i, country in enumerate(existing_df_3d.index):
    ax.annotate(country, (existing_df_3d.iloc[i].PC2, existing_df_3d.iloc[i].PC1))
    
plt.title("PCA")
plt.tight_layout()
#plt.show()
plt.savefig("pca_nodublin")


# In[58]:


#https://mubaris.com/posts/kmeans-clustering/
# https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html
# https://nikkimarinsek.com/blog/7-ways-to-label-a-cluster-plot-python
# https://datascience.stackexchange.com/questions/26783/clustering-for-multiple-variable


# In[59]:


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5)

clusters = kmeans.fit(train)


# In[60]:


existing_df_2d['cluster'] = pd.Series(clusters.labels_, index=existing_df_2d.index)


# In[61]:


existing_df_2d.plot(
    kind='scatter',
    x='PC2',y='PC1',
    c=existing_df_2d.cluster.astype(np.float), 
    figsize=(16,8))


# ##### Provinces

# In[62]:


#https://datascience.stackexchange.com/questions/26783/clustering-for-multiple-variable
#https://medium.com/square-corner-blog/so-you-have-some-clusters-now-what-abfd297a575b


# In[63]:


train2 = df[['total__diff_loanarrears',
'total_diff_mortgage_count',
# 'diff_male_population',
'sum_societal',
'sum_population',
'sum_commuter',
 #'ratio_commuter_population',
 #'2011_Forced',
# '2011_Voluntary',
# '2012_Forced',
# '2012_Voluntary',
# '2013_Forced',
 #'2013_Voluntary',
 #'2014_Forced',
 #'2014_Voluntary',
 #'2015_Forced',
 #'2015_Voluntary',
# '2016_Forced',
#  '2015_LA_Arrears',
'Provinces',
 'sum_forced_possesion',
 'sum_voluntary_possesion']]


# In[64]:


dic = {"Leinster" : 1, "Ulster" : 2,"Munster" : 3, "Connacht" : 4}
train2 = train2.replace({"Provinces": dic})
train2


# In[65]:


X = train2[train2.columns.difference(['Provinces'])]
y = train2['Provinces'].reshape(-1, 1)


# In[67]:


Nc = range(1, 20)

kmeans = [KMeans(n_clusters=i) for i in Nc]

kmeans

score = [kmeans[i].fit(y).score(y) for i in range(len(kmeans))]

score

plt.plot(Nc,score)

plt.xlabel('Number of Clusters')

plt.ylabel('Score')

plt.title('Elbow Curve')

#plt.show()
plt.savefig("elbow_curve")


# In[107]:


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5)

clusters = kmeans.fit(train2)


# In[108]:


existing_df_2d['cluster'] = pd.Series(clusters.labels_, index=existing_df_2d.index)


# In[109]:


existing_df_2d.plot(
    kind='scatter',
    x='PC2',y='PC1',
    c=existing_df_2d.cluster.astype(np.float), 
    figsize=(16,8))


# In[110]:


existing_df_2d.columns


# In[111]:


wh1 =existing_df_2d[['PC1', 'PC2']]


# In[112]:


cor = wh1.corr() #Calculate the correlation of the above variables
sns.heatmap(cor, square = True) #Plot the correlation as heat map


# In[113]:


wh1 =existing_df_2d[['PC1', 'PC2']]
##### Normalizing the table
#Standard Scalar

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
#Scaling of data

ss = StandardScaler()
X = ss.fit_transform(wh1)


# (1) k-means clustering
# 
# In general, k-means is the first choice for clustering because of its simplicity. Here, the user has to define the number of clusters (Post on how to decide the number of clusters would be dealt later). The clusters are formed based on the closeness to the center value of the clusters. The initial center value is chosen randomly. K-means clustering is top-down approach, in the sense, we decide the number of clusters (k) and then group the data points into k clusters.

# In[114]:


from sklearn.cluster import KMeans, AgglomerativeClustering, AffinityPropagation #For clustering
from sklearn.mixture import GaussianMixture #For GMM clustering


# In[115]:


#K means Clustering 
def doKmeans(X, nclust=2):
    model = KMeans(nclust)
    model.fit(X)
    clust_labels = model.predict(X)
    cent = model.cluster_centers_
    return (clust_labels, cent)

clust_labels, cent = doKmeans(wh1, 2)
kmeans = pd.DataFrame(clust_labels)
wh1.insert((wh1.shape[1]),'kmeans',kmeans)


# In[116]:


#Plot the clusters obtained using k means
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['PC1'],wh1[ 'PC2'],
                     c=kmeans[0],s=50)
ax.set_title('K-Means Clustering')
ax.set_xlabel('PC1')
ax.set_ylabel( 'PC2')
plt.colorbar(scatter)
plt.savefig("kmeans")


# In[117]:


#Important-- Rerun the code cell when selecting the columns as well as normalizing before running a different clustering algorithm

wh1 =existing_df_2d[['PC1', 'PC2']]
##### Normalizing the table
#Standard Scalar

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
#Scaling of data

ss = StandardScaler()
X = ss.fit_transform(wh1)


# (2) Agglomerative Clustering
# 
# Also known as Hierarchical clustering, does not require the user to specify the number of clusters. Initially, each point is considered as a separate cluster, then it recursively clusters the points together depending upon the distance between them. The points are clustered in such a way that the distance between points within a cluster is minimum and distance between the cluster is maximum. Commonly used distance measures are Euclidean distance, Manhattan distance or Mahalanobis distance. Unlike k-means clustering, it is "bottom-up" approach.
# 
# Python Tip: Though providing the number of clusters is not necessary but Python provides an option of providing the same for easy and simple use.

# In[119]:


def doAgglomerative(X, nclust=2):
    model = AgglomerativeClustering(n_clusters=nclust, affinity = 'euclidean', linkage = 'ward')
    clust_labels1 = model.fit_predict(X)
    return (clust_labels1)

clust_labels1 = doAgglomerative(wh1, 2)
agglomerative = pd.DataFrame(clust_labels1)
wh1.insert((wh1.shape[1]),'agglomerative',agglomerative)


# In[120]:


#Plot the clusters obtained using Agglomerative clustering or Hierarchical clustering
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['PC1'],wh1['PC2'],
                     c=agglomerative[0],s=50)
ax.set_title('Agglomerative Clustering')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
plt.colorbar(scatter)
plt.savefig("agglome")


# (3) Affinity Propagation
# 
# It does not require the number of cluster to be estimated and provided before starting the algorithm. It makes no assumption regarding the internal structure of the data points. For further details on clustering, refer http://www.learndatasci.com/k-means-clustering-algorithms-python-intro/

# In[121]:


#Important-- Rerun the code cell when selecting the columns as well as normalizing before running a different clustering algorithm

wh1 =existing_df_2d[['PC1', 'PC2']]
##### Normalizing the table
#Standard Scalar

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
#Scaling of data

ss = StandardScaler()
X = ss.fit_transform(wh1)


# In[122]:


def doAffinity(X):
    model = AffinityPropagation(damping = 0.5, max_iter = 250, affinity = 'euclidean')
    model.fit(X)
    clust_labels2 = model.predict(X)
    cent2 = model.cluster_centers_
    return (clust_labels2, cent2)

clust_labels2, cent2 = doAffinity(wh1)
affinity = pd.DataFrame(clust_labels2)
wh1.insert((wh1.shape[1]),'affinity',affinity)


# In[123]:


#Plotting the cluster obtained using Affinity algorithm
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['PC1'],wh1['PC2'],
                     c=affinity[0],s=50)
ax.set_title('Affinity Clustering')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
plt.colorbar(scatter)
plt.savefig("affinity")


# (4) Guassian Mixture Modelling
# 
# It is probabilistic based clustering or kernel density estimation based clusterig. The clusters are formed based on the Gaussian distribution of the centers. For further details and pictorial description, refer https://home.deib.polimi.it/matteucc/Clustering/tutorial_html/mixture.html

# In[124]:


#Important-- Rerun the code cell when selecting the columns as well as normalizing before running a different clustering algorithm

wh1 =existing_df_2d[['PC1', 'PC2']]
##### Normalizing the table
#Standard Scalar

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
#Scaling of data

ss = StandardScaler()
X = ss.fit_transform(wh1)


# In[125]:


def doGMM(X, nclust=2):
    model = GaussianMixture(n_components=nclust,init_params='kmeans')
    model.fit(X)
    clust_labels3 = model.predict(X)
    return (clust_labels3)

clust_labels3 = doGMM(wh1,2)
gmm = pd.DataFrame(clust_labels3)
wh1.insert((wh1.shape[1]),'gmm',gmm)


# In[126]:


#Plotting the cluster obtained using GMM
fig = plt.figure()
ax = fig.add_subplot(111)
scatter = ax.scatter(wh1['PC1'],wh1['PC2'],
                     c=gmm[0],s=50)
ax.set_title('Gaussian Mixture Model')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
plt.colorbar(scatter)
plt.savefig("gmm")

