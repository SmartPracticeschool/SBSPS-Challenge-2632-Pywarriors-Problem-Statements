#Declaring a list
money_list=[]
bill_list=[]
def bill_count(amt,money_list):
    #Initializing the minimum number of bills (the output) to zero
    min_count=0
    money_list.sort()
    number_of_bills=len(money_list)
    #Converting the list of strings to list of integers
    for i in range(number_of_bills):
        bill_list.append(int(money_list[i]))
    #Condition to check if the amount of money is lesser than the list of money bills available
    if(amt<bill_list[0]):
        print("Enter the total amount such that it is greater than the list of money bills available")
        return
    for i in range(number_of_bills):
        #Condition to check if the money bills are negative
        if(bill_list[i]<0):
            print("The money bill cannot be negative")
            break;
        #Condition to check if the money bills are not from the valid INR currency bills
        if(bill_list[i] not in INR):
            print("Enter a valid money bill. The valid money bills are 1,2,5,10,20,50,100,200,500,2000")
            return
    index=number_of_bills-1
    while(amt!=0):
        if(amt>=bill_list[index]):
            amt=amt-bill_list[index]
            min_count+=1
        else:
            index=index-1
    print(min_count)
    
    
#The valid INR currency bills
INR=[1,2,5,10,20,50,100,200,500,2000]
#Getting the input for the total amount
amount=int(input("Enter the total amount: "))
#Note that the python interpreter considers this list as a list of integers
input_list = input("Enter a list of money bills separated by space: ")
#Splitting the input list of money bills into separate elements
list_of_bills  = input_list.split()
#Calling the function
bill_count(amount,list_of_bills)