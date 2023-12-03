import json

f = open ('data.json', "r")
 
# Reading from file
data = json.loads(f.read())

#print(dictionary.items()) #prints keys and values
#print(dictionary.keys()) #prints keys
#print(dictionary.values()) #prints values

"""Another style of iterating through the json keys"""
for i in data.keys():
  print(i)


# Iterating through the json list values
for i in data.values():
    print(i)
 
# Closing file
f.close()

dictionary = {
    "name": "abcdefgh",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
  #This is the main branch version
  #This is the main branch version
  #This is the main branch version
 #This is the main branch version
  #This is the main branch version
  #This is the main branch version
  #This is the main branch version
  #This is the main branch version
 
  #This is the main branch version
 
 
 
 
 
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)

file = open('file_path', 'w')
file.write('hello world !')
file.close()

file = open('file_path2.json', 'w')
file.write(json_object)
file.close()

file = open('file_path2.json', 'a')
file.write("\n\nappended Text")
file.close()


# Using With
#with statement is used in exception handling to make the code cleaner and much more readable. It simplifies the management of common resources like file streams. Unlike the above implementations, there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources. 

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L) #accepts a list of strings

# Appending to file
with open("myfile.txt", 'a') as file1:
    file1.write("Today")


# Reading from file
with open("myfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())