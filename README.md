# Project Charter (v1)


## NOTICE: This project is suspended. I was doing this while I was looking for a developer job, I got the job now and focusing on learning about the team and getting onbaord.

## Project summary

I am building a clone of the [Airbnb website](https://www.airbnb.com/) for learning purposes. I believe I will learn more about developing complex websites and applications by building across the tech stack. From scrapping data from the internet, cleaning and storing data in a database, accessing it using a backend framework and serving via Restful API, to building a front-end application using a modern framework.

## Goals of project

- Build a clone of the home page of [Airbnb.com](https://www.airbnb.com/) using real data.

## Deliverables

1. Scrap all the types of house navigation, listing card information, and details of each listing.
2. Clean data and store it in an MYSQL database
3. Create a **node application** that accesses the database and serves requests via Restful API
4. Create a **react application** that consumes the node-backend that looks like the Airbnb homepage

## Scope

### In - scope

- Scrapping all data required from the home page
- Back-end reading database and serving requests via restful API
- Pagination
- Front-end sending a request to the back end and displays items

### Out-of-scope

- Cookies and Sessions
- User account creation & management, authentication, and authorizations.

## Success Criteria

- All the data needed is stored in the database and can be queried using SQL.
- Restful ends points can be called and they return appropriate responses
- Front-end applications can be visited.
  - House-type navigation is listed
  - Home page listings are displayed with all the content inside the card of the website
  - When a house type navigation is clicked only listings belonging to it are displayed
  - When you click on a listing a [detail page](https://www.airbnb.com/rooms/49328466?adults=1&category_tag=Tag%3A8225&children=0&enable_m3_private_room=false&infants=0&pets=0&search_mode=flex_destinations_search&check_in=2023-04-18&check_out=2023-04-23&federated_search_id=aa5d814f-1190-4ded-ab5d-40ccc39fbf98&source_impression_id=p3_1680548784_3Jj3BivsYpNstkEP) is navigated to that shows the listing details.

---

![Work break down structure](/images/WBS1.png "Work break down structure image")

### Phase one complete

The reflection and the code for this page are in the "scraping phase" folder.
