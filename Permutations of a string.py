## Program to return all the permutations of a string

import numpy, math

#### Function

def returnperm(string):
    '''
    function to return permutations of a string
    calls itself recursively, untill the string length becomes 2
    '''
    # retlist is a list of strings to be returned
    retlist = []
    
    #find length of string
    slen = len(string)
    
    #convert string to list of characters
    slist = list(string)
    
    #take each element as first element, and create a new string
    
    #counter to fill the first element
    counter1 = 0
    
    #used character list: to avoid repetitions
    usedchar = []
    
    #loop over length of string, to pick the first element
    for kk in range(slen):
        # newstring is the shuffled string, initialize it to an empty list
        newstring = []
        
        #first element is fc
        fc = slist[counter1]
        #print fc, usedchar
        
        if ((kk == 0) or (fc not in usedchar)):
            
           #this is appended to used char as well
            usedchar.append(fc)
            
            #this is appended to the newstring
            newstring.append(fc)
            
            #remstring is list of all other characters, except fc        
            if (kk == 0):
                remstring = slist[1:]
            else:
                remstring = [x for x in slist if x != fc]
 
            # if len of remstring =1, this is the last character, hence a shuffled string can be formed
            if (len(remstring) == 1):
                shufstring = ''.join(newstring+remstring)
                #add this shuffled string to return list
                retlist.append(shufstring)

            else:
            # len of remstring is not 1, call the function recursively, to return a list of permutations
                newlist = returnperm(remstring)
                #create shuffled strings from each of the permutations of this partial string
                for ii in newlist:
                    shufstring = fc+ ii
                    retlist.append(shufstring)

        #update counter to fill choose the next element as the first element in the string
        counter1 += 1
    
    return (retlist)   


#### Input
string = 'aav'

print 'length of string is', len(string)

permutations = returnperm(string)

print 'number of permutations are', len(permutations)

print permutations
