## Here write useful functions to make the Notebook cleaner
import socket

def getDataPath():
    if (socket.gethostname()=='DESKTOP-AK02NII'): return '/home/francesco/Projects/data/kaggle-titanic'
    return ''