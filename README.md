# Data-Analysis-for-Patient-Safety

Introduction
The aim of this research is to evaluate the quality and level of safety of patients in Greek hospitals. It examines the perception that patients have regarding their safety, as well as the opinions of the staff regarding the safety provided by the hospital.

Research Methodology
To conduct the research, questionnaires were initially distributed to the personnel of hospitals in the Attica region and to their patients. Two different questionnaires were used, the PMOS-30 for patients and the HSOPSC for hospital staff. Both of these questionnaires are widely used for assessing the safety culture of hospitals and produce valid results. The HSOPC questionnaires were sent to hospital staff in Google Forms format via email. The PMOS-30 questionnaires were given to patients in printed form for completion.

After gathering a satisfactory amount of data from both questionnaires, statistical analysis of the results was conducted to draw conclusions regarding the opinions of patients and staff regarding the safety culture of the hospital. The conclusions take into account the opinions of both patients and staff collectively. Finally, the personal and demographic data of the participants are analyzed in relation to their scores on the questions in order to determine which groups of participants have a positive or negative opinion about the safety of hospitals.

Method of Statistical Data Analysis

After collecting the samples, the questionnaires were checked for adequacy in responses, and 24 questionnaires from the HSOPSC and 38 from the PMOS-30 were excluded. Subsequently, the responses from the PMOS-30 questionnaire were digitized and transferred into an Excel format.

Statistical analysis of the data was conducted using the open-source Jupyter Notebook application in Python 3.9 programming language. Python libraries such as pandas and matplotlib were also utilized.

At the beginning of the analysis, the samples consisted of 486 responses from the HSOPSC questionnaires and 518 responses from the PMOS-30 questionnaires.

Initially, the sample was analyzed according to demographic and professional characteristics. Box plots and histograms, along with result tables, were used to describe the sample profile as accurately as possible.

Next, the questions were categorized into the parameters described above. For each parameter, internal consistency was initially checked using Cronbach's alpha. After confirming that all parameters had internal consistency, an analysis of the results was conducted for each parameter.

In the analysis of the results, categorical variables are presented as absolute and relative frequencies, while quantitative variables are presented as mean, standard deviation, and median. Normality plots were used to check the normal distribution of quantitative variables. To investigate the relationship between a quantitative variable and a dichotomous variable, the t-test (Student's test) was used, while analysis of variance (ANOVA) was used to investigate the relationship between a quantitative variable and a categorical variable with more than two categories.

For investigating the relationship between two quantitative variables following a normal distribution, the Pearson correlation coefficient was used. For investigating the relationship between a categorical variable and an ordinal variable, the chi-square test was used. In cases where the dependent variable was a quantitative variable following a normal distribution and statistically significant independent variables (>2) emerged at the 0.2 level in the bivariate analysis, multiple linear regression was applied.

For the elements of the questionnaire with positively worded statements regarding safety, responses of "Agree" and "Strongly Agree" are considered positive, while for the elements with negatively worded statements regarding safety, responses of "Disagree" and "Strongly Disagree" are considered positive.

The percentage of positive responses for each parameter is calculated using the formula: (number of positive responses / total number of responses) * 100%.
