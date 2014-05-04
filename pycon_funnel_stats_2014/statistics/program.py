from bs4 import BeautifulSoup


def total(page):
    soup = BeautifulSoup(page)
    number = len(soup.find_all('tbody'))
    total = int(number)/2
    return total

def proposallist(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals, number = [], []
    i, j, k = 0, 0, 0

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        if level == "Beginner":
            i = i + 1
        elif level == "Intermediate":
            j = j + 1
        elif level == "Advanced":
            k = k + 1

    number.append(i)
    number.append(j)
    number.append(k)
    return number
    
