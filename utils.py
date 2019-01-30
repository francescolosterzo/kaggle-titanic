## Here write useful functions to make the Notebook cleaner
import socket
import numpy as np

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

def getFullParameters(fit_result, x):
    """
    get the full parameters (coefficients and errors) out of the fit result for a LogisticRegression model.
    The procedure is taken from here: https://stats.stackexchange.com/questions/89484/how-to-compute-the-standard-errors-of-a-logistic-regressions-coefficients
    Return value: arrays containing coefficients and errors (intercept in the first position)
    """
    
    # probability matrix
    probs = fit_result.predict_proba(x)

    # design matrix: add a column of 1 for the intercept
    x_design = np.hstack([np.ones((x.shape[0], 1)), x])

    V = np.diagflat(np.product(probs, axis=1))

    # covariance matrix
    cov = np.linalg.inv(np.dot(np.dot(x_design.T, V), x_design))
    
    # errors
    errors = np.sqrt(np.diag(cov))
    #errors = np.sqrt( np.abs(np.diag(cov)) )

    params = np.insert(fit_result.coef_, 0, fit_result.intercept_)
    
    return params, errors