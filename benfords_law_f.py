from __future__ import division
from scipy.stats import ks_2samp
import string
import urllib2
import math
import matplotlib.pyplot as plt
import numpy as np

#start off with report type #cf, bs ,is
ticker="NVDA"
url = urllib2.urlopen("http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t="+ticker+"&reportType=is&period=12&dataType=A&order=desc&columnYear=10&number=3")
name='urldl_'+ticker+'.csv'
with open(name,'wb') as output:
  output.write(url.read())
output.close()

with open(name, 'r') as myfile:
  data = myfile.read()

repls = ('4Q',''),('3Q',''),('2Q',''),('1Q',''),(' 2018', ''),(' 2017', ''),(' 2016', ''),(' 2015', ''),(' 2014', ''),(' 2013', ''),(' 2012', ''),(' 2011', ''),(' 2010', ''),(' 2009', ''),(' 2008', ''),(' 2007', ''),(' 2006', ''),(' 2005', ''),(' 2004', ''),(' 2003', ''),(' 2002',''),(' 2001', ''),(' 2000', ''),(' 1999', ''),(' 1998', ''),(' 1997', ''),(' 1996', ''),(' 1995', '')
data=reduce(lambda a, kv: a.replace(*kv), repls, data)
digits=filter(lambda x: x.isdigit(), data)
benford=map(int,str(digits))
benford=filter(lambda a: a != 0, benford)

name2='urldl_enron.txt'
with open(name2, 'r') as myfile2:
  data2 = myfile2.read()
data2=reduce(lambda a, kv: a.replace(*kv), repls, data2)

digits2=filter(lambda x: x.isdigit(), data2)
benford2=map(int,str(digits2))
benford2=filter(lambda a: a != 0, benford2)
print benford2
n2=len(benford2)
print n2

def benford_law(d):
  return math.log(1+(1/d),10)

experiment=[]
experiment2=[]
model=[]
for i in range(1,10):
  print i,  'probability', round(benford.count(i)/n*100,2) , 'benford says', benford_law(i)*100
  experiment.append(benford.count(i)/n*100)
  experiment2.append(benford2.count(i)/n2*100)
  model.append(benford_law(i)*100)

x = range(1,10)
#plt.plot(x,experiment)
plt.bar(x,experiment2,edgecolor='black', linewidth=.4, color='#cccccc')
plt.bar(x,model, color='#25a0d8',  edgecolor='black', linewidth=.4, width=.5)
plt.legend([ 'Enron',  'Benford\'s law '], loc='upper right')
txt='Kolmogorov D statistic: ',round(ks_2samp(experiment2,model)[0],2), 'p-value:',round(ks_2samp(experiment2,model)[1],3)

plt.xticks(np.arange(1,10,1))
plt.xlabel('Digit')
plt.ylabel('Frequency of Occurence in Percent')
plt.title('Enron vs. Benford\'s Law  '+str(txt))
plt.show()
#print ks_2samp(experiment2,model), 'enron'
#print ks_2samp(experiment,model), 'intel'
#Ks_2sampResult(statistic=0.0, pvalue=1.0) same
#Ks_2sampResult(statistic=1.0, pvalue=0.001) clearly different
