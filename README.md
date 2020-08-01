# Pred2Town

Authors:

José Ribeiro - site: https://sites.google.com/view/jose-sousa-ribeiro

Lair Meneses - site: http://lattes.cnpq.br/5112686666929641

Denis Costa - site: http://lattes.cnpq.br/8063713696787401

Wando Miranda - site: http://lattes.cnpq.br/6925939035060395

Ronnie Alves (Orientador) - site: https://sites.google.com/site/alvesrco/

# Search summary

Relevant research has been standing out in the computing community aiming to develop computational models capable of predicting occurrence of crimes, analyzing contexts of crimes, extracting profiles of individuals linked to crimes, and analyzing crimes according to time. This, due to the social impact and also the  complex origin of the data, thus showing itself as an interesting computational challenge. This research presents a computational model for the prediction of homicide crimes, based on tabular data of crimes registered in the city of Belém - Pará, Brazil. Statistical tests were performed with 8 different classification methods, both Random Forest, Logistic Regression, and Neural Network presented best results, AUC ~ 0.8. Results considered as a baseline for the proposed problem.

# The procedures performed in this research can be divided into 4 parts:

## 1 - Pre-processing of raw data from police reports.

In order not to expose individuals' personal information, we do not provide information here from the raw database of occurrence reports in the city of study. Due to the high dimensionality of the data, such processing was carried out using an SQL database and specific script developed by the authors.
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

The result of the cleaning mentioned above is the dataset: 
 - Pred2Town_Orange_Pre-process_to_Orange_Pre-process.csv

## 2 - Pre-processing of temporal tabular data.

The pre-processing performed in the Tabular database based on time and space, defended by this research are listed below:
- Selection of records for urbanized neighborhoods (removal of records for small islands).
- Normalization application (min-max) of quantitative attributes;
- Application of transforming categorical data to ordinals (neighborhood);
- Creation of a binary Class attribute based on the number of homicides that occurred in the following month equal to zero (non-homicide) and greater than zero (homicide occurrence);
- The processes mentioned above were performed in the Orange Dataming project file: Pred2Town_Orange_Pre-process.ows (Orange Tool: https://orange.biolab.si/)

The result of the database transformation and cleaning is the file: 
- Pred2Town_Orange_Pre-processed_by_Orange_bin.csv

## 3 - Measurement of performances;

The performance measures of the 8 algorithms analyzed in this study are available in the Orange Datamining project file: 
- Pred2Town_Performances.ows (Orange Tool: https://orange.biolab.si/)

## 4 - Statistical analysis;
All statistical analyzes of the 8 algorithms were performed using the Spider 4.0.1 development environment through the python script developed by the authors:
- Pred2Town_Statistic_Analisys.py

This, using as input the data generated in the previous step regarding the executions of 100 cross-validation tests: 
- Pred2Town_Output_to_Statistic_Analisys.csv


