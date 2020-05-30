library(readr)

complexity_measures_sarah <- read_csv('data/measures_csv/sarah_measures_child_adult.csv')
complexity_measures_adam <- read_csv('data/measures_csv/adam_measures_child_adult.csv')

# sarah child
mwt_chi <- lm(MWT_CHI ~ ages, data=complexity_measures_sarah)
summary(mwt_chi)
mct_chi <- lm(MCT_CHI ~ ages, data=complexity_measures_sarah)
summary(mct_chi)
mtl_chi <- lm(MTL_CHI ~ ages, data=complexity_measures_sarah)
summary(mtl_chi)
muw_chi <- lm(MUW_CHI ~ ages, data=complexity_measures_sarah)
summary(muw_chi)
mwl_chi <- lm(MWL_CHI ~ ages, data=complexity_measures_sarah)
summary(mwl_chi)
mul_chi <- lm(MUL_CHI ~ ages, data=complexity_measures_sarah)
summary(mul_chi)

# sarah adult
mwt_adt <- lm(MWT_ADT ~ ages, data=complexity_measures_sarah)
summary(mwt_adt)
mct_adt <- lm(MCT_ADT ~ ages, data=complexity_measures_sarah)
summary(mct_adt)
mtl_adt <- lm(MTL_ADT ~ ages, data=complexity_measures_sarah)
summary(mtl_adt)
muw_adt <- lm(MUW_ADT ~ ages, data=complexity_measures_sarah)
summary(muw_adt)
mwl_adt <- lm(MWL_ADT ~ ages, data=complexity_measures_sarah)
summary(mwl_adt)
mul_adt <- lm(MUL_ADT ~ ages, data=complexity_measures_sarah)
summary(mul_adt)

# adam child
mwt_chi <- lm(MWT_CHI ~ ages, data=complexity_measures_adam)
summary(mwt_chi)
mct_chi <- lm(MCT_CHI ~ ages, data=complexity_measures_adam)
summary(mct_chi)
mtl_chi <- lm(MTL_CHI ~ ages, data=complexity_measures_adam)
summary(mtl_chi)
muw_chi <- lm(MUW_CHI ~ ages, data=complexity_measures_adam)
summary(muw_chi)
mwl_chi <- lm(MWL_CHI ~ ages, data=complexity_measures_adam)
summary(mwl_chi)
mul_chi <- lm(MUL_CHI ~ ages, data=complexity_measures_adam)
summary(mul_chi)

# adam adult
mwt_adt <- lm(MWT_ADT ~ ages, data=complexity_measures_adam)
summary(mwt_adt)
mct_adt <- lm(MCT_ADT ~ ages, data=complexity_measures_adam)
summary(mct_adt)
mtl_adt <- lm(MTL_ADT ~ ages, data=complexity_measures_adam)
summary(mtl_adt)
muw_adt <- lm(MUW_ADT ~ ages, data=complexity_measures_adam)
summary(muw_adt)
mwl_adt <- lm(MWL_ADT ~ ages, data=complexity_measures_adam)
summary(mwl_adt)
mul_adt <- lm(MUL_ADT ~ ages, data=complexity_measures_adam)
summary(mul_adt)
