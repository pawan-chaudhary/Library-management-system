import datetime
import list2D as l
global list2d
date1=datetime.date.today()
date2=datetime.timedelta(days=10)
def display_items(list2d):
        choose=False
        while choose!=1 and choose!=2 and choose!=3:
                try:
                        choose=int(input("Enter only a number where you want a go through:"))
                except:
                        print("please enter number only")
                if choose==1:
                        display1(list2d)
                        choose1=False
                        while choose1!="yes" and choose1!="no":                                
                                choose1=input("Do you want to borrow a book?\nYes or No:").lower()
                                while choose1=="yes":
                                        name,address,phone_num=user_info()
                                        book_name,book_author,quantity,total,choice = borrow(list2d)                                      
                                        createReceipt( name, address, phone_num, book_name,book_author, quantity,total, list2d)
                                        choose1=input("Do you want to do any other transaction? yes or no:").lower()
                                
                                if choose1=="no":
                                        exit1()
                                else:
                                        print("Invalid Character")
                elif choose==2:
                        True
                        return_book(list2d)
                elif choose==3:
                        exit1()
                else:
                        print("Invalid Integer")

def createReceipt( username,address, phone_num, bookname, author, quantity, price, list2d):
        receipt = "Name:"+username+"\nAddress:"+address+"\nPhone Number:"+str(phone_num)+"\nBookname: "+ bookname+"\nAuthor: "+author +"\nQuantity: " + str(quantity)+ "\nPrice: $" + str(price)
        print( receipt )
        print("Date of borrowed:",str(date1))
        print("Date to be returned:",str(date1+date2))
        print("Note: If you return books after returning date then you will be charged by $0.2 per day for each book.")
        record_file=open("record.txt","a")
        record_file.write("Name:"+username+", Bookname:"+ bookname+", Address:"+address+", Quantity:" + str(quantity)+", Phone Number:"+str(phone_num)+", Date:"+str(date1))
        record_file.write("\n")
        record_file.close()
        file=open(username+".txt","w")
        file.write("Name:"+username+"\nAddress:"+address+"\nPhone Number:"+str(phone_num)+"\nBookname:"+ bookname+"\nAuthor:"+author +"\nQuantity:" + str(quantity)+ "\nPrice: $" + str(price)+"\nDate of borrowed:"+str(date1)+"\nDate to be returned:"+str(date1+date2))
        file.close()
        
def display1(list2d):
        display_list=print("\nS.No\tBook Name\t\tAuthor\t\t\tQuantity\tPrice\n\n")
        for i in range(len(list2d)):
                print(i+1,end="\t")
                for j in range(len(list2d[i])):
                        if (len(list2d[i][0])>25):
                                print(list2d[i][j],end="\t")
                        else:
                                print(list2d[i][j],end="\t\t")
                        
                print("\n")
        return display_list
def borrow(list2d):
        display1(list2d)
        choice=int(input("Which book do you want to borrow\nPlease enter serial number only:"))
        quantity=int(input("Enter quantity you want:"))
        for i in range(len(list2d)):
                for j in range(len(list2d[i])):
                        if choice==i:
                                book_name=list2d[i-1][0]
                                book_author=list2d[i-1][1]
                                global change
                                change=list2d[i-1][3].replace("$","")
                                if j==choice-1:
                                        list2d[j][2]=str(int(list2d[j][2])-quantity)
                                      
        total=int(change)*quantity
        stock_file=open("books.txt","w")
        for list1 in list2d:
                stock_file.write(",".join(list1))
                stock_file.write("\n")
        stock_file.close()
        return book_name,book_author,quantity,total,choice

def user_info():
        name=input("Enter your name:")
        address=input("Enter your address:")
        phone_num=int(input("Enter your phone number:"))
        return name,address,phone_num

def return_book(list2d):
        display1(list2d)
        name=input("Enter your name:")
        choose4=int(input("Which book do you want to returned\nPlease enter serial number only:"))
        return_quantity=int(input("How many book do you want to return:"))
        for i in range(len(list2d)):
                for j in range(len(list2d[i])):
                        if choose4==i:
                                book_name1=list2d[i-1][0]
                                book_author1=list2d[i-1][1]
                                if j==choose4-1:
                                        list2d[j][2]=str(int(list2d[j][2])+return_quantity)
        write_file=open("books.txt","w")
        for each in list2d:
                write_file.write(",".join(each))
                write_file.write("\n")
        write_file.close()
        print("Book Name:",list2d[i-1][0])
        print("Book Author:",list2d[i-1][1])
        print("Quantity:",return_quantity)
        file1=open("return_receipt.txt","a")
        file1.write("Name:"+name+", Book Name:"+list2d[i-1][0]+", Author:"+list2d[i-1][1]+", Quantity:"+str(return_quantity))
        file1.write("\n")
        file1.close()
        print("|=============================Thank You==================================|\n|==========The Book You Have Borrowed Are Successfully Returned==========|")
                
                                
                                
                                
        
        
        
        


def exit1():
        print("|========================Thank You========================|\n|=====================Please visit again==================|\n|====================!!!Have a gooday!!!==================|")





