import matplotlib.pyplot as plt
from typing import Sequence
import matplotlib
import pandas as pd
import numpy

#get data
ds = pd.read_csv ('dataset.csv', usecols=[0,1])
print(ds)

def construct_histogram(X, n_split):
   res, bins = numpy.histogram(X, n_split**2)
   return res
    
            
def dp_histogram(histo, epsilon):
    new_histo = numpy.array(histo)
    new_hist = [0] * len(histo)
    for i in range(len(new_histo)):
        num = numpy.random.laplace(0, 1/epsilon)
        new_hist[i] = new_histo[i] + num
    new_hist = numpy.floor(new_hist)
    return (new_hist)

def post_process(noisy_histo):
    # remove negatives
    for i in range(len(noisy_histo)):
        if (noisy_histo[i] < 0):
            noisy_histo[i] = 0
    # probabilities
    for i in range(len(noisy_histo)):
        noisy_histo[i] =  noisy_histo[i]/1000
    return noisy_histo

def visualize_2d(X, filename, y=None):

 fig, ax = plt.subplots()

 ax.scatter(X[:, 0], X[:, 1], cmap=plt.get_cmap('jet'))
 ax.set_xlabel(r'$x_1$', fontsize=15)
 ax.set_ylabel(r'$x_2$', fontsize=15)
 plt.tight_layout(pad=0.1)
 plt.savefig(filename)


hist = construct_histogram(ds,16)
print(hist)
noisy_histo = dp_histogram(hist, 1)
print(noisy_histo)
post_histo = post_process(noisy_histo)
print(post_histo)
visualize_2d(post_histo, 'testhist.png')