# *Viva Air Airlines Technical Test*
![Image taken from semana.com, all rights reserved](https://www.semana.com/resizer/GKkKmcAFX6zqGHp1qPPe558Fo4o=/1200x675/filters:format(jpg):quality(50)//cloudfront-us-east-1.images.arcpublishing.com/semana/H27MWAZHXFGU3PBAJNS3GQMSVA.jpg)

## *About The Project*

This project is carried out in order to test my knowledge about the correct construccion of a REST Api for the Viva Air Airlines, for this project it was used the technologies mentioned below:

 - **Python** 
 - **Django** 
 - **Django Rest Framework** 
 - **Django Redis** 
 - **Docker** 

This project consist in the creation of an app endpoint that takes two arguments, the first argument you can input is **i** wich determines **the index** from where do you want to start retriving the stories, **beeing 0 the latest story**. The second argument that you can input is **n** wich determines **the number of stories** that you want to recive.

## *Installation Procces*

 - To see this project work first you need to install all the dependencies mentioned in the file `dependencies.txt`
 - The next step is to clone this repositorie into your machine using the git comand `git clone`
 - You will need to two terminals, in the first one run the command `python3 manage.py runserver` while you are in the project folder, this will start the **django server**, if you are having trouble starting the server please go to this link: [Django Documentation](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
 - In the second terminal run the command `redis-server` while you are in the project folder,  this will start the **redis server** wich holds the  cache memory, if you are having trouble starting the server please go to this link: [Redis Documentation](https://redis.io/docs/getting-started/)
 
 Now its all set, you can go to this link http://127.0.0.1:8000/api/

## *Usage*

For the usage of this Api you have two submit the values mentioned above in the ***About The Project*** section, the simpliest way to achive this is using the browser bar with the syntax shown below:

    Example syntax:
    
    http://127.0.0.1:8000/api/?i=0&n=3
    http://127.0.0.1:8000/api/?n=4&i=2
   
Note that if any of the two arguments is missing its going to rise an error message, same way for negative values or if any of the values exceeds the length avalible.

Also note that the memory cache will hold the information shown for the next **ten seconds**, after this you can do another search using the same syntax

## *Authors*
 - ***Alexander Cardona Herrera***
