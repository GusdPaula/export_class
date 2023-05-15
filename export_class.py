import pandas as pd

class NewExport(pd.DataFrame):
    """New Export Class to change the header

    Inheritance
    -----------
    pd.Dataframe : Pandas class that will be used and changed

    Attributes
    ----------
    path_ : str
        The file path.

    Methods
    -------
    pd.read_excel: Dataframe
        This will return a pandas DataFrame to be changed

    """

    def __new__(cls, path):
        """
        Parameters:
        -----------

        cls: class
            The pandas Dataframe class.

        path: str
            The file path to be read in pd.read_excel()
        
        """

        # Reading the file
        instance = pd.read_excel(path)

        # Getting the header
        for row in range(len(instance)):
            possible_header = instance.iloc[row, 2]
            if possible_header == 'Type':
                break
        
        # Defining the new header
        new_header = instance.iloc[row]
        instance.columns = new_header

        # Deleting rows that were above the new header
        instance = instance[row + 1:]
        instance.reset_index(drop=True, inplace=True)
        
        return instance
    
    def __init__(self, path) -> None:
        """
        Parameters:
        -----------
        path: str
            The file path to be read in pd.read_excel()
        
        """
        super().__init__()
        self.path_ = path
