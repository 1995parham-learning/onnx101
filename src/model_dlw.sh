#!/usr/bin/env bash

# download the random forest (for baly) model from s3
# mc cp smapp-teh1/nostra-baly/1/rf_1_25_85_0_0_0_0.pkl model.pkl

# download the neural network (for gilan) model from s3
mkdir nn-model
mc cp -r smapp-teh1/nostradamus/gilan_16_13_10_7_haversine_day_type_recent_tf/0001/ nn-model
