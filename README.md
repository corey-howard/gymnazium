# Fourth Milestone Project - Gone Fishing

![device-mockup](media/gone-fishing-mockup.jpg)

Welcome to Gone Fishing, a site to fulfill all the relevant needs for people who enjoy fishing. This site is for all degrees of
fishing experience whether complete novice or expert, there are items to purchase for all levels of experience. A place to shop for
all range of fishing supplies, whether it be for Carp, match/coarse, night fishing, etc. the shop caters for all. Gone Fishing, has also
been created to be the hub for all things fishing within the sporting industry, a one stop destination for anglers. This has been
achieved by incorporating different purposes to the site, as well as a shop, it is a place to keep up to date with current events within
the fishing sporting world, to comment and engage with other members of the site, to share experiences and advice with one another. Alongside
all this, anglers visiting the site can also look up places to fish. They can do this by viewing the wide selection of fisheries in the UK 
stored within the locations section of the site, each fishery has a description of the location including; breeds of fish there, price list,
night fishing permitted or not, amenities and much more.

I decided to create this site because of my fond interest in angling and what the sport can do for people's wellbeing. Fishing is a sport
that is primarily carried out as an individual but it doesn't stop you from going with friends and family together. It is a fantastic
opportunity to meeet up with friends, converse and talk about what's going on in your life whilst enjoying the great outdoors. I wanted this
site to be more than a shop, and to reflect other aspects of the sport, which is where the events (what's happening in the fishing world) and
locations sections came in. The aim would be to eventually have this site be the hub for all things angling and the got to place to shop,
locate and connect.

## Table of Contents

1. [UXD - User Experience Design](#1.-uxd---user-experience-design)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
    * [Scope Plane](#scope-plane)
    * [Structure Plane](#structure-plane)
    * [Skeleton Plane](#skeleton-plane)
    * [Wireframes](#wireframes)
    * [Surface Plane](#surface-plane)

2. [Features](#2.-features)
    * [Existing Features](#existing-features)
    * [Features left to implement](#features-left-to-implement)

3. [Technologies Used](#3.-technologies-used)

4. [Testing](#4.-testing)

5. [Deployment](#5.-deployment)
    * [How to run this project locally](#how-to-run-this-project-locally)

6. [Credits](#6.-credits)
    * [Content](#content)
    * [Media](#media)
    * [Code](#media)
    * [Acknowledgements](#acknowledgements)

## 1. UXD - User Experience Design

---

### Strategy

---

The purpose of this site is primarily a fully functioning ecommerce store that sells fishing gear and supplies. Users will be able to
find products via browsing through clearly defined categories, alternatively can use the search bar to search for key words of the product
they are looking for. Users can add products to the basket which will have a running price total for the user to see whilst they continue
to browse the site, once in the checkout page the user will be able to delete or ammend quantities of products in the bag. The user can then
pay for their products via a secure Stripe payment service, by filling in delivery address and contact information along with payment details.
The user will have the option to save their information for next time they make a purchase and the fields will be prefilled next time, this
can only be done if the user has signed up and made an account already, alternatively they can be directed to the sign up page mid checkout.
Once the user has successfully completed the checkout process, an email will be automatically sent to the customer that details their order.
Users who have signed up for an account can not only save their details for future purchases but also can view their profile, where their
previous purchase history can be viewed. The site should be easy to navigate and clear to the user where to go, with a chain of events for
more complicated functions such as purchasing products there should be prompts and clear indications as to where to go next.

Away from the ecommerce side of the site, the secondary purpose of the site is to provide information for anglers such as current events.
Users will be able to navigate to the events section and read articles relevant to the sport. Going forward a comments section will be
available so users can comment and converse with other members of the site. There is also a contact page for users to get in touch with the
site owner and send a message/feedback/ask a question. The sent messages are sent to the site owner who will be notified of a message via
email which prompts the owner to view the message in the site admin. The site should be appealing for anglers, so the use of colour and
images should be relevant and appealing to the users who will predominantly be people interested in angling.

As the site owner, going forward, it would be great to turn this site into more of a platform for socialising. This could be achieved
via the comments section of posts in the events page, especially if posts are created for specific discussions, i.e Best bait to use for
catching Carp or Top locations for fishing in the South East of England and then users can comment and participate via that post. The aim
would be to make this site the go to place for all things angling, and the first site anglers think of for serving their needs. To add
further revenue, the site could incorporate some relevant advertising and perhaps with a fishing location section set up, the site could
provide a booking platform for fisheries and take commission from each booking.

#### User Stories

### Viewing Navigation

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 1 | Shopper | View a list of products | Select some to purchase |
| 2 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes |
| 3 | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products i'd like to purchase |
| 4 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much |
| 5 | Site User | Easily locate where event articles will be | Go straight to the articles |
| 6 | Site User | Easily find the Fisheries section | View fishing locations quickly |

### Registration and User Accounts

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 7 | Site User | Easily register for an account | Have a personal account and be able to view my profile |
| 8 | Site User | Easily login or logout | Access my personal account information |
| 9 | Site User | Easily recover my password if I forget it | Recover access to my account |
| 10 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| 11 | Site User | Have a personalised user profile | View my personaly order history and order confirmations, and save my payment information |

### Events and Fisheries

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 12 | Site User | Easily view event posts | Keep up to date with what is happening in the angling world |
| 13 | Site User | Be able to add comments to posts | Converse with other members of the site to share tips and advice |
| 14 | Site User | Easily view fisheries around the UK | Plan where I will go on my next fishing trip |
| 15 | Site User | See in detail what each fishery location has to offer | See what fish are there, whether night fishing available and amenities |

### Sorting and Searching

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 16 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and catergorically sorted products |
| 17 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 18 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as "Supplements" or "Trainers" |
| 19 | Shopper | Search for a product by name or description | Find a specific product I would like to purchase |
| 20 | Shopper | Easily see what i've searched for and the number of results | Quickly decide whether the product I want is available |

### Purchasing and Checkout

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 21 | Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 22 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all I items I will receive |
| 23 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| 24 | Shopper | Easily enter my payment information | Checkout quickly and with no hassles |
| 25 | Shopper | Feel my personaly and payment information is safe and secure | Confirdently provide the needed information to make a purchase |
| 26 | Shopper | View and order confirmation after checkout | Verify that I haven't made any mistakes |
| 27 | Shopper | Receive an order confirmation after checking out | Keep the confirmation of what i've purchased for my records |

### Admin and Store Management

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 28 | Site Owner | Add a product | Add new items to my store |
| 29 | Site Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| 30 | Site Owner | Delete a product | Remove items that are no longer for sale |
| 31 | Site Owner | Add events posts | Provide up to date events for the sites users |
| 32 | Site Owner | Access contact form message requests | View the message and reply to the user accordingly |

* Many of the user stories have been taken from the Code Institute full stack framework tutorial as it was also creating
an ecommerce site.

---

### Scope Plane

---

#### Functional Specifications

* The functional specifications will mostly follow the information set out in the user stories.

#### Content Requirements

* The user will be immediately faced with a simplistic site, with clear navigational buttons to go to where the want.
* There will be easy to follow navigation with categories and search bar to find products.
* The Background will be fitting for the sites purpose.
* The colour scheme and font choices used throughout the site will be complimentary of each other and display clearly for users
on all devices. The aim is not to be flambouyant in this case, the purpose is to provide clear and concise content for the user
and maintain consistent at all times.
* The site will consist of everything set out in the user stories minus the ability for users to make comments on events posts
and Fisheries section.
* Due to time constraints the fisheries section was not able to be completed, but will be added when deadlines are not a factor.
* The comments section for the events page was trickier to implement than first thought, however this will be implemented when
more time is available going forward.

---

### Structure Plane

---

The site has been structured with the user in mind from the offset. To achieve this, Bootstrap was used as I think it
provides very straight-forward styling that is easily achieved. I will explain in more detail the structure of each component that
makes up the site in the following Skeleton Plane section, as I believe it links better with how the information is represented
via the wireframes. However, the basic structure logistically can be described in the following priorities:

1. The first page that is presented to the user is the Home page, which contains main hero image and navigation bar to the rest of the sites
pages.
2. The first page should be designed in such a way that makes it clear what it is straightaway, in this instance a relatable image to angling.
3. The logo and navigation bar will be present at the very top of the page horizontally, logo offset to the left, with search bar top middle,
the shopping basket and profile page icons will be present top left of the screen and navigation buttons central to page below logo and search
bar. On smaller devices, the nav bar will be changed to burger style navigation menu, and be present top left of page. The search bar will
reduce down to a search icon to be clicked and then the search bar will appear. The search, profile and shopping basket icons will now appear
at the top of the page central on mobile devices.
4. The navigation menu priority order is important, which is why it will be ordered by importance and relevance.
5. On top of the home page background image will be a 'Shop Now' button which is a clear indication that the site is primarily an ecommerce
store and will take the user to the products page. However above the button is the sites slogan of Shop Locate Connect, which shows the other
purposes of the site, which in this case are part of future developments currently.
6. All products navigation button provides a drop down to direct users to a page that displays all the sites products in an order requeted
by the user.
7. The navigation buttons Carp, Coarse & Match and Equipment, all provide drop down sub pages that link to the different categories of
products asociated with that page.
8. The Events navigation button will direct users to the Events page which displays articles of news events and competitions around the UK
focused solely on aspects of fishing only.
9. The Contact navigation button takes the user to the Contact page where they can get in touch with the business and send a message/question.
It also displays the location via Google Maps for them to get in contact directly and links to social media pages that are yet to be created.
10. My Account section will provide users with either the option to log in or register for an account on the site, once logged in, the My
Account button will change to different options, depending if superuser is logged in will display product management option, alternatively,
normal account holders will have the options of viewing their profile or logging out.
12. The shopping basket icon, will hold any products that the user chooses to add to their basket, whilst constantly providing a total price.

The diagram below shows how the pages of the site link with one another and what pages you can get to and from depending on the page you are
focusing on. Chart made using [Lucid Charts](https://www.lucidchart.com/pages/).

![Navigation Flow Chart](media/ms4_flow_chart.jpg)

---

### Skeleton Plane

---

I used Wireframes when designing how the information will be represented and how the user will be able to navigate across the site.
Once the wireframes were created, I had a clear drirection on where to begin creating the site and what pages should be created thereafter.
The wireframes for this site can be found here:


The site requires a database to hold much of it's data such as the product information/images, event articles, etc, the database used is the
Postgres relational database with a data model. However, due to this project being deployed using Heroku, I was able to use SQLite during
development and Heroku Postgres when deployed. All the data is contained within the Postgres database and the appropriate models have been 
created.

The below diagram explains the structure of my database and how it conforms:



#### Wireframes

Prior to starting this project I created Wireframes using an extension on Microsoft Powerpoint. Wireframes helped to plan and visualise how
the site would look before writing any code and also was a way to plan out how the apps and pages within the site will link to each other.
This saved a lot of time as it was quicker to plan and make changes to wireframe designs than experimenting whilst coding. Although my project
idea changed halfway through from a gym site to Fishing site, the wireframes were practically the same apart from the additional models Away
from the ecommerce part of the site so my wireframes were changed to reflect this. You can find the pdf file to my Wireframes in the
Wireframes folder of this repository.

---

### Surface Plane

---

I've stated previously that I decided to use Bootstrap for styling this site along with utilising many of the options it had to offer,
also of course cusomised css styling was used too. When deciding on Typography I wanted a font and font weight that was clear and legible
throughout the site and did not clash with backgrounds and colours used. It was also important that the same font was used consistently
throughout the site as to conform with industry standards. I researched other angling sites similar to my project and made note of fonts
that they used, in the end I settled on using a font from Google fonts, [Roboto](https://fonts.google.com/specimen/Roboto?selection.family=Roboto).

Where the background is concerned, on the home page I decided I wanted an eye catching background image that would span the whole page minus
the header section. I searched Shutterstock for idylic fishing sites that also displayed fishing being carried out at the same time, by doing
this, hopefully acts as a prompt for users to want to go fishing/purchase the supplies they need to go fishing. Throughout the rest of the site
I decided a white background more than sufficed what was needed and fir the purpose of the site. As predominantly the site is for ecommerce,
the white background makes the products stand out on the page. The same can be said for other parts of the site such as the events page, the
articles all have an image element and they stand out very nicely on a white background.

Due to the background being predominantly white it helped decide on colour schemes throughout the rest of the site as most colours won't
clash with White so much. I wanted to use colours that would appeal to the target audience, so anglers, and what better colour than the colour
they are mostly familiar with, dark Green. Most fishing products on the market such as bags, chairs, bivvys, umbrellas, etc. tend to be Green
of some sort. The reason for this is to match in with the surroundings. I got further information for colours from a website called
[Colours Wall](https://colorswall.com/palette/114299/), where I searched for colour palettes that were inspired by fishing, I came across one
named Fly Fishing Dry Colour, which had a perfect Green #6a7225 that I chose to use throughout the site. I decided to use this colour
specifically for elements such as buttons, banners, and icons. Font colour I decided to go for clarity so Black #000 has been used throughout
the site. It believe it is the ideal font colour for this site due to the contrasting white background.

![Fishing Colour Palette](media/fishing-colour.png)

The site has many images and have been referenced in the credits section of this document as to where they were obtained from. The product
images were predominantly obtained from [Angling Direct](https://www.anglingdirect.co.uk/) and the events section images were obtained
from multiple sources. All the images on this site have been chosen to fit their purpose as best as possible and relate to what they're
paired with. I have also used [font awesome](https://fontawesome.com/) icons throughout the site, these can be seen in the header as
navigation aids and in the contact app linking to social media pages. Font Awesome icons provide great visual aids that help users understand
what they are being directed to without having to use words on some occassions.

## 2. Features

---

### Existing Features

---

The site is made using Django framework which makes it easier to add and build upon the site, this is due to being able to create additional
apps when there is a need to add additonal features to the site. The apps are linked together using Python language and models are created
to perform functions.

### Base

I created a templates folder which houses the base.html, this contains all the content that will be displayed on each page of the site.
This way I can use jinja templating language for all the other pages to inherit the code from base.html, then I only need to concentrate
on the code/content specific to that page. The base.html template declares that it's a html document and houses the head element that contains
all the link tags for the site. The body element is also stored in base.html which contains the background image, the navbar/logo, mobile
navbar and logo, the main element where content from other pages will be displayed and finally the script tags.

The logo is purely the name of the site and acts as a link to return back to the home page, with styling emphasis on the font, the word 'Gone'
being italicised to represent movement as in going fishing. The logo sits top left of the site, but is hidden on smaller devices as there is
no room. The shopping bag and account icons sit top right of the site and is ever present, continuously providing a running total of the
customers order. In between both of these, centre of the site is the search bar, users can type in keywords to search for products for sale.
Below all this is the navbar which spans horizontally across the site, the navigation buttons have been ordered in relevance/most commonly 
used from left to right. The navbar will collapse into a burger style navigation menu on smaller screen sizes. The last feature of the header
is the free delivery threshold message permanently displayed, this is to provide constant reminder of how much customers need to spend to
receive free delivery, so is a prompt for customers to potentially spend more. All the features explained in this section are displayed on 
each page of the site, all pages are extensions from base.html

#### Home

Below the header on the home page is the background image that spans the rest of the page. On top of the image is a navigational button
'Shop Now' which directs customers to the products page. The slogan for the site is also displayed on top of the background image and has
been styled to fade into view when the page loads, this is to highlight the three main functions of the site, to be able to shop, locate
fisheries and connect via the events page, as mentioned previously, some of those functions are due in future developments.

#### Log In

The Log In page, quite self-explanatory, is the page where users who have already registered can log in using their credentials. This is
comprised of a bootstrap form including two fields, one for username and one for password. The form uses pythons flask to check the users
log in credentials match to those that are stored in the Postgres database. There are two buttons below the form, one to log the user in, if
pressed and log in was successful, will redirect the user to the home page, if unsuccessful will return back to the log in page. The other 
button is to return the user back to the home without wanting to login. There are also links that users can follow to register for an account
if they have not already signed up already, and also a link to reset the users password if they have forgotten it. The forget password
function works and users are actually able to successfully reset their password.

#### Register

The Register page is where users who have not already made an account on the site can do so. The page is made up of a bootstrap form where
users are required to fill in their email, pick a username and password. Once they submit this form, an email is sent to them asking them to
verify their email address, once this is verified, the users are able to return to the site and access their profile. The code for the
submission form also checks if usernames and email addresses are already in use and issues a prompt to the user that this is the case.

#### Profile

The profile page is a a really useful tool for the users who hold an account on the site. Here you can see your saved delivery information,
which can also be changed here, so when the user makes future purchases the delivery details field will be pre filled with the users
information. Also, on the profile page users can view their purchase history. Everytime a user completes a transaction on the site, their 
order summary will be visible in the purchase history section. More details can be obtained from the order history by clicking on the
unique order number, this will open a new page which displays the transaction in more depth, then there are navigation buttons to return
back to the profile or to the sites home page.

#### Product Management - Superuser access only

If logged in to the site and have admin access authorised then in the My Account section there is also a Product Management page, quite
simply, users who are able to see this page is because they have admin authorisation. Which means they have access to add additional products
to the ecommerce section of the site. On this the user is presented with a form where they can choose what category they want to add the
new product to, then the details for the product can be inputted such as SKU code, price, description, image, etc. Once the form is submitted
the new product is automatically added into it's designated category ready to view on the site.

### All products

The All Products section allows users to view all the products in the ecommerce store but can also be sorted via different means such as,
price low to high, A-Z, rating, etc. Whatever option is chosen will take the user to the All products page, ordered by what the user chose.
One the user is on the all products page, there is a drop down menu available at the top right hand side of the page, where the user can 
change the order preference. There is also a button visible at all times at the bottom left of the page which will return the user to the top
of the page once clicked.

### Product Pages

Similar to the All products page, the site also categorises the ecommerce products. Firstly the products are categorised by type of fishing
style and also products that don't fit into a style, so on the navigation bar this is what will be shown. The navigation bar has the options
to shop products by Carp fishing, Coarse & Match fishing and lastly by Equipment that can be for all types of fishing styles. Each of these
navigation buttons open up sub categories so users cna shop for fishing rods specifically for Carp fishing for example. The site is structured
in this way due to believing this is how a customer would want to shop and also from researching other fishing ecommerce sites. When viewing
the products pages the user can see an image, description, price, rating and what category the product is in. If the user is logged in and has
admin priviledges then the option to edit and delete the products are visible to super users only. The Edit button will take the user to the
edit product page where they can change all aspects of the product and even delete the product all together, which also deletes it from the
database. When the user clicks on a product the user is taken to the product detail page which provides a more in depth description of the 
product and the ability to add the product to the shopping bag along with choosing the quantity to add. This brings together all of the CRUD
functionalities for the site, where we have covered the ability to create products in the product management page and django admin, the 
availability to read and see the products, and lastly the ability to update and delete the products via the products pages.

### Events

The events page is essentially a blog app, where the site owner can create posts in the django admin for the site users to read. The page is 
structured using bootstrap card elements, which includes an image and a preview to the post anlong with the post heading and the author/created
on date. All the information/data is gathered from the database using jinja, and can be pulled and displayed where appropriately needed to form
the event posts. The main events page holds multiple card elements that depict each event posts, there is a button at the bottom of each post,
'Read more' which when the user clicks on takes them to the events detail page. This page focuses on the selected post and displays the full
article. At the bottom of the page there is a navigation button which will take the user back to the main events page. Only users with django
superadmin credentials are able to create blogs within the django admin, here they are also able to edit existing event posts and even delete.

### Contact

The Contact app is a page where users can get in touch with the site/company owners in relation to any query they have and also get in touch
via the company social media outlets, users can also locate where they can get in touch with the site owner via the google map feature. The 
page is set out using a bootstrap form for the contact enquiry where all the fields link directly to the django admin. The user must fill in
all fields in the form including, their name, email address, phone number and their message. Once the form is filled and submitted then the
user is presented with a success toast message informing them their message was sent successfully and someone will respond shortly. In the
backend, what happens is an email is sent to the site owner informing them that a message has been sent/from who and to view the message
in the django admin. The message can be viewed in the Contact app in the django admin and the site owner can then respond to them via one
of the details provided by the user that sent the message. Note: The social links are currently only set up to take the user to the
coresponding social media outlet, as currently there are no social media pages set up for this company.

---

### Features left to implement

---

As mentioned previously in this document, there are a few features left to implement on this project. The Events app would ideally expand to
become more of a place to chat between users, so a comments feature would be an addiitonal feature, where users can comment on the articles
posted and converse with other users. There would also be generic posts such as 'Tips for Carp fishing' for example where users who wanted
to contribute to that section can/users who want to get tips about that subject know to look there.

Another feature that is planned to be introduced in the future is a Fisheries app, this would feature many fishing locations across the UK
and provide in depth descriptions of each location. It will go into depth in relation to what fish are available, whether night fishing is
permitted, on site facilities/amenities, parking and of course price list. This could also be an oppurtunity for the site to create additional
revenue by building relationships with the UK fisheries and perhaps sell tickets through the site and take commission.

These additional features would help create the culture for what the site aims to be, the central hub for all things angling. The aim would
be for Gone Fishing to be the first place anglers would think to visit for all their angling needs and plan there whole trip/restock through
the site.

## 3. Technologies Used

### Languages

* HTML 5: 
    * Used to create the main content of the website

* CSS 3: 
    * Used to create custom styles for the website

* JavaScript: 
    * To use JQuery

* Python:
    * To import and use Django and various functions, including jinja templating and implementing CRUD funtionality

### Libraries and Frameworks

* Bootstrap v4.4.1: 
    * Used for CSS shortcuts such as; Navbar, Cards, Forms and styling, etc.

* JQuery:
    * JQuery used for javascript functions as it is simple to use and reduces the amount of code needed. 
    Used for the mobile sidenav, collapsable sections and the floating action button.

* MYSQLite:
    * Used as a development database.

* Postgres:
    * Database used for deployed version of the site.

* AWS:
    * Amazon Web Services to hold and store all the media used for the site

* Google Fonts: 
    * Used to change from default Fonts.

* Font Awesome:
    * USed to create icons as visual aid to users.

### Tools

* Stripe:
    * Payment processing software implemented to take payments for the ecommerce store.

* GitHub:
    * For hosting the website, version control of this repository using Git and source code management.

* GitPod:
    * Used as a platform environment for creating the code for the website.

* Heroku:
    * Used to deploy the website

* Favicon
    * Used to create the favicon for the website.

* Google Images:
    * For sourcing background image for website.

## 4. Testing

### User Stories

Throughout creating this project I made sure I referred to the user stories created for this site to ensure they were complied with. Testing
of this site involved a mixture of making sure the user stories were able to be acomplished and many other factors such as constantly checking
responsiveness and checking written code for errors and compliance. To start with, I have tested the site by attempting to achieve the user
stories and the results can be seen below. As reference, I have named each test in relation to the User story ID displayed in the table
displayed earlier in this document under [User Stories](#user-stories).

* User ID 1:
    * *Checked all products pages and filtering features, all work and display well. Products can be successfully added to shopping bag to
    be purchased.*
* User ID 2:
    * *Went onto all the stores products detail pages and all display correct informtaion to the user.*
* User ID 3:
    * *Trialled adding products to shopping bag and navigated through all othe rpages on site, the bag total was always on display for the user
    throughout the site.*
* User ID 4:
    * *On the home page as a user I can easily identify where the Events page is via the navigation bar.*
* User ID 5:
    * *This user story can not be achieved as it is part of future developments as stated.*
* User ID 6:
    * *Registered for an acoount, was sent an email to verify that the email address belonged to me, followed the link in the email and it
    successfully directed me to the Gone Fishing home page as expected. When logged in to site, was able to access the profile page under
    My Account.*

    ![Registration Verification](media/registration-verification.jpg)

* User ID 7:
    * *Can easily log in and out and access personal account information.*
* User ID 8:
    * *Navigated to log in page and clicked on forgot password link, entered email address and submitted the form. Was sent an email with
    a link to reset the password, follwoed the link and successfully changed my password and had access again to account.*
* User ID 9:
    * *This has instead been achieved via a toast message that appears once the registration has been completed, highlighting that the user
    will receive an email to confirm registration.*
* User ID 10:
    * *After completing a transaction, viewed user profile page whilst logged in, can see order history/transactions and payment information
    has been saved to the profile for future use.*
* User ID 11:
    * *As a user I can access the event posts and keep up to date with angling news. When click on invidiual posts the user is taken to the
    events detail page showing the post in more depth and the back button successfully takes user back to the Events main page.*
* User ID 12:
    * *This user story can not be achieved as it is part of future developments as stated.*
* User ID 13:
    * *This user story can not be achieved as it is part of future developments as stated.*
* User ID 14:
    * *This user story can not be achieved as it is part of future developments as stated.*
* User ID 15:
    * *On the  All products pages I used all the filter options and they sorted the products correctly.*
* User ID 16:
    * *Went into a specific product category and used sorted the products via the options within the category sorting, all options presented
    the data in the correct format chosen.*
* User ID 17:
    * *This can be achieved in the All Products page and works successfully.*
* User ID 18:
    * *In the search bar, I searched for keywords that I knew were in the product description or name and the correct results were gathered. I
    also searched for keywords that I knew were not in any of the products description or name and was presented with "0" results found.*
* User ID 19:
    * *When searching for products using the search bar, successful search results shows the products that obtain the key word searched and
    the user can also see how many results have been gathered. The user can also purchase the product from the results gathered if they wish.*
* User ID 20:
    * *Tested selecting a product to add to the shopping bag and used the quantity +/- buttons, adding the product to the bag worked successfully.*
* User ID 21:
    * *Once I added products to the shopping bag, I clicked on the shopping bag and it successfully took me to the shopping bag page so can see
    the products added in detail.
* User ID 22:
    * *In the shopping bag I adjusted the quantity of products, either by increment or decrement by using the update function, both worked
    successfully. The remove funcion also works perfectly fine.
* User ID 23:
    * *Made a purchase as a user, inputted personal delivery details and entered the Stipe test payment number in the card number field, all
    worked successfully. I was directed the payment success page where a breakdown of the order is displayed and a toast message displays
    describing the payment was successful. Was sent a confirmation email with all the details of my order. The checkout was quick and easy
    and the button to navigate back to the homepage works successfully.*

    ![Stripe Payment Success](media/payment-success.jpg)

* User ID 24:
    * *Through the checkout process as a user I would feel that my perosnal details are secure as they can only be seen via my profile, and
    also you have the option to not save the details for next time if you decide not to. There is also no evidence to show that the card
    details appear anywhere else such as on the confirmation emails or left to see on other pages.*
* User ID 25:
    * *After checkout user is presented with the order confirmation where they can check if they've made any mistakes and can get in touch
    with the site if they have.*
* User ID 26:
    * *Confirmation email was received after successfully checking out.*
* User ID 27:
    * *Whilst logged in as a super user, navigated to the product management page, filled in all the relevant fields in the form and product
    was added successfully. Adding products in the django admin also works fine.*
* User ID 28:
    * *When in the products pages and logged in as a super user, there are 2 options available to the user, edit and delete. Clicked on the
    edit button on one of the products and tested updating some of the fields, changes saved and implemented successfully. Editing products 
    in the django admin works fine too.*
* User ID 29:
    * *When in the products pages and logged in, pressed the delete button on one of the products and the product was removed from the site
    and database successfully. Future improvements needed for this, such as a prompt to ask the user if they are sure they want to delete
    the product, as at the moment pressing the delete button deletes it without warning. Deleting products in the Django admin works fine too.*
* User ID 30:
    * *Events posts can only be added in the django admin, navigated to the events section in the admin and filled in the relevant fields
    and successfully created an event post.*
* User ID 31:
    * *Sent a message in the contact page then accessed the django admin, navigated to the contacts app and the message is displayed
    successfully here for the admin to reply how they wish.*

### Responsive Design

Throughout the creation of this project, I have tested the responsiveness at each point of adding a new feature. I mostly achieved
this by using Chrome Dev tools, once I implemented a feature I would then check how the site looked/worked on different screen sizes,
if there was an issue I would fix it there and then before moving on. You can see examples of how the site looks on different screen
sizes in the examples below:

* For screens at 1440px click [here](https://photos.google.com/photo/AF1QipOi3t-CEY2QkciIdKmN1IQZK9ynrkGnPHqolWCD)
* For screens at 1024px click [here](https://photos.google.com/photo/AF1QipO4csru0GVVOl4gN7aUp6Hm7nTJxGW9z-HFM-y6)
* For screens at 768px click [here](https://photos.google.com/photo/AF1QipMBeKsV1nPkuveggvUAdOakEi-ktx77Z1e6HgQA)
* For screens at 425px click [here](https://photos.google.com/photo/AF1QipN3GgSM_8g3y_s07AjUWHGIqFcj8R-toqxVLcQ8)
* For screens at 380px click [here](https://photos.google.com/photo/AF1QipNsghd_TXqz82HIXt3psc-MWjUUabYqLd2YzKLj)
* For screens at 320px click [here](https://photos.google.com/photo/AF1QipNekntxGgTvkfFFWXvba-7k7laMPfJPeubPwv3Y)

I also tested my sites responsiveness on a two websites such as [Am I responsive?](http://ami.responsivedesign.is/#) Which I used to create
my device mockup image also. The second site being [Responsive Design Checker](https://responsivedesignchecker.com/), which is where I 
physically checked to see how this website looked and worked on a wide variety of devices including many Apple and Samsung devices.

### Browser Compatability

I used [Browserstack](https://www.browserstack.com/) to check how compatable this site was on the major internet browsers including Chrome, 
Edge, Mozilla, Opera, Safari and Internet Explorer. The site worked perfectly fine on all these browsers and their editions, I could not 
find any faults when testing buttons, links, forms, mobile navbar, and the site appeared to run smoothly throughout all tests. 

I also used Browserstack to see how well the site worked on different desktop, mobile and tablet devices. On the vast majority of devices the site worked perfectly well, however, I did spot a strange
fault that only occured in iphones. The error is the background image does not stay fixed, so as you scroll down the page eventually the
background image disappears, you can see the bug [here](https://photos.google.com/photo/AF1QipPtwbJIR6mFdE5NEBiYmbP2hWqD6SsH0qcdt1-h).
I done some more tests to narrow down the root device/browser that might be the cause, upon further investigation, it appears that the
only devices it affects are iphones and ipads (which is quite broad), and it doesn't matter what browser, the bug appears on both Chrome
and Safari. I thought this must be all Apple products then, but when I tested on Mac devices, this bug wasn't there. As much as I don't
like having this bug present, the only way I currently know how to resolve this is by using media queries and removing the CSS background-
fixed property and then repeat the image. I have made the difficult decision not to do this, reason being, I believe there is
probably a better way to resolve it without ruining the site for all other tablets/mobiles that the site works perfectly fine on. Once
I figure out how to resolve this, then I will.

### Bug Fixes

When user added slang term and definition to the site/database, upon page reloading, the slang term had been created successfully but 
the definition was showing as 'None'. 
See code where bug was found [here](https://photos.google.com/search/_tra_/photo/AF1QipOV9v2UV1f9gGjXTTmPIrD1zi7fkJss4SQab77w)
Image of bug on live site [here](https://photos.google.com/search/_tra_/photo/AF1QipNZBpRea9erDs8FKK4yk3lDMHdfa525Yg1Td5OR)
Upon investigation, there were no errors but there was a mistake in the app.py file under the app.route declaration. Instead of 
request.form.get("slang_definition) I had written, request.form.get("slang_description"). Was difficult to spot but I discovered it eventually.

I realised last minute before submitting this project that my code was missing quite a key component. When users add a slang term, it would
only appear on the site if it began with a capital letter, due to the jinja if statement only retrieving slang terms beginning with 'A', 'B',
'C', etc. That has now been resolved. However, any slang terms added to the site starting with lowercase, is not sorted alphabetically. If
I had more time I would be able to resolve this. I have attempted to resolve this by adding to the python code within the sort() function
key=str.lower, which upon research should sort the words alphabetically regardless of the word starting with an uppercase or lowercase letter.
Unfortunately, I could not get this to work in time before submission, so is left as a bug.

### Online Validators

* To test my HTML code for errors I used the [Nu HTML Checker](https://validator.w3.org/nu/).
    * The test returned many errors, but were all for duplicate ID's which I believe is caused by the looping over by Jinja. The ID's it
    seems, are within the jinja loop, I can't think of a solution around this so will note that it is an issue here currently, but will
    continue to actively try and resolve. Perhaps changing the ID's to class rules instead.
    UPDATE 12/01/21: It looked like changing the ID's into class rules is a solution that will work, however there is currently a GitPod
    issue, where code is not updating to the local preview so I am unable to see if the changes i'm making work. As the project submission
    date for this project is 13/01/21, I don't want to run the risk of breaking this project over a bug at this moment in time.
* To test my CSS code for errors I used the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
    * The test returned no errors, but did however return many warnings, all for Materialize as it appears unknown to this validator tool.
* To test my JavaScript code for errors I used the [JS Hint](https://jshint.com/).
    * The test returned no errors or warnings.
* To test my Python code for errors I used the [PEP 8 Online validator](http://pep8online.com)
    * The test returned no errors or warnings.

## 5. Deployment

This project was developed using Gitpod, committed to Git and pushed to GitHub for hosting, and deployed by using Heroku.

### How to run this project locally

To clone this project from GitHub:

1. Follow the link which will take you to this projects [GitHub repository](https://github.com/corey-howard/chew-the-fat).
2. Under the repository name in the 'Code' action button locate the clone HTTPS.
3. Copy the clone URL for the repository which is https://github.com/corey-howard/chew-the-fat.git.
4. In your local IDE open Git Bash.
5. Change the current working directory to where you want the cloned directory to be created.
6. Type, git-clone, and paste the URL for this repository.

To download the code from GitHub:

1. Follow the link which will take you to this projects [GitHub repository](https://github.com/corey-howard/chew-the-fat).
2. Under the repository name in the 'Code' action button click on Download ZIP.
3. Choose the directory you wish to download it to.
4. Unzip the file and then it is available to use.

To deploy this project to Heroku:

These instructions are based upon using a Windows OS. Please consult your OS for python commands.
You will also need to recreate the database in MongoDB.

1. Firstly, create a requirements.txt file by using the terminal command pip freeze > requirements.txt
2. Create a Procfile by using the terminal command echo web: python app.py > Procfile
3. Git add and git commit the new requirements.txt and Procfile then git push these to GitHub
4. On the Heroku site, create a new app by pressing the 'New' button in your dashboard. Create a name for the project and select Europe.
5. On the Heroku dashboard, on the newly created app, click on 'Deploy' > 'Deployment Method' and then select GitHub.
6. Make sure the correct GitHub repository is linked to the Heroku app.
7. On the Heroku app dashboard, click on 'Settings' and then 'Reveal Config Vars'
8. Set the following config vars:

Key | Value
--- | ---
|   IP             |   0.0.0.0                                                                                                       |
|   MONGO_DB_NAME  |   cockney_rhyming_slang                                                                                         |
|   MONGO_URI      |   mongodb+srv://root:r00tUser@myfirstcluster.9mrfl.mongodb.net/cockney_rhyming_slang?retryWrites=true&w=majority|                       |
|   PORT           |   5000                                                                                                          |
|   SECRET_KEY     |   < create your own >                                                                                           |

9. On the dashboard under deploy, click on 'Deploy Branch'. Once this is completed you can open the app.

## 6. Credits

### Content

This project inlcudes some concepts from the Code Institute tutorial for the flask task manager mini project. When I was completing that
tutorial I had already looked ahead to what the requirements were for this MS3 project and made extensive notes whilst completing the
tutorial. It was also my first time using Materialize, which I grew very fond of using, due to it's ease of use and sleek look, which
swayed me to use instead of Bootstrap.

For the login/creating user and profile sections of this project I did require help in achieving this by refering to the tutorial video
as I could not think of another way of achieving this.

Home page h1 fade in:

https://codepen.io/shawkdsn/pen/haGzE

Cockney rhyming slang terms

https://happy2movelondon.co.uk/complete-dictionary-of-cockney-rhyming-slang/

Blog Articles used from:

https://anglingtrust.net/news/

### Media

Responsive Design Checker

https://responsivedesignchecker.com/

Browserstack to check how site works on different browsers/devices

https://www.browserstack.com/

Font Awesome Icons

https://fontawesome.com/

Font

https://fonts.google.com/specimen/Delius?selection.family=Delius

Favicon

https://favicon.io/emoji-favicons/input-latin-letters

Brick wall background

https://images.unsplash.com/22/brick-wall.JPG?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb

Device mockup image

http://ami.responsivedesign.is/#

Google Maps

https://www.google.co.uk/maps

### Research Tools/Help Guides

PEP 8 compliance

https://www.python.org/dev/peps/pep-0008/


### Acknowledgements

I would like to thank the Code Institute and their team of content Tutors, Support Tutors and Student Care Team for all their help and
support during/before this project. It is by their teaching and guidance that I am fulfilling a passion to learn web development.

Special mention to my mentor Gerald McBride, for his sage wisdom and undoubted encouragement. Thank you for your guidance throughout
this project and being available for support when I need it.

A big thank you again to Stuart Crang from Learning People, for helping me start this journey and for the useful information/
advice you share on LinkedIn.

Lastly, to my peers on Slack and LinkedIn, thank you for troubleshooting tips, coding advice and for bouncing ideas off each other.


IMAGE LINKS
https://www.muscleblitz.com/gym-background-wallpaper-8
https://www.shutterstock.com/

BLOG IMAGES
http://www.fishomania.net/gallery/nggallery/page/2
https://www.forensisgroup.com/can-an-environmental-expert-testify-on-tclp-in-a-sewage-discharge-case/
https://www.thetimes.co.uk/article/why-i-want-the-monster-fish-story-to-be-a-whopper-k67smb7pp
https://www.thetimes.co.uk/article/hugo-rifkind-reviews-mortimer-and-whitehouse-gone-fishing-the-pair-use-humour-like-chimps-use-gentle-grooming-wgdt5cxjt
https://www.payszpz.ga/products.aspx?cname=big+boilies&cid=8&xi=4&xc=20&pr=29.99
https://www.gov.uk/government/news/take-care-when-buying-your-fishing-licence-online
https://www.treehugger.com/largest-freshwater-fish-in-the-world-4869287
https://tnc.news/2020/06/29/environment-minister-to-let-municipalities-dump-raw-sewage-into-waterways-until-2040/

PRODUCT IMAGE LINKS
Manilla Boilies: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/t/sticky_baits_manilla_shelf_life_boilies.jpg
Nash Scopex Squid Boilies: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/b0feda7636da30efa34d4678755a2414/N/a/Nash_Scopex_Squid_Stabilised_Boilies_1.jpg
Freezer range boilies: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/m/a/mainline_cell_freezer_boilies.jpg
Amino Blend 365: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/c/c/cc_moore_500ml_amino_blend_365.jpg
Shimano baitrunner reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/h/shimano_baitrunner_st_rb_reel.jpg
Shimano Ultegra reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/h/shimano_ultegra_xtd_reel.jpg
Wychwood Riot reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/w/y/wychwood_riot_big_pit_reel_black_1.jpg
Daiwa Emblem reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/a/daiwa_emblem_spod_reel_1_1.jpg
Daiwa Longbow rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/D/a/Daiwa_Longbow_DF_Rods_2.jpg
Fox EOS rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/F/o/Fox_EOS_Carp_Rod_2.jpg
Shimano Tribal rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/h/Shimano_Tribal_TX-2_Carp_Rod_1.jpg
Greys aircurve rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/g/r/greys-aircurve-shrink-wrap-handle-rod.jpg
JRC defender combo: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/J/R/JRC_Defender_Combo_1.jpg
Sonik 2 Rod kit: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/o/sonik_xtractor_2_rod_carp_kits_1_1.jpg
Bowning sphere rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/B/r/Browning_Sphere_Feeder_Rod.jpg
Greys PRODIGY ROD: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/g/r/greys_prodigy_txl_specialist_feeder_rod_10ft_1.jpg
Preston Carbonactive rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/P/r/Preston_Carbonactive_Supera_Rod_4.jpg
Shakespeare Superteam rod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/h/shakespeare_superteam_float_rod_1_1_1.jpg
Daiwa Ninja reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/a/daiwa_ninja_match_reel.jpg
Shimano Super reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/h/Shimano-Super-GT-RD-Reel-1.jpg
Preston Centris Reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/P/r/Preston_Centris_NT_520_Reel.jpg
Daiwa Spare reel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/a/daiwa_tdm_4012_spare_spool.jpg
Leeda Coarse combo: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/L/e/Leeda_8ft_Tele_Coarse_Kit_1.jpg
Ron Thompson Combo: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/r/o/ron_thompson_ott_11ft_pellet_waggler_and_feeder_twin_pack_combo_hero_1.jpg
Hempseed: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/y/dynamite_baits_frenzied_hempseed_tin_700g_1.jpg
Halibut pellets: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/y/dynamite_baits_marine_halibut_pellets_1.jpg
Delkim ev bite alarm: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/e/delkim_ev-d_1.jpg
JRC Triple bite alarm: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/J/R/JRC_Radar_CX_Alarm_Set_3_1_Multi_LED_1.jpg
Nash Case Bite alarm: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/N/a/Nash-R3-Prestentation-Case.jpg
Nash bite alarm: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/n/a/nash_s3_alarm_blue_1.jpg
JRC 2man bivvy: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/J/R/JRC-Extreme-TX-1-Man-Bivvy-1_1.jpg
Nash Hide Bivvy: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/n/a/nash_titan_hide_1.jpg
Korum brolly shelter: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/k/o/korum_50inch_graphite_brolly_53.jpg
Fox bivvy: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/F/o/Fox_Retreat_2_Man_1.jpg
Advanta chair: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/a/d/advanta_endurace_low_chair_updated_jpeg_1.jpg
Trakker chair: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/T/r/Trakker-Levelite-Transformer-Chair-1.jpg
Fox chair: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/F/o/Fox_Duralight_Chair_1.jpg
Sonik chair: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/o/sonik_sk-tek_lite_armchair.jpg
Daiwa 2 piece suit: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/D/a/Daiwa-Matchwinner-Two-Piece-Suit-1.jpg
Drennan cap: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/D/r/Drennan_Aqua_Black_Cap.jpg
Preston Tshirt: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/P/r/Preston_White_T-Shirt.jpg
Sundridge Gloves: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/u/Sundridge_Hydra_Full_Finger_Super_Stretch_Khaki_Gloves.jpg
Daiwa Monofil line: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/a/daiwa_sensor_monofil_line.jpg
Daiwa sensor line: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/p/r/primary_1_8_5442.jpg
Drennan supplex line: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/r/drennan-supplex-hooklength-1.1.jpg
Maxima Chameleon line: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/m/a/maxima-cameleon.jpg
Trakker rod sleeve: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/T/r/Trakker_NXG_Rod_Sleeve_13ft_1.jpg
Saber supra rod bag: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/a/Saber_Supra_3_Rod_Sleeve_12ft_2.jpg
Fox rucksack: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/f/o/fox_specialist_compact_rucksack.jpg
Aqua rucksack: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/a/q/aqua_black_series_large_rucksack24.jpg
Wychwood Landing net: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/W/y/Wychwood-Signature-Landing-Net_4.jpg
Savage landing net: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/a/Savage_Gear_Pro_Folding_Rubber_Large_Mesh_Landing_Net_1.jpg
Guru Keepnet: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/g/u/guru_keep_net_2.5m_pc_1.jpg
Matrix keepnet: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/M/a/Matrix_Carp_Keepnet.jpg
Dinsmores rod rest: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/i/dinsmore_tele_v_rod_rest_2_x_75cm_1.jpg
Jag Buzzbar: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/J/A/JAG_2_Rod_Fixed_Buzzbars.jpg
Nash buttlock: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/5/2/5242e9b21b065_t2795-96-buttlocks-new_1.jpg
Advanta rod pod: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/a/d/advanta_discovery_rvs_3_rod_pod_new_postisions_1.jpg
Reuben scales: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/R/e/Reuben_Heaton_3000_Series_Flyweight_Mk_2_Scale_1.jpg
Fox digital scales: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/F/o/Fox-Digital-Scales-60kg-Inc-Case.jpg
Korda scales: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/k/o/korda-scales.jpg
Berkley digital scales: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/B/e/Berkley-Classic-50lb-Digital-Scales.jpg
Fox tackle box: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/f/o/fox-royale-system-loaded-box.jpg
Leeda tackle box: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/p/r/primary_1_8_2061.jpg
Fox rage box: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/f/o/fox_rage_stack_and_store_boxes_1.jpg
Spro rigged box: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/p/Spro_Freestyle_Rigged_Box_Medium_1.jpg
Trakker sleeping bag: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/t/r/trakker_big_snooze_plus_compact_sleeping_bag.jpg
Advanta sleeping bag: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/a/d/advanta_discovery_cx4_4_season_sleeping_bag_1.jpg
Sonik sleeping bag: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/S/o/Sonik_SK-TEK_Sleeping_Bag.jpg
Snugpak sleeping bag: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/n/snugpak_techlite_compact_sleeping_bag_dpm_5.jpg
Vas waders: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/V/A/VA600-70_Vass-Tex_600_Chest_Wader_available_in_Stud_or_No_2.jpg
Trakker waders: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/T/r/Trakker_N2_Chest_Waders_1.jpg
Daiwa waders: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/D/a/Daiwa-Nylon-Hip-Waders.jpg
Fox Waders: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/f/o/fox_camo_lightweight_waders_6.jpg
Boilie needle: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/R/i/RidgeMonkey_RM-Tec_Nite_Glow_Boilie_Needle_1.jpg
Jag sharpening kit: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/j/a/jag_sharpening_kit_1.jpg
Wychwood drill set: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/w/y/wychwood_firefly_needle_drill_set_6.jpg
Daiwa pliers: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/D/a/Daiwa_Prorex_Long_Nose_Pliers_Curved.jpg
Korda spinner swivel: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/k/o/korda_spinner_swivel.jpg
Korda lead: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/k/o/korda_heli_leads_4oz.jpg
Korda rig: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/K/o/Korda-Krank-Ready-Rig.jpg
Korda PVA bags: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/k/o/korda-soldz.jpg
Anchor weights: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/p/r/primary_1_8_6244.jpg
Kamsan hooks: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/K/a/Kamasan_B911_Spade_Hooks.jpg
Premier floats: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/P/r/Premier-Floats-Loaded-Clear-Waggler-Set-of-5.jpg
Nisa cage: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/N/i/Nisa-plastic-cage-feeder.jpg
Super crush ground bait: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/s/o/sonubaits_spicy_meaty_method_mix.jpg
Dynamite sweetcorn: https://www-anglingdirect-co.uk.imgeng.in/media/catalog/product/cache/e2e09cb9e3f3e81e7a4cf8dbd1821470/d/b/db_xl_plain_sweetcorn_tin_jpg.jpg


FONTS
https://fonts.google.com/

EMAIL HOSTING
https://www.ionos.co.uk/