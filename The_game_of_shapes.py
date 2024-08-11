# פתיח עבור המשתמש
def Acceptance_of_the_user():
      print("Welcome to the shapes game! ")
      print()
      print("Welcome to enjoy your choice! ")
      print()

# אופציות לבחירת הצורה
def List_for_options_to_choose_from():
    print("1. Triangle")
    print("2. inverted triangle")
    print("3. pyramid") 
    print("4. diamond")
    print("5. square")

    choice = input("Enter your choice: ")

    if choice.isdigit():
       choice_as_num = int(choice)

       if choice_as_num >= 1 and choice_as_num <= 5:
            return choice_as_num 
       else:
            print("Error") 
            return List_for_options_to_choose_from() 

#קלט מהמשתמש עבור בחירת הגודל
def Choose_size_for_shape():
    size = input("Choose the size for your shape from 1 - 20: ")

    if size.isdigit():
       choose_as_size = int(size)

       if choose_as_size >= 1 and choose_as_size <= 20:
            return choose_as_size
       else:
            print("Error")
            return Choose_size_for_shape()
    else:
        print("Error: Invalid input")
        return Choose_size_for_shape() 



#צורת משולש
def Triangle_shape(size):

    for i in range(size):
     print("*" * i)

#צורת משולש הפוך
def Inverted_triangle_shape(size):

    for i in range(size,-1,-1):
     print("*" * i)

#צורת פירמידה
def pyramid_shape(size):

    for i in range(size,0,-1):
     print(" " * i + "*" * (1 + (size - i)* 2))


   #צורת יהלום
def diamond_shape(size):

    for i in range(size,1,-1):
      print(" " * i + "*" * (1 + (size - i)* 2))

    for i in range(1,size + 1 ):
      print(" " * i + "*" * (1 + (size - i) * 2))

 #צורת ריבוע
def square_shape(size):
    for  i in range(1,size + 1):
      print("*" * size) 
   

#סיום תהליך
def end_process():
     print("Thank you for choosing a shape!")

     while True:
         answer = input("would you like to see another shape? y/n: ").strip().lower()

         if answer == "n":
             print("Thanks for playing! Goodbye")
             return False 
             
         elif answer == "y":
             return True
             
         else:
             print("Invalid answer, please try again: y/n:")
             


#פנקציה ראשית
def The_game_of_shapes():
    Acceptance_of_the_user()
    continue_game = True

    while continue_game:
         choise = List_for_options_to_choose_from()
         size = Choose_size_for_shape()

         if choise == 1:
            Triangle_shape(size)
         elif choise == 2:
            Inverted_triangle_shape(size)
         elif choise == 3:
            pyramid_shape(size)
         elif choise == 4:
            diamond_shape(size)
         elif choise == 5:
            square_shape(size)
         
         continue_game = end_process()


if __name__ == "__main__":
      The_game_of_shapes()
      