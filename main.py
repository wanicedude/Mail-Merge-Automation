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


    
#Replace the [name] placeholder with the actual name.
for name in names:
    letto = content.replace("[name]", name)
    with open(f"../../Documents/GITHUB/Mail Merge Automation/Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(letto)