from bs4 import BeautifulSoup


def total(page):
	soup = BeautifulSoup(page)
	number = len(soup.find_all('tbody'))
	total = int(number)/2
	return total
