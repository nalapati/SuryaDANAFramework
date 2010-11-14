'''
Created on Nov 12, 2010

@author: surya
'''
from DANAExceptions.DANAException import DANAException

class PreProcessingError(DANAException):
    """ This Exception is thrown if the a dataItem
        in the repository could not be preprocessed 
        successfully
    """
   
    def __init__(self, str, preProcessResult):
        """ Contructor
        
            Keyword Arguments:
            str              -- String corresponding to the reason why 
                                preProcessing failed.
        """
        self.phase = "PPROC"
        self.str = str

    def __str__(self):
        """ String representation
        """
        return self.str