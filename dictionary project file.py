# Dictionary management system project
#1) Add a word
#2)Search for meaning
#3)Display all words
#4)Update meaning
#5)Delete word
#6)Exit

my_dict = {}
while True:
    print("-------dictionary of words-----------")
    print("1.Add a Word")
    print("2.Search for a meaning ")
    print("4.Update a meaning")
    print("5.Delete word")
    print("6.Exit")

    choice = input("enter your choice: ")
    if choice == '1':
        wrd = input("enter a word: ").lower()
        mng = input("enter the meaning: ")
        my_dict[wrd] = mng
        print("word added successfully.")

    elif choice == '2':
        wrd = input("enter a word: ").lower()
        if wrd in my_dict:
            print("meaning:",my_dict[wrd])
        else:
            print("word not found in my_dict.")

    elif choice == '3':
        if my_dict:
            print("words and their meanings my_dict: ")
            for wrd, mng in my_dict.items():
                print(f"{wrd}:{mng}")
        else:
            print("my_dict is empty. ")

    elif choice == '4':
        wrd = input("enter the word to update the meaning: ").lower()
        if wrd in my_dict:
            new_mng = input("enter the new meaning: ")
            my_dict[wrd] = new_mng
            print("meaning updated successfully. ")
            print("updated meaning:",my_dict[wrd])
        else:
            print("word not found in the my_dict. ")

    elif choice == '5':
        wrd = input("enter the word to delete: ").lower()
        if wrd in my_dict:
            del my_dict[wrd]
            print("word deleted successfully. ")
        else:
            print("word not found in my_dict. ")

    elif choice == '6':
        print("exit")
        break

    else:
        print("invalid choice! please enter number between 1 and 6.")
    






     


    


    





        




        
    

    


    

        
    

           


        

    

            




        

                 
    
        
