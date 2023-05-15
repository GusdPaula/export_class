class NewExport(pandas.core.frame.DataFrame)
 |  NewExport(path)
 |  
 |  New Export Class to change the header
 |  
 |  Inheritance
 |  -----------
 |  pd.Dataframe : Pandas class that will be used and changed
 |  
 |  Attributes
 |  ----------
 |  path_ : str
 |      The file path.
 |  
 |  Methods
 |  -------
 |  pd.read_excel: Dataframe
 |      This will return a pandas DataFrame to be changed    
 |  
 |  Method resolution order:
 |      NewExport
 |      pandas.core.frame.DataFrame
 |      pandas.core.generic.NDFrame
 |      pandas.core.base.PandasObject
 |      pandas.core.accessor.DirNamesMixin
 |      pandas.core.indexing.IndexingMixin
 |      pandas.core.arraylike.OpsMixin
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, path) -> None
 |      Parameters:
 |      -----------
 |      path: str
 |          The file path to be read in pd.read_excel()
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(cls, path)
 |      Parameters:
 |      -----------
 |
 |      cls: class
 |          The pandas Dataframe class.
 |
 |      path: str
 |          The file path to be read in pd.read_excel()
 |
 |  ----------------------------------------------------------------------