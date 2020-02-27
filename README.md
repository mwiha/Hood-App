## Nyumba-Kumi

# Description  
This project allows users to post their hood, hospitals, police stations and businesses around their neighbourhood


## User Story  
  
* A user can view different neighbourhoods  
* A user can post their neighbourhood 
* A user can join or leave a different neighbourhood  
* Search for businesses  
* A user can write a post for other users to see
* A user can view their profile page. 
* A user can add a business name that is near the neigbourhood 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash
https://github.com/mwiha/Hood-App.git
```
##### Navigate into the folder and install requirements  
 ```bash
 cd Neighbourhood pip install -r requirements.txt 
 ```
##### Install and activate Virtual  
```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies  
```bash
 pip install -r requirements.txt 
``` 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations hood
 ``` 
 Now Migrate

```bash
python manage.py migrate 
```
##### Run the application  
```bash
python manage.py runserver 
```
##### Testing the application  
```bash
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  


## specifications

| BEHAVIOUR	       | INPUT	        | OUTPUT        |
| -------------- | :-------------: | ----------: |
|To view page |login|displays the hoods|
| User wants to view occasions	| User visits the site  |   Displays the occasions in the neighbourhood |
| User wants to view the neighbourhood events	| They click on the event	| Website events are displayed |


  
 
## Technology used  
  
* Python3.6  
* Django 1.11  
* 
  
  
## Known Bugs  
* There are no known bugs currently  
  
## Contact Information   
* For question,contributions or comments please email me at 
     alicemwihaki99@gmail.com

## Licence
Copyright (c) 2019 Alice Mwihaki
