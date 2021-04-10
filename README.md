# Fourth Milestone Project - Gone Fishing

![device-mockup](static/images/device-mockup.png)

Welcome to Gone Fishing, a site to fulfill all the relevant needs for people who enjoy fishing. This site is for all degrees of
fishing experience whether complete novice or expert, there are items to purchase for all levels of experience. A place to shop for
all range of fishing supplies, whether it be for Carp, match/coarse, night fishing, etc. the shop caters for all. Gone Fishing, has also
been created to be the hub for all things fishing within the sporting industry, a one stop destination for anglers. This has been
achieved by incorporating different purposes to the site, as well as a shop, it is a place to keep up to date with current events within
the fishing sporting world, to comment and engage with other members of the site, to share experiences and advice with one another. Alongside
all this, anglers visiting the site can also look up places to fish. They can do this by viewing the wide selection of fisheries in the UK 
stored within the locations section of the site, each fishery has a description of the location including; breeds of fish there, price list,
night fishing permitted or not, amenities and much more.

I decided to create this site 

I decided to make this site because I have always had a keen interest in Cockney Rhyming Slang and it's origins.
The language is believed to have been created for a few reasons, some of which include; market traders wanting to converse between
each other without onlookers knowing what is being said, providing a sense of community by having their own language only
locals knew, but the most common reason is known to be for criminals to communicate with each other without Police
knowing what is being said. What I find fascinating is that it is still used to this day, there are so many terms that we would all
use in our day to day conversations, not knowing that it is derived from Cockney Rhyming Slang. 

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

The purpose of this site is to create a dictionary of rhyming slang terms and their definitions, potential users may have heard 
a term that they are not familiar with and can find it on this site. Users are encouraged to make accounts and add terms/definitions 
to the site to expand on the ever-growing database. The site should be simplistic and have the information that the user is searching
for straight in front of them on the first page. There should also be minimal content to read from the start, as the user
has come to this site for a quick answer to a question and are not there to read a backstory to the site's existence.

As the site owner, going forward, it would be great to turn it into more of a platform for socialising. Perhaps adding a forum/chat
funtionality. It could become a place for users to converse about London life, share experiences and of course continue to expand on
the Cockney Rhyming Slang dictionary. These actions can be implemented along side the main focus of the website being a dictionary, to
perhaps bring in revenue by eventually advertising tourist attractions and forwarding users to ticket sales for these attractions as
an example.

#### User Stories

### Viewing Navigation

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 1 | Shopper | View a list of products | Select some to purchase |
| 2 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes |
| 3 | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products i'd like to purchase |
| 4 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much |

### Registration and User Accounts

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 5 | Site User | Easily register for an account | Have a personal account and be able to view my profile |
| 6 | Site User | Easily login or logout | Access my personal account information |
| 7 | Site User | Easily recover my password if I forget it | Recover access to my account |
| 8 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| 9 | Site User | Have a personalised user profile | View my personaly order history and order confirmations, and save my payment information |

### Sorting and Searching

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 10 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and catergorically sorted products |
| 11 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| 12 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as "Supplements" or "Trainers" |
| 13 | Shopper | Search for a product by name or description | Find a specific product I would like to purchase |
| 14 | Shopper | Easily see what i've searched for and the number of results | Quickly decide whether the product I want is available |

### Purchasing and Checkout

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 15 | Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
| 16 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all I items I will receive |
| 17 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| 18 | Shopper | Easily enter my payment information | Checkout quickly and with no hassles |
| 19 | Shopper | Feel my personaly and payment information is safe and secure | Confirdently provide the needed information to make a purchase |
| 20 | Shopper | View and order confirmation after checkout | Verify that I haven't made any mistakes |
| 21 | Shopper | Receive an order confirmation after checking out | Keep the confirmation of what i've purchased for my records |

### Admin and Store Management

| USER STORY ID | AS A/AN | I WANT TO BE ABLE TO... | SO THAT I CAN... |
|:-------------:|:-------:|:----------------------- |:---------------- |
| 22 | Store Owner | Add a product | Add new items to my store |
| 23 | Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| 24 | Store Owner | Delete a product | Remove items that are no longer for sale |
---

### Scope Plane

---

#### Functional Specifications

* The functional specifications will mostly follow the information set out in the user stories.

#### Content Requirements

* The user will be immediately faced with a simplistic site, with all the slang terms on the first page they reach.
* There will be easy to follow navigation with limited pages to choose depending on if the user is logged in or not.
* The Background will be fitting for the sites purpose and not distracting.
* The colour scheme and font choices used throughout the site will be complimentary of each other and display clearly for users
on all devices. The aim is not to be flambouyant in this case, the purpose is to provide clear and concise content for the user
and maintain consistent at all times.
* With simplicity in mind and taking into consideration all the points above, the site still needs to fill like it belongs to
it's purpose and makes sense. For example, it is a dictionary for a language originating from London, so a bright, rural theme/feel
probably wouldn't fit.
* The site will include it's main funtionality of being a dictionary search tool and, for users to be able to create accounts and
add slang terms themselves from the initial site creation. Future content could include forums, chat functionalities, advertising
or even sale of merchandise.

---

### Structure Plane

---

The site has been structured with the user in mind from the offset. Simplicity has been reiterated a lot so far but it has been
at the forefront of every idea and design aspect for this site. To achieve this, I decided to use Materialize as I think it
provides very straight-forward styling that is easily achieved. I will explain in more detail the structure of each component that
makes up the site in the following Skeleton Plane section, as I believe it links better with how the information is represented
via the wireframes. However, the basic structure logistically can be described in the following priorities:

1. The first page that is presented to the user is the Home page, which contains all the slang terms they have come to find.
2. The first page should be designed in such a way that makes it clear what it is straightaway.
3. The logo and navigation bar will be present at the very top of the page horizontally, logo central, navigation buttons to the right
with the most commonly used buttons/pages displayed left to right.
4. As the name of the site isn't inherently clear as to what the site does, the heading will be displayed directly below the top nav-wrapper.
5. An alphabet that includes href links for users to navigate to slang terms beginning with the letter they choose will be displayed
next, before the dictionary begins.
6. The dictionary will then be displayed, with all terms separated by large headers of the corresponding starting letter to the term.
The slang term will come first, followed by it's definition. Each slang term will be within a materialize collapsable which displays
more information when clicked on, such as the name of the user who created the entry and the date it was created on.
7. The next page along in the navigation will be the Log In page, for user to log in and add slang entries..
8. The next page along in the navigation will be the register page, for users who wish to add slang entries to the site, they must
register an account to do this.
9. When a user is logged in the Add Slang page will appear on the navigation bar, this is to prevent users adding slang entries without
an account.
10. The other page that is available to users is their Profile page, here will be an explanation as to what a user has access to on the
site. Also available are navagation buttons to return back to the Home page or the option to Add Slang.
11. Lastly, the Log Out button will be available at the end of the navigation bar, only for users that are logged in, to log out.

---

### Skeleton Plane

---

I used Wireframes when designing how the information will be represented and how the user will be able to navigate across the site.
Once the wireframes were created, I had a clear direction on where to begin creating the site and what pages should be created thereafter.
As the contents of the dictionary and the information of the sites user accounts are stored as data and retrieved from a database, 
I also designed how the database would work for the site. I decided to use MongoDB which is a NoSQL document-oriented database.
The database is quite simple and named cockney_rhyming_slang, it is comprised of two collections, one named words and the other users. 
All the slang entries created are stored/retrieved in the words collections and all the user account details are stored/retrieved in the 
users collection. The structuring of these collections can be viewed in the images below:

cockney_rhyming_slang.words:

![Words Collection](static/images/words-collection.png)

cockney_rhyming_slang.users:
(Password manipulated so cannot be seen)

![Users Collection](static/images/users-collection.png)

#### Wireframes

You can find the pdf file to my Wireframes in the Wireframes folder of this repository.

---

### Surface Plane

---

I've stated previously that I decided to use Materialize for styling this site along with utilising many of the options it had to
offer. When deciding on Typography I wanted to have a font that could be conceived as 'handwritten', as it is a site for words and
in a dictionary function, I thought a handwritten font would be quite apt. I used google fonts to find a suitable font that followed
the criteria I set out but was also clear to read, I eventually decided on the font [Delius](https://fonts.google.com/specimen/Delius?selection.family=Delius).

I decided on a background that would match the urban feel I was trying to achieve, so I searched for London brick wall backgrounds and
eventually found one I thought was suitable.

I tried to choose a colour scheme that would compliment the background but also so they did not clash, whilst making sure all content was
clear and visible. I ended up using materialize colour of blue-gray darken-1, Gray is neutral and tends to be quite a popular choice in
web design so it fit my criteria. I went with a traditional white font throughout the site apart from where backgrounds are white, I chose
the contrasting blue-gray. I also have multiple flash messages that appear throughout the site, I wanted these to be bold and stand out well,
so I chose the background colour of these to be yellow accent-4 with white font.

The site only has one image which is the background image, apart from that I have also used [font awesome](https://fontawesome.com/) icons
throughout the site as a visual aid for users.

## 2. Features

---

### Existing Features

---

### Base

I created a template called base.html to hold all the content that will be displayed on each page of the site. This way I can use jinja
templating language for all the other pages to inherit the code from base.html, then I only need to concentrate on the code/content
specific to that page. The base.html template declares that it's a html document and houses the head element that contains all the link 
tags for the site. The body element is also stored in base.html which contains the background image, the navbar/logo, mobile navbar and logo, 
section for flash messages to display, the main element where content from other pages will be displayed and finally the script tags.

The logo and navbar is displayed at the top of the page, the logo is centralised and acts as link back to the home page (words.html), the
navbar is displayed on the right at the top, with the navigation button is order of relevance/most commonly used from left to right. All
these features are responsive and work on different screen sizes, the navbar converts into a collapsable navbar when screen sizes become
too small to display the full navbar.

#### Home

The main feature of the home page (words.html) is that of the dictionary of slang terms. As part of the UX it was important that users
are able to obtain the information they desired from the very first page they encounter. Below the navbar the heading is displayed, this
is to clarify what the site is for, as the site name does not neccessarily give a clear indication to what the site is. Following that is
the alphabet running from A-Z, these act as links for users to quickly navigate through the dictionary, as most users will arrive at the
site knowing what slang term they're looking for, they can click on the letter it begins with and will be navigated to that point. The
slang term and their definitions are then displayed after the alphabet links, the slang terms are separated by a heading of each letter of
the alphabet, these act as the scrollspy's. The slang entries are displayed in a materialize collapsable, so the slang term and it's
definition are displayed, but when clicked on, the user who created the entry and the date it was created on are displayed. If a user is
logged in to the site and have previously created a slang entry, an edit button will appear next to the entry, this will only appear to
the user who has created the entry so other users cannot edit it. I decided against using a sticky navbar because I didn't believ it was 
neccessary for the site, this is because there is only one main feature of the site which is the dictionary itself, so as a user is scrolling
through the terms, it's not in their best interest to need to quickly navigate to another part of the site. With this being said, I did 
believe it to be neccessary to have a function that will return the user to the top of the page at any point, so I created a floating action 
button to achieve this.

#### Log In

The Log In page, quite self-explanatory, is the page where users who have already registered can log in using their credentials. This is
comprised of a materialize form including two fields, one for username and one for password. The form uses pythons flask to check the users
log in credentials match to those that are stored in the mongoDB database. There are two buttons below the form, one to log the user in, if
pressed and log in was successful, will redirect the user to the home page, if unsuccessful will return back to the log in page. The other 
button is for incase the user found themselves on the log in page without actually registering, so clicking on the register button will take
the user to the registration page.

#### Register

The Register page is basically a carbon copy of the Log In page, apart from the flask code that governs it. When a user tries to create
their username, it is checked to see if the username already exists and if so, returns the user back to the registration page to try again.
Once the user has successfully registered via clicking the register button, it directs them to their profile page.

#### Profile

The Profile page is quite simply a go to page for once the user has successfully registered, it takes them to their profile to show that
their registration was a success. There is also a brief introduction to the site and a few rules for when adding slang entries to the site.
It has quite a nice feature that displays the users name at the top of the page, this is achieved again by using jinja and targeting the
username. I have tried torepeat this throughout when addressing the user directly by using their username. Below this are two navigation 
buttons, one to take the user back to the home page, the other is the add slang button. Clicking this will take the user to the add slang page.

#### Add Slang

The Add Slang page is where users that have logged in can access, here they can add slang entries for the dictionary. It is made up of a 
simple materialize form, with two fields to be filled. One being the slang term and the other being slang definition. Both of which is linked 
to the mongoDB collection for words under their respective id's of slang_term and slang_definition. Once the user has successfully created
the slang term and it's definition, it is stored in the database and is inserted into the home page dictionary in alphabetical order, this
has been achieved by sorting the data alphabetically in the python code. The users slang entries will be clearly visible as they will have
an edit button next to them that only they can see.

#### Edit

The final page of the site is the Edit Slang page, quite simply this is where users can edit the input fields of their entries, perhaps for
if they've noticed spelling mistakes or maybe the definitipn isn't quite correct. The user can also delete their entry altogether. These
changes first and foremost are made to the database, but as the data is retieved from the database, these changes will also appear on the site.
These actions can be completed by pressing the edit slang button or delete slang button. If the user changes their mind they can press the
cancel button, all 3 buttons available to the user on this page will redirect the user to the home page, following any changes they decided
to make.

---

### Features left to implement

---

As part of the UX I mentioned that it would be good to progress this site further in future developments, by intoducing a chat functionality
between the users. This could be in the form of a forum or perhaps in the same concept of some social platform such as Facebook. This could
be a place where users are encouraged to converse on the subjects surrounding London life, tourist attractions, places to eat, places to see.
In a business sense, the site could introduce advertising for London tourist attractions, perhaps provide links to relevant sites to book
tickets. If enough users participate in using the site, a brand could be developed and merchandise could possibly be sold, so an introduction
of a site shop could be an idea.

## 3. Technologies Used

### Languages

* HTML 5: 
    * Used to create the main content of the website

* CSS 3: 
    * Used to create custom styles for the website

* JavaScript: 
    * To use JQuery

* Python:
    * To import and use Flask and various functions, including jinja templating.

### Libraries and Frameworks

* Materialize v1.0.0: 
    * Used for CSS shortcuts such as; Navbar, Cards, Forms, etc.

* JQuery:
    * JQuery used for javascript functions as it is simple to use and reduces the amount of code needed. 
    Used for the mobile sidenav, collapsable sections and the floating action button.

* Flask:
    * Used Flask as it is a useful library that has an extensive category of Python functions for use.

* Google Fonts: 
    * Used to change from default Fonts.

* Font Awesome:
    * USed to create icons as visual aid to users.

### Tools

* MongoDB:
    * Used to create database that will store the data for the site in collections created.

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

* As a user I want to be presented with a simple, enjoyable and easy to use site, that is also visually appealing.
    * *This has been achieved by having the slang terms available to the user via the very first page, there is minimal
    content to have to digest beforehand as well. The site only includes pages that are neccessary, which reduces it's
    complexity to the user, allowing them to concentrate on the pages that are relevant to them. Humour has 'attempted'
    to be injected into the site via the Flash messages, by including cockney rhyming slang into these messages. The
    colour scheme is appropriate and clear for the user to see without clash.*
* As a user I want to be able to navigate around the site with ease.
    * *This has been achieved by having a navbar at the top of the page with links to pages only relevant to the user.
    Floating action button has also been added on the home page that takes the user to the top of the page from whatever
    point they are currently at.*
* As a user I want to be able to easily find the slang term I am looking for, via a logical ordering system.
    * *This has been achieved by including an alphabet from A-Z at the top of the page, users can click on a letter
    of their choice and will be taken to said letter that slang terms begin with. The slang terms have also been ordered
    alphabetically for users to easily find the term they are looking for.*
* As a user I would like the option to add to the dictionary of slang terms.
    * *This has been achieved by including an option for users to register an account with the site, they can then log in
    and add a slang term with it's definition.*
* As a user I want to have access to the slang terms/defintions i've created and have the option to edit/remove them.
    * *This has been achieved by including an edit button next to all slang terms that the user who is logged in has created.
    By clicking on the button, the user has the option to edit and even delete the entry if they wish.*
* As a user I want to enjoy using the site enough to want to return.
    * *This has been achieved by the website being more of a service to users, if a user happens to need to know the definition
    of a slang term then they know they can return to the site. Hopefully the content, ease of use and injection of humour makes
    enough of an impact for the users to want to return.*

### Responsive Design

Throughout the creation of this project, I have tested the responsiveness at each point of adding a new feature. I mostly achieved
this by using Chrome Dev tools, once I implemented a feature I would then check how the site looked/worked on different screen sizes,
if there was an issue I would fix it there and then before moving on. You can see examples of how the site looks on different screen
sizes in the examples below:

* For screens at 1440px click [here](https://photos.google.com/photo/AF1QipPYgeLtRtc-9oKcB0p9jpgbHRFge00axsWqeXWJ)
* For screens at 1024px click [here](https://photos.google.com/photo/AF1QipPJIN5TR4jRCFKNkj5Xa_ki-V1P7GATUxvejIv4)
* For screens at 768px click [here](https://photos.google.com/photo/AF1QipM3rzP18WSJpOhiYL6PHmsy29D8wc9O9hK1eIEC)
* For screens at 425px click [here](https://photos.google.com/photo/AF1QipMBpLN754EPerH3aL-QRsL29SDEzVpGajqXmDMN)
* For screens at 380px click [here](https://photos.google.com/photo/AF1QipPw0FpIhQiSGCdlrIdOpTKn-4q6Mh1NCM0_Dge0)
* For screens at 320px click [here](https://photos.google.com/photo/AF1QipOt_ui5ZoRY352q49wkhL_T9ACH3-vZmnLxOYzM)

I also tested my sites responsiveness on a two websites such as [Am I responsive?](http://ami.responsivedesign.is/#) Which I used to create
my device mockup image also. The second site being [Responsive Design Checker](https://responsivedesignchecker.com/), which is where I 
physically checked to see how this website looked and worked on a wide variety of devices including many Apple and Samsung devices.

### Browser Compatability

I used [Browserstack](https://www.browserstack.com/) to check how compatable this site was on the major internet browsers including Chrome, 
Edge, Mozilla, Opera, Safari and Internet Explorer. The site worked perfectly fine on all these browsers and their editions, I could not 
find any faults when testing button, links, forms, mobile navbar, and the site appeared to run smoothly throughout all tests. 

I also used Browserstack to see how well the site worked on
different desktop, mobile and tablet devices. On the vast majority of devices the site worked perfectly well, however, I did spot a strange
fault that only occured in iphones. The error is the background image does not stay fixed, so as you scroll down the page eventually the
background image disappears, you can see the bug [here](https://photos.google.com/photo/AF1QipPtwbJIR6mFdE5NEBiYmbP2hWqD6SsH0qcdt1-h).
I done some more tests to narrow down the root device/browser that might be the cause, upon further investigation, it appears that the
only devices it affects are iphones and ipads (which is quite broad), and it doesn't matter what browser, the bug appears on both Chrome
and Safari. I thought this must be all Apple products then, but when I tested on Mac devices, this bug wasn't there. As much as I don't
like having this bug present, the only way I currently know how to resolve this is by using media queries and removing the CSS background-
fixed property and then repeat the image. I have made the difficult decision not to do this, reason being, I believe there is
probably a better way to resolve it without ruining the site for all other tablets/mobiles that the site works perfectly fine on. Once
I figure out how to resolve this, then I will.

*__UPDATE: I managed to resolve the background image bug. This was achieved by loosely following the solution I outlined above, but Instead
of removing the background-attachment: fixed; css styling in media queries, I just changed the background-repeat styling rule to repeat. I
thought if the background image is fixed on the vast majority of devices then I don't have to worry about the image repeating as it will be
fixed, but now the image will repeat on iphones and ipads, as the background-attachment: fixed styling rule does not work on these devices.__*

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