path = 'days.txt'

#open the file using open method and this method require two parameters path and mode
myFile = open(path,'r')

#read method read the whole method in defualt or we can pass number of charchters it need to be read
print(myFile.read())

#read only one line 
print(myFile.readline())

#read the whole file and out put dictionary 
print(myFile.readlines())

file = open('read.txt','r')
data = file.readline() 
print(data)


list = file.readlines(20)
print(list)

#===================================================
#write to the file defualtly overrideif there is any txt
file_input = open('read.txt','w')
file_input.write('Write Using Python')
print(file.read())

#apend to txt in the end of the file
inputFile = open('read.txt','a')
file_input.write('This line is append to this txt')

#call the garbage colletor to object
file_input.close()
inputFile.close()