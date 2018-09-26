import numpy as np
import seaborn as sns
import matplotlib

h = np.fromfile("numeric_heights.txt", sep = ",")
w = np.fromfile("numeric_weights.txt", sep = ",")
    
def bmi(h,w):
    """Takes a height file with comma seperators and a weight file
    with comma seperators as arguements. Creates an array for both
    files and multiplies those arrays to return a distribution of
    BMI (Body Mass Index) values and a visualization."""
    
    a = np.array((w)/(h*2.54/100)**2)
    h = np.fromfile("./numeric_heights.txt", sep = ",")
    w = np.fromfile("./numeric_heights.txt", sep = ",")

    a.tofile("BMI.txt", sep = ",", format = "%s")
    
    return (a) 
    raise NotImplementedError()

sns.distplot(bmi(h, w),color = "m")
matplotlib.pyplot.show()
