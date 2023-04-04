# Ticket system 

The Ticket system is an Assessment I did for my Software Project. In this Assessment, we were supposed to to a 
project where you could generate Tickets for a HELP DESK program. In order to do that, I connected the code to a data base, where I could storage the data and use it to generate statistics later on. When you download this code, please be sure to download the Access DataBase as well in order to it to function. 

## Connecting to the database

The first and the most important part (at least I think it is the most important lol) is connecting to the data base, to to that you have to download the extension. Just go to your cmd, type `pip install pyodbc` and you will be good to go. 

### macOS

If you're using **Apple Silicon** architecture, you might find that the `pyodbc` extension, at its latest compilation, won't work. This is given to the fact its binary is not compatible with your processor. If that's the case, you can install and re-compile the extension using the following command:

```sh
pip install --no-binary :all: pyodbc
```

If, by any reason, the extension was already installed, you can force it to re-install using the `--force-reinstall` flag:

```sh
pip install --force-reinstall --no-binary :all: pyodbc
```

## Features

### Login   
The login function will define which access you'll have. 
If you are an ADMIN:
User = ADMIN
Password = ADMIN

If you are a STAFF member: 
User = STAFF
Password = STAFF

If you are a SUPPORT member: 
User = SUPPORT 
Password = SUPPORT


### ADMIN 
The ADMIN will have two options: see the statistics of the tickets or see all the tickets. 
Type 1 to see the statistics or 2 to see the tickets. 

### STAFF
The STAFF member will also have two options: Reopen a previous ticket or add a new one. 
Type 1 to reopen or 2 to add. 

If you want to reopen a ticket, you need to have the ID of the ticket. *REMEMBER: the tickets start from 2000
After selecting the ticket you want to reopen, the system will ask if you really want to reopen it, type 
YES if you are sure, type NO if you waqnt to end the request. 

If you want to add a new ticket, just insert the issue and it will automatic generate a Ticket ID and save your Issue in the database with a OPENED status. 
After adding a new ticket, the program will ask you if you want to add a new one. 
Type YES if you want to proceed and add a new ticket or type NO if you want to exit the program. 

### SUPPORT 
The support team will only be able to answer tickets. In order to do that, type the Ticket ID of the ticket you want to solve. 
And then, add a resolution to that problem. 
When finished, the program will ask you if you would like to solve any other ticket. 
Type YES if you would like to or NO if you want to finish the process. 

### Access
Every time you add, reopen or close a ticket, the database will automatically be updated. 
The STATUS will change for every action you take. 

### Future implements 
As I am writing this README file, I found some other functions that I would like to implement on this project. 
For example blocking the access for the SUPPORT if the ticket is already closed. 

### FUN! 
The main goal of this project was to undestand the OOP programming. But while I was coding it, I had so much fun that I just don't want to stop implementing things to this project. 
