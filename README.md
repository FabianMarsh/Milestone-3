# Character Forge
 
Character Forge is a Dungeons and Dragons Fifth Edition character creator, it is designed to make the character creation process simpler and easier. 
On top of this Character Forge allows users to share character ideas and concepts.
 
## UX
 
### Project Goals
 
Character Forge is designed to make the character creation process of Dungeons and Dragons Fifth Edition character simpler, quicker and more accessible. On top of this many players of the popular tabletop RPG 
struggle with ideas for characters, so to quash this issue shared by the community Character Forge also has a Character Gallery feature which enables users to share and spread their ideas. The end goal being to have 
more creative and interesting characters for all to enjoy.
 
### User Goals
 
The target audience for Character Forge are player's of tabletop role playing games new and old. Character Forge is designed to be easy to use and accessible.
 
* Clear landing page explaining what the website is.
* Way to access Character Gallery to seamless viewing of other users' characters.
* Step by step character creation.
* Input important data for the user.
* Have a clear editable character sheet to simulate a physical character sheet for when they would play.
 
Character Forge Solves these issues by:
 
* The landing page is simply welcoming the user to the site, giving instructions of how to use the site.
* The Character Gallery feature is accessible to all users not just members of the site. Allowing users that are just passing by to also be inspired. On top of this all characters are displayed in cards displaying the important information first, and after expanding shows more in depth information.
* The character creation process is split into tabs, helping the user make one important decision at a time, classes, backgrounds and races are divided into collapsibles allowing the user to display tidbits of information at a time rather than being overwhelmed. The process is made easier by guiding the user to the next tab or step in the process one by one.
* Once the character creation process is complete Character Forge does all the heavy lifting for the user. This includes calculating their armor class and passive perception for them, which is a confusion many new players to the medium have. 
* The site also outputs the data in the form of a digital character sheet. This is to simulate that of a physical character sheet to aid the player if they were to copy the information over to a paper copy. On top getting them used to where the information is typically stored.
 
### Developer and Business Goals
 
* Outdo the competition by making standard content more accessible to users.
* Having an easier to use user interface.
* Allow for sharing of character concepts.
* Offering the standard presentation of character information.
 
Character Forge achieves these by:
 
* Making all content available within the player's handbook accessible, rather than locking most content behind a paywall. Which can be frustrating to new player's as they lack the knowledge to substitute in any content they wish to include in their character.
* Character Forge is very simple in how it needs to be used. To access the character creation the only requirement is that a user be logged into the website. After this the character creation walks them through the creation process, keeping aspects simple and concise so the user knows what they're doing. This is achieved by the tabs it lets the user know what choice they are making and when.
* Other character creation websites lack a shared community feature most only allow for comments on various classes and races, but Character Forge will allow them to share their wonderful creations with each other within the software itself rather than creating in one website and then taking it over to another. This keeps the process simpler for users.
* Character Forge presents information once characters are created in the Wizards of the Coast Fifth Edition standard by outputting the detailed version of the character information into a digital character sheet rather than the websites own mockup of the character sheet which places information in different areas, this can confuse a player, especially those that are new to the game.
 
### User Stories 
 
* As a new player, I want to create my first character, but I am not confident enough to do it on my own. Coming to the home page I see this website tells me to login and I can get created, after logging in I can see the New Character tab has appeared. Clicking on it I see the steps I am going to take, the process is easy to take and areas that aren't intuitive have prompts and placeholders to guide me through the process.
* As a player with an artistic block, I navigate to the character gallery. I look over other creators' characters and after some time have inspiration to make a new character. I noticed I could make a character on the site, as well and quickly made Marithoss. One complaint is that there is nowhere to upload an image of what my character would look like.
* As an experienced player, I have become frustrated with the limited options of other character creators and decided to give this one a chance. Took a moment to get signed up but was delighted to see the amount of options for creating a character, as other creators lock most options behind a paywall. After making a handful of characters I am very happy with how quick and easy it is to make characters. And how the character sheet is calculated and generated for you.
* As an admin user, I want like to ensure all fields are being input into the database, going to the new character tab, everything seems to be in order until I get to the submit tab and notice the wisdom modifier isn't what it should be showing a +1 instead of a +3, other than this everything is pushing to the database as it should.
 
### Design Choices
 
Throughout the development process many design choices came and went and this section goes into detail of the final product.
 
* __Colour Palette:__ The palette is a combination of reds, oranges and yellows this to emphasize the forge aspect of Character Forge. The blazing orange iron gets when it is being worked on and the fires of a forge are why these colours were chosen. To really send it home that the user is creating something great with this website.
* __Type Face:__ The typeface chosen to represent dwarven runes, "Cinzel '' from __Google Fonts__ gives this effect, the reason behind choosing dwarven runes is because within fantasy lore dwarves are always excellent craftsmen. The other bespoke typeface chosen is "Courgette '' this is used on top the character card panels to give the effect of a sophisticated engraving, one that you would find on a fine blade. Giving the image of another piece of art is finished.
* __Background Image:__ When the website first loads a great forge is presented to the user, this is the great Character Forge, the forge the user will use to create their very own character. It represents the amount of great works that were made here and the many more that they will create alongside other player's to be shared within the Character Gallery.
* __Character Gallery:__ The Character Gallery is kept simple being more for practicality than design, again this is an aspect of dwarven architecture. The cards are left simple as it is assumed some users will spend a lot of time here, making the design too eyecatching can overwhelm or tire out a user after a time. Before the card is expanded It shows only the eye catching information, this being the character name, character description and who created the character. These details can stop a scrolling user as certain aspects interest them.
* __Character Creation:__ The creation process is split into six types to not overwhelm the user with the amount of choices they're going to be making. Creating a character isn't easy but that doesn't mean the tools can't be simple. As the user is guided through the first few types the colour of the collapsibles goes from a bright orange slowly progressing to a deep red. This shows the forge becoming hotter as they delve deeper into their creation and closer to the final product. The "Character Details'' tab is left to be a simple form, as this information can be represented with dropdowns and text inputs quite easily. After this is the "Ability Scores' ' tab these allow the user to input a stat between 3 and 30 this is because by the rules of dnd a character cannot have a stat lower than 3 or higher than 30, so there is this limitation. Below this is the stat modifier table. New players tend to have a hard time figuring out their modifiers, though Character Forge calculates this for the user, it's good for the user to understand why there 20 is a +5. Finally is the "Submit" tab that collects the information the user has stored in cookies and ensures the user is sure they want to finalise their creation.
* __Character Edit:__ This page recreates the character sheet from the player's handbook, this for older player's is a format that is familiar to them. Whereas, for newer players it helps them get used to the format most d&d groups will be using.
 
### Wireframes
 
* [Home](wireframes/home.pdf)
* [Character Gallery](wireframes/character_gallery.pdf)
* [Login/Register](wireframes/login_register.pdf)
* [New Character Class/Race/Background](wireframes/class_race_background.pdf)
* [New Character Ability Scores](wireframes/ability_scores.pdf)
* [New Character Submit](wireframes/submit.pdf)
* [Profile](wireframes/profile.pdf)
* [Edit Character](wireframes/view_edit.pdf)
 
## Features 
 
All features within Character Forge are made to be simple and easy to use. To do all of the heavy lifting so that the user doesn't have to. 
 
### Existing Features
 
* __Navbar:__ Allows the user to access other pages contained within the website.
* __Mobile Sidenav:__ Allows users on mobile and tablet devices to access the navbar without taking up screen space.
* __Character Gallery:__ Allows users to view other users characters that have been created in a simplified format.
* __More Details:__ The purpose of the more details dropdown is to keep the initial card concise, and then if a viewer is interested they can expand and learn more about the character.
* __Login:__ Allows users to login into their account, accessing their profile and the new character tab. Also has a link to the register page if a user doesn't already have an account.
* __Register:__ Allows a new user to create an account if they don't already have one, links to the login page if they already have an account.
* __User Profile:__ Similar to the character gallery with a handful of differences notably only characters the user has created appear here, and when more details is pressed there is an edit and delete button only accessible through the profile tab and only on the characters that user has created.
* __Delete Character:__ Pressing this button opens a model to ask the user if they are sure they want to delete the current character in a fashion fitting fantasy setting.
* __Edit Button:__ Pressing this button opens the edit/detailed view screen of the selected character.
* __Edit Character:__ On this screen the user can view a detailed character sheet of all the information of their character, on top of this they can edit any aspect of the character sheet and have it pushed to the database, updating any change made by the user.
* __New Character:__ Allows users to create a new character.
* __Creation Tabs:__ Allows access to all aspects of the new character page. The active tab depends on which stage of the creation process the user is on, going onto the next tab as one is completed. 
* __Class Collapsible:__ Shows all available classes for a user to select in a collapsible for easier viewing. When a class has been selected the selected class is displayed at the top to confirm to the user their selection.
* __Race Collapsible:__ Shows all available races for a user to select in a collapsible for easier viewing. When a race has been selected the selected race is displayed at the top to confirm to the user their selection.
* __Background Collapsible:__ Shows all available backgrounds for a user to select in a collapsible for easier viewing. When a background has been selected the selected background is displayed at the top to confirm to the user their selection.
* __Character Details:__ A standard form to fill in various roleplay elements about the character. On top of this some form elements are not available until the first three tabs have been completed. Once they have been the language, skill and tool proficiency and instruments selectors.
* __Language Select:__ Accesses the amount of languages the race and background combined allow the user to pick and generates a select element with the available languages to the character. Above informs the user what languages they have from the selected race.
* __Skill Select:__ Accesses the skills that the selected class has access to, as well as how many the class is allowed to pick and generates a select element for each.
* __Tool Select:__ Accesses the amount of tool proficiencies available to the class, race and background and generates a select element for each, filling the option elements with artisan's tool. Below the select lets the user know about any other tool proficiencies they may have.
* __Instrument Select:__ Accesses the amount of instruments the class and background has access to, and generates a select option the amount allowed.
* __Ability Score:__ Only allows the user to input an integer into this form. After the values have been inputted the backend only generates the modifier for the respective stat. Below the input fields is a table to explain what value equates to which modifier. 
* __Submit:__ The final step of the character creation process is to confirm what the user has selected. Other than choosing to cancel the chosen options, and to create the character. The screen shows what has been selected by the user before they choose to commit to the character.
 
### Feature to Implement
 
* __Profile Customisation:__ This feature would allow a user to change their username, add a profile picture, and a profile description. This also be editable after the initial creation of the profile.
* __Profile Viewing:__ Would allow users to see another user's profile and the characters that particular user has made.
* __Equipment Selection:__ Within the new character page after a class has been selected within the details tab there would be a select for the starting equipment of the character.
* __Class Features:__ Include the features the class receives when leveling up, and have them appear within the features tab of the detailed view/edit page.
* __Character Level Up:__ Allow automated level up by the press of a button, giving the user the options that leveling up would allow them, such as selecting a subclass.
* __Multiclass:__ Would allow the user to select an additional class when leveling up.
* __Character Search:__ This would allow users to search a class, race, background, profile name and view relevant characters.
* __Character Picture:__ Would allow for storing a character picture within the database and would be viewable as a part of the simplified character view below character name.
* __Delete Modal:__ This was originally a feature that was buggy, the feature will when the delete button is pressed will pop up a modal asking the user if they're sure. As part of defensive programming.
* __Character Ability Score Improvement:__ Certain races increase specific stats, this is currently not a feature due to time constraints.
 
## Technologies Used
 
* [HTML5](https://html.spec.whatwg.org/multipage/)
    * __HTML5__ was used to build the structural elements of the webpage.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
    * This was used to style the elements made by __HTML5__, as well as position them.
* [Python3](https://www.python.org/download/releases/3.0/)
    * Python3 was used to code the backend elements within the app.py file.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * Is a micro framework used to create app routes and to define python functions. Along with connect to __MongoDB__.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Used for __Flask's__ reliance as well as being able to code python elements within the frontend aspects of the project.
* [MongoDB](https://www.mongodb.com/)
    * Was used to stored information on character creation elements, along with store user accounts and characters
* [Pymongo](https://pypi.org/project/pymongo/)
    * Allows __Python__ to access commands to communicate between the app and __MongoDB__. And thus Allowing __Flask__ to communicate as well.
* [BSON](http://bsonspec.org/)
    * The __BSON__ Object_ID aspect was used to access specific objects stored with the __MongoDB__ database, allowing for retrieving and updating data.
* [Python3 Math](https://docs.python.org/3/library/math.html)
    *Was imported specifically to round down modifiers that were calculated. Within the get_modifier function.
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
    *The salt and hash aspects were used to keep users passwords safe and secure, using __Werkzeug's__ encryption and decryption.
* [Pip3](https://pip.pypa.io/en/stable/)
    * Was used to install requirements of __Flask__ as well as easily compile a requirements.txt for the requirements of the project.
* [Heroku](https://dashboard.heroku.com)
    * Used as a hosting platform.
* [Materialize](https://materializecss.com/)
    * An external CSS library used to create styling easily, saving time on in house styling.
* [Github](https://github.com/)
    * Used as a hosting platform for testing. Along with helping with any rollback needed to access backup files.
* [Gitpod](https://www.gitpod.io/)
    * Was used for its ready to code environment allowing the project to begin and end.
* [Google Fonts](https://fonts.google.com/)
    * Used to embed more fonts to allow for a bespoke experience.
* [Font Awesome](https://fontawesome.com/)
    * Was used for the sole purpose of displaying the trigger for the mobile sidenav. That being three horizontal bars.
* [Lucid Chart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=en_tier1_desktop_branded_x_exact&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-536921399221:kwd-55720648523&km_CPC_Country=1007106&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&mkwid=sVrXnwD0X_pcrid_442433236001_pkw_lucid%20chart_pmt_e_pdv_c_slid__pgrid_55688909257_ptaid_aud-536921399221:kwd-55720648523_&gclid=Cj0KCQiA2uH-BRCCARIsAEeef3mrcqypE42KqiTgBBEyCXBx6WTJ5kk939rZXNMyQC33lVWoaGbqk2EaAmprEALw_wcB)
    * Used to make wireframes for the planning stages of the project.
 
## Testing
 
1. Register Form:
    i. Go to the "Register" tab.
    ii. Enter Username. Ensuring details must be at least 5 Characters with a maximum of 15.
    iii. Enter Password. Ensuring details must be at least 5 Characters with a maximum of 15.
    iv. Submit details. 
    v. Brought to "Profile" tab, with flash message of "Registration Successful".
 
2. Register Form with existing user:
    i. Go to the "Register" tab.
    ii. Enter Username. Must be at least 5 Characters with a maximum of 15.
    iii. Enter Password. Must be at least 5 Characters with a maximum of 15.
    iv. Submit details. 
    v. Remain on the "Register" tab, with a flash message of "Username already exists".
 
3. Login Form:
    i. Go to the "Login" tab.
    ii. Input Username. Ensuring details must be at least 5 Characters with a maximum of 15.
    iii. Input Password. Ensuring details must be at least 5 Characters with a maximum of 15.
    iv. Submit details.
    v. Brought to "Profile" tab with flash welcome message "Welcome, {{ User }}".
 
4. Login Form, with incorrect details:
    i. Go to the "Login" tab.
    ii. Input Username. Ensuring details must be at least 5 Characters with a maximum of 15.
    iii. Input Password. Ensuring details must be at least 5 Characters with a maximum of 15.
    iv. Submit details.
    v. Remain on the "Login" page with a flash message of "Incorrect Username and/or Password".
 
5. Navbar tabs:
    i. Load the website "Home" page, navbar shows "Home", "Character Gallery", "Login" and "Register".
    ii. Go to the "Login" page and enter login details.
    iii. Redirects to the "Profile" page, navbar now shows "Home", "Character Gallery","Profile", "New Character", "Logout".
 
6. Navbar, with deleting cookies:
    i. Login to profile.
    ii. Open developer tools and delete session cookies.
    iii. Should remove login specific nav elements.
    iv. This is the case however, I remain on profile despite having no session cookie.
 
To fix this bug all tabs that require the user to be logged first check for the session user cookie, if it does not exist the user is redirected to the "Login" page.
 
7. Create Character Collapsibles:
    i. Load "New Character" tabs
    ii. Open and close "Class" tabs, ensuring they all open and close. Opening tabs should close an open one.
    iii. Open and close "Race" tabs, ensuring they all open and close. Opening tabs should close an open one.
    iv. Open and close "Background" tabs, ensuring they all open and close. Opening tabs should close an open one.
 
8. Selecting an option from the Collasibles appears at the top of that tab:
    i. Open "New Character" page 
    ii. Select Class should be forced onto the "Race" tab.
    iii. Go back to "Class" tab, see "{{ Class }} Selected" is present at top of the screen
    iv. Select race, should be forced onto the "Background" tab.
    v. Go back to "Race" tab, see "{{ race }} Selected" is present at top of the screen
    vi. Select background should be forced onto the "Details" tab.
    vii. Go back to "Background" tab, see "{{ background }} Selected" is present at top of the screen
 
9. Character Details if Statements:
    i. Load the "New Character" page, ignore the first 3 tabs and go to the "Details" tab. Should say at the bottom of the page, "You haven't picked a class or a background yet! Come back when you have!"
    ii. Navigate back to the "Class" tab, select class and go back to the "Details" tab. Should say at the bottom of the page, "You haven't picked a class or a background yet! Come back when you have!"
    iii. Open the "Race" tab, and select a race, go back to the "Details" tab. Should say at the bottom of the page, "You haven't picked a class or a background yet! Come back when you have!"
    iv. Open the "Background" tab and select the background and go back to "Details". Should load select elements with appropriate options.
 
10.  Skill Proficiencies:
    i. Go to the "New Character" page, select Barbarian for class, Elf for race, Charlatan for Background and open the "Details" tab.
    ii. Expect 2 skill selects containing Animal Handling Athletics Intimidation Nature Perception Survival, no language selects and no tool select, but should have Disguise kit, Forgery kit underneath.
 
This particular test was done many times to ensure the right values appeared in the correct selects. This was just one example.
 
11. Character Details Validation:
    i. Open the "New Character" page and navigate to the "Details" tab.
    ii. Attempt to submit the form with empty fields, expecting an error message.
    iii. Fill the first field and submit the form, expecting an error message. 
    iv. Fill all text fields and not dropdowns. Expect an error message.
    v. Fill all fields, submit form, be forced onto "Ability Score" tab.
 
There were some oversights with this tab, as the "Personality Traits", "Ideals", "Flaws" and "Bonds" were lacking a required value. On top of this the "instruments" field when no value is selected returns null causing an error.
 
12. Choose Ability Scores:
    i. Open the "New Character" page, go to "Ability Scores" tab.
    ii. Try to submit a form with empty fields, except for error messages.
    iii. Enter field below 3, expect value to be rejected.
    iv. Enter value above 30, expect value to be rejected.
 
All are present and correct except for the "Wisdom Modifier", which is calculated wrong. After debugging the "Wisdom Modifier" was taking the "Strength" stat, so was calculating incorrectly.
 
13. Submit Character:
    i. Load the "New Character" page, fill previous tabs and open the "Submit" tab.
    ii. Ensure "Character Name", "Class", "Race", "Background", "Ability Scores", "Modifiers" are visible.
    iii. Submit form. Should take to the "Profile" page / Cancel pops all cookies and returns to the "Profile" page.
 
14. Profile Card Panels.
    i. Open "Profile" page
    ii. Display all character card panels created by that user. In closed form.
    iii. Should display "Character Name", "Character Description", and "More Details" collapsible.
    iv. selecting "More Details" should expand to display the character's "Class" "Race", "Background", "Ability Scores", "Maximum Hit Points", "Armor Class", along with the "Delete" and "Edit" buttons.
 
15. Character Gallery Card Panels:
    i. Open "Character Gallery" page.
    ii. Display all characters made by all profiles.
    iii. Should display "Character Name", "Character Description", and "More Details" collapsible.
    iv. selecting "More Details" should expand to display the character's "Class" "Race", "Background", "Ability Scores", "Maximum Hit Points" and "Armor Class".
 
16. Delete Button:
    i. Go to the "Profile" page.
    ii. Open "More Details" expands to display the "Delete" button.
    iii. Clicking on the "Delete" should open the model to ensure the user is sure of the deletion.
    iv. Clicking "Throw Them Off the Edge" should remove the character from the database, and "No, Let Them Live" will cancel the operation.
 
The modal displays as it should but only when the first card panel is open, it doesn't matter which card the delete button is pressed on it will delete the first character card. No fixes could be found so the modal has been scrapped for the time being.
 
 
 
17. View/Edit Button:
    i. Go to the "Profile" page.
    ii. Open "More Details" expands to display the "Edit" button.
    iii. Pressing the "Edit" button takes the user to the detailed view/edit page.
    iv. Changing all fields except for the death saves, are saved within the database.
 
Death saves not being pushed to the database is intentional, and do not need to be saved.
 
### Differences Between the Desktop and Mobile versions
 
#### Navbar
 
On Desktop the navbar displays to the far right of the screen, whereas on mobile it is hidden away as a side nav accessible by the fontawesome bars.
 
#### Character Gallery and Profile
 
On the desktop card panels display in a row of three, whereas on the mobile version they fill the row themselves.
 
#### New Character
 
Mobile version has the tabs nav as scrollable allowing for it to take up less space on the screen but still be fully accessible. "Ability Score" input fields display on their own rows, whereas on desktop they show in a row of six. 
Also on mobile the "Modifier" table is split in two and displayed on top of each other, and on the desktop they display side by side.
 
#### Edit Character
 
On the desktop view the "Character Sheet" is split into two rows and three main columns. Whereas on the mobile view the columns each take up the full length of the screen allowing for easy viewing of content.
 
## Deployment

### Local Deployment

This project was coded within the [Gitpod IDE](https://www.gitpod.io/) and then pushed to [Github](https://github.com/) using the built in functions.

1. Log into Github.
2. From the list of repositories on screen, select __milestone-3-dnd-character-creator__.
3. install the requirements.txt using the "pip3 install -r requirements" terminal command
4. After this it's as simple as typing "python3 app.py" within the terminal which will run the file

### How to run this project locally

To clone this project into Gitpod you will need:

1. A GitHub account. [Create a Github account here](https://github.com/)
2. Be using the Chrome browser

After follow these steps:

1. install the [Gitpod Browser Extension](https://gitpod.io)for Chrome.
2. After installation, restart the browser.
3. Log into your Gitpod account.
4. Navigate to the [Github repository](https://github.com/FabianMarsh/milestone-3-dnd-character-creator).
5. Click the green "Gitpod" button in the top right corner of the repository
6. This will trigger a new Gitpod workspace to be created from the code in github where you can work locally.

To work on this project within a local IDE such as Gitpod

1. Follow this link to the [Github repository](https://github.com/FabianMarsh/milestone-3-dnd-character-creator).
2. Under the repository name click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone , and then paste the URL you copied in step 3.

git clone https://github.com/FabianMarsh/milestone-3-dnd-character-creator

7. Press Enter. Your local clone will be created.

### Heroku Deployment

To deploy __milestone-3-character-creator__ to Heroku take the following steps

1. Create a requirements.txt file using the terminal command pip3 freeze > requirements.txt .
2. Create a Procfile using the terminal command echo web: python3 app.py > Procfile .
3. git add , git commit , and git push using the terminal commands to push to Github.
4. Sign into or register to [Heroku](https://dashboard.heroku.com/apps).
5. Create a new app on Heroku by clicking the "New" button in the dashboard. Give it a bespoke name and set the region to Europe
6. From the Heroku dashboard of the newly made created application, click on "Deployment method" and select Github.
7. Confirm the linking of Heroku and the GitHub repository.
8. Within the Heroku dashboard for the application, click on "Settings" then "Reveal Config Vars".
9. Set the following config vars:

Key | Value
--- | -----
DEBUG | FALSE
IP | 0.0.0.0
PORT | 5000
SECRET_KEY | <your_secret_key>
MONGO_URI | mongodb+srv://FabianM:2DzJy3w4S9o191zD@my-first-cluster.lyiaq.mongodb.net/dnd_character_creator?retryWrites=true&w=majority
MONGO_DBNAME | dnd_character_creator

* To get your MONGO_URI read the MongoDB Atlas documentation [here](https://docs.mongodb.com/manual/reference/connection-string/)

10. In the daskboard click "Deploy"

11. In the "Manual Deployment" section of this page, make sure the master branch is selected and click on "Deploy Branch".

12. The site has been successfully deployed

## Credits
 
### Content
 
* Text used for the "New Character" page, all fields contained within the __MongoDB__ database and the recreation of the character sheet on the "Edit Character" page were copied a PDF version of [The Wizards of the Coast Dungeons and Dragons 5th edition Player's Handbook](https://company.wizards.com/)
* The sample document for deployment for a [Backend Milstone]((https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/5a170081aab6478d881d96db05038a28/698b06ef0bd34c9fa300958e72747941/?activate_block_id=block-v1%3ACodeInstitute%2BDCP101%2B2017_T3%2Btype%40sequential%2Bblock%40698b06ef0bd34c9fa300958e72747941)) was used for reference when writing up the Heroku Deployment section.
* The sample document for [How to run this project locallt]((https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/5a170081aab6478d881d96db05038a28/698b06ef0bd34c9fa300958e72747941/?activate_block_id=block-v1%3ACodeInstitute%2BDCP101%2B2017_T3%2Btype%40sequential%2Bblock%40698b06ef0bd34c9fa300958e72747941)) was used for reference when writing the how to run this project locally section.

### Media
 
forge_background.jpg was taken from [deviantart](https://www.deviantart.com/binaryreflex/art/The-Earth-Forge-447070094)
 
### Acknowledgements
 
* [D&D Beyond](https://www.dndbeyond.com/)
* [Roll20](https://roll20.net/)
* [aurora](https://aurorabuilder.com/)
