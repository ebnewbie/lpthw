from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


#we are using argv to open a file without only asking python to open that file. The code we used allows us to open different files.
#the input part is what allows us to tell python to open a file, any file.
#this code also allows us to read what's within the file. 
