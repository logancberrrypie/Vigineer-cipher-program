#Imports modules
from os.path import getsize
from os.path import isfile
from re import match
from time import sleep

#Declares function called checker with 3 parameters
def checker(text , final , file):
    #Checks to see if the lenght of text is bigger than 15
    if len(text) > 15:
        #Outputs to the console
        print("The file "+str(file)+"has been encrypted / decrypted")
    #If the lenght of text is not bigger than 15 then this will be ran
    else:
        #Outputs to the console
         print("The word / phrase '",text,"'has been encrypted / decrypted to : ",final)

#Declares function called file_write with 2 parameters
def file_write(file , final):
    #Will try and complete the following :
    try:
        #Opens up the file in write mode and sets it equal to f
        f = open(file , mode="w")
        #Writes final into file f
        f.write(final)
        #Closes file f
        f.close()
    #Excepts a permission error meaning that it does not error.This error is caused when python does not have permission to edit a file.
    except PermissionError:
        #Outputs to the console
        print("Im sorry but I we do not have permission to access that file \n\
Therefore we are unable to output the encrypted or decrypted phrase to the file however we have encrypted / decrypted it into \n\
 '"+final+"' \n")

#Declares function called file_read with 1 parameter
def file_read(file):
    #Opens the file the user specified in reading mode and set it equal to f
    f = open(file, mode="r")
    #Set variable text equal to the contents of f
    text = f.read()
    #Closes the file f
    f.close()
    #Returns the value of text
    return text

#Declares function called encryption with 5 parameters
def encryption(alphabet , final , text , key, file , len_):
    #Checks to see if i is bigger than 0 and smaller than the lengh of text
    for i in range(0,len(text)):
        #Sets temp equal to the position of the encrypted letter once the offset has been added to it and modulared
        temp = (alphabet.find(text[i])+alphabet.find(key[(i%len(key))]))%len_
        #Sets final equal to itself and the temp'th letter of alphabet
        final +=alphabet[temp]
    #Runs function file_write with parameters of file and final
    file_write(file , final)
    #Runs function checker with parameters of text . final and file
    checker(text , final , file)

#Declares function decryption with 5 parametersz
def decryption(alphabet , final , text , key, file , len_):
    #Checks to see if i is bigger than 0 and smaller than the lengh of text
    for i in range(0,len(text)):
        #Sets temp equal to the position of the encrypted letter once the offset has been added to it and modulared
        temp = (alphabet.find(text[i])-alphabet.find(key[(i%len(key))]))%len_
        #Sets final equal to itself and the temp'th letter of alphabet
        final = final + alphabet[temp]
    #Runs function file_write with parameters of file and final
    file_write(file , final)
    #Runs function checker with parameters of text . final and file
    checker(text , final , file)


#Declares function called main
def main():
    #Sets variable alphabet equal to the extended / 94 character python alphabet
    alphabet = str("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ")
    #Sets variable short equal to the standard 26 letter alphabet
    short = str("abcdefghijklmnopqrstuvwxyz")
    #Sets variable final equal to and empty string
    final = ""
    #Sets string variable choice to the users input
    choice = str(input(" \n\
What do you want? \n\
1. Encryption (Extended alphabet)  \n\
2. Decryption (Extended alphabet) \n\
3. Encryption (Standard alphabet)  \n\
4. Decryption (Standard alphabet) \n\
5. What are these 2 alphabets? ~<--HELP HERE \n\
6. Quit \n"))
    #Checks to see if choice does not equal a correct value
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        #outputs to the console
        print("Please enter 1 or 2")
        #Runs function main
        main()
    #Checks to see if choice equals "5" -- note this is checking a string against a string
    if choice == "5":
        #Runs function without any arguments
        text_output_main()
        #Runs function without any arguments
        main()
    #Checks too see if choice equals "6" -- note this is checking a string against a string
    if choice == "6":
        #Quits the program
        quit()
    #Asks for an input
    file = input("Please state the file directory which you want to encrypt / decrypt from or type the text you want with @@ before! \n\
An example would be '@@hello' \n")
    #Checks too see if the first 2 characters of file are both not '@'
    if file[0] != "@" and file [1] != "@":
        #Checks to see if the file exists.This is using part of the OS module which we imported
        if isfile(file):
            #Outputs to console
            print("File is present.File size is :"+str(getsize(file))+" bytes big!")
            text = file_read(file)
            if choice == "3" or choice == "4":
                #This checks to see if any characters apart from a-z lower case are in variable text
                if  not match("^[a-z]*$", text):
                    #Outputs to console
                    print("Invalid input.Please you inputted a character that is not in the 26 letter alphabet! ")
                    #Intiates variable to an empety string
                    text = str("")
                    #Runs function without any arguments
                    main()
        else:
            #Outputs to console
            print("File is not present \n\
    Please try again \n")
            #Runs function
            main()
    """

    This section does the removing of any '@' in the input and creates a file or reads the file at the location specified
    It uses mechanics used previously so if you need to understand any line their will be the line commented somewhere else

    """
    if file[0] == "@" and file[1] == "@":
        text = file[2:len(file)]
        if choice == "3" or choice == "4":
            if  not match("^[a-z]*$", text):
                    print("Invalid input.Please you inputted a character that is not in the 26 letter alphabet! ")
                    text = str("")
                    main()
        file = input("Where would you like the file for the output to be created? ")
        try:
            f = open(file,mode="w")
            f.close()
        except:
            print("Invalid location")
            main()
    key = input("What key do you want to use? ")
    if choice == "3" or choice == "4":
        if  not match("^[a-z]*$", key):
            print("Invalid input.Please you inputted a character that is not in the 26 letter alphabet! ")
            key = str("")
            main()
    """
Various 1 line if statements running diffrent functions.All of which have 6 arguments
    """
    if choice == "1": encryption(alphabet , final , text , key, file , 94)
    elif choice == "2": decryption(alphabet , final , text , key, file , 94)
    elif choice == "3": encryption(short , final , text , key, file , 26)
    elif choice == "4": decryption(short , final , text , key, file , 26)
    else:
        quit()

    #This function tells the user the diffrence between the alphabets.
    #I put this in a function too make the main function 'cleaner' and easier for me to write code onto.
    def text_output_main():
        print("Python does not accept every character which the computer can handle.")
        sleep(1)
        print("Infact python only allows 96 characters to be inputted.")
        sleep(1)
        print("The diffrence between the this programs 2 alphabets is that the extended alpahebt is 94 characters long ")
        sleep(1)
        print("The 2 characters it does not accept are the 2 sex symbols ")
        sleep(1)
        print("The normal alphabet is the lower case english 26 letter alphabet. ")
        sleep(1)

#Contious loop  
while True:
    #Pauses program for 1 second
    sleep(1)
    main()
