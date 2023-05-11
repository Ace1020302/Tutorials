# Header comments here 
# FILL THIS OUT!
# Name
# Date
# Project
# Class

def main():
    # Congrats! This is the penulitmate tutorial!
    # Aren't you glad this tutorial doesn't LOOP back around. Me too!
    # Unforutnately, looping and conditionals are the topics of this tutorial

    # Conditionals are easy! It's simply just true and false... on steroids
    cond = True
    oppositeCond = not cond
    print("Condition 1 : " + cond)
    print("Condition 1's Opposite: " + oppositeCond)

    # Conditional statements happen if true, and don't if not
    if(cond): # checking if cond is true
        print("cond is true")

    # Else If's
    speech = input() 
    
    if(speech == "Hello There"):
        print("You are Obi-Wan")
    elif(speech == "This is the Way"):
        print("You are Mandolorian.")
    else:
        print("You typed something")

    # Different types of comparions operators (NEED TO KNOW)

        # ==  ->  Equality Check (if both are same, they return true)
        # !=  -> Not Equal Check (if both are same, return false)
        # >, >=   ->   Checks if left value is higher than right. Returns true if so.
        # <, <=   ->   Checks if right value is higher than left. Returns true if so.
        # or  -> OR operator    Checks if either condition around it is true (if so, then returns true)
        # and  -> AND operator   Checks if both conditions around it are true (if so, then returns false)
    brotherAge = 10
    sisterAge = 20
    if(brotherAge != sisterAge):
        print("Not twins")





# Checks if the name of the file is the main file and then runs it if true
if __name__ == "__main__":
    main()