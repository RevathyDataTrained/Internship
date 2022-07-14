#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium


# In[1]:


import selenium


# In[2]:


from selenium import webdriver


# In[3]:


browser=webdriver.Chrome()


# In[4]:


#Assignment1
data=browser.get("https://www.naukri.com/")


# In[5]:


from selenium.webdriver.common.by import By
searchjob=browser.find_element(By.CLASS_NAME, "suggestor-input")
searchjob.send_keys("Data Analyst")


# In[ ]:





# In[ ]:





# In[339]:


searchlocation=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
searchlocation.send_keys("Bangalore")


# In[340]:


searchbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
searchbtn


# In[341]:


searchbtn.click()


# In[ ]:





# In[342]:


title=browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')






# In[343]:


titleList=[]
for i in range(0,10):
    titleList.append(title[i].text)
titleList  
len(titleList)
    
    
    


# In[344]:


company=browser.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')


# In[345]:


CompanyList=[]
for i in range(0,10):
    CompanyList.append(company[i].text)
print(CompanyList)  
len(CompanyList)


# In[346]:


years=browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')




# In[347]:


YearList=[]
for i in range(0,10):
    YearList.append(years[i].text)
print(YearList)  
len(YearList)


# In[348]:


location=browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')


# In[349]:


LocationList=[]
for i in range(0,10):
    LocationList.append(location[i].text)
print(LocationList)  
len(LocationList)


# In[350]:


import pandas as pd


# In[351]:


jobs=pd.DataFrame()
jobs["Tile"]=titleList
jobs["Company_Name"]=CompanyList
jobs["Experiance"]=YearList
jobs["Location"]=LocationList



# In[352]:


jobs


# In[481]:


#Assignment2
data=browser.get("https://www.naukri.com/")


# In[372]:


searchjob=browser.find_element(By.CLASS_NAME, "suggestor-input")


# In[392]:


searchjob.send_keys("Data Scientist")


# In[374]:


searchlocation=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div/input")
searchlocation.send_keys("Bangalore")


# In[375]:


searchbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
searchbtn


# In[376]:


searchbtn.click()


# In[377]:


title=browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')


# In[378]:


titleList=[]
for i in range(0,10):
    titleList.append(title[i].text)
titleList  
len(titleList)


# In[379]:


company=browser.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')


# In[ ]:





# In[380]:


CompanyList=[]
for i in range(0,10):
    CompanyList.append(company[i].text)
print(CompanyList)  
len(CompanyList)


# In[381]:


years=browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')


# In[382]:


YearList=[]
for i in range(0,10):
    YearList.append(years[i].text)
print(YearList)  
len(YearList)


# In[383]:


location=browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')


# In[ ]:





# In[384]:


LocationList=[]
for i in range(0,10):
    LocationList.append(location[i].text)
print(LocationList)  
len(LocationList)


# In[385]:


jobs=pd.DataFrame()
jobs["Tile"]=titleList
jobs["Company_Name"]=CompanyList
jobs["Experiance"]=YearList
jobs["Location"]=LocationList


# In[ ]:





# In[386]:


jobs


# In[387]:


#Assignment3


# In[437]:


browser=webdriver.Chrome()
data=browser.get("https://www.naukri.com/")


# In[438]:


searchjob=browser.find_element(By.CLASS_NAME, "suggestor-input")


# In[439]:


searchjob.send_keys("Data Scientist")


# In[440]:


searchbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[6]")
searchbtn


# In[441]:


searchbtn.click()


# In[ ]:





# In[442]:


salary=browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[6]/div[2]/div[2]/label/i")
salary


# In[ ]:





# In[443]:


salary.click()


# In[444]:


location=browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[6]/div[2]/div[3]/label/i")


# In[445]:


location.click()


# In[446]:


title=browser.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')


# In[447]:


titleList=[]
for i in range(0,10):
    titleList.append(title[i].text)
titleList  
len(titleList)


# In[448]:


company=browser.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')


# In[449]:


CompanyList=[]
for i in range(0,10):
    CompanyList.append(company[i].text)
print(CompanyList)  
len(CompanyList)


# In[450]:


years=browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')


# In[451]:


YearList=[]
for i in range(0,10):
    YearList.append(years[i].text)
print(YearList)  
len(YearList)


# In[452]:


location=browser.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')


# In[453]:


LocationList=[]
for i in range(0,10):
    LocationList.append(location[i].text)
print(LocationList)  
len(LocationList)


# In[454]:


jobs=pd.DataFrame()
jobs["Tile"]=titleList
jobs["Company_Name"]=CompanyList
jobs["Experiance"]=YearList
jobs["Location"]=LocationList


# In[455]:


jobs


# In[128]:


#Assignment4
browser=webdriver.Chrome()
data=browser.get("https://www.flipkart.com/")


# In[129]:


from selenium.webdriver.common.by import By
sunglass=browser.find_element(By.CLASS_NAME, "_3704LK")


# In[130]:


sunglass.send_keys("sunglass")


# In[ ]:





# In[131]:


searchbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
searchbtn


# In[ ]:





# In[132]:


searchbtn.click()


# In[ ]:





# In[166]:


brand=browser.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
price=browser.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
describtion=browser.find_elements(By.XPATH,'//a[@class="IRpwTa"]')



# In[167]:


brandlist=[]
for i in brand:
    brandlist.append(i.text)
len(brandlist)   
pricelist=[]
for i in price:
    pricelist.append(i.text)
len(pricelist) 
descriptionList=[]
for i in describtion:
    descriptionList.append(i.text)
    
len(descriptionList)  


# In[168]:


nextbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
nextbtn


# In[169]:


nextbtn.click()


# In[170]:


brand=browser.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
price=browser.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
describtion=browser.find_elements(By.XPATH,'//a[@class="IRpwTa"]')


# In[171]:


for i in brand:
    brandlist.append(i.text)
len(brandlist)   

for i in price:
    pricelist.append(i.text)
len(pricelist) 

for i in describtion:
    descriptionList.append(i.text)
    
len(descriptionList)


# In[172]:


nextbtn.click()


# In[173]:


brand=browser.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
price=browser.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
describtion=browser.find_elements(By.XPATH,'//a[@class="IRpwTa"]')


# In[174]:


for i in range(0,20):
    brandlist.append(brand[i].text)
len(brandlist) 
   

for i in range(0,20):
    pricelist.append(price[i].text)
len(pricelist) 

for i in range(0,20):
    descriptionList.append(describtion[i].text)
    
len(descriptionList)


# In[175]:


import pandas as pd
sunglasses=pd.DataFrame()
sunglasses["Brand"]=brandlist
sunglasses["Price"]=pricelist
sunglasses["Description"]=descriptionList


# In[176]:


sunglasses


# In[ ]:


#Assignment5


# In[197]:


browser=webdriver.Chrome()
data=browser.get("https://www.flipkart.com/")


# In[198]:


from selenium.webdriver.common.by import By
sunglass=browser.find_element(By.CLASS_NAME, "_3704LK")


# In[199]:


sunglass.send_keys("iphone 11")


# In[ ]:





# In[200]:


searchbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
searchbtn


# In[201]:


searchbtn.click()


# In[202]:


mobile=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
mobile.click()


# In[500]:


row=browser.find_elements(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[6]/div/div[4]/div[1]/div/div/div[1]/p')
brand
price=browser.find_elements(By.XPATH,'//p[@class="_2-N8zT"]')
describtion=browser.find_elements(By.XPATH,'//div[@class="t-ZTKy"]')
row


# In[501]:


for i in row:
    print(i.text)


# In[236]:


describtion


# In[203]:


#Assignment:6
browser=webdriver.Chrome()
data=browser.get("https://www.flipkart.com/")


# In[204]:


from selenium.webdriver.common.by import By
sneakers=browser.find_element(By.CLASS_NAME, "_3704LK")


# In[205]:


sneakers.send_keys("sneakers")


# In[206]:


searchbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
searchbtn


# In[207]:


searchbtn.click()


# In[208]:


brand=browser.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
price=browser.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
describtion=browser.find_elements(By.XPATH,'//a[@class="IRpwTa"]')


# In[210]:


brandlist=[]
for i in brand:
    brandlist.append(i.text)
len(brandlist)   
pricelist=[]
for i in price:
    pricelist.append(i.text)
len(pricelist) 
descriptionList=[]
for i in describtion:
    if i.text=="":
         descriptionList.append("None")
    else:
         descriptionList.append(i.text)
        
        
   
    
descriptionList


# In[211]:


nextbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
nextbtn


# In[212]:


nextbtn.click()


# In[213]:


brand=browser.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
price=browser.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
describtion=browser.find_elements(By.XPATH,'//a[@class="IRpwTa"]')


# In[ ]:





# In[214]:


for i in brand:
    brandlist.append(i.text)
len(brandlist)   

for i in price:
    pricelist.append(i.text)
len(pricelist) 

for i in describtion:
    if i.text=="":
         descriptionList.append("None")
    else:
         descriptionList.append(i.text)
        
    
len(descriptionList)


# In[ ]:





# In[215]:


nextbtn=browser.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]")
nextbtn.click()


# In[216]:


brand=browser.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
price=browser.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
describtion=browser.find_elements(By.XPATH,'//a[@class="IRpwTa"]')


# In[217]:


for i in range(0,20):
    brandlist.append(brand[i].text)
len(brandlist) 
   

for i in range(0,20):
    pricelist.append(price[i].text)
len(pricelist) 

for i in range(0,33):
    if describtion[i].text=="":
         descriptionList.append("None")
    else:
         descriptionList.append(describtion[i].text)
        
    



# In[218]:


len(descriptionList)


# In[219]:


len(pricelist) 


# In[ ]:





# In[220]:


len(brandlist)


# In[221]:


import pandas as pd
Sneakers=pd.DataFrame()
Sneakers["Brand"]=brandlist
Sneakers["Price"]=pricelist
Sneakers["Description"]=descriptionList
Sneakers


# In[ ]:


#Assignment8


# In[ ]:





# In[ ]:





# In[ ]:





# In[260]:


browser=webdriver.Chrome()
data=browser.get("https://www.amazon.in/")


# In[261]:


core=browser.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")


# In[262]:


core.send_keys("Intel Core i7")


# In[263]:


search=browser.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
search.click()


# In[264]:


filter=browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/div/label/i")
filter.click()


# In[293]:


title=browser.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
ratings=browser.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-beside-button a-text-bold"]')
rate=browser.find_elements(By.XPATH,'//span[@class="a-price-whole"]')


# In[296]:


for i in ratings:
    print(i.text)


# In[294]:


intelcore=pd.DataFrame()


# In[295]:


titlelist=[]
pricelist=[]
ratinglist=[]
for i in range(0,10):
    titlelist.append(title[i].text)
len(titlelist) 
   

for i in range(0,10):
    pricelist.append(rate[i].text)
len(pricelist) 

for i in range(0,2):
    ratinglist.append(ratings[i].text)
    
ratinglist


# In[297]:


intelcore["Title"]=titlelist
intelcore["Price"]=pricelist


# In[324]:


intelcore


# In[329]:


#Assignment:9

browser=webdriver.Chrome()
data=browser.get("https://www.ambitionbox.com/")    


# In[330]:


searchjob=browser.find_element(By.XPATH, "/html/body/div[1]/nav/nav/a[6]")

searchjob.click()


# In[331]:


jobtitle=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/div/span/input")
jobtitle.send_keys("Data Scientist")


# In[332]:


search=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[1]/div/div/div/button")
search.click()


# In[333]:


loc=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[1]/i")
loc.click()


# In[334]:


location=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input")
location.send_keys("Noida")


# In[335]:


selectloc=browser.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div[1]/div/input")
selectloc.click()


# In[359]:


company_name=browser.find_elements(By.XPATH,'//p[@class="company body-medium"]')
Details=browser.find_elements(By.XPATH,'//p[@class="body-small-l"]')



# In[398]:


company_nameList=[]
for i in range(0,10):
    company_nameList.append(company_name[i].text)
len(company_nameList)   
DetailsList=[]
salarylist=[]
locationlist=[]
for i in range(0,10):
    DetailsList.append(Details[i].text)


# In[399]:


job=pd.DataFrame()
job["company_name"]=company_nameList
job["Details"]=DetailsList



# In[400]:


job


# In[414]:


#Assignment:10
browser=webdriver.Chrome()
data=browser.get("https://www.ambitionbox.com/")


# In[415]:


salary=browser.find_element(By.XPATH, "/html/body/div[1]/nav/nav/a[4]")

salary.click()


# In[416]:


designation=browser.find_element(By.XPATH, "/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input")

designation.send_keys("Data Scientist")


# In[474]:


Average_salary=browser.find_elements(By.XPATH,'//div[@class="solid-salary-bar salary-bar-wrapper"]')
salaryrange=browser.find_elements(By.XPATH,'//div[@class="value body-medium"]')
company_name=browser.find_elements(By.XPATH,'//div[@class="company-info-wrapper"]')
exp=browser.find_elements(By.XPATH,'//div[@class="sbold-list-header"]')




# In[478]:


MinimumList=[]
MaximumList=[]
AverageList=[]
company_nameList=[]
experiance_list=[]
for i in range(0,20,2):
    MinimumList.append(salaryrange[i].text)
  

for i in range(1,20,2):
    MaximumList.append(salaryrange[i].text)   
for i in range(0,10):
    AverageList.append(Average_salary[i].text)   
for i in company_name:
    word=(i.text)[0:10]
    if word=="Sof":
        continue
        
    company_nameList.append((i.text)[0:10])
for i in range(0,10):
    experiance_list.append((exp[i].text)[0:3] )
    

experiance_list
    
    
    
    
  
  


# In[479]:


salary=pd.DataFrame()
salary["company_name"]=company_nameList
salary["Experiance"]=experiance_list
salary["Minimum_Salary"]=MaximumList
salary["Average_Salary"]=AverageList
salary["Maximum_salary"]=MaximumList


# In[480]:


salary


# In[ ]:





# In[ ]:




