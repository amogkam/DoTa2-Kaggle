import pandas as ps
import numpy as np
import csv

data = []

with open('MatchDetail.csv', 'rt') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',', quotechar='|')
	data = [row for row in datareader]

gold_training = []

sum_gold = 0
for i in range(1,6):
	n = -1
	while (data[i][n] == 0):
		n -= 1
	sum_gold += int(data[i][n])

print(sum_gold)
