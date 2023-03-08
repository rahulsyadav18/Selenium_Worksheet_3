#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
import time
import requests


# # QUESTION 1

# In[2]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[3]:


driver.get('https://www.amazon.in./')


# In[4]:


search_tab=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search_tab.click()
search_tab.send_keys('Guiter')


# In[5]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search.click()


# In[1]:


data=input('Enter your keyword:   ')


# # QUESTION 2

# In[ ]:


driver.get('https://www.amazon.in./')


# In[6]:


product_url=[]
start=0
end=3
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url[0:10]:
        product_url.append(i.get_attribute('href'))
        nex_button=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
    nex_button.click()
    time.sleep(2)
    


# In[15]:


len(product_url)


# In[ ]:


#product_url


# In[13]:


brand=[]
Name_of_product=[]
price=[]
delivery=[]
Available=[]
for url in product_url:
    driver.get(url)
    time.sleep(2)
    
    try:
        brand1=driver.find_element(By.XPATH,'//span[@class="a-size-base po-break-word"]')
        brand.append(brand1.text)
                
    except NoSuchElementException:
        brand.append('-')
                                          
    try:
        name=driver.find_element(By.XPATH,'//span[@class="a-size-large product-title-word-break"]')
        Name_of_product.append(name.text)
    except:
        Name_of_product.append('-')
    
    try:
        price1=driver.find_element(By.XPATH,'//span[@class="a-price-whole"]')
        price.append(price1.text)
    except NoSuchElementException:
        price.append('-')
    
    try:
        delivery1=driver.find_element(By.XPATH,'//span[@class="a-text-bold"]')
        delivery.append(delivery1.text)
    except NoSuchElementException:
        delivery.append('-')
        
    try:
        availability1=driver.find_element(By.XPATH,'//span[@class="a-text-bold"]')
        Available.append(availability1.text)
    except NoSuchElementException:
        Available.append('-')
        


# In[11]:


brand


# In[97]:


Name_of_product


# In[14]:


df1=pd.DataFrame({'Brand Name':brand,'Name of Product':Name_of_product,'Price':price,'Delivery':delivery,'Availability': Available})
df1


# # QUESTION 3

# In[3]:


driver.get('https://images.google.com/')


# In[4]:


search_tab=driver.find_element(By.XPATH,'//input[@class="gLFyf"]')
search_tab.click()
search_tab.send_keys('cake')


# In[7]:


search=driver.find_element(By.XPATH,'//span[@class="z1asCe MZy1Rb"]')
search.click()


# In[8]:


for _ in range (20):
    driver.execute_script("window. scrollBy(0,1000)")
    
images=driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')

img_urls=[]
img_data=[]
for i in images:
    source=i.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_urls.append(source)

for i in range(len(img_urls)):
    if i>10:
        breakBy.XPATH,
    print('Downloading {0} of {1} images'.format(i,10))
    response=requests.get(img_urls[i])
    file=open(r"C:\Users\Shree\Desktop\Datatrained"+str(i)+".jpg","wb")
    file.write(response.content)


# # QUESTION 4

# In[16]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[17]:


driver.get('https://www.flipkart.com/')


# In[18]:


button=driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]')
button.click()


# In[19]:


search=driver.find_element(By.XPATH,'//input[@class="_3704LK"]')
search.send_keys('Oneplus Nord')
search_c=driver.find_element(By.XPATH,'//button[@class="L0Z3Pu"]')
search_c.click()


# In[20]:


Brand_name=[]
Ram=[]
Rom=[]


# In[21]:


try:
    brand1=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
    for i in brand1:
        Brand_name.append(i.text)

except NoSuchElementException:
        Brand_name.append('-')      


# In[22]:


try:
    ram1=driver.find_elements(By.XPATH,'//li[@class="rgWa7D"]')
    for i in ram1:
        Ram.append(i.text)

except NoSuchElementException:
        Ram.append('-')


# In[23]:


len(Brand_name)


# In[24]:


ram=Ram[:]


# In[25]:


ram


# In[26]:


price=[]
price1=driver.find_elements(By.XPATH,'//div[@class="_30jeq3 _1_WHN1"]')
for i in price1:
    price.append(i.text)


# In[27]:


rating=[]
rating1=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK"]')
for i in rating1[0:24]:
    rating.append(i.text)


# In[28]:


len(rating)


# In[39]:


ram1=ram[::5][:24]
display=ram[1::5][:24]
rear_camera=ram[2::5]
battery=ram[3::5]
warrenty=ram[4::5]


# In[30]:


ram[:110]


# In[38]:


del ram[39]
ram


# In[40]:


df4=pd.DataFrame({'Brand_Name':Brand_name,'Ram':ram1,'display':display,'rear_camera':rear_camera,'Battery':battery,'Warrenty':warrenty,'Price':price,'Rating':rating})
df4


# In[41]:


len(Brand_name),len(ram1),len(display),len(rear_camera),len(battery),len(warrenty),len(price),len(rating)


# # QUESTION 5

# In[40]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[41]:


driver.get('https://www.google.com/maps/')


# In[42]:


location= driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]")
location.send_keys('Delhi')
location_k=driver.find_element(By.XPATH,'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button')
location_k.click()


# In[43]:


url_string=driver.current_url
url_string


# In[44]:


alt_log=url_string.split('@')
alt_log=alt_log[1]
alt_log


# In[45]:


alt_log=alt_log.split('data')
alt_log=alt_log[0]


# In[46]:


alt_log


# # QUESTION 6

# In[53]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[54]:


driver.get('https://www.digit.in/')


# In[55]:


laptop=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[3]/a')
laptop.click()
laptop_gaming=driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[3]/div/div/div[2]/div/ul[1]/li[3]/a')
laptop_gaming.click()


# In[56]:


website1=[]
website=driver.find_elements(By.XPATH,'//a[@class="review spec"]')
for i in website:
    website1.append(i.get_attribute('href'))


# In[57]:


OS=[]
Display=[]
Processor=[]
Memory=[]
price=[]
Websites=[]
for url in website1:
    driver.get(url)
    time.sleep(2)

    try:
        os1=driver.find_element(By.XPATH,'//div[@class="value"]')
        OS.append(os1.text)
                
    except NoSuchElementException:
        OS.append('-')
        
    try:
        Display1=driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[3]/div/ul/li[2]/div/p[2]/strong')
        Display.append(Display1.text)
                
    except NoSuchElementException:
        Display.append('-')
        
    try:
        Processor1=driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[3]/div/ul/li[3]/div/p[2]/strong')
        Processor.append(Processor1.text)
                
    except NoSuchElementException:
        Processor.append('-')
        
    try:
        price1=driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[4]/div/h2/strong')
        price.append(price1.text)
                
    except NoSuchElementException:
        price.append('-')
        
    try:
        Websites1=driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[1]/div[3]/strong')
        Websites.append(Websites1.text)
                
    except NoSuchElementException:
        Websites.append('-')


# In[58]:


print(len(Display),len(Processor),len(OS),len(price),len(Websites))


# In[59]:


df6=pd.DataFrame({'OS':OS,'Display':Display,'Processor':Processor,'price':price,'Websites':Websites})
df6


# # QUESTION 7

# In[124]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[125]:


driver.get('http://www.forbes.com/')


# In[126]:


menu=driver.find_element(By.XPATH,'//*[@id="globalHeaderMenu"]')
menu.click()


# In[127]:


menu=driver.find_element(By.XPATH,'//div[@class="mpBfVZz3"]')
menu.click()


# In[128]:


menu2=driver.find_element(By.XPATH,'//li[@class="TjJgrPSg _2bNo56RE secondary"]')
menu2.click()


# In[132]:


Rank=[]
Name=[]
Net_worth=[]
Age=[]
Citizenship=[]
Source=[]
Industry=[]

rank1=driver.find_elements(By.XPATH,'//div[@class="rank"]')
for i in rank1[:50]:
    Rank.append(i.text)
    
name1=driver.find_elements(By.XPATH,'//div[@class="personName"]')
for i in name1[:50]:
    Name.append(i.text)
    
worth1=driver.find_elements(By.XPATH,'//div[@class="netWorth"]')
for i in worth1[:50]:
    Net_worth.append(i.text)
    
age1=driver.find_elements(By.XPATH,'//div[@class="age"]')
for i in age1[:50]:
    Age.append(i.text)

citizenship1=driver.find_elements(By.XPATH,'//div[@class="countryOfCitizenship"]')
for i in citizenship1[:50]:
    Citizenship.append(i.text)
    
Source1=driver.find_elements(By.XPATH,'//span[@class="source-text"]')
for i in Source1[:50]:
    Source.append(i.text)
    
Industry1=driver.find_elements(By.XPATH,'//span[@class="source-text"]')
for i in Industry1[:50]:
    Industry.append(i.text)


# In[133]:


print(len(Rank),len(Name),len(Net_worth),len(Age),len(Citizenship),len(Source),len(Industry))


# In[134]:


Industry


# In[135]:


df7=pd.DataFrame({'Rank':Rank,'Name': Name,'Net_worth': Net_worth,'Age': Age,'Citizenship':Citizenship,'Source':Source,'Industry':Industry})
df7


# # QUESTION 8

# In[42]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[43]:


driver.get('https://www.youtube.com/watch?v=wQrV75N2BrI')


# In[44]:


for _ in range(1000):
    driver.execute_script('window.scrollBy(0,500)')


# In[45]:


comments=[]
comment1=driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-expander"]') 
for i in comment1:
    comments.append(i.text)
comments#=comments[9:115]


# In[49]:


comments=comments[2:]
len(comments)


# In[47]:


name=[]
name1=driver.find_elements(By.XPATH,'//span[@class=" style-scope ytd-comment-renderer"]')
for i in name1:
    name.append(i.text)


# In[48]:


len(name)


# In[50]:


timeposting=[]
time1=driver.find_elements(By.XPATH,'//a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
for i in time1:
    timeposting.append(i.text)
#time=timeposting[9:-2]


# In[52]:


len(timeposting)


# In[56]:


time=timeposting[7:-10]
len(time)


# In[ ]:


Upvoke_n=[]
Upvoke1=driver.find_elements(By.XPATH,'//div[@class="style-scope ytd-comment-action-buttons-renderer"]')
try:
    for i in Upvoke1:
        Upvoke_n.append(i.text)
except:
    Upvoke_n.append('-')


# In[ ]:


len(Upvoke_n)


# In[59]:


df8=pd.DataFrame({'Comments given by':name,'Comment':comments,'Time when posted':time})#,'Upvoke (Likes)': Upvoke})
df8


# # QUESTION 9

# In[11]:


driver=webdriver.Chrome(r'C:\Users\Shree\Desktop\Datatrained\chromedriver.exe')


# In[12]:


driver.get('https://www.hostelworld.com/')


# In[14]:


menu=driver.find_element(By.XPATH,'//input[@class="search-input"]')
menu.click()
menu.send_keys('London')
menu.click()


# In[16]:


click1=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/ul/li[2]')
click1.click()


# In[17]:


click2=driver.find_element(By.XPATH,'//button[@class="button primary large"]')
click2.click()


# In[21]:


product_url=[]
start=0
end=2
for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]/a')
    for i in url:
        product_url.append(i.get_attribute('href'))
        button=driver.find_element(By.XPATH,'//i[@class="core-icon icon-core-chevron-right"]')
        time.sleep(2)


# In[22]:


product_url


# In[23]:


len(product_url)


# In[42]:


name=[]
distance=[]
comment=[]
prize=[]
total_reviews=[]
start=0
end=2
for page in range(start,end):
    name1=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
    for i in name1:
        name.append(i.text)
    dis1=driver.find_elements(By.XPATH,'//span[@class="description"]')
    for i in dis1:
        distance.append(i.text)
    comment1=driver.find_elements(By.XPATH,'//div[@class="keyword"]')
    for i in comment1:
        comment.append(i.text)
    prize1=driver.find_elements(By.XPATH,'//div[@class="price title-5"]')
    try:
        for i in prize1:
            prize.append(i.text)
    except:
        prize.append('-')
    total_r1=driver.find_elements(By.XPATH,'//div[@class="reviews"]')
    for i in total_r1:
        total_reviews.append(i.text)


# In[45]:


comment=comment[1:]


# In[33]:


prize1=[]
start=0
end=2
for page in range(start,end):
    prize=driver.find_elements(By.XPATH,'//div[@class="price-col"]')
    try:
        for i in prize:
            prize1.append(i.text)
    except:
        prize1.append('Nil')    


# In[35]:


#prize1


# In[35]:


len(prize1)


# In[40]:


drom=prize1[1::2]
len(drom)
private=prize1[::2]
len(private)


# In[56]:


review2=[]
start=0
end=2
for page in range(start,end):
    review_or=driver.find_elements(By.XPATH,'//div[@class="score orange big"]')
    review_bl=driver.find_elements(By.XPATH,'//div[@class="score gray big"]')
    try:
        for i in review_or:
            review2.append(i.text)    
    except:
        for i in review_bl:
            review2.append(i.text)


# In[58]:


len(review2)


# In[47]:


len(name),len(distance),len(comment),len(total_reviews),len(drom),len(private)


# In[60]:


df9=pd.DataFrame({'Name of Hotel': name,'Diatance fromcentre':distance,'Comments':comment,'Total Reviews': total_reviews,'Dromitory Prize':drom,'Private Romm prize':private})
df9

