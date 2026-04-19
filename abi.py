Message = input("WRITE A MESSAGE: ")
file = open("message.txt", "w")
file.write(Message)
file.close()    
file = open("message.txt", "r")
print(file.read())      
file.close()
file = open("message.txt", "a")       
message = input("WRITE A MESSAGE: ")
file.write("\n" + message)

try:
    file = open("message.txt", "r") 
except:
    print("FILE NOT FOUND")