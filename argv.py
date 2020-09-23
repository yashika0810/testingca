from sys import argv

nameofprogram,filename = argv
print("Name of program is", nameofprogram)
print("Name of file is", filename)


while True:
    try:
  
        fh=open(filename,'r')
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print("The name entered is wrong!! Please provide correct name")

        try_again=input("Do you want to try again!! Press Y for yes and N for no")
        if try_again=="Y":
            filename = input("Please provide the correct name this time")
        elif try_again =="N":
            break
        else:
            pass





