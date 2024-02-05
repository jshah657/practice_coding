#Let's start basic: How do you comment your code? Its by adding a hashtag in the front of your sentence or word. Like this one. 

#print hello world
print("Hello World")

# Assign a value to a varibale. What is variable? Think of a variable as a storage for your assigned value that you can use throught the coding. For example: 
name = {"first name" : "Jay",
        "last name" : "Shah",
        "age" : 31,
        "spouse name" : "Heemali Patel"}
print(name)

# As you can see that the above variable has multiple values which are fortmatted using dictionary. Let's print first name and last name. 
print(name['first name'] + " " + name["last name"])

# Let's understand array. Array is the list of items in brackets. It can be an integer or a string. 
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0]) #as you can see that [0] is the first value in the array. 
print(numbers[0:2]) #this should print 1,2

# Let's understand errors in Python code. 
# Runtime errors = RuntimeError are caught in Python code that is not defined. 
 
# Let's understand variables. Following variables are defined to store values in variables. 
firstName = "Jay"
lastName = "Shah"
age = 31 
jobRole = "Senior system integrator"
company = "Arthrex"
education = "Masters of Information Systems"
# See following variable called welcomeMessage, it calls various variables within string message by applying format function. 
welcomeMessage = ("We are super excited to announce that we have hired a new employee in our team. I would like to introduce {} {}. {} is {} years old.").format(firstName, lastName, firstName, age)
print(welcomeMessage) 
# Another way to add variables to a string is to use f before sentence. For example: 
newWelcomeMessage = f"We are super excited to announce that we have hired a new employee in our team. I would like to introduce {firstName} {lastName}. {firstName} is {age} years old."
print(newWelcomeMessage)

#let's understand number types: 
a = 99 
print(type(a))
b = 99.0
print(type(b))

#You can also use the following to generate a number into a float. 
print(float(1))

# something interesting I have learned about division is to generate an output in integer, you can use two back slashes and for float you can use one. 
d = 99 
e = 11 
ans = d / e
print(ans)

# Example of quick calculation.
message_1 = "Lets find out how old are you?"
age_number = input("Enter the year you were born ")
current_year = 2024
answer = int(current_year) - int(age_number)
print(message_1)
print(f"You are only {answer} years old. You are still young!")