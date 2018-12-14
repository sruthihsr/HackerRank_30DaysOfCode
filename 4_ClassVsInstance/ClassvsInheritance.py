class Person:
    def __init__(self,initialAge):
        if(initialAge > 0):
            self.age = age
        else :
            print ("Age is not valid, setting age to 0.")
            self.age=0
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if(self.age<13):
            print("You are young.")
        elif(self.age<18):
            print("You are a teenager.")
        else :
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age+=1
    
t = int(input())
