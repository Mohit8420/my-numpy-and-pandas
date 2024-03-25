import pandas as pd

data = []

while True :
    print('\nOptions ----------------------------------------------------------------')
    print('1) Book the room \n2) Print the ticket')
    choice = int(input('enter yor choice number (eg. 1 or 2) :  '))
 
    if choice == 1 :
        name = input(' Enter customer name : ')
        id = int(input(' Enter customer ID number : '))
        days = int(input('For how many days you want to stay : '))
        
        data.append({'name' :  name , 'id' :  id , 'days':  days })

        print(" you have been succesfully registerd with our hotel ")

    elif choice == 2 :
        df = pd.DataFrame(data)

        if not df.empty : 
         print(' your ticket is here ------------->\n')
         print(df)

        else : 
            print('you have not booked a ticket yet')
        

    else : 
        print('no ticet is booked by you now ')


    further = input('do you want any more sevice (yes or no) :  ')
    if not further == 'yes':
        print('thank you ')
        break
       

    
