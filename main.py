#TODO: Create a letter using starting_letter.txt 

letter = open("../../Documents/GITHUB//Mail Merge Automation/Input/Letters/starting_letter.txt")
content = letter.read()
print(content)

#use a for loop to create a list of names in the invited names .txt
names = []
with open("../../Documents/GITHUB//Mail Merge Automation/Input/Names/invited_names.txt") as invited_names:
    name_content = invited_names.readlines()
        
    # This will remove the "\n" in each names
    for x in name_content:
        names_with = x.replace("\n", "")
        names.append(names_with)
print(names)


    
#Replace the [name] placeholder with the actual name.

#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp