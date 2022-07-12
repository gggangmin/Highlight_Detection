import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tic

def exp_plot(exp, num_of_comparisions, xlabel, ylabel, sub=0, format='%.1f', yscale='none'):
    df = pd.read_excel('exp.xlsx', sheet_name=exp, header=1)
    print(df)
    c, a = sub*num_of_comparisions+1, chr(ord('a')+sub)
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(tic.FormatStrFormatter(format))
    xtics, marker = df.iloc[:,0:1].values.flatten(), 'o*s^+D'

    plt.xticks(np.arange(0,len(xtics)), xtics)
    for i in np.arange(0, num_of_comparisions):
        data = df.iloc[:,(c+i):(c+i+1)]           
        #print data             
        plt.plot(np.arange(0,len(xtics)), data, marker=marker[i], fillstyle='none', label=df.columns[i+1])

    yfactor = 10 if (yscale=='log') else 0.3
    if (yscale=='log'): plt.yscale(yscale)
    x1,x2,y1,y2 = plt.axis()
    '''
    plt.axis((x1,x2,y1,y2+(y2-y1)*yfactor))
    plt.xlabel(xlabel); 
    plt.ylabel(ylabel)
    plt.legend(loc='upper left', frameon=False, ncol=3)
    print(exp+a)
    plt.savefig(exp+a+'.eps', format='eps', bbox_inches='tight', dpi=500)
    plt.savefig(exp+a+'.pdf', format='pdf', bbox_inches='tight')
    '''
    #plt.show()

xlabel = ['q.k', 'q.p', '|q.keywords|', 'N']
ylabel = ['Processing Time (ms)', 'Processing Time (ms)', 'Processing Time (ms)', 'Processing Time (ms)']
format = ['%.0f', '%.0f', '%.0f', '%.0f']
yscale = ['none', 'none', 'none', 'log']
plt.rcParams['font.size'] = 11.0
num_of_comparisions = 3

for e in np.arange(0,4):    
    #exp_plot('exp'+str(e), xlabel[e], ylabel[e], sub=0, format[e])    
    exp_plot('exp'+str(e), num_of_comparisions, xlabel[e], ylabel[e], sub=0, format=format[e], yscale=yscale[e])
    #for f in np.arange(0,3):
    #    form = format[f] if e+1==4 else "%.1f"
    #    exp_plot('exp'+str(e+1), xlabel[e], ylabel[f], sub=f, format=form)
