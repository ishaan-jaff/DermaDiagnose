import numpy as np
dataset = np.loadtxt("/Users/ishaanjaffer/Downloads/DataSet.csv",delimiter=",")
#https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
# Understood how a multiclass classifier works 
# Only thing taken from website was the formula for Gaussian Probability
#I wrote the ML algorithm, and all the code here 

# Dataset taken from http://archive.ics.uci.edu/ml/machine-learning-databases/dermatology/

import random
import math 

def seperateClass(datset):
    classes = dict()
    #target = getTarget(dataset)
    
    for x in range(len(dataset)):
        values = dataset[x]
        values = values[:10]
        
        
     
        target = int(dataset[x][10])
        
        if target not in classes:
           classes[target] = []
        classes[target].append(values)
    return (classes)



#print(seperateClass(dataset))

def meanStandard(list):
    
    mean  = sum(list)/float(len(list))
    variance = sum([pow(x-mean,2) for x in list])/float(len(list)-1)
    sDev = math.sqrt(variance)
    return mean,sDev


#print(meanStandard([1,2,3,4,5]))

def attributeProbability(value,mean,deviation):
    if(mean==0 and value ==0):
        return 1
    if(deviation==0):
        return 0
        
    exponent = math.exp(-(math.pow(value-mean,2)/(2*math.pow(deviation,2))))
    probability = (1 / (math.sqrt(2*math.pi) * deviation)) * exponent
    return (probability)
#print(attributeProbability(3,2.66,0.1))
    

def attributeMeanS(dataset,classes):
    final = dict()
    for disease in classes:
        diseaseList = [ ]
        for attribute in range(10):
            tempList = [ ]
            for list in classes[disease]:
                tempList.append(int(list[attribute]))
            diseaseList.append(meanStandard(tempList))
        
            
        final[disease] = diseaseList
    return final
    
            
#print(attributeMeanS(dataset,seperateClass(dataset)))
        
def diseaseProb(final,input):
        prob = dict()
        for disease in final:
            prob[disease]  = 1 
            list =  final[disease]
            
            for x in range(len(list)):
                mean,deviation = list[x]
                #print(mean,deviation)
                
                
                #print(mean,deviation)
                
                prob[disease]*=attributeProbability(input[x],mean,deviation)
                
        return prob
        
#print(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),[1,1,3,0,0,0,0,0,0,17]))

def getDisease(prob):
    max = 10^-30
    name = 0
    max1 = 10^-30
    name1=0
    name2="Nothing"
    for disease in prob:
        if(prob[disease]>max):
            max = prob[disease]
            name = disease 
    prob[name] = 0
    for disease in prob:
        if(prob[disease]>max1):
            max1 = prob[disease]
            name1 = disease 
    
    
    if name ==1:
        name =  "Psoriasis"
    if name ==2:
        name = "Seboreic dermatitis"
    if name==3:
        name= "Lichen planus"
    if name==4:
        name= "Pityriasis rosea"
    if name ==5:
        name= "Chronic dermatitis"
    if name==6:
        name= "Pityriasis rubra pilaris"
    
    if name1 ==1:
        name2 =  "Psoriasis"
    if name1 ==2:
        name2 = "Seboreic dermatitis"
    if name1==3:
        name2= "Lichen planus"
    if name1==4:
        name2= "Pityriasis rosea"
    if name1 ==5:
        name2= "Chronic dermatitis"
    if name1==6:
        name2= "Pityriasis rubra pilaris"
    return (name,name2)
    #return "NONE"
    
#print(getDisease(diseaseProb(attributeMeanS(dataset,seperateClass(dataset)),[1,0,1,1,0,1,1,1,1,1])))
            


    
        
            
    
    