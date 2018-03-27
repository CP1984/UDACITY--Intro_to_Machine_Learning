#!/usr/bin/python


def outlierCleanerByMyself(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = (predictions - net_worths)**2
    
    cleaned_data = zip(ages, net_worths, error)
    cleaned_data.sort(key = lambda tup: tup[2])
    cleaned_data = cleaned_data[:int(len(cleaned_data) * 0.9)]
    
    return cleaned_data

