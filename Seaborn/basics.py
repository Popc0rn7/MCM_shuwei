import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
#style setting
sns.set_style('whitegrid')
sns.axes_style()
#environment setting
sns.set_context()
sns.plotting_context()
#color
sns.color_palette(n=8)

sns.boxplot(iris['sepal_length'])
