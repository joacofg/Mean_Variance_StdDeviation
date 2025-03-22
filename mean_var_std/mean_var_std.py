import numpy as np

def calculate(list_of_nums):
    if len(list_of_nums) != 9:
        raise ValueError("List must contain nine numbers.")
        
    # Convert to 3x3 numpy array
    arr = np.array(list_of_nums).reshape(3, 3)
    
    calculations = {
        'mean': [list(arr.mean(axis=0)), list(arr.mean(axis=1)), float(arr.mean())],
        'variance': [list(arr.var(axis=0)), list(arr.var(axis=1)), float(arr.var())],
        'standard deviation': [list(arr.std(axis=0)), list(arr.std(axis=1)), float(arr.std())],
        'max': [list(arr.max(axis=0)), list(arr.max(axis=1)), float(arr.max())],
        'min': [list(arr.min(axis=0)), list(arr.min(axis=1)), float(arr.min())],
        'sum': [list(arr.sum(axis=0)), list(arr.sum(axis=1)), float(arr.sum())]
    }
    
    return calculations