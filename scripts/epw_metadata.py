from pvlib.iotools import epw
import pandas as pd

def get_epw_metadata(epw_file: str):
    """
    Extract metadata from an EnergyPlus Weather (EPW) file.
    
    Parameters
    ----------
    epw_file : str
        Path to EPW file.
        
    Returns
    -------
    metadata : dict
        Dictionary containing metadata.
    """
    metadata = epw.read_epw(epw_file).metadata
    return metadata

epw_file = "" # path to EPW file
metadata = get_epw_metadata(epw_file)
print(metadata.head())