from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.logging.set_verbosity(tf.logging.INFO)

COLUMNS = ["data","open","high","close","low","volume","price_change","p_change","ma5","ma10","ma20","v_ma5","v_ma10","v_ma20","turnover","price_2","price_3","price_4","price_5","price_6","pred"]

FEATURES = ["open","close","volume","price_change","p_change","ma5","ma10","ma20","turnover","price_2","price_3","price_4","price_5","price_6"]

LABEL = "pred"


def input_fn(data_set):
  feature_cols = {k: tf.constant(data_set[k].values) for k in FEATURES}
  labels = tf.constant(data_set[LABEL].values)
  return feature_cols, labels



def main(unused_argv):
  # Load datasets
  training_set = pd.read_csv("data_train.csv", skipinitialspace=True,skiprows=1, names=COLUMNS)
  test_set = pd.read_csv("data_test.csv", skipinitialspace=True,skiprows=1, names=COLUMNS)

  # Set of 10 examples for which to predict median house values
  prediction_set = pd.read_csv("data_test.csv", skipinitialspace=True,skiprows=1, names=COLUMNS)

  # Feature cols
  feature_cols = [tf.contrib.layers.real_valued_column(k) for k in FEATURES]

  # Build 2 layer fully connected DNN with 10, 10 units respectively.
  regressor = tf.contrib.learn.DNNRegressor(feature_columns=feature_cols, hidden_units=[20,20,20,20,20],model_dir="E:/python/data_model")

  # Fit
  regressor.fit(input_fn=lambda: input_fn(training_set), steps=5000)

  # Score accuracy
  ev = regressor.evaluate(input_fn=lambda: input_fn(test_set), steps=1)   
  loss_score = ev["loss"]
  print("Loss: {0:f}".format(loss_score))



  # Print out predictions
  y = regressor.predict(input_fn=lambda: input_fn(prediction_set))

  leng = len(prediction_set)
  
  # .predict() returns an iterator; convert to a list and print predictions
  predictions = list(itertools.islice(y, leng))
  print("Predictions: {}".format(str(predictions)))
  
  #plot
  plt.figure(1)
  a = prediction_set["pred"].values
  x = np.linspace(1,leng,leng)
  y = np.linspace(0,0,leng)
  
  i = 0
  correct = 0
  total = 0
  while i < leng:
    if a[i] > 1:
       total = total + 1
       if a[i] * predictions[i] > 0:
          correct = correct + 1
    i = i + 1
  print("correction is: %d / %d" %(correct,total))

  plt.plot( x, a, 'r')
  plt.plot(x,predictions,'g')
  plt.plot( x, y, 'y')
  plt.show()


if __name__ == "__main__":
  tf.app.run()




