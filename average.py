#!/usr/bin/env python


import sys
import pandas as pd

def main():
	filename = sys.argv[1]
	year = int(sys.argv[2])
	factor = sys.argv[3]

	survey_df = pd.read_csv(filename)
	sub_year = survey_df[survey_df.year == year]
	grouping_df = sub_year.groupby(factor)['weight']
	mean_by_group = grouping_df.mean()

	print mean_by_group

if __name__ == "__main__":
	main()