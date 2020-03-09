#  QA-CRUD-PROJECT (Creating a Five Asided Team)

##  Project Breif
To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

###  Initilal Idea:  
My project is going to be a CRUD application that allows you the user to pick a team composed of 5 different players from several different leagues/eras, once created the user will be displayed their team and given the option to create another.

###  Players 
-	The players included will be the TOP players who have played for that team

-	Players who played for multiple teams will represent the team they are most known for playing for 

### Leagues
-	The list will include players from all the top 5/6 leagues 
-	Each league will have 20/30 players, ranging from current 2020 to early 2000s 

-	User will be given a list of leagues to choose from 

-	The setup will be League > Team > Player, in each league there will be the BIG Six which is the top 6 teams in each team there will be 10/15 players

-	 (Potentially) There will be another list of players who aren’t associated to the top leagues who can still be picked. 

###  Interface
-	User will be faced with a pitch menu with empty (grey slots) once user clicks on one of these they will be directed onto the leagues, followed by the player in that league.

-	User will be able to edit any choice they have made by removing the player in the chosen position and reselecting their choice. 

-	Each position will have an assigned group of players, for example if a goalkeeper is chosen then the user will only see goal keepers, if a defender is chosen the user will only be able to view defenders. 

-	There will be images associated with each player profile, will appear when the user has chosen his selection 

-	The user will not be able to add the same player in two separate positions, some sort of error/ method should not allow them to 

-	Once finished the user should be able to lock in their choices/ save their team and make a new one. 

## Website Structure
![Website Structure](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/Html%20Frame.png "Website Structure")

## Technologies used 
* [Gantt Chart](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/ERD%20Diagram%20(Database).png)
* Database: Azure SQL Server 
* Programming language: Python
* Unit Testing with Python (Pytest)
* Front-end: Flask (HTML)
* Version Control: Git
* CI Server: Jenkins
* Cloud server: Azure VM

## Entity Relationship Diagram 
![ERD](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/ERD%20Diagram%20(Database).png "ERD")
My initial ERD describes the relationships between all of my tables within my database, as you can see the user can has the capability of choosing from many leagues, as this is the permis of my project and will dictate what the user is allowed to choose in the next step which is the league that the club belongs to. 

![Added Table](https://github.com/zReginaldo/QA-CRUD-PROJECT/blob/master/Documentation/ERD%20Diagram%202.png "Added Table")
My final ERD had some slight changes, in order to display the users chosen 5 aside team I had to create another table that onoce the five player values had been confirmed would go into, then print this on a separate HTML page. 



