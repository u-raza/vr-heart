
# coding: utf-8

# In[30]:

import numpy as np
import csv
from scipy import signal
import matplotlib.pyplot as plt
data = np.genfromtxt('data.csv', delimiter=",")


# In[31]:

def time_domain_calc(sdata):
    duration = sdata[-1,1] - sdata[0,1]
    sample_size = sdata.shape[0]
    fs = duration/sample_size
    
    f, Pxx = signal.periodogram(sdata[0:,2], fs)
    plt.plot(f, Pxx)
    axes = plt.gca()
    axes.set_xlim([0,0.6])
    axes.set_ylim([0,50000])
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()
    
    return [f, Pxx]


# In[32]:

subjects = np.unique(data[:, 0])
print("Total subjects found in data:", len(subjects))

rfile = open('results_spectrum.csv', 'w', newline='')
writer = csv.writer(rfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

for subject in subjects:    
    s = np.array(data[data[:,0] == subject])
    ss = s[s[:,3]==1]
    phase = "Stressed"
    print("Subject", subject, phase)
    result = time_domain_calc(ss)
    writer.writerow([subject, phase, ss.shape[0]] + result)
    
    sr = s[s[:,3]==3]
    phase = "Relaxed"
    print("Subject", subject, phase)
    result = time_domain_calc(sr)
    writer.writerow([subject, phase, sr.shape[0]] + result)
    

rfile.close()


# In[ ]:



