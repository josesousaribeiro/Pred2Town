# Pred2Town - Prediction of Homicides in Urban Centers: A Machine Learning Approach

Authors:

José Ribeiro - site: https://sites.google.com/view/jose-sousa-ribeiro

Lair Meneses - site: http://lattes.cnpq.br/5112686666929641

Denis Costa - site: http://lattes.cnpq.br/8063713696787401

Wando Miranda - site: http://lattes.cnpq.br/6925939035060395

Ronnie Alves (Orientador) - site: https://sites.google.com/site/alvesrco/

# Search summary

Relevant research has been highlighted in the computing community to develop machine learning models capable of predicting the occurrence of crimes, analyzing contexts of crimes, extracting profiles of individuals linked to crime, and analyzing crimes over time. However, models capable of predicting specific crimes, such as homicide, are not commonly found in the current literature. This research presents a machine learning model to predict homicide crimes, using a dataset that uses generic data (without study location dependencies) based on incident report records for 34 different types of crimes, along with time and space data from crime reports. Experimentally, data from the city of Belém - Pará, Brazil was used. These data were transformed to make the problem generic, enabling the replication of this model to other locations. In the research, analyses were performed with simple and robust algorithms on the created dataset. With this, statistical tests were performed with 11 different classification methods and the results are related to the prediction’s occurrence and non-occurrence of homicide crimes in the month subsequent to the occurrence of other registered crimes, with 76% assertiveness for both classes of the problem, using Random Forest. Results are considered as a baseline for the proposed problem.

# Important

The disclosure of statistical information present in this study is duly authorized by the Secretariat of Public Security and Social Defense of the State of Pará, Brazil. Document available at: 

[Autorization](https://github.com/josesousaribeiro/Pred2Town/tree/master/Autorization%20of%20Data's%20Utilization)

# The procedures performed in this research can be divided into 5 parts:

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

## 2 - Pre-processing of tabular data.

The pre-processing performed in the tabular database based on time and space, defended by this research are listed below:
- Selection of records for urbanized neighborhoods (removal of records for small islands).
- Normalization application (min-max) of quantitative attributes;
- Application of transforming categorical data to ordinals (neighborhood);
- Creation of a binary Class attribute based on the number of homicides that occurred in the following month equal to zero (non-homicide) and greater than zero (homicide occurrence);

The data is in: [dataset](dataset_pred2town_bel.csv)

The translation of data labels is in: [Portuguese to English](https://github.com/josesousaribeiro/Pred2Town/blob/master/Translation%20of%20clean%20data%20labels).

## 3 - Tunning process.

Table 2 presents all the best parameters found from the execution of the grid search process based on cross-validation with folds size equal to 7, and the metric used to measure the performance of each fold execution was the Area Under ROC – AUC. It was decided to use cross-validation at this stage of creation to identify the most stable machine learning models in the face of data as input.


![alt text](https://github.com/josesousaribeiro/Pred2Town/blob/master/Figures%20and%20Tables/Table%202%20-%20Tunning.png)

## 4 - Measurement of performances and statistical analysis.

The tests performed with the 11 algorithms were divided into two moments:

A) Performance Analysis: Comparison of performances based on Accuracy - ACC and Confusion Matrices;

B) Statistical Analysis: based on the Friedman test and score AUC.

All statistical analyzes of the 11 algorithms were performed using the Spyder 4.0.1 development environment through the python script developed by the authors:

[Notebook_Pred2Town_XAI_1.1](Notebook_Pred2Town_XAI_v1.1.ipynb)

## 5 - Visualization of RF results.

In order to present the performance of the RF algorithm in a contextualized way with the space of the study city, in Figure 1, a visualization layer created in the model's output is presented, which distributes each tested instance according to the neighborhood it belongs to. In this way, it is possible to have an understanding of which are the neighborhoods that the algorithm hits the most and in which it misses the most. Note that even without an algorithm receiving the neighborhood attribute as data entry, it manages to learn the patterns of the occurrence of crimes and thus can predict the occurrence of homicide.

![alt text](https://github.com/josesousaribeiro/Pred2Town/blob/master/Figures%20and%20Tables/Figura%203%20-%20Map.png)

Figure 1 - Map with the results of the Random Forest algorithm.


## References

[All references of research](References).




