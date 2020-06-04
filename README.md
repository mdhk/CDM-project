## Introduction

This repository contains several notebooks that were used for the project for the course Computational Dialog Modelling.
It also contains several figures that were used in the report, and/or referred to from the report.

## Code

[```main.ipynb```](https://github.com/mdhk/CDM-project/blob/master/main.ipynb) includes code to extract the data from the CHILDES corpus, 
functions to calculate several turn-based metrics, 
and code to generate recurrence matrices and to compute recurrence rates.
Additional measures can be found in [```main_additional_measures.ipynb```](https://github.com/mdhk/CDM-project/blob/master/main_additional_measures.ipynb).
Both of these notebooks employ several helper functions located in the [```tools```](https://github.com/mdhk/CDM-project/tree/master/tools) folder.

Code for semantic alignment can be found in notebook [```semantic_recurrence.ipynb```](https://github.com/mdhk/CDM-project/blob/master/semantic_recurrence.ipynb).
Functions used to prepare all corpus data for GLM fits can be found in another notebook, titled
[```GLM_data.ipynb```](https://github.com/mdhk/CDM-project/blob/master/GLM_data.ipynb).

R code for the linear regressions testing change in complexity over time, and for the GLM testing effects of alignment on complexity is in [```linear_regressions.r```](https://github.com/mdhk/CDM-project/blob/master/linear_regressions.r) and [```glm_models.r```](https://github.com/mdhk/CDM-project/blob/master/glm_models.r), respectively.

## Figures
Generated plots can be found in the folder  [```figures```](https://github.com/mdhk/CDM-project/tree/master/figures).

## Authors

- Marianne de Heer Kloots
- Kayleigh Douglas
- Ard Snijders
