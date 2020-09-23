# with open('data.txt', 'r') as file:
#     data=file.readlines()
#     for i in data:
#         word=i.split()
#         print(word)


try:
    filehandler=open("data.txt", 'a+')
    content=filehandler.read()
    data=filehandler.write("Adding one line")
    print(content)
    

except:
    print("Enter the right name")


finally:
    filehandler.close()
