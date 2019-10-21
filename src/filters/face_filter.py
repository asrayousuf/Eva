''' 
The purpose of this file is to detect faces in a video and return the frames that have a human face in it
'''


import numpy as np
import pandas as pd

from copy import deepcopy
from src.filters import FilterTemplate
from src.filters.models.ml_randomforest import MLRandomForest

class FilterFace(FilterTemplate):
  def __init__(self):
  	pass

  def addPreModel(self, model_name, model):
    """
    Add preprocessing machine learning/statistical models such as PCA, Sampling, etc
    :param model_name: name of model must be string
    :param model: model
    :return: None
    """
    pass

  def addPostModel(self, model_name, model):
    """
    Add postprocessing machine learning/statistical models such as SVM, DNN, random forest, etc
    :param model_name: name of model must be string
    :param model: model
    :return: None
    """
    pass

  def addPostModel(self, model_name, model):
  	pass

   def deletePreModel(self, pre_model_name):
    """
    Delete preprocessing model from models dictionary
    :param model_name: name of model
    :return: None
    """
    pass

  def deletePostModel(self, post_model_name):
  	"""
    Delete postprocessing model from models dictionary
    :param model_name: name of model
    :return: None
    """
  	pass

  def train(self, X:np.ndarray, y:np.ndarray):
  	pass

  def predict(self, X:np.ndarray, pre_model_name:str = None, post_model_name:str = None)->np.ndarray:
  	pass

  def getAllStats(self):
  	pass



if __name__ == "__main__":


  filter = FilterFace()

  X = np.random.random([100,30,30,3])
  y = np.random.random([100])
  y *= 10
  y = y.astype(np.int32)

  division = int(X.shape[0] * 0.8)
  X_train = X[:division]
  X_test = X[division:]
  y_isface_train = y[:division]
  y_isface_test = y[division:]

  filter.train(X_train, y_isface_train)
  print("filter finished training!")
  y_isface_predict = filter.predict(X_test, post_model_name='rf')
  print("filter finished prediction!")
  stats = filter.getAllStats()
  print(stats)
  print("filter got all stats")