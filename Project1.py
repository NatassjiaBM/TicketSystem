#Connecting to database
import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\admin\Pessoal\Whitecliffe\codes\Natassjia\Assigment_One\TicketDataBase.accdb;')


#Fetchall pega todos os registros da tabela
usertype = ""
userid = 0

#Creating Login input
def login():
    print('Enter your username: ')
    uname = input()
    print('Enter your password: ')
    pwd = input()
    #usar a palavra chave global para impedir que o Python crie uma copia local da variável global
    global usertype
    global userid
#Selecting the Login table from the DataBase
#F = extended text 
    ssql = f"Select * from Login where '{uname}' = Login and '{pwd}' = Password"
    #print(ssql)
    cursor = conn.cursor()
    cursor.execute(ssql)
#Goes to the database, verifies if it exists. If the data doesn't exists, it transforms itself to NONE and doesn't return any data from the database.
    row = cursor.fetchone()
    if row is None:
        print("Incorrect user or password")
        return 0 #False
    else:
        #Row = dessa linha pegue essa .coluna
        usertype = row.UserType
        userid = row.LoginID
        return 1 #True
    

#Create different functions for different User Types


#ADMIN MENU - Gives the admin options between STATS AND TICKETS 
def __adminmenu__():
    print('Welcome, ADMIN. Type 1 to see the Statistics or 2 to see the Tickets')
    answer = input()
    if answer.lower() == "1":
        __stats__()
    elif answer.lower() == "2":
        __alltickets__()
    else: 
        print('Please type 1 or 2')
        __adminmenu__()

#ALL TICKETS - displays all the tickets to the admin
def __alltickets__():
    print('Here you have all the tickets.')
    allTickets = f"Select * from Ticket as totaltickets order by TicketID"
    cursor = conn.cursor()
    cursor.execute(allTickets)
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
    print('Press 1 to go back to main menu or 2 to exit the program')
    resposta = input()
    if resposta == "1":
            __main__()
    elif resposta == "2":
            exit()
    else:
            print('We dont recognize this answer. Exiting the program')
            exit()



#Stats - shows the ADMIN the statistics of the Tickets.
def __stats__():
    print('Welcome, ADMIN.')
    totalTickets = f"Select count ('Status') as totalall from Ticket"
    cursor = conn.cursor()
    cursor.execute(totalTickets)
    rowc = cursor.fetchone() 
    totalall = rowc.totalall
    print("\n ***************") 
    print("The total of Tickets is ", totalall)

    openedTickets = f"Select count ('Status') as totalOpened from Ticket where Status = ('OPENED')"
    cursor.execute(openedTickets)
    rowc = cursor.fetchone() 
    totalOpened = rowc.totalOpened
    print("\n ***************")
    print("The total of OPEN Tickets is ", totalOpened)
   
    closedTickets = f"Select count('Status') as totalClosed FROM Ticket where Status = 'CLOSED'"
    cursor.execute(closedTickets)
    rowc = cursor.fetchone() 
    totalClosed = rowc.totalClosed
    print("\n ***************") 
    print("The total of CLOSED tickets is ", totalClosed)
   
    reopenedTickets = f"Select Count ('Status') as totalReopened from Ticket where Status = 'REOPENED'"
    cursor.execute(reopenedTickets)
    rowc = cursor.fetchone() 
    totalReopened = rowc.totalReopened
    print("\n ***************")
    print("The total of REOPENED Tickets is ", totalReopened)

    print("\n ***************") 
    percentageClosed = totalClosed / totalall * 100
    # cursor.execute(percentageClosed)
    # rowc = cursor.fetchone()
    # Percentage = rowc.Percentage
    print("The IT team has solved ", percentageClosed, "of the Tickets.")
    print("\n ***************")
    print("Would you like to see the Tickets? Type 1 to yes or 2 to go back to Login.")
    answer = input()
    if answer.lower() == "1":
        __alltickets__()
    elif answer.lower() == "2":
        login()
    else:
        print('Please, type 1 or 2')
        __stats__()
    

# STAFF MENU - would you like to ADD or UPDATE ticket? 
def __staffmenu__():
    print('Welcome staff. Type 1 to REOPEN a ticket or 2 to ADD a new ticket')
    answer = input()
    if answer.lower() == "1":
        __updateTicket__()
    elif answer.lower() == "2":
        __newTicket__()
    else: 
        print('Please type 1 or 2')
        __staffmenu__()

#New Tickets - Allows the STAFF to add new tickets.
def __newTicket__():
    print('Please, insert the issue')
    problem = input()
    addTicket = f"Insert into Ticket(Issue, DateOpened, ProblemSolution, Status, StaffID) values ('{problem}', Date(), 'None', 'OPENED', '300')"
    cursor = conn.cursor()
    cursor.execute(addTicket)
    conn.commit()
    ticketID = f"SELECT TicketID as lastticket FROM Ticket  WHERE TicketID=(SELECT max(TicketID) FROM Ticket);"
    cursor.execute(ticketID)
    rowt = cursor.fetchone()
    ticketID = rowt.lastticket
    print('New ticket added. The Ticket ID is', ticketID)
    print('Would you like to ADD a new ticket? Type yes or no')
    answer = input()
    if answer.lower() == "yes":
        __newTicket__()
    elif answer.lower() == "no":
        exit()
    else:
        print("Please, type yes or no. Exiting program, please login again")
        exit()

    
    
#Update Ticket - Allows the STAFFF to reopen the tickets
def __updateTicket__():
    print("Please, insert the ID of the Ticket you need to update") #My answer is not being validaded
    answer = input()
    findTicket= f"Select * from Ticket where {answer} = TicketID"
    cursor = conn.cursor()
    cursor.execute(findTicket)  
## ADD RETURN FALSE IF NOT FIND TE TICKET ID ##
    yesorno = input("Would you like to update it?(Yes or No)")
    if yesorno.lower() == 'yes':
        print("Please, insert the new issue")
        newIssue = input()
        updateTicket = f"Update Ticket set Issue = '{newIssue}', ProblemSolution = 'Ticket Reopened',   DateOpened = Date(), Status = 'REOPENED', StaffID = '300' where TicketID = {answer}"
        #print(updateTicket)
        cursor.execute(updateTicket)
        conn.commit()
        print("Your ticket has been sucesfully updated!")
        again = input('Would you like to update a new ticket? (Yes/No)')
        if again.lower() == 'yes':
            __updateTicket__()
        elif again.lower() == 'no':
            print('Ok, going back to main menu')
            __main__()
        else:
            print("Please, type yes or no.")
    elif yesorno.lower() == 'no':
        exit()
    else: 
        print("Please, type yes or no.")
        exit()


#Support - Allows the IT team to answer the tickets. 
def __support__():
    print('Please, insert the Ticket ID')
    TicketID = input()
    FindTicketID = f"Select * from Ticket where {TicketID} = TicketID"
    #print(FindTicketID)
    cursor = conn.cursor()
    cursor.execute(FindTicketID)
    print('Insert a resolution to this issue')
    ProblemSolution = input()
    addSolution = f"Update Ticket set ProblemSolution = '{ProblemSolution}', DateClosed = Date(), Status = 'CLOSED', StaffID = '200' where TicketID = {TicketID}"
    cursor = conn.cursor()
    cursor.execute(addSolution)
    conn.commit()
    answerAgain = input("Would you like to update a new one?(Yes or No)")
    if answerAgain.lower() == 'yes':
        __support__()
    elif answerAgain.lower() == 'no':
        print('Ok')
        exit()
    else:
        print('Please type yes or no') 
        __support__()

#Defines which of the menus will show to each staff member.
def __main__():    
    loggedIn = login()
    if loggedIn == 1:
        if usertype == 'ADMIN': 
            __adminmenu__()
        elif usertype == 'SUPPORT':
            __support__()
        elif usertype == 'STAFF':
            __staffmenu__()
    else:
        print('Try again...')
        login()
            

__main__()