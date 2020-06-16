#Declaring a list
money_list=[]
def bill_count(amt,money_list):
    #Initializing the minimum number of bills (the output) to zero
    min_count=0
    money_list.sort()
    number_of_bills=len(money_list)
    #Condition to check if the amount of money is lesser than the list of money bills available
    if(amt<money_list[0]):
        print("Enter the total amount such that it is greater than the list of money bills available")
        return
    for i in range(number_of_bills):
        #Condition to check if the money bills are negative
        if(money_list[i]<0):
            print("The money bill cannot be negative")
            break;
        #Condition to check if the money bills are not from the valid INR currency bills
        if(money_list[i] not in INR):
            print("Enter a valid money bill. The valid money bills are 1,2,5,10,20,50,100,200,500,2000")
            return
    index=number_of_bills-1
    while(amt!=0):
        if(amt>=money_list[index]):
            amt=amt-money_list[index]
            min_count+=1
        else:
            index=index-1
    print(min_count)
    
    
#The valid INR currency bills
INR=[1,2,5,10,20,50,100,200,500,2000]
#Getting the input for the total amount
amount=int(input("Enter the total amount: "))
#Getting the input for the number of elements in the list of bills Ex.: If the list of money bills are [10,20] the input for no_of_money_bills should be 2
no_of_money_bills=int(input("Enter the total number of money bills available:"))
list_of_bills=[]
#Getting the input for the list of money bills
print("Enter the list of money bills:")
for i in range(no_of_money_bills):
    money=int(input())
    list_of_bills.append(money)
#Calling the function
bill_count(amount,list_of_bills)