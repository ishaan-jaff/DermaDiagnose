

from tkinter import *
from roundRectangle import *
from tkinter import filedialog
from browseFiles import *
import cv2
import numpy as np 
from PIL import Image, ImageTk
from scalingAtt import*
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
from attributeFunctions import*
from plot import*
from attObject import*
from classifier import*
from plot import*
from test import*
from readTxt import*

# basic structure taken from 15-112 notes , only arrangement of different modes and run function for canvas used 
# Image taken from #https://www.google.com/url?q=https://spectrum.ieee.org/image/Mjg4NDUxMw.jpeg&usg=AFQjCNGWKKTPHb4huLl1vLTRfuTPIEkl4Q

#Image takne from https://www.google.com/url?q=https://healthitaccelerator.com/wp-content/uploads/2017/03/AIMed-#Logo.png&usg=AFQjCNFosUmU8R8_gJPqbhoXDlLtYC3xQA

# Image taken from #https://www.google.com/url?q=https://ak1.picdn.net/shutterstock/videos/22386121/thumb/9.jpg&usg=AFQjCNEfCaBrYMgAbLf3GZGQF#EUVniLSRg
def opencvToTk(frame):
    """Convert an opencv image to a tkinter image, to display in canvas."""
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_image)
    tk_image = ImageTk.PhotoImage(image=pil_img)
    return tk_image

####################################
#helper functions 
def drawBackButton(canvas,data):
    round_rectangle(canvas,5,5,80,30,10,fill="lightblue")
    canvas.create_text(40,17,
                       text="Back", font="Arial 15")
def drawHomeButton(canvas,data):
    round_rectangle(canvas,5,35,80,60,10,fill="lightblue")
    canvas.create_text(40,47,
                       text="Home", font="Arial 15")




####################################
####################################
# init
####################################

def init(data):
    # There is only one init, not one-per-mode
    data.mode = "homeScreen"
    data.scalp = 0
    data.kneeElbow = 0
    data.family = 0
    data.oralM = 0
    data.age=""
    data.scalpText = ""
    data.kneeText=""
    data.oralText = ""
    data.ageBool = False 
    data.itch=""
    data.itchBool = False 
    data.image = ""
    data.imageBool =False
    data.scalpBox = "slateblue4"
    data.famBox = "slateblue4"
    data.oralBox = "slateblue4"
    data.kneeBox ="slateblue4"
    data.ageBox = "slateblue4"
    data.itchBox = "slateblue4"
    data.result = ""
    data.list = [data.ageBool,data.itchBool,data.scalp,data.kneeElbow,data.oralM]
    data.nameBool = 0
    data.name =""
    data.nameBox = "slateblue4"
    data.past = ""
    data.vals = ['0','0','0','0','0','0','0','0','0','0']
    data.exist=0
    data.existBool=0
    data.existName=""
    data.new =0 
    data.newName = ""
    data.newBool=0
    data.existBox ="slateblue4"
    data.newBox = "slateblue4"
    data.result1=""
    
    

####################################
# mode dispatcher
####################################

def mousePressed(event, data):
    if (data.mode == "homeScreen"): homeScreenMousePressed(event, data)
    elif (data.mode == "dataInput"):   dataInputMousePressed(event, data)
    elif (data.mode == "history"):   historyMousePressed(event, data)
   
    elif (data.mode == "results"):       resultsMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "homeScreen"): homeScreenKeyPressed(event, data)
    elif (data.mode == "dataInput"):   dataInputKeyPressed(event, data)
    elif (data.mode == "history"):   historyKeyPressed(event, data)
   
    elif (data.mode == "results"):       resultsKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "homeScreen"): homeScreenTimerFired(data)
    elif (data.mode == "dataInput"):   dataInputTimerFired(data)
    elif (data.mode == "history"):   historyTimerFired(data)
  
    elif (data.mode == "results"):       resultsTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "homeScreen"): homeScreenRedrawAll(canvas, data)
    elif (data.mode == "dataInput"):   dataInputRedrawAll(canvas, data)
    elif (data.mode == "history"):   historyRedrawAll(canvas, data)
  
    elif (data.mode == "results"):       resultsRedrawAll(canvas, data)
    

####################################
# homeScreen mode
####################################

def homeScreenMousePressed(event, data):
    
    if(event.x>=data.width/2-400 and event.x <=data.width/2-200):
        if(event.y>=600 and event.y<=650):
            data.mode = "dataInput"
    
    if(event.x>=data.width/2+200 and event.x <=data.width/2+400):
        if(event.y>=600 and event.y<=650):
            data.mode = "history"        

def homeScreenKeyPressed(event, data):
    if event.keysym=="n":
        
        data.mode = "dataInput"
    

def homeScreenTimerFired(data):
    pass
def drawButton(canvas,data):
    round_rectangle(canvas,data.width/2-400,600,data.width/2-200,650,20,fill="lightblue")
    canvas.create_text(data.width/2-300, 625,
                       text="Begin Diagnosis", font="Arial 20")
    round_rectangle(canvas,(data.width/2)+200,600,(data.width/2)+400,650,20,fill="lightblue")
    canvas.create_text(data.width/2+300, 625,
                       text="Check Patient History", font="Arial 18")

        
def homeScreenRedrawAll(canvas, data):

    canvas.create_rectangle(0,0,data.width,data.height,fill="ghostwhite")
    
    data.temp=Image.open("/Users/ishaanjaffer/Downloads/dermaD.jpg")
    
    data.photo = ImageTk.PhotoImage(image = data.temp)
    
    canvas.create_image(0,0,image=data.photo,anchor=NW)
    
    """data.temp1=Image.open("/Users/ishaanjaffer/Downloads/dermaD1.jpg")
    
    data.photo1 = ImageTk.PhotoImage(image = data.temp1)
    
    canvas.create_image(200,600,image=data.photo1,anchor=NW)"""
    
    drawButton(canvas,data)
    canvas.create_text(data.width/2, data.height-90,
                       text="Welcome to DermaDiagnose!", font="Arial 45 bold")
    canvas.create_text(data.width/2, 625,
                       text="Click 'n' or the buttons to continue", font="Arial 18 italic")
                       
    """image1 = tk.PhotoImage("/Users/ishaanjaffer/Downloads/ppp.jpeg")
    canvas.create_image(data.width/2,data.height/2,image=image1)"""

    
####################################
# history mode
####################################
def historyMousePressed(event, data):
    if (event.x>=data.width/3.5 and event.x <= data.width/2.2):
        if(event.y>=90 and event.y<=130):
            data.nameBool = 1 
            data.nameBox = "turquoise3"
    if(event.x>=5 and event.x<=80):
        if(event.y>=5 and event.y<=30):
            data.mode="homeScreen"
            data.past=""
            data.name=""
    if(event.x>=5 and event.x<=80):
        if(event.y>=35 and event.y<=60):
            data.mode="homeScreen"
            data.past=""
            data.name=""
    
def historyKeyPressed(event, data):
    if(data.nameBool==True):
        if(event.keysym=="BackSpace"):
            data.name = data.name[0:len(data.name)-1]
        elif(event.keysym=="Return"):
            data.nameBool = False
            data.nameBox = "slateblue4"
            data.past = readResults(data.name)
            #print(data.past)
        else:
            data.name+=event.keysym
    
def historyTimerFired(data):
    pass
def historyRedrawAll(canvas, data):
    drawBackButton(canvas,data)
    drawHomeButton(canvas,data)
    round_rectangle(canvas,data.width/3.5,90,data.width/2.2,130,30,fill=data.nameBox)
    canvas.create_text(data.width/6,110,text="Enter Patients First Name",font = "Arial 20")
    canvas.create_text(data.width/6,160,text="Click enter/return when done entering",font = "Arial 15")
    canvas.create_text(data.width/2.85,110,text=data.name,font = "Arial 20")
    
    
    
    round_rectangle(canvas,10,180,990,700,30,fill="lightblue")
    canvas.create_text(data.width/2,data.height/2,text=data.past,font = "Arial 20")
    
    
    
    





####################################
# results mode
####################################

def opencvToTk(data):
    """Convert an opencv image to a tkinter image, to display in canvas."""
    rgb_image = cv2.cvtColor(data.image, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_image)
    tk_image = ImageTk.PhotoImage(image=pil_img)
    return tk_image
    


def resultsMousePressed(event, data):
    if(event.x>=5 and event.x<=80):
        if(event.y>=5 and event.y<=30):
            data.mode="dataInput"
            data.existName=""
            data.existBox = "slateblue4"
            data.exist=0
            data.new=0
            data.newBox = "slateblue4"
            data.newName=""
            
    if(event.x>=5 and event.x<=80):
        if(event.y>=35 and event.y<=60):
            data.mode="homeScreen"
            data.existName=""
            data.existBox = "slateblue4"
            data.exist=0
            data.new=0
            data.newBox = "slateblue4"
            data.newName=""

            
    
    if(event.x>=data.width/2-200 and event.x<=data.width/2+200):
        if(event.y>=70 and event.y<=110):
            if data.exist==0:
                data.exist=1
                data.new=0
            else:
                data.exist=0
    
    if(event.x>=data.width/2-200 and event.x<=data.width/2+200):
        
        if(event.y>=200 and event.y<=240):
            
            if data.new==0:
                data.new =1
                data.exist=0
            else:
    
                data.exist=0
    if(event.x>=data.width/2-200 and event.x<=data.width/2+200):
        if(event.y>=120 and event.y<=160):
            data.existBool = 1
            data.existBox = "turquoise3"
    
    if(event.x>=data.width/2-200 and event.x<=data.width/2+200):
        if(event.y>=260 and event.y<=300):
            data.newBool = 1
            data.newBox = "turquoise3"
            
def resultsKeyPressed(event, data):
    if(data.existBool==True):
        if(event.keysym=="BackSpace"):
            data.existName = data.existName[0:len(data.existName)-1]
        elif(event.keysym=="Return"):
            data.existBool = False
            data.existBox = "lawngreen"
            data.vals.insert(0,data.result)
            addData(data.existName,data.vals)
            data.existName = "SAVED"

            
        else:
            data.existName+=event.keysym
    
    if(data.newBool==True):
        if(event.keysym=="BackSpace"):
            data.newName = data.newName[0:len(data.newName)-1]
        elif(event.keysym=="Return"):
            data.newBool = False
            data.newBox = "lawngreen"
            data.vals.insert(0,data.result)
            createFile(data.newName,data.vals)
            data.newName = "SAVED"
            
        else:
            data.newName+=event.keysym
def resultsTimerFired(data):
    pass

def resultsRedrawAll(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="azure")
    drawHomeButton(canvas,data)
    #cv2.imshow("Image",data.image)
    data.temp1=Image.open("/Users/ishaanjaffer/Downloads/pro.jpeg")
    
    data.photo1 = ImageTk.PhotoImage(image = data.temp1)
    
    
    
    drawBackButton(canvas,data)

    data.temp2=Image.open("/Users/ishaanjaffer/Downloads/aiMed.png")
    
    data.photo2 = ImageTk.PhotoImage(image = data.temp2)
    
    canvas.create_image(0,700,image=data.photo2,anchor=NW)
    
    drawBackButton(canvas,data)
    
    
    
    canvas.create_text(data.width/2,30,
                       text="Result:"+"This is most likely"+" "+ data.result, font="Arial 21 bold")
    canvas.create_text(data.width/2,53,
                       text="There is a chance this could be"+" "+ data.result1, font="Arial 21 bold")
    
    round_rectangle(canvas,data.width/2-200,70,data.width/2+200,110,30,fill="slateblue4")
    canvas.create_text(data.width/2,90,text="Save Results existing patient",font = "Arial 18")
    #canvas.create_text(data.width/4.25,63,text="existing patient",font = "Arial 18")
    
    round_rectangle(canvas,data.width/2-200,200,data.width/2+200,240,30,fill="slateblue4")
    canvas.create_text(data.width/2,220,text="Save Results new patient",font = "Arial 18")
    
    if(data.exist ==1):
        canvas.create_text(data.width/2-300,140,text="Enter name of patient",font = "Arial 18")
        
        canvas.create_text(data.width/2-300,160,text="Click Enter/Return when done",font = "Arial 14")
        round_rectangle(canvas,data.width/2-200,120,data.width/2+200,160,30,fill=data.existBox)
        canvas.create_text(data.width/2,140,text=data.existName,font = "Arial 18")
    elif(data.new==1):
        canvas.create_text(data.width/2-300,280,text="Enter name of patient",font = "Arial 18")
        
        canvas.create_text(data.width/2-300,300,text="Click Enter/Return when done",font = "Arial 14")
        round_rectangle(canvas,data.width/2-200,260,data.width/2+200,300,30,fill=data.newBox)
        canvas.create_text(data.width/2,280,text=data.newName,font = "Arial 18")
    canvas.create_image(0,350,image=data.photo1,anchor=NW)
    #print(data.new)


    
    

####################################
# dataInput mode
####################################



        

def inputBoxes(canvas,data):
    round_rectangle(canvas,data.width/3.5,90,data.width/2.8,130,30,fill=data.ageBox)
    canvas.create_text(data.width/5,110,text="Age",font = "Arial 20")
    
    round_rectangle(canvas,data.width/3.5,160,data.width/2.8,200,30,fill=data.itchBox)
    canvas.create_text(data.width/5.5,180,text="Amount of itching",font = "Arial 20")
    #canvas.create_text(data.width/5.5,190, text= "on a scale of 0-3",font = "Arial 20")
    #canvas.create_text(data.width/5.5,220, text="(3=severe itching" ,font = "Arial 18")
    #canvas.create_text(data.width/5.5,250, text=" 0=no itching)" ,font = "Arial 18")
    
    round_rectangle(canvas,data.width/3.5,230,data.width/2.8,270,30,fill=data.scalpBox)
    canvas.create_text(data.width/5.5,250,text="Scalp affected",font = "Arial 20")
    
    round_rectangle(canvas,data.width/3.5,300,data.width/2.8,340,30,fill=data.kneeBox)
    canvas.create_text(data.width/5.5,320,text="Knee/Elbow affected",font = "Arial 20")
    
    round_rectangle(canvas,data.width/3.5,370,data.width/2.8,410,30,fill=data.oralBox)
    canvas.create_text(data.width/5.5,390,text="Oral/mucosal",font = "Arial 20")
    
    round_rectangle(canvas,data.width/6.5,data.height/1.5,data.width/3.1,data.height/1.34,30,fill=data.famBox)
    canvas.create_text(data.width/4.25,data.height/1.43,text="Family history with",font = "Arial 18")
    canvas.create_text(data.width/4.25,data.height/1.39,text="skin disease",font = "Arial 18")
    
    
    round_rectangle(canvas,data.width/1.8,data.height-100,data.width/1.39,data.height-50,30,fill="lightblue")
    canvas.create_text(data.width/1.57,data.height-75,text="Select Image",font = "Arial 18")
    
    
    round_rectangle(canvas,data.width/11,data.height-100,data.width/3,data.height-50,30,fill="lightblue")
    canvas.create_text(data.width/4.62,data.height-85,text="Use Webcam Image",font = "Arial 18")
    canvas.create_text(data.width/4.62,data.height-65,text="Click 's' to take a picture",font = "Arial 16")
    
    


def showInput(canvas,data):
    round_rectangle(canvas,data.width/1.8,100,data.width/1.1,data.height-150,30,fill="turquoise3")
    
    canvas.create_text(data.width/3.15,110,text=data.age,font = "Arial 20")
    canvas.create_text(data.width/1.3,120,text=data.age,font = "Arial 20")
    
        
    #canvas.create_text(data.width/1.3,120,text="invalid form,enter digits", font = "Arial 20")
        
    canvas.create_text(data.width/1.7,120,text="Age",font = "Arial 20",fill = "slateblue4")
    
    canvas.create_text(data.width/1.6,180,text="Amount of Itch",font = "Arial 20",fill="slateblue4")
    
   
    canvas.create_text(data.width/1.3,180,text=data.itch,font = "Arial 20")
    canvas.create_text(data.width/3.15,180,text=data.itch,font = "Arial 20")
    
    #canvas.create_text(data.width/1.3,180,text="invalid form",font = "Arial 20")
        
    canvas.create_text(data.width/3.15,250,text=data.scalpText,font = "Arial 20")
    
    
    canvas.create_text(data.width/1.55,250,text="Scalp involvement",font = "Arial 20",fill="slateblue4")
    canvas.create_text(data.width/1.3,250,text=data.scalpText,font = "Arial 20")
    
    canvas.create_text(data.width/3.15,320,text=data.kneeText,font = "Arial 20")
    canvas.create_text(data.width/1.55,320,text="Knee involvement",font = "Arial 20",fill="slateblue4")
    canvas.create_text(data.width/1.3,320,text=data.kneeText,font = "Arial 20")
    
    canvas.create_text(data.width/3.15,390,text=data.oralText,font = "Arial 20")
    canvas.create_text(data.width/1.6,390,text="Oral Mucosal",font = "Arial 20",fill="slateblue4")
    canvas.create_text(data.width/1.615,420,text="involvement",font = "Arial 20",fill="slateblue4")
    canvas.create_text(data.width/1.3,390,text=data.oralText,font = "Arial 20")
    
    
    if(data.family == 1):
        canvas.create_text(data.width/1.52,480,text="Family history present",font = "Arial 20",fill="slateblue4")
        
        
        
        

    
    

def dataInputMousePressed(event, data):
  
    #for back button 
    if(event.x>=5 and event.x<=80):
        if(event.y>=5 and event.y<=30):
            data.mode = "homeScreen"
            data.age=""
            data.scalpText = ""
            data.kneeText=""
            data.oralText = ""
            data.family=0
            data.itch=""
            if(data.itchBool==0):
                data.itchBox = "slateblue4"
            if(data.scalp==0):
                data.scalpBox = "slateblue4"
            if (data.kneeElbow==0):
                data.kneeBox = "slateblue4"
            if(data.oralM==0):
                data.oralBox = "slateblue4"
            if(data.ageBool==0):
                data.ageBox = "slateblue4"
            data.family=0
    if(event.x>=5 and event.x<=80):
        if(event.y>=35 and event.y<=60):
            data.mode = "homeScreen"
            data.age=""
            data.scalpText = ""
            data.kneeText=""
            data.oralText = ""
            data.family=0
            data.itch=""
            if(data.itchBool==0):
                data.itchBox = "slateblue4"
            if(data.scalp==0):
                data.scalpBox = "slateblue4"
            if (data.kneeElbow==0):
                data.kneeBox = "slateblue4"
            
            data.oralBox = "slateblue4"
            if(data.ageBool==0):
                data.ageBox = "slateblue4"
            data.family=0
            
   
    
    #canvas,data.width/11,data.height-100,data.width/3,data.height-50
    if(event.x>=data.width/11 and event.x<= data.width/3):
        if(event.y>=data.height-100 and event.y<=data.height-50):
            data.mode="results"
            cap = cv2.VideoCapture(0)
            
            
            while(True):
                # Capture frame-by-frame
                ret, data.image = cap.read()
                
                
            
                
            
                # Display the resulting frame
                cv2.imshow('frame',data.image)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    cap.release()
                    cv2.destroyAllWindows()
                    dataset = np.loadtxt("/Users/ishaanjaffer/Downloads/DataSet.csv",delimiter=",")
                
                    if(showRed(data.image).redRatio()==0):# if no red at all immediately use showRed algorithm 
                        
                        
                    
                        
                        data.vals = values(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                        data.vals.insert(2,int(data.itch))
                        
                        data.vals.extend([int(data.oralText),int(data.kneeText),int(data.scalpText),int(data.family),int(data.age)])
                        
                        
                        data.result,data.result1 = getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),data.vals))
                        
                        showAttributes(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                        
                        
                    
                    elif(red(data.image).redRatio()>=100):# in the case on red detecting algorithm gives extreme value use the other red #algorithm 
                        
                        
                    
                        data.vals = values(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                        data.vals.insert(2,int(data.itch))
                        
                        data.vals.extend([int(data.oralText),int(data.kneeText),int(data.scalpText),int(data.family),int(data.age)])
                    
                        data.result,data.result1 = getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),data.vals))
                        
                        showAttributes(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                        
                    else:# use this for non extreme cases 
                        
                        
                        
                        data.vals = values(red(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                        data.vals.insert(2,int(data.itch))
                            
                        
                        
                        data.vals.extend([int(data.oralText),int(data.kneeText),int(data.scalpText),int(data.family),int(data.age)])
                        
                        data.result,data.result1 = getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),data.vals))
                        
                        
                        showAttributes(red(data.image),scaling(data.image),koebner(data.image),pap(data.image))
            
                    
                
                    
                            
                                
                    
                    #img = img
                                    #showAttributes(showRed(img),scaling(img),koebner(img),pap(img))
                                    
                    cap.release()
                            
    
   #for select image 
    if(event.x>=data.width/1.8 and event.x<= data.width/1.39):
        if(event.y>=data.height-100 and event.y<=data.height-50):
            data.mode = "results"
            data.image = cv2.imread(getPath())
            dataset = np.loadtxt("/Users/ishaanjaffer/Downloads/DataSet.csv",delimiter=",")
        
            if(showRed(data.image).redRatio()==0):# if no red at all immediately use showRed algorithm 
                
                
               
                
                data.vals = values(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                data.vals.insert(2,int(data.itch))
                
                data.vals.extend([int(data.oralText),int(data.kneeText),int(data.scalpText),int(data.family),int(data.age)])
                
                
                data.result,data.result1 = getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),data.vals))
                
                showAttributes(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                
                
            
            elif(red(data.image).redRatio()>=100):# in the case on red detecting algorithm gives extreme value use the other red #algorithm 
                
                
               
                data.vals = values(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                data.vals.insert(2,int(data.itch))
                
                data.vals.extend([int(data.oralText),int(data.kneeText),int(data.scalpText),int(data.family),int(data.age)])
            
                data.result,data.result1 = getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),data.vals))
                
                showAttributes(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                
            else:# use this for non extreme cases 
                
                
                
                data.vals = values(red(data.image),scaling(data.image),koebner(data.image),pap(data.image))
                data.vals.insert(2,int(data.itch))
                    
                   
                
                data.vals.extend([int(data.oralText),int(data.kneeText),int(data.scalpText),int(data.family),int(data.age)])
                
                data.result,data.result1 = getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),data.vals))
                
                
                showAttributes(red(data.image),scaling(data.image),koebner(data.image),pap(data.image))
    
            
   
   

    
    
   
    
    # for age 
    if (event.x>=data.width/3.5 and event.x <= data.width/2.8):
        if(event.y>=90 and event.y<=130):
            
            if(data.ageBool == 0):
                data.ageBool = 1
                data.itchBool,data.scalp,data.kneeElbow,data.oralM = 0,0,0,0
                data.ageBox = "turquoise3"
            else:
                data.ageBool = 0
                data.ageBox = "slateblue4"
    # for itch
    if(event.x>=data.width/3.5 and event.x <= data.width/2.8):
        if(event.y>=160 and event.y<=200):
            if(data.itchBool == 0):
                data.itchBool = 1
                data.ageBool,data.scalp,data.kneeElbow,data.oralM=0,0,0,0
               
                data.itchBox = "turquoise3"
            else:
                data.itchBool = 0
                data.itchBox = "slateblue4"
    
    
    #for scalp 
    if(event.x>=data.width/3.5 and event.x <=data.width/2.8):
        if(event.y>=230 and event.y<= 270):
            if(data.scalp == 0):
                data.scalp = 1
                data.ageBool,data.itchBool,data.kneeElbow,data.oralM = 0,0,0,0
                data.scalpBox = "turquoise3"
            else:
                data.scalp = 0
                data.scalpBox = "slateblue4"
                
    #for knee and elbow 
    
    
    if(event.x>=data.width/3.5 and event.x <=data.width/2.8):
        if(event.y>=300 and event.y<= 340):
            if(data.kneeElbow == 0):
                data.kneeElbow = 1
                
                data.ageBool,data.itchBool,data.scalp,data.oralM=0,0,0,0
                data.kneeBox = "turquoise3"
            else:
                data.kneeElbow = 0
                data.kneeBox = "slateblue4"
    # for oral Mucosal
    
    
    if(event.x>=data.width/3.5 and event.x <=data.width/2.8):
        if(event.y>=370 and event.y<=410):
            if data.oralM == 0:
                data.oralM = 1
                
                data.ageBool,data.itchBool,data.scalp,data.kneeElbow=0,0,0,0
                data.oralBox = "turquoise3"
            
            else:
                data.oralM = 0
                data.oralBox ="slateblue4"
                
    # for family history 
    
    if(event.x>=data.width/6.5 and event.x <=data.width/3.1):
        if(event.y>=data.height/1.5 and event.y<= data.height/1.34):
            if data.family == 0:
                data.family = 1
                data.famBox = "turquoise3"
                data.oralM=0
            else:
                data.family = 0
                data.famBox = "slateblue4"
            
    
    

def dataInputKeyPressed(event, data):
    dataset = np.loadtxt("/Users/ishaanjaffer/Downloads/DataSet.csv",delimiter=",")
    if(event.keysym=='n'):
        data.mode = "results"
        data.image = cv2.imread(getPath())
        
        if(showRed(data.image).redRatio()==0):# if no red at all immediately use showRed algorithm 
            
            showAttributes(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
            #getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),values()))
            
            
        
        elif(red(data.image).redRatio()>=100):# in the case on red detecting algorithm gives extreme value use the other red #algorithm 
            
            showAttributes(showRed(data.image),scaling(data.image),koebner(data.image),pap(data.image))
        else:# use this for non extreme cases 
            
            showAttributes(red(data.image),scaling(data.image),koebner(data.image),pap(data.image))



    if (data.ageBool==True ):
        if(event.keysym=="BackSpace"):
            data.age = data.age[0:len(data.age)-1]
        elif(event.keysym=="Return"):
            data.ageBool = False
        else:
            data.age+=event.keysym
    if(data.itchBool==True):
        if(event.keysym=="BackSpace"):
            data.itch = data.itch[0:len(data.itch)-1]
        elif(event.keysym=="Return"):
            data.itchBool = False
        else:
            data.itch+=event.keysym
    if(data.scalp==True):
        if(event.keysym=="BackSpace"):
            data.scalpText = data.scalpText[0:len(data.scalpText)-1]
        elif(event.keysym=="Return"):
            data.scalp = False
        else:
            data.scalpText+=event.keysym
    
    if(data.kneeElbow==True):
        if(event.keysym=="BackSpace"):
            data.kneeText = data.kneeText[0:len(data.kneeText)-1]
        elif(event.keysym=="Return"):
            data.kneeElbow = False
        else:
            data.kneeText+=event.keysym
    if(data.oralM==True):
        if(event.keysym=="BackSpace"):
            data.oralText = data.oralText[0:len(data.oralText)-1]
        elif(event.keysym=="Return"):
            data.oralM = False
        else:
            data.oralText+=event.keysym

    
            
            
            
            
            
            
            
            
        
        
        
                
                

                
    
        

        
        

def dataInputTimerFired(data):
    pass
    

def dataInputRedrawAll(canvas, data):
    drawHomeButton(canvas,data)
    
    if(data.itchBool==0):
        data.itchBox = "slateblue4"
    if(data.scalp==0):
        data.scalpBox = "slateblue4"
    if (data.kneeElbow==0):
        data.kneeBox = "slateblue4"
    if(data.oralM==0):
        data.oralBox = "slateblue4"
    if(data.ageBool==0):
        data.ageBox = "slateblue4"
    
        
    data.itchBool,data.scalp,data.kneeElbow,data.oralM,data.age
    canvas.create_text(data.width/2,15,text="This is the data input page",font = "Arial 25")
    canvas.create_text(data.width/2,45,text="Click on the purple rectangles to enter/type in data(press enter/return when done with a feature)",font = "Arial 19")
    canvas.create_text(data.width/2,65,text="Enter only numbers on a scale of 0-3. 3 being the highest",font = "Arial 15")
    canvas.create_text(data.width/5,data.height/1.6,text="Select box if applicable",font = "Arial 25")
    
    drawBackButton(canvas,data)
    inputBoxes(canvas,data)
    showInput(canvas,data)
   
       
    
    
    
    

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
   
        
    canvas = Canvas(root,width=data.width, height=data.height)
    
    canvas.pack()
    
        
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
   
   

    
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000,800)