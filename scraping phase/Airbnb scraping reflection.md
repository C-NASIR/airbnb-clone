# Reflection on scraping the AirBnB website.

## Goal: Scrap the data on the Airbnb home page.

### ********\*\*\*\*********Processes********\*\*\*\*********

**Scrapy**: Scrapy is one of the best Python data scraping frameworks.

I learned about scrapy and how to use it. I practiced using the [https://quotes.toscrape.com/](https://quotes.toscrape.com/) website and it worked perfectly. But, when I tried to use with Airbnb home page nothing worked.

- I tried other websites, some worked some didn’t.
- I tried putting a delay in the code using the Python time module, but it didn’t work.
- I tried slowly walking through the code step by step. This was very challenging because scrapy uses declarative programming instead of imperative programming. So, I switch to an imperative programming package called Beautiful Soup (Http Parser)

**Beautiful Soup with Request module**: I learned about beautiful soup and practiced with [https://quotes.toscrape.com/](https://quotes.toscrape.com/).

Then, I tried scraping the Airbnb home page and slowly walked through the code. I figured out what the problem was.

The problem was how the Airbnb website is implemented vs how [https://quotes.toscrape.com/](https://quotes.toscrape.com/) is implemented. The [https://quotes.toscrape.com/](https://quotes.toscrape.com/) website returns an HTML document with all the elements already displayed. The Airbnb website uses a front-end framework (react) to create the page. This means there is a delay between when the Python request and Beautiful Soup modules try to read the website and when the content is present.

I waited for the page to load by using the time module in Python. It didn’t work. But, now I knew what the problem was. So, I started looking for another tool. I found Selenium a browser automation tool.

**Selenium:** I learned selenium and practiced with some websites.

I quickly learned how to wait for pages to load before interacting with them. I wrote some Python code to get the navigation titles and icons of the Airbnb website. It worked.

Finally, I could read some stuff. Nice. Then, I designed my plan to scrap the data from the homepage.

1. Read the title of the page.
2. Identify the CSS class names you need to read the navigation.
3. Get one navigation title and icon.
4. Get all navigation titles and icons.
5. Choose properties you want to get from the listings like name, image, location, price, etc
6. identify the CSS class names you need to query the listings.
7. Get the complete details of a single listing.
8. Get all the details of the listings on the page.
9. Figure out how to click on a component in selenium.
10. Loop through the navigations and click on one to make sure it works.
11. Connect reading the listings to navigation. Getting all the listings of each nav category.
12. Print out all the data in the correct format ready to be uploaded to a database or exported to another file.

<aside>
💡 I created a youtube playlist of this scraping with selenium. Suppose you would like to scrape or just want to watch how I am doing it. Feel free to watch.
</aside>

[Scraping Airbnb Youtube Playlist](https://youtube.com/playlist?list=PLdIF6sRfbwq7A3aUIkQaSYcdonZZDSgxB)


### **\*\*\*\***Reflection and What I have learned**\*\*\*\***

This was a fun project to work on. I loved it. Things I have learned along the way.

- It is important to find the right tool for the job.
- It is important to be flexible and willing to learn things you didn’t know before.
- There is always more than one answer to a question.
- If you keep going, you will figure out even if it is my complete accident.
