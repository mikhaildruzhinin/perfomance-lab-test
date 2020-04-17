#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
import statistics
import numpy as np

def collect_data(filepath):
	numbers = []
	with filepath.open('rt', encoding='utf-8') as src:
		for line in src:
			numbers.append(int(line))
	return numbers


def main():
	parser = argparse.ArgumentParser(description='task1')
	parser.add_argument('filepath', type=Path, help='Путь к считываемому файлу')
	args = parser.parse_args()
	filepath = args.filepath.absolute()
	numbers = collect_data(filepath)
	print('%.2f' % np.percentile(numbers, 90))
	print('%.2f' % statistics.median(numbers))
	print('%.2f' % max(numbers))
	print('%.2f' % min(numbers))
	print('%.2f' % statistics.mean(numbers))

if __name__ == '__main__':
	main()
