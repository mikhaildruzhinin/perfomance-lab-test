#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

def get_quadrangle(filepath):
	x = []
	y = []
	with filepath.open('rt', encoding='utf-8') as src:
		for line in src:
			x_line, y_line = line.split()
			x.append(float(x_line))
			y.append(float(y_line))
	x.append(x[0])
	y.append(y[0])
	return x, y

def get_points(x, y, filepath):
	with filepath.open('rt', encoding='utf-8') as src:
		for line in src:
			x_o, y_o = line.split()
			x_o = float(x_o)
			y_o = float(y_o)

			cross_products = []
			for i in range(4):
				cross_product = (x[i + 1] - x[i]) * (y_o - y[i]) - (y[i+1] - y[i]) * (x_o - x[i])
				cross_products.append(cross_product)
			answer = find_location(cross_products)
			print(answer)

def find_location(cross_products):
	if all(product >= 0 for product in cross_products) or all(product <= 0 for product in cross_products):
		if cross_products.count(0) == 2:
			return 0
		elif cross_products.count(0) == 1:
			return 1
		else:
			return 2
	else:
		return 3

def main():
	parser = argparse.ArgumentParser(description='task2')
	parser.add_argument('filepath1', type=Path, help='Координаты фигуры')
	parser.add_argument('filepath2', type=Path, help='Координаты точек')
	args = parser.parse_args()
	filepath = args.filepath1.absolute()
	x, y = get_quadrangle(filepath)
	filepath = args.filepath2.absolute()
	get_points(x, y, filepath)

if __name__ == '__main__':
	main()
