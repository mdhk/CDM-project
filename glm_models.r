library(readr)
library(modEvA)
library(sjPlot)

adam_measures <- read_csv('data/measures_csv/adam-measures-with-d-2.csv')
sarah_measures <- read_csv('data/measures_csv/sarah-measures-with-d-2.csv')

adam_glm <- glm(CHI_CP ~ Semantic*Age + PosBi*Age + LexUni*Age + ADT_CP*Age,
                data=adam_measures)
adam_dsq <- Dsquared(model = adam_glm, adjust = TRUE)
summary(adam_glm)
print(paste('adjusted D^2:', adam_dsq))


sarah_glm <- glm(CHI_CP ~ Semantic*Age + PosBi*Age + LexUni*Age + ADT_CP*Age,
                 data=sarah_measures)
sarah_dsq <- Dsquared(model = sarah_glm, adjust = TRUE)
summary(sarah_glm)
print(paste('adjusted D^2:', sarah_dsq))

# plot interaction effects
# Age:Adt_Complexity (Adam)
plot_model(adam_glm, type='eff', terms=c('ADT_CP', 'Age'))
# Age:PosBi_Recurrence (Adam)
plot_model(adam_glm, type='eff', terms=c('PosBi', 'Age'))

# Age:Adt_Complexity (Sarah)
plot_model(sarah_glm, type='eff', terms=c('ADT_CP', 'Age'))
