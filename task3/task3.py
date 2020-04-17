#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

def collect_data(directory):
	crowds = [0] * 16	
	for i in range(1,5,1):
		filepath = (directory / f'Cash{i}.txt').absolute()
		with filepath.open('rt', encoding='utf-8') as src:
			for num, line in enumerate(src):
				line = float(line.strip())
				crowds[num] += line	
	return crowds

def main():
	parser = argparse.ArgumentParser(description='task3')
	parser.add_argument('directory', type=Path, help='Путь к каталогу с файлами')
	args = parser.parse_args()
	crowds = collect_data(args.directory)
	print(crowds.index(max(crowds)) + 1)

if __name__ == '__main__':
	main()
