
# coding: utf-8

# In[1]:

import numpy as np
import csv
from scipy import signal
import matplotlib.pyplot as plt
data = np.genfromtxt('data.csv', delimiter=",")


# In[4]:

def time_domain_calc(sdata):
    duration = sdata[-1,1] - sdata[0,1]

    avnn = np.mean(sdata[0:,2])
    sdnn = np.std(sdata[0:,2])
    avhr = 60/(avnn/1000)
    sample_size = sdata.shape[0]
    ssd = []
    for row in range(sample_size-1):
        ssd.append(abs(sdata[row+1,2] - sdata[row,2])**2)
    rmssd = np.sqrt(sum(ssd)/(sample_size-1))
    rmssd_norm = rmssd/avnn
    
    return [duration, avhr, avnn, sdnn, rmssd, rmssd_norm]


# In[5]:

subjects = np.unique(data[:, 0])
print("Total subjects found in data:", len(subjects))

rfile = open('results.csv', 'w', newline='')
writer = csv.writer(rfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

for subject in subjects:    
    s = np.array(data[data[:,0] == subject])
    ss = s[s[:,3]==1]
    phase = "Stressed"
    print("Subject", subject, phase)
    result = time_domain_calc(ss)
    writer.writerow([subject, phase, ss.shape[0]] + result)
    
    sr = s[s[:,3]==3]
    # print(sr.shape)
    phase = "Relaxed"
    print("Subject", subject, phase)
    result = time_domain_calc(sr)
    writer.writerow([subject, phase, sr.shape[0]] + result)
    

rfile.close()


# In[ ]:



