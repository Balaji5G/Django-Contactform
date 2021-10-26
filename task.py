"""this code will ask the user to choose which opertaion they wanna perform"""
import numpy
def sample_data(values, aggregation):
    """this function will return the operation depends upon the user submission"""
    sampled_value = 0
    if aggregation == 1: 
        sampled_value = sum(values)
    elif aggregation == 2:
        sampled_value = max(values)
    elif aggregation == 3:
        sampled_value = min(values)
    elif aggregation == 4:
        sampled_value = sum(values)/len(values)
    elif aggregation == 5:
        sampled_value = numpy.std(values)
    else:
        print('not a valid selection')
    return sampled_value
if __name__ =='__main__':
    list_of_values = [2,4.0,8.0,20.0,60.0]
    aggregation_type = int(input('Choose\n1.Sum\n2.Max\n3.Min\n4.Average\n5.Standard deviation\n')) 
    result = sample_data(list_of_values, aggregation_type)
    print(result)
    