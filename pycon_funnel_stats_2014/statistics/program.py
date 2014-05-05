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
    b_core, b_embedded, b_infrastructure, b_scientific = 0, 0, 0, 0
    b_software, b_web, b_workshops = 0, 0, 0
    i_core, i_embedded, i_infrastructure, i_scientific = 0, 0, 0, 0
    i_software, i_web, i_workshops = 0, 0, 0
    a_core, a_embedded, a_infrastructure, a_scientific = 0, 0, 0, 0
    a_software, a_web, a_workshops = 0, 0, 0

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
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

def section(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    beginner, intermediate, advanced, sections = [], [], [], []
    b_core, b_embedded, b_infrastructure, b_scientific = 0, 0, 0, 0
    b_software, b_web, b_workshops = 0, 0, 0
    i_core, i_embedded, i_infrastructure, i_scientific = 0, 0, 0, 0
    i_software, i_web, i_workshops = 0, 0, 0
    a_core, a_embedded, a_infrastructure, a_scientific = 0, 0, 0, 0
    a_software, a_web, a_workshops = 0, 0, 0

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Core Python":
                b_core = b_core + 1
            elif section == "Embedded Python":
                b_embedded = b_embedded + 1
            elif section == "Infrastructure":
                b_infrastructure = b_infrastructure + 1
            elif section == "Scientific Computing":
                b_scientific = b_scientific + 1
            elif section == "Software Development Tools":
                b_software = b_software + 1
            elif section == "Web Development":
                b_web = b_web + 1
            elif section == "Workshops":
                b_workshops = b_workshops + 1
        elif level == "Intermediate":
            if section == "Core Python":
                i_core = i_core + 1
            elif section == "Embedded Python":
                i_embedded = i_embedded + 1
            elif section == "Infrastructure":
                i_infrastructure = i_infrastructure + 1
            elif section == "Scientific Computing":
                i_scientific = i_scientific + 1
            elif section == "Software Development Tools":
                i_software = i_software + 1
            elif section == "Web Development":
                i_web = b_web + 1
            elif section == "Workshops":
                i_workshops = i_workshops + 1
        elif level == "Advanced":
            if section == "Core Python":
                a_core = a_core + 1
            elif section == "Embedded Python":
                a_embedded = a_embedded + 1
            elif section == "Infrastructure":
                a_infrastructure = a_infrastructure + 1
            elif section == "Scientific Computing":
                a_scientific = a_scientific + 1
            elif section == "Software Development Tools":
                a_software = a_software + 1
            elif section == "Web Development":
                a_web = a_web + 1
            elif section == "Workshops":
                a_workshops = a_workshops + 1


    beginner.append(b_core)
    beginner.append(b_embedded)
    beginner.append(b_infrastructure)
    beginner.append(b_scientific)
    beginner.append(b_software)
    beginner.append(b_web)
    beginner.append(b_workshops)

    intermediate.append(i_core)
    intermediate.append(i_embedded)
    intermediate.append(i_infrastructure)
    intermediate.append(i_scientific)
    intermediate.append(i_software)
    intermediate.append(b_web)
    intermediate.append(i_workshops)

    advanced.append(a_core)
    advanced.append(a_embedded)
    advanced.append(a_infrastructure)
    advanced.append(a_scientific)
    advanced.append(a_software)
    advanced.append(a_web)
    advanced.append(a_workshops)

    sections.append(beginner)
    sections.append(intermediate)
    sections.append(advanced)
    return sections

