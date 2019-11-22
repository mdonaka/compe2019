#!/bin/sh
python main.py < \
	parameters/$1 | \
	python print_clean.py > \
	result/$1
