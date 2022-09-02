from bs4 import BeautifulSoup
import requests
import smtplib
import time
title_price = {}
def refresh_message():
    #url = 'https://www.amazon.in/FancyDressWale-Halloween-Inflatable-Tyrannosaurus-Performance/dp/B085RGBGLC/ref=sr_1_1?crid=1WFJNKSGHPAGC&dchild=1&keywords=dinosaur+costume+for+adults&qid=1594392785&sprefix=dinasour+costime%2Caps%2C292&sr=8-1'

    #for url in urls 

    #sauce = urllib.request.urlopen(url).read()
    #soup = bs4.BeautifulSoup(sauce, "html.parser")
    products.append(get_title(new_soup))
    prices.append(get_price(new_soup))
    ratings.append(get_rating(new_soup))
    reviews.append(get_review_count(new_soup))
    avail.append(get_availability(new_soup))
    '''j = 0
    for p in prices:
        if p == '':
            prices.remove(p)
            products.pop(j)
        j = j + 1 '''
    i = 0
    for product in products:
        title_price[product] = prices[i]
        title_rating[product] = ratings[i]
        title_num_reviews[product] = reviews[i]
        title_avail[product] = avail[i]
        i = i + 1

    #sorted_price = sorted(title_price.values())
    #sorted_title_price = sorted(title_price.items(), key = lambda x: x[1])
    #sorted_title_price = sorted(title_price.items(), key = lambda x:(x[1], x[0]))
    sorted_title_price = sorted(title_price.items(), key = lambda x: x[1], reverse = True)
    #title_price = dict(sorted_title_price)
    j = dict(sorted_title_price)
    '''for i in sorted_title_price:
        for k in title_price.keys():
            if title_price[k] == i:
                sorted_title_price[k] = title_price[k]
                break'''
    #for key, value in     
    #title_price = dict(sorted(title_price.items(), key=lambda item: item[1]))
    #prices = soup.find(id="priceblock_ourprice").get_text()
    #prices = float(prices.replace(",", "").replace("₹", ""))
    #prices_list.append(prices)
    #return prices
#title_price = dict(sorted(title_price.items(), key=lambda item: item[1]))
#message = f""
def create_message():
    message = f""
    for title in j:
        #print(title)
        cr_price = j[title]
        cr_rating = title_rating[title]
        cr_reviews = title_num_reviews[title]
        cr_avail = title_avail[title]
        str1 = f"Product Title = {title}\n"
        str2 = f"{str1}Product Price = {cr_price}\n"
        str3 = f"{str2}Product Rating = {cr_rating}\n"
        str4 = f"{str3}Number of Product Reviews = {cr_reviews}\n"
        str5 = f"{str4}Availability = {cr_avail}\n\n"
        message += str5 #str1 + str2 + str3 + str4 + str5
    print("message sent")

    return message 
def send_email(message, sender_email, sender_password, receiver_email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sender_email, sender_password)
    message = message.replace("\u2013", " ")
    s.sendmail(sender_email, receiver_email, message)
    s.quit()
    # Function to extract Product Title
def get_title(soup):
     
    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
 
        # Inner NavigatableString Object
        title_value = title.string
 
        # Title as a string value
        title_string = title_value.strip()
 
        # # Printing types of values for efficient understanding
        # print(type(title))
        # print(type(title_value))
        # print(type(title_string))
        # print()
 
    except AttributeError:
        title_string = ""   
 
    return title_string
 
# Function to extract Product Price
def get_price(soup):
 
    try:
        #price = soup.find("span", attrs={'class':'a-offscreen'}).string.strip()
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()
 
    except AttributeError:
 
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
 
        except:     
            price = ""  
 
    return price
 
# Function to extract Product Rating
def get_rating(soup):
 
    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
         
    except AttributeError:
         
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = "" 
 
    return rating
 
# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
         
    except AttributeError:
        review_count = ""   
 
    return review_count
 
# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()
 
    except AttributeError:
        available = "Not Available"
 
    return available    



 
products = []
prices = []
ratings = []
reviews = []
avail = []

title_rating = {}
title_num_reviews = {}
title_avail = {}
sorted_title_price = {}
sender_email = "t43375073@gmail.com"
sender_password = "t@lcum43375073!"
receiver_email = "t43375073@gmail.com" 
if __name__ == '__main__':
 
    # Headers for request
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.147 Safari/537.36',
                'Accept-Language': 'en-US'})
    #some how amazon will start to block you if you send to many requests from the same IP Address/User Agent
    #change the user agent with information from this website, 
    #https://www.whatismybrowser.com/guides/the-latest-user-agent/?utm_source=whatismybrowsercom&utm_medium=internal&utm_campaign=breadcrumbs
    #For the current user agent it was originally 157 not 147 and it worked. I don't know what other numbers we can change.
    # The webpage URL
    URL = "https://www.amazon.com/playstation-5/s?k=playstation+5"
    #"https://www.amazon.com/water/s?k=water"
    
    #"https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
    
    
     
    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
 
    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
 
    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
 
    # Store the links
    links_list = []
    '''
    product title array
    product title: product price dict
    product title: rating dict
    product title: availability dict
        '''
    

    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))
 
 


    # Loop for extracting product details from each link 
    for link in links_list:
 
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
 
        new_soup = BeautifulSoup(new_webpage.content, "lxml")

        products.append(get_title(new_soup))
        prices.append(get_price(new_soup))
        ratings.append(get_rating(new_soup))
        reviews.append(get_review_count(new_soup))
        avail.append(get_availability(new_soup))
    '''j = 0
    for p in prices:
        if p == '':
            prices.remove(p)
            products.pop(j)
        j = j + 1 '''  
        # Function calls to display all necessary product information
    '''print("Product Title =", get_title(new_soup))
        print("Product Price =", get_price(new_soup))
        print("Product Rating =", get_rating(new_soup))
        print("Number of Product Reviews =", get_review_count(new_soup))
        print("Availability =", get_availability(new_soup))
        print()
        print()'''
    i = 0
   # print(products)
    for product in products:
        title_price[product] = prices[i]
        title_rating[product] = ratings[i]
        title_num_reviews[product] = reviews[i]
        title_avail[product] = avail[i]
        i = i + 1
    
    #sorted_price = sorted(title_price.values())
    #sorted_title_price = sorted(title_price.items(), key = lambda x:(x[1], x[0]))
    sorted_title_price = sorted(title_price.items(), key = lambda x: x[1], reverse = True)
    j = dict(sorted_title_price)
    #sorted_title_price = sorted(title_price.items(), key = lambda x: x[1])
    #print(title_price)
    print(j)

    '''for i in sorted_title_price:
        for k in title_price.keys():
            if title_price[k] == i:
                sorted_title_price[k] = title_price[k]
                break'''
    #write to file in the format of the above prints in a for loop
    send_email(create_message(), sender_email, sender_password, receiver_email)
    
    while True:
        lowest_price = list(j.values())[0]
        refresh_message()
        curr_lowest = list(j.values())[0]
        if curr_lowest < lowest_price:
            #flag = price_decrease_check(prices_list)
            #if flag:
                #decrease = prices_list[-1] - prices_list[-2]
                #message = f"The price has decrease please check the item. The price decrease by {decrease} rupees."
            send_email(create_message(), sender_email, sender_password, receiver_email) #ADD THE OTHER AGRUMENTS sender_email, sender_password, receiver_email
        time.sleep(43000)
        #count += 1