#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path
import numpy as np

def collect_data(filepath):
	working_hours = np.zeros((720), dtype=int)
	with filepath.open('rt', encoding='utf-8') as src:
		for line in src:
			enter_time, exit_time = line.split()
			enter_hour, enter_minutes = enter_time.split(':')
			exit_hour, exit_minutes = exit_time.split(':')
			enter_hour, enter_minutes, exit_hour, exit_minutes = int(enter_hour), int(enter_minutes), int(exit_hour), int(exit_minutes)
			working_hours[(enter_hour - 8)*60 + enter_minutes : (exit_hour - 8)*60 + exit_minutes ] += 1
	return working_hours

def find_max_visitors(working_hours):
	k = False
	for i in range(working_hours.shape[0]):
		for j in range(working_hours.shape[1]):
			if working_hours[i,j] == working_hours.max() and not k:
				start_interval = correct_time_format(i,j)
				k = True
			if working_hours[i,j] != working_hours.max() and k:
				end_interval = correct_time_format(i,j)
				k = False
				print(f'{start_interval} {end_interval}')

def correct_time_format(i, j):
	if j < 10:
		corrected_time = f'{i + 8}:0{j}'
	else:
		corrected_time = f'{i + 8}:{j}'
	return corrected_time

def main():
	parser = argparse.ArgumentParser(description='task4')
	parser.add_argument('filepath', type=Path, help='Путь к считываемому файлу')
	args = parser.parse_args()
	filepath = args.filepath.absolute()
	working_hours = collect_data(filepath)
	working_hours = working_hours.reshape(12,60)
	find_max_visitors(working_hours)

if __name__ == '__main__':
	main()
