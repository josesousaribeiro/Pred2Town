import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import scikit_posthocs as sp
import numpy

from scipy import stats
from sklearn.metrics import roc_auc_score
from scipy.stats import friedmanchisquare



datafile = "Pred2Town_Output_to_Statistic_Analisys.csv"
data = pd.read_csv(datafile)



models_names = [
        'Random Forest',
        'Neural Network',
        'Logistic Regression',
        'SVM', 
        'Tree',
        'Naive Bayes',
        'kNN', 
        'AdaBoost']



folds = max(data['Fold'])

a=np.zeros((folds,len(models_names)))
for i in range(0,folds):
    for j in range(0,len(models_names)):    
        y_true = np.array(data[data.Fold==i+1][models_names[j]])
        y_scores = np.array(data[data.Fold==i+1]['Class'])
        a[i][j]=roc_auc_score(y_true, y_scores)

means=[]
for i in range(0,len(models_names)):
   means.append(np.average(a[:,i]))

    


fig7, ax7 = plt.subplots()
ax7.set_title('Acumulated of 100 executions - AUC Score')
ax7.set_xticklabels(np.repeat(models_names, 1),rotation=90, fontsize=12)
ax7.boxplot(a)
ax7.scatter(range(1,len(models_names)+1),means)
plt.savefig('boxpot.png')
plt.show()


#Friedman 


print(friedmanchisquare(*a))

posthoc = sp.posthoc_nemenyi_friedman(a)
print(posthoc)

ax = sns.heatmap(posthoc, vmin=0, vmax=1, xticklabels=models_names,yticklabels=models_names,cmap="Greens",linewidths=.5,annot=True,fmt='.2f')
plt.savefig('matrix.png')
plt.show()




for i in range(0,len(models_names)):

    data2plot = a[:,i]
    density = stats.kde.gaussian_kde(data2plot)
    x = numpy.arange(0.41, 0.95, .001)
    plt.plot(x, density(x))

plt.legend(models_names)            
plt.title('Density of 100 executions - AUC Score')
plt.savefig('density.png')
plt.show()






