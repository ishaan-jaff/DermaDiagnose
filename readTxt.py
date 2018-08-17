#import os
# This creates,writes to and reads txt files
#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# Did not use any code from here 
# only understood/learned how the open(), and .write functions work
# I implemented them mysellf
def readResults(name):
    file =  open('/Users/ishaanjaffer/Desktop/dermaDiag/%s.txt'% name, 'r')  
    return (file.read())
    
#readResults('check10')

def createFile(name,values):
    list = ["Disease","Erythema","Scaling","Itching","Koebner Phenomenon","Polygonal Papules","Oral and Mucosal","Knee and Elbow","Scalp","Family history","Age"]
    f= open("/Users/ishaanjaffer/Desktop/dermaDiag/%s.txt"%name,"w+")
    f.write("READING"+"\r")
    
    for element in range(len(list)):
        if element == 5:
            f.write(list[element] + ":" + str(values[element])+','+' '+' '+'\r')
        if not element == len(list)-1:
            
            f.write(list[element] + ":"+str(values[element])+','+' ')
        else:
            f.write(list[element] + ":"+str(values[element])+','"\r")
            
    f.close() 
#createFile("name",[0,1,3,2,1,2,1,1])
    
def addData(name,values):
    f= open("/Users/ishaanjaffer/Desktop/dermaDiag/%s.txt"%name,"r")
    s = f.readlines()
    
    with open('/Users/ishaanjaffer/Desktop/dermaDiag/%s.txt'% name, "a") as myfile:
        myfile.write("READING" + "\r")

    
    
        list = ["Disease","Erythema","Scaling","Itching","Koebner Phenomenon","Polygonal Papules","Oral and Mucosal","Knee and Elbow","Scalp","Family history","Age"]
        
        for element in range(len(list)):
            value  = str(values[element])
            if element == 5:
                myfile.write(list[element] + ":" + value +','+'\r')
                
            
            if not element == len(list)-1:
            
                myfile.write(list[element] + ":" + value+','+' '+' ')
            else:
                myfile.write(list[element] + ":" + value+','+' '+'\r'+'\r')
                
    
#addData("name", [50,0,0,2,1,2,1,1])
        
     
    