def is_leap(year):
	leap = False
	if year in range(1900,100001):
		if year % 100 == 0:
			if year % 400 == 0:
				leap = True
		elif year % 4  == 0:
			leap = True
	return leap

if __name__ == '__main__':
	year = int(raw_input())
	print is_leap(year)