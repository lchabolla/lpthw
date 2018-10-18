from sys import argv # imports sys package and calls argv feature

script, filename = argv # unpacks argv

txt = open(filename) # define txt variable with open method with filename variable

print(f"Here's your filename: {filename}") # print filename
print(txt.read()) # print content of txt variable (filename)

## print("Type the filename again:") # prompt user to enter filename
## file_again = input("> ") # define file_again variable and prompts user for more input

## txt_again = open(file_again) # defines txt_again variable which opens file_again

##print(txt_again.read()) # prints contents of open file store in txt_again variable

txt.close()
#txt_again.close()
