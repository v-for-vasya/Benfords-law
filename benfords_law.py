from __future__ import division
from scipy.stats import ks_2samp
import string
import urllib2
import math
import matplotlib.pyplot as plt
import numpy as np

"""
ticker - the stock ticker capitalised
fin_statement - a type of financial statement that can be: cf=cash flow, bs=balance sheet, is=income statement
"""

def benford_compare(ticker,fin_statement):

  url = urllib2.urlopen("http://financials.morningstar.com/ajax/ReportProcess4CSV.html?t="+ticker+"&reportType="+fin_statement+"&period=12&dataType=A&order=desc&columnYear=10&number=3")
  name='stock_'+ticker+'.csv'

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
  n=len(benford)

  def benford_law(d):
    return math.log(1+(1/d),10)

  experiment=[]
  model=[]
  for i in range(1,10):
    print i,  'probability', round(benford.count(i)/n*100,2) , 'benford says', benford_law(i)*100
    experiment.append(benford.count(i)/n*100)
    model.append(benford_law(i)*100)

  x = range(1,10)
  plt.plot(x,experiment)
  plt.plot(x,model)
  plt.legend([ticker,  'Benford\'s law '], loc='upper right')
  txt='Kolmogorov D statistic: ',round(ks_2samp(experiment,model)[0],2), 'p-value:',round(ks_2samp(experiment,model)[1],3)
  plt.title(txt)
  plt.show()

benford_compare("AMD","cf") #search for the stock ticker AMD and go through its cash flow statement (cf) to compare to Benford's distribution

#Ks_2sampResult(D-statistic=0.0, pvalue=1.0) Most likely derived from the same distribution with minimal difference
#Ks_2sampResult(D-statistic=1.0, pvalue=0.001) clearly different and most likely do not follow Benford's law implying manipulation
