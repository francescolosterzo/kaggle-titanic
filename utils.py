## Here write useful functions to make the Notebook cleaner
import socket

def getDataPath():
    """
    returns the path to the data files based on the device you are working on
    """
    if (socket.gethostname()=='DESKTOP-AK02NII'): return '/home/francesco/Projects/data/kaggle-titanic'
    if (socket.gethostname()=='Francescos-MBP'): return '/Users/francesco/PersonalProjects/data/kaggle-titanic'
    return ''

def replaceElementInList(oldElement, newElement, List):
    """
    replaces all the occurrences of oldElement in List with newElement
    Return value: the new list
    """
    
    newList = List.copy()
    
    for n, i in enumerate(newList):
        if i==oldElement:
            newList[n] = newElement
    
    return newList