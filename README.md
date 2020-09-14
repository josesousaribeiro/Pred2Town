# Pred2Town - Prediction of Homicides in Urban Centers: A Machine Learning Approach

Authors:

José Ribeiro - site: https://sites.google.com/view/jose-sousa-ribeiro

Lair Meneses - site: http://lattes.cnpq.br/5112686666929641

Denis Costa - site: http://lattes.cnpq.br/8063713696787401

Wando Miranda - site: http://lattes.cnpq.br/6925939035060395

Ronnie Alves (Orientador) - site: https://sites.google.com/site/alvesrco/

# Search summary

Relevant research has been standing out in the computing community aiming to develop computational models capable of predicting occurrence of crimes, analyzing contexts of crimes, extracting profiles of individuals linked to crimes, and analyzing crimes according to time. This, due to the social impact and also the  complex origin of the data, thus showing itself as an interesting computational challenge. This research presents a computational model for the prediction of homicide crimes, based on tabular data of crimes registered in the city of Belém - Pará, Brazil. Statistical tests were performed with 8 different classification methods, both Random Forest, Logistic Regression, and Neural Network presented best results, AUC ~ 0.8. Results considered as a baseline for the proposed problem.

# Important

The disclosure of statistical information present in this study is duly authorized by the Secretariat of Public Security and Social Defense of the State of Pará, Brazil. Document available at: https://github.com/josesousaribeiro/Pred2Town/blob/master/Autorization%20of%20Data's%20Utilization/Authorization%20to%20use%20data%20on%20behalf%20of%20Jose%CC%81%20Ribeiro.PDF

# The procedures performed in this research can be divided into 4 parts:

Note, in order not to expose the personal information of individuals, we do not provide in this repository information a raw database of reports of occurrence reports of the city of study.

Due to issues related to information confidentiality, only tabular data, as a result of the cleaning and pre-processing processes carried out by this research, can be provided in this repository.

## 1 - Pre-processing of raw data from police reports.

The main pre-processing and data transformations carried out were:
- Exclusion of 9 sparse attributes (with unregistered data) and id;
- Exclusion of 21 attributes not directly related to the crime context;
- Exclusion of 2 attributes related to personal data of registered individuals;
- Exclusion of 2 attributes related to the location of the crime that occurred due to inconsistency;
- Exclusion of 2 attributes of crime’s georeferencing (latitude and longitude), due to inconsistency;
- Removing special characters (such as: @ # $% ˆ & * áíóúç?! ºª • §∞ ¢ £ ™ ¡);
- Consolidation of neighborhoods in the city of study;
- Exclusion of records related to occurrences in neighborhoods located on islands or in rural areas due to high inconsistency;
- Exclusion of police reports instances considered non-crimes;
- Exclusion of duplicate occurrence records (since a crime can be registered in more than one police report, in this case by different people);

## 2 - Pre-processing of temporal tabular data.

The pre-processing performed in the Tabular database based on time and space, defended by this research are listed below:
- Selection of records for urbanized neighborhoods (removal of records for small islands).
- Normalization application (min-max) of quantitative attributes;
- Application of transforming categorical data to ordinals (neighborhood);
- Creation of a binary Class attribute based on the number of homicides that occurred in the following month equal to zero (non-homicide) and greater than zero (homicide occurrence);

The processes mentioned above were performed in the Orange Dataming project(Orange Tool: https://orange.biolab.si/);
The result of the database transformation and cleaning is the file: 
- https://github.com/josesousaribeiro/Pred2Town/blob/master/Pred2Town_Orange_Pre-processed_by_Orange_bin.csv

### Description and translation of clean database labels:
https://github.com/josesousaribeiro/Pred2Town/blob/master/Translation%20of%20clean%20data%20labels

## 3 - Measurement of performances;

The performance measures of the 8 algorithms analyzed in this study are available in the Orange Datamining project file: 
- Pred2Town_Performances.ows (Orange Tool: https://orange.biolab.si/)

The result is:
- https://github.com/josesousaribeiro/Pred2Town/blob/master/Pred2Town_Output_to_Statistic_Analisys.csv.zip

## 4 - Statistical analysis;
All statistical analyzes of the 8 algorithms were performed using the Spider 4.0.1 development environment through the python script developed by the authors:
- Pred2Town_Statistic_Analisys.py
This, using as input the data generated in step 3.





