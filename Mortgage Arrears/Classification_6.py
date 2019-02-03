
# coding: utf-8

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
pd.set_option('display.precision',4)

pd.set_option('display.width',170, 'display.max_rows',200, 'display.max_columns',900)


# In[2]:


df = pd.read_csv("mortgage_arrears.csv")


# ##### 26 in the Republic of Ireland and 6 in Northern Ireland .
# This project is about Republic of Ireland
# ##### State

# In[3]:


#list(df.columns)


# In[4]:


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

# In[5]:


df = df.head(26)


# ###### Create new features using the difference between yearly and 5 yearly data from census

# In[6]:


#Mortgage Count
df['diff_mortgage_count_1'] = df['2012_Mortgate_Count'] - df['2011_Mortgate_Count']
df['diff_mortgage_count_2'] = df['2013_Mortgate_Count'] - df['2012_Mortgate_Count']
df['diff_mortgage_count_3'] = df['2014_Mortgate_Count'] - df['2013_Mortgate_Count']
df['diff_mortgage_count_4'] = df['2015_Mortgate_Count'] - df['2014_Mortgate_Count']
df['diff_mortgage_count_5'] = df['2016_Countof_mortgages'] - df['2015_Mortgate_Count'] # Different column name
df['diff_mortgage_count_6'] = df['2017_Mortgate_Count'] - df['2016_Countof_mortgages']


# In[7]:


#New House Prices
df['diff_new_house_price_1'] = df['2012_New_House_Price'] - df['2011_New_House_Price']
df['diff_new_house_price_2'] = df['2013_New_House_Price'] - df['2012_New_House_Price']
df['diff_new_house_price_3'] = df['2014_New_House_Price'] - df['2013_New_House_Price']
df['diff_new_house_price_4'] = df['2015_New_House_Price'] - df['2014_New_House_Price']
df['diff_new_house_price_5'] = df['2016_New_House_Price '] - df['2015_New_House_Price'] # Extra space in the column name
df['diff_new_house_price_6'] = df['2017_New_House_Price'] - df['2016_New_House_Price ']



# In[8]:


#Second House Prices
df['diff_secondhand_house_price_1'] = df['2012_Second_Hand_Price'] - df['2011_Second_Hand_Price']
df['diff_secondhand_house_price_2'] = df['2013_Second_Hand_Price'] - df['2012_Second_Hand_Price']
df['diff_secondhand_house_price_3'] = df['2014_Second_Hand_Price'] - df['2013_Second_Hand_Price']
df['diff_secondhand_house_price_4'] = df['2015_Second_Hand_Price'] - df['2014_Second_Hand_Price']
df['diff_secondhand_house_price_5'] = df['2016_Second_Hand_Price'] - df['2015_Second_Hand_Price']
df['diff_secondhand_house_price_6'] = df['2017_Second_Hand_Price'] - df['2016_Second_Hand_Price']


# In[9]:


#Sum House Prices
df['diff_sum_house_price_1'] = df['2012_Sum_of_Price'] - df['2011_Sum_of_Price']
df['diff_sum_house_price_2'] = df['2013_Sum_of_Price'] - df['2012_Sum_of_Price']
df['diff_sum_house_price_3'] = df['2014_Sum_of_Price'] - df['2013_Sum_of_Price']
df['diff_sum_house_price_4'] = df['2015_Sum_of_Price'] - df['2014_Sum_of_Price']
df['diff_sum_house_price_5'] = df['2016_Sum_of_Price'] - df['2015_Sum_of_Price']
df['diff_sum_house_price_6'] = df['2017_Sum_of_Price'] - df['2016_Sum_of_Price']


# In[10]:


#Average Interest Rate
df['diff_interestrate_1'] = df['2012_AVG_Interest_Rate'] - df['2011_AVG_Interest_Rate']
df['diff_interestrate_2'] = df['2013_AVG_Interest_Rate'] - df['2012_AVG_Interest_Rate']
df['diff_interestrate_3'] = df['2014_AVG_Interest_Rate'] - df['2013_AVG_Interest_Rate']
df['diff_interestrate_4'] = df['2015_AVG_Interest_Rate'] - df['2014_AVG_Interest_Rate']
df['diff_interestrate_5'] = df['2016_AVG_Interest_Rate'] - df['2015_AVG_Interest_Rate']
df['diff_interestrate_6'] = df['2017_AVG_Interest_Rate'] - df['2016_AVG_Interest_Rate']


# In[11]:


#Loan Arrears
df['diff_loanarrears_1'] = df['2012_LA_Arrears'] - df['2011_LA_Arrears']
df['diff_loanarrears_2'] = df['2013_LA_Arrears'] - df['2012_LA_Arrears']
df['diff_loanarrears_3'] = df['2014_LA_Arrears'] - df['2013_LA_Arrears']
df['diff_loanarrears_4'] = df['2015_LA_Arrears'] - df['2014_LA_Arrears']
df['diff_loanarrears_5'] = df['2016_LA_Arrears'] - df['2015_LA_Arrears']
df['diff_loanarrears_6'] = df['2017_LA_Arrears'] - df['2016_LA_Arrears']


# In[12]:


#Loans Approved
df['diff_loanapproved_1'] = df['2012_Loans Approved'] - df['2011_Loans Approved']
df['diff_loanapproved_2'] = df['2013_Loans Approved'] - df['2012_Loans Approved']
df['diff_loanapproved_3'] = df['2014_Loans Approved'] - df['2013_Loans Approved']
df['diff_loanapproved_4'] = df['2015_Loans Approved'] - df['2014_Loans Approved']
df['diff_loanapproved_5'] = df['2016_Loans_Approved'] - df['2015_Loans Approved']
df['diff_loanapproved_6'] = df['2017_Loans Approved'] - df['2016_Loans_Approved']


# In[13]:


#Loans Paid
df['diff_loanpaid_1'] = df['2012_Loans_Paid'] - df['2011_Loans_Paid']
df['diff_loanpaid_2'] = df['2013_Loans_Paid'] - df['2012_Loans_Paid']
df['diff_loanpaid_3'] = df['2014_Loans_Paid'] - df['2013_Loans_Paid']
df['diff_loanpaid_4'] = df['2015_Loans_Paid'] - df['2014_Loans_Paid']
df['diff_loanpaid_5'] = df['2016_Loans_Paid'] - df['2015_Loans_Paid']
df['diff_loanpaid_6'] = df['2017_Loans_Paid'] - df['2016_Loans_Paid']


# ###### Diversity in county according to Sex. Take a difference between the 5 years

# In[14]:



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


# In[15]:



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


# In[16]:


df['diff_diversity_bothsexes'] = df['2016_diversity_bothsexes'] - df['2011_diversity_bothsexes']


# In[17]:


#df['diff_diversity_bothsexes']


# In[18]:


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


# In[19]:


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


# In[20]:


df['diff_diversity_female'] = df['2016_diversity_female'] - df['2011_diversity_female']


# In[21]:


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


# In[22]:


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


# In[23]:


df['diff_diversity_male'] = df['2016_diversity_male'] - df['2011_diversity_male']


# In[24]:


df['diff_male_population'] = df['2016_Male_Population'] - df['2011_Male_Population']


# In[25]:


df['diff_female_population'] = df['2016_Female_Population'] - df['2011_Female_Population']


# In[26]:


df['diff_total_population'] = df['2016_Total_Population'] - df['2011_Total_Population']


# In[27]:


df['diff_migration_population'] = df['2016_Migration_Population'] - df['2011_Migration_Population']


# In[28]:


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


# In[29]:


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


# In[30]:


#martital Status
df['diff_Married_First_Marriage'] = df['2016_Married_First_Marriage'] - df['2011_Married_First_Marriage']
df['diff_divorced'] = df['2016_Divorsed'] - df['2011_Divorsed']
df['diff_Same_Sex_Civil Partners'] = df['2016_Same_Sex_Civil Partners'] - df['2011_Same_Sex_Civil Partners']
df['diff_Remarried'] = df['2016_Remarried'] - df['2011_Remarried']
df['diff_Seperated'] = df['2016_Seperated'] - df['2011_Seperated']
df['diff_Single'] = df['2016_Single'] - df['2011_Single']
df['diff_Widowed'] = df['2016_Widowed'] - df['2011_Widowed']
df['diff_Remarried'] = df['2016_Remarried'] - df['2011_Remarried']



# In[31]:


#Commmuter Information
df['diff_all_depature_timeAll_Persons'] = df['2016_all_depature_timeAll_Persons'] - df['2011_all_depature_timeAll_Persons']
df['diff_all_depature_time_Children at school aged between 5 and 12 years'] = df['2016_all_depature_time_Children at school aged between 5 and 12 years'] - df['2011_all_depature_time_Children at school aged between 5 and 12 years']
df['diff_all_depature_time_Students at school or college aged between 13 and 18 years'] = df['2016_all_depature_time_Students at school or college aged between 13 and 18 years'] - df['2011_all_depature_time_Students at school or college aged between 13 and 18 years']
df['diff_all_depature_time_Students at school or college aged 19 years and over'] = df['2016_all_depature_time_Students at school or college aged 19 years and over'] - df['2011_all_depature_time_Students at school or college aged 19 years and over']
df['diff_all_depature_time_Population aged 15 years and over at work'] = df['2016_all_depature_time_Population aged 15 years and over at work'] - df['2011_all_depature_time_Population aged 15 years and over at work']


# In[32]:


#Type of house
df['diff_AllPrivate'] = df['2016_AllPrivate'] - df['2011_AllPrivate']


# In[33]:


df['total_diff_mortgage_count'] = df[['diff_mortgage_count_1',
 'diff_mortgage_count_2',
 'diff_mortgage_count_3',
 'diff_mortgage_count_4',
 'diff_mortgage_count_5',
 'diff_mortgage_count_6']].sum(axis=1)


# In[34]:


df['total__diff_loanarrears'] = df[['diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
 'diff_loanarrears_4',
 'diff_loanarrears_5',
 'diff_loanarrears_6']].sum(axis=1)


# In[35]:


#df


# In[36]:


df.shape


# In[37]:


train = df[['County',
# 'diff_mortgage_count_1',
#  'diff_mortgage_count_2',
#  'diff_mortgage_count_3',
#  'diff_mortgage_count_4',
#  'diff_mortgage_count_5',
#  'diff_mortgage_count_6',
#  'diff_new_house_price_1',
#  'diff_new_house_price_2',
#  'diff_new_house_price_3',
#  'diff_new_house_price_4',
#  'diff_new_house_price_5',
#  'diff_new_house_price_6',
#  'diff_secondhand_house_price_1',
#  'diff_secondhand_house_price_2',
#  'diff_secondhand_house_price_3',
#  'diff_secondhand_house_price_4',
#  'diff_secondhand_house_price_5',
#  'diff_secondhand_house_price_6',
#  'diff_sum_house_price_1',
#  'diff_sum_house_price_2',
#  'diff_sum_house_price_3',
#  'diff_sum_house_price_4',
#  'diff_sum_house_price_5',
#  'diff_sum_house_price_6',
#  'diff_interestrate_1',
#  'diff_interestrate_2',
#  'diff_interestrate_3',
#  'diff_interestrate_4',
#  'diff_interestrate_5',
#  'diff_interestrate_6',
 'diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
 'diff_loanarrears_4',
 'diff_loanarrears_5',
 'diff_loanarrears_6',
#  'diff_loanapproved_1',
#  'diff_loanapproved_2',
#  'diff_loanapproved_3',
#  'diff_loanapproved_4',
#  'diff_loanapproved_5',
#  'diff_loanapproved_6',
#  'diff_loanpaid_1',
#  'diff_loanpaid_2',
#  'diff_loanpaid_3',
#  'diff_loanpaid_4',
#  'diff_loanpaid_5',
#  'diff_loanpaid_6',
#    'diff_diversity_bothsexes',
#    'diff_diversity_female','diff_diversity_male',
 'diff_male_population',
 'diff_female_population',
 'diff_total_population',
 'diff_migration_population',
 'diff_1-14years_population',
 'diff_15-19years_population',
 'diff_20-24years_population',
 'diff_25-29years_population',
 'diff_30-34years_population',
 'diff_35-44years_population',
 'diff_45-54years_population',
 'diff_55-64years_population',
 'diff_65-74years_population',
 'diff_75years_over_population',
 'diff_employment',
#  'diff_average',
 'diff_Married_First_Marriage',
 'diff_divorced',
 'diff_Same_Sex_Civil Partners',
 'diff_Remarried',
 'diff_Seperated',
 'diff_Single',
 'diff_Widowed',
   'diff_AllPrivate',
 'diff_All persons aged 15 years and over',
 'diff_Employer or own account worker',
 'diff_Employee',
 'diff_Assisting_relative',
 'diff_Unemployed looking for first regular job',
 'diff_Unemployed having lost or given up previous job',
 'diff_Student',
 'diff_Looking after home/family',
 'diff_Retired',
 'diff_Unable to work due to permanent sickness or disability',
 'diff_Other economic status',
 'diff_all_depature_timeAll_Persons',
 'diff_all_depature_time_Children at school aged between 5 and 12 years',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years',
 'diff_all_depature_time_Students at school or college aged 19 years and over',
 'diff_all_depature_time_Population aged 15 years and over at work',
   #Loans Approved

#  '2011_Loans Approved',
#  '2012_Loans Approved',
#  '2013_Loans Approved',
#  '2014_Loans Approved',
#  '2015_Loans Approved', 
# '2016_Loans_Approved',#
#  '2017_Loans Approved',

# #Loans Paid
# '2011_Loans_Paid',
# '2012_Loans_Paid',
# '2013_Loans_Paid',
#  '2014_Loans_Paid',
# '2015_Loans_Paid',
#  '2017_Loans_Paid', 
#  '2016_Loans_Paid',

# Repossesions of the houses

'2011_Forced',
 '2011_Voluntary',
 '2012_Forced',
 '2012_Voluntary',
 '2013_Forced',
 '2013_Voluntary',
 '2014_Forced',
 '2014_Voluntary',
 '2015_Forced',
 '2015_Voluntary',
 '2016_Forced',
#  '2017_Voluntary',
#  '2017_Forced',#May be remove this
#  '2017_Voluntary.1',#Remove this

# #Number of Employees
 '2012_Employees',
 '2013_Employees',
 '2014_Employees',
 '2015_Employees',
 '2016_Employees',

#Arrears—
# '2011_LA_Arrears',
# '2012_LA_Arrears',
#  '2013_LA_Arrears',
# '2014_LA_Arrears',
'2015_LA_Arrears',
 '2016_LA_Arrears',
#'2017_LA_Arrears',
# Target Label
'Provinces'
           ]]


# In[38]:


train['2012_Employees'] = train['2012_Employees'].apply(lambda x: float(x.replace(',', '')))
train['2013_Employees'] = train['2013_Employees'].apply(lambda x: float(x.replace(',', '')))
train['2014_Employees'] = train['2014_Employees'].apply(lambda x: float(x.replace(',', '')))
train['2015_Employees'] = train['2015_Employees'].apply(lambda x: float(x.replace(',', '')))
train['2016_Employees'] = train['2016_Employees'].apply(lambda x: float(x.replace(',', '')))


# ## Feature Selection

# In[39]:


#Remove county and the target label
#https://github.com/amueller/ml-workshop-4-of-4/blob/master/notebooks/02%20Feature%20selection.ipynb
#X = features.drop('delinquent', axis=1)
X = train[train.columns.difference(['County','Provinces'])]
y = train['Provinces']


# In[40]:


#Removing features with low variance
from sklearn.feature_selection import VarianceThreshold
threshold = 0.90
vt = VarianceThreshold().fit(X)

# Find feature names
feat_var_threshold = X.columns[vt.variances_ > threshold * (1-threshold)]
feat_var_threshold


# In[41]:


pd.DataFrame({'variance': vt.variances_,
              'select_feature': vt.get_support()},
            index=X.columns).T


# In[42]:


#Top 15 most important features
#According to RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X, y)
importance_scores = model.feature_importances_
feature_importances = [(feature, score) for feature, score in zip(X.columns, importance_scores)]
sorted(feature_importances, key=lambda x: -x[1])[:5]


# In[43]:


#Recursive Feature Elimination
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

lr = LogisticRegression()
rfe = RFE(estimator=lr, n_features_to_select=15, step=1)
rfe.fit(X, y)
select_features_rfe = rfe.get_support()
feature_names_rfe = X.columns[select_features_rfe]
print(feature_names_rfe)


# In[44]:


set(['diff_All persons aged 15 years and over',
 'diff_employment', 
 'diff_Single',
 'diff_total_population',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years'])


# In[45]:


#Set of the Select Kbest and RFE
set(feat_var_threshold) & set(feature_names_rfe) & set(['diff_All persons aged 15 years and over',
 'diff_employment', 
 'diff_Single',
 'diff_total_population',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years'])


# In[46]:


X = train[['diff_Single',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years',
 'diff_employment']]


# In[47]:


#Standard Scalar
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
ss = StandardScaler()
X = ss.fit_transform(X)


# In[48]:


from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier, VotingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score, roc_auc_score
from sklearn import model_selection
loocv = model_selection.LeaveOneOut()

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('K-NN', KNeighborsClassifier(n_neighbors=5)))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC(probability=True)))
models.append(('RFC', RandomForestClassifier()))
models.append(('ADA', AdaBoostClassifier()))
models.append(('GBC', GradientBoostingClassifier()))
models.append(('MLP', MLPClassifier()))

# Evaluate each model in turn
accuracy = []
names = []
std =[]
#loocv = model_selection.LeaveOneOut()

for name, model in models:
    results = model_selection.cross_val_score(model, X, y, cv=loocv)
    accuracy.append(results.mean()*100.0)
    std.append(results.std()*100.0)
    #roc.append(roc_auc_score(y_test, predictions))
    
    names.append(name)
for name, acc,s in zip(names, accuracy,std):
    #Accuracy mean and standard deviation
    print("Model: {0:10s} : Accuracy: {1:4.3f}% | ({2:4.3f}%)".format(name,acc,s))
    ## boxplot algorithm comparison


# #### The accuracy is no good. We try stepwise classification or greedy selection of variables

# In[49]:


train = df[['County',
# 'diff_mortgage_count_1',
#  'diff_mortgage_count_2',
#  'diff_mortgage_count_3',
#  'diff_mortgage_count_4',
#  'diff_mortgage_count_5',
#  'diff_mortgage_count_6',
#  'diff_new_house_price_1',
#  'diff_new_house_price_2',
#  'diff_new_house_price_3',
#  'diff_new_house_price_4',
#  'diff_new_house_price_5',
#  'diff_new_house_price_6',
#  'diff_secondhand_house_price_1',
#  'diff_secondhand_house_price_2',
#  'diff_secondhand_house_price_3',
#  'diff_secondhand_house_price_4',
#  'diff_secondhand_house_price_5',
#  'diff_secondhand_house_price_6',
#  'diff_sum_house_price_1',
#  'diff_sum_house_price_2',
#  'diff_sum_house_price_3',
#  'diff_sum_house_price_4',
#  'diff_sum_house_price_5',
#  'diff_sum_house_price_6',
#  'diff_interestrate_1',
#  'diff_interestrate_2',
#  'diff_interestrate_3',
#  'diff_interestrate_4',
#  'diff_interestrate_5',
#  'diff_interestrate_6',
 'diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
 'diff_loanarrears_4',
 'diff_loanarrears_5',
 'diff_loanarrears_6',
#  'diff_loanapproved_1',
#  'diff_loanapproved_2',
#  'diff_loanapproved_3',
#  'diff_loanapproved_4',
#  'diff_loanapproved_5',
#  'diff_loanapproved_6',
#  'diff_loanpaid_1',
#  'diff_loanpaid_2',
#  'diff_loanpaid_3',
#  'diff_loanpaid_4',
#  'diff_loanpaid_5',
#  'diff_loanpaid_6',
#    'diff_diversity_bothsexes',
#    'diff_diversity_female','diff_diversity_male',
 'diff_male_population',
 'diff_female_population',
 'diff_total_population',
 'diff_migration_population',
#  'diff_1-14years_population',
#  'diff_15-19years_population',
#  'diff_20-24years_population',
#  'diff_25-29years_population',
#  'diff_30-34years_population',
#  'diff_35-44years_population',
#  'diff_45-54years_population',
#  'diff_55-64years_population',
#  'diff_65-74years_population',
#  'diff_75years_over_population',
 'diff_employment',
#  'diff_average',
 'diff_Married_First_Marriage',
 'diff_divorced',
 'diff_Same_Sex_Civil Partners',
 'diff_Remarried',
 'diff_Seperated',
 'diff_Single',
 'diff_Widowed',
#    'diff_AllPrivate',
#  'diff_All persons aged 15 years and over',
#  'diff_Employer or own account worker',
#  'diff_Employee',
#  'diff_Assisting_relative',
#  'diff_Unemployed looking for first regular job',
#  'diff_Unemployed having lost or given up previous job',
#  'diff_Student',
#  'diff_Looking after home/family',
#  'diff_Retired',
#  'diff_Unable to work due to permanent sickness or disability',
#  'diff_Other economic status',
 'diff_all_depature_timeAll_Persons',
 'diff_all_depature_time_Children at school aged between 5 and 12 years',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years',
 'diff_all_depature_time_Students at school or college aged 19 years and over',
 'diff_all_depature_time_Population aged 15 years and over at work',
   #Loans Approved

#  '2011_Loans Approved',
#  '2012_Loans Approved',
#  '2013_Loans Approved',
#  '2014_Loans Approved',
#  '2015_Loans Approved', 
# '2016_Loans_Approved',#
#  '2017_Loans Approved',

# #Loans Paid
# '2011_Loans_Paid',
# '2012_Loans_Paid',
# '2013_Loans_Paid',
#  '2014_Loans_Paid',
# '2015_Loans_Paid',
#  '2017_Loans_Paid', 
#  '2016_Loans_Paid',

# Repossesions of the houses

'2011_Forced',
 '2011_Voluntary',
 '2012_Forced',
 '2012_Voluntary',
 '2013_Forced',
 '2013_Voluntary',
 '2014_Forced',
 '2014_Voluntary',
 '2015_Forced',
 '2015_Voluntary',
 '2016_Forced',
#  '2017_Voluntary',
#  '2017_Forced',#May be remove this
#  '2017_Voluntary.1',#Remove this

# #Number of Employees
#  '2012_Employees',
#  '2013_Employees',
#  '2014_Employees',
#  '2015_Employees',
#  '2016_Employees',

#Arrears—
# '2011_LA_Arrears',
# '2012_LA_Arrears',
#  '2013_LA_Arrears',
# '2014_LA_Arrears',
'2015_LA_Arrears',
 '2016_LA_Arrears',
#'2017_LA_Arrears',
# Target Label
'Provinces'
           ]]


# In[50]:


#list(train.columns)


# In[51]:


train['sum_forced_possesion'] = df['2011_Forced'] + df['2012_Forced'] + df['2014_Forced'] + df['2015_Forced'] + df['2016_Forced']


# In[52]:


train['sum_voluntary_possesion'] = df['2011_Voluntary'] + df['2012_Voluntary'] + df['2014_Voluntary'] + df['2015_Voluntary']


# In[53]:


train['sum_societal'] = df[['diff_employment',
 'diff_Married_First_Marriage',
 'diff_divorced',
 'diff_Same_Sex_Civil Partners',
 'diff_Remarried',
 'diff_Seperated',
 'diff_Single',
 'diff_Widowed']].sum(axis =1)


# In[54]:


train['sum_population'] = df[['diff_male_population',
 'diff_female_population',
 'diff_total_population',
 'diff_migration_population']].sum(axis =1)


# In[55]:


train['sum_commuter'] = df[['diff_all_depature_timeAll_Persons',
 'diff_all_depature_time_Children at school aged between 5 and 12 years',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years',
 'diff_all_depature_time_Students at school or college aged 19 years and over',
 'diff_all_depature_time_Population aged 15 years and over at work']].sum(axis =1)


# In[56]:


train['ratio_commuter_population'] = train['sum_commuter'] / train['sum_population']


# In[57]:


list(train.columns)


# In[58]:


df1 = train[['County',
 'diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
 'diff_loanarrears_4',
 'diff_loanarrears_5',
 'diff_loanarrears_6',
 'diff_employment',
           'sum_forced_possesion',
 'sum_voluntary_possesion',
            'sum_population',
             'sum_commuter',
             #'ratio_commuter_population',
             '2015_LA_Arrears',
 '2016_LA_Arrears',
            'Provinces']]


# https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/

# In[61]:


df2 = train[['County',
 'diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
 'diff_loanarrears_4',
 'diff_loanarrears_5',
 'diff_loanarrears_6',
 'diff_employment',
           'sum_forced_possesion',
 'sum_voluntary_possesion',
            'sum_population',
             'sum_commuter',
             'ratio_commuter_population',
             
             #'2015_LA_Arrears',
 #'2016_LA_Arrears',
            'Provinces']]

X2 = df2[df2.columns.difference(['County','Provinces'])]
y2 = df2['Provinces']
#Standard Scalar
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
ss = StandardScaler()
X2 = ss.fit_transform(X2)

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier, VotingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score, roc_auc_score

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('K-NN', KNeighborsClassifier(n_neighbors=5)))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC(probability=True)))
models.append(('RFC', RandomForestClassifier()))
models.append(('ADA', AdaBoostClassifier()))
models.append(('GBC', GradientBoostingClassifier()))
models.append(('MLP', MLPClassifier()))

# Evaluate each model in turn
accuracy = []
names = []
std =[]
#loocv = model_selection.LeaveOneOut()

for name, model in models:
    results = model_selection.cross_val_score(model, X2, y2, cv=loocv)
    accuracy.append(results.mean()*100.0)
    std.append(results.std()*100.0)
    #roc.append(roc_auc_score(y_test, predictions))
    
    names.append(name)
for name, acc,s in zip(names, accuracy,std):
    #Accuracy mean and standard deviation
    print("Model: {0:10s} : Accuracy: {1:4.3f}% | ({2:4.3f}%)".format(name,acc,s))
    ## boxplot algorithm comparison


# ## Summing the features do not work well and hence have to go back to selecting the different variables.

# In[62]:


df2 = df[['County',
 'diff_loanarrears_1',
 'diff_loanarrears_2',
 'diff_loanarrears_3',
'diff_loanarrears_4',
'diff_loanarrears_5',
 'diff_loanarrears_6',
# 'diff_mortgage_count_1',
#  'diff_mortgage_count_2',
#  'diff_mortgage_count_3',
#  'diff_mortgage_count_4',
#  'diff_mortgage_count_5',
#  'diff_mortgage_count_6',
#'total__diff_loanarrears',
#'total_diff_mortgage_count',
# 'diff_male_population',
 'diff_female_population', # strange require female population for more accuracy
#  #'diff_total_population',
# # 'diff_migration_population',
 'diff_employment',
 'diff_Married_First_Marriage',
 'diff_divorced',
 #'diff_Same_Sex_Civil Partners',
 'diff_Remarried',
'diff_Seperated',
 'diff_Single',
 'diff_Widowed',
  'diff_all_depature_timeAll_Persons',
 'diff_all_depature_time_Children at school aged between 5 and 12 years',
 'diff_all_depature_time_Students at school or college aged between 13 and 18 years',
 'diff_all_depature_time_Students at school or college aged 19 years and over',
 'diff_all_depature_time_Population aged 15 years and over at work',
#             'sum_societal',
# 'sum_population',
 #'sum_commuter',
 #'ratio_commuter_population',
 '2011_Forced',
 '2011_Voluntary',
'2012_Forced',
'2012_Voluntary',
'2013_Forced',
 '2013_Voluntary',
'2014_Forced',
'2014_Voluntary',
 '2015_Forced',
 #'2015_Voluntary',
 '2016_Forced',
#  '2015_LA_Arrears',
#  '2016_LA_Arrears',
 'Provinces',
#  'sum_forced_possesion',
#  'sum_voluntary_possesion'
            ]]
X2 = df2[df2.columns.difference(['County','Provinces'])]
y2 = df2['Provinces']
#Standard Scalar
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
ss = StandardScaler()
X2 = ss.fit_transform(X2)

from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier, VotingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,accuracy_score, roc_auc_score

models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('K-NN', KNeighborsClassifier(n_neighbors=5)))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC(probability=True)))
models.append(('RFC', RandomForestClassifier()))
models.append(('ADA', AdaBoostClassifier()))
models.append(('GBC', GradientBoostingClassifier()))
models.append(('MLP', MLPClassifier()))

# Evaluate each model in turn
accuracy = []
names = []
std =[]
#loocv = model_selection.LeaveOneOut()

for name, model in models:
    results = model_selection.cross_val_score(model, X2, y2, cv=loocv)
    accuracy.append(results.mean()*100.0)
    std.append(results.std()*100.0)
    #roc.append(roc_auc_score(y_test, predictions))
    
    names.append(name)
for name, acc,s in zip(names, accuracy,std):
    #Accuracy mean and standard deviation
    print("Model: {0:10s} : Accuracy: {1:4.3f}% | ({2:4.3f}%)".format(name,acc,s))
    ## boxplot algorithm comparison


# https://machinelearningmastery.com/how-to-tune-algorithm-parameters-with-scikit-learn/
# 
# https://medium.com/@elutins/grid-searching-in-machine-learning-quick-explanation-and-python-implementation-550552200596

# In[87]:


from sklearn import ensemble
gridSearch_params = {'loss':'deviance', 'learning_rate':0.1, 'n_estimators':200,'min_samples_split':2, 'max_depth':3,  'min_samples_leaf': 1,'random_state':2}

#{'random_state': 20,'criterion': 'friedman_mse', 'learning_rate': 0.05, 'loss': 'deviance', 'max_depth': 8, 'max_features': 'sqrt', 'min_samples_leaf': 0.13636363636363638, 'min_samples_split': 0.13636363636363638, 'n_estimators': 10, 'subsample': 1.0}

loocv = model_selection.LeaveOneOut()
model =  ensemble.GradientBoostingClassifier(**gridSearch_params)
results = model_selection.cross_val_score(model, X2, y2, cv=loocv)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))



# In[88]:


#https://stackoverflow.com/questions/40057049/using-confusion-matrix-as-scoring-metric-in-cross-validation-in-scikit-learn
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
y_pred = cross_val_predict(model, X2, y2, cv=loocv)
conf_mat = confusion_matrix(y2, y_pred)
conf_mat


# In[89]:


# https://stackoverflow.com/questions/39685740/calculate-sklearn-roc-auc-score-for-multi-class
from scipy import interp

from  sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import LabelBinarizer

def class_report(y_true, y_pred, y_score=None, average='micro'):
    if y_true.shape != y_pred.shape:
        print("Error! y_true %s is not the same shape as y_pred %s" % (
              y_true.shape,
              y_pred.shape)
        )
        return

    lb = LabelBinarizer()

    if len(y_true.shape) == 1:
        lb.fit(y_true)
    #Value counts of predictions
    labels, cnt = np.unique(
        y_pred,
        return_counts=True)
    n_classes = len(labels)
    pred_cnt = pd.Series(cnt, index=labels)

    metrics_summary = precision_recall_fscore_support(
            y_true=y_true,
            y_pred=y_pred,
            labels=labels)

    avg = list(precision_recall_fscore_support(
            y_true=y_true, 
            y_pred=y_pred,
            average='weighted'))
    metrics_sum_index = ['precision', 'recall', 'f1-score', 'support']
    class_report_df = pd.DataFrame(
        list(metrics_summary),
        index=metrics_sum_index,
        columns=labels)

    support = class_report_df.loc['support']
    total = support.sum() 
    class_report_df['avg / total'] = avg[:-1] + [total]

    class_report_df = class_report_df.T
    class_report_df['pred'] = pred_cnt
    class_report_df['pred'].iloc[-1] = total

    if not (y_score is None):
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        for label_it, label in enumerate(labels):
            fpr[label], tpr[label], _ = roc_curve(
                (y_true == label).astype(int), 
                y_score[:, label_it])

            roc_auc[label] = auc(fpr[label], tpr[label])

        if average == 'micro':
            if n_classes <= 2:
                fpr["avg / total"], tpr["avg / total"], _ = roc_curve(
                    lb.transform(y_true).ravel(), 
                    y_score[:, 1].ravel())
            else:
                fpr["avg / total"], tpr["avg / total"], _ = roc_curve(
                        lb.transform(y_true).ravel(), 
                        y_score.ravel())

            roc_auc["avg / total"] = auc(
                fpr["avg / total"], 
                tpr["avg / total"])

        elif average == 'macro':
            # First aggregate all false positive rates
            all_fpr = np.unique(np.concatenate([
                fpr[i] for i in labels]
            ))

            # Then interpolate all ROC curves at this points
            mean_tpr = np.zeros_like(all_fpr)
            for i in labels:
                mean_tpr += interp(all_fpr, fpr[i], tpr[i])

            # Finally average it and compute AUC
            mean_tpr /= n_classes

            fpr["macro"] = all_fpr
            tpr["macro"] = mean_tpr

            roc_auc["avg / total"] = auc(fpr["macro"], tpr["macro"])

        class_report_df['AUC'] = pd.Series(roc_auc)

    return class_report_df


# In[90]:


sk_report = classification_report(
    digits=6,
    y_true=y2, 
    y_pred=cross_val_predict(model, X2, y2, cv=loocv))
print(sk_report)


# In[91]:


report_with_auc = class_report(
    y_true=y2,
    y_pred=cross_val_predict(model, X2, y2, cv=loocv), 
    y_score= cross_val_predict(model, X2, y2, cv=loocv, method='predict_proba'))

print(report_with_auc)


# In[92]:


r_auc = pd.DataFrame(report_with_auc)


# In[94]:


r_auc['AUC'].plot(kind ='barh')


# In[95]:


plt.rcParams["figure.figsize"] = (15,10)


# In[112]:


predictors=list(df2[df2.columns.difference(['County','Provinces'])])
model.fit(X2, y2)
feat_imp = pd.Series(model.feature_importances_, predictors).sort_values(ascending=True)
feat_imp.plot(kind='barh', title='Importance of Features')
plt.xlabel('Feature Importance Score')


# In[111]:


feat_imp.tail(10).plot(kind='barh', title='Importance of Features')
plt.xlabel('Feature Importance Score')
plt.ylabel('Feature')


# In[167]:


from sklearn.externals.six import StringIO  

dtc = DecisionTreeClassifier(min_samples_leaf=0.125, min_samples_split=0.125)
dtc.fit(X2, y2)
from sklearn import tree


# In[169]:


tree.export_graphviz(dtc, out_file="tree.dot", feature_names=predictors, proportion=True)

