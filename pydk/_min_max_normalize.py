
def _min_max_normalize(arr, scaler=1):
    
    """Min-max normalize and optionally scale entire result."""
    
    array_min =  arr.min()
    array_max = arr.max()
    
    return ((arr - array_min) / (array_max - array_min)) * scaler