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

def beginner(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    beginner = []
    core_python = []
    embedded_python = []
    infrastructure = []
    scientific_computing = []
    software_development = []
    web_development = []
    workshops = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Core Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                core_python.append(temp)
            elif section == "Embedded Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                embedded_python.append(temp)
            elif section == "Infrastructure":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                infrastructure.append(temp)
            elif section == "Scientific Computing":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                scientific_computing.append(temp)
            elif section == "Software Development Tools":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                software_development.append(temp)
            elif section == "Web Development":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                web_development.append(temp)
            elif section == "Workshops":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                workshops.append(temp)
    
    beginner.append(core_python)
    beginner.append(embedded_python)
    beginner.append(infrastructure)
    beginner.append(scientific_computing)
    beginner.append(software_development)
    beginner.append(web_development)
    beginner.append(workshops)
    return beginner

def intermediate(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    intermediate = []
    core_python = []
    embedded_python = []
    infrastructure = []
    scientific_computing = []
    software_development = []
    web_development = []
    workshops = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Core Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                core_python.append(temp)
            elif section == "Embedded Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                embedded_python.append(temp)
            elif section == "Infrastructure":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                infrastructure.append(temp)
            elif section == "Scientific Computing":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                scientific_computing.append(temp)
            elif section == "Software Development Tools":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                software_development.append(temp)
            elif section == "Web Development":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                web_development.append(temp)
            elif section == "Workshops":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                workshops.append(temp)
    
    intermediate.append(core_python)
    intermediate.append(embedded_python)
    intermediate.append(infrastructure)
    intermediate.append(scientific_computing)
    intermediate.append(software_development)
    intermediate.append(web_development)
    intermediate.append(workshops)
    return intermediate

def advanced(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    advanced = []
    core_python = []
    embedded_python = []
    infrastructure = []
    scientific_computing = []
    software_development = []
    web_development = []
    workshops = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Core Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                core_python.append(temp)
            elif section == "Embedded Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                embedded_python.append(temp)
            elif section == "Infrastructure":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                infrastructure.append(temp)
            elif section == "Scientific Computing":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                scientific_computing.append(temp)
            elif section == "Software Development Tools":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                software_development.append(temp)
            elif section == "Web Development":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                web_development.append(temp)
            elif section == "Workshops":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[0].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                temp.append(detail[1].find_all('td')[7].string)
                temp.append(detail[1].find_all('td')[8].string)
                workshops.append(temp)
    
    advanced.append(core_python)
    advanced.append(embedded_python)
    advanced.append(infrastructure)
    advanced.append(scientific_computing)
    advanced.append(software_development)
    advanced.append(web_development)
    advanced.append(workshops)
    return advanced

def b_core(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    core = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Core Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return core

def b_embedded(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    embedded = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Embedded Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return embedded

def b_infrastructure(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    infrastructure = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Infrastructure":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return infrastructure

def b_scientific(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    scientific = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Scientific Computing":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return scientific

def b_software(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    software = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Software Development Tools":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return software

def b_web(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    web = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Web Development":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return web

def b_workshops(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    workshops = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Beginner":
            if section == "Workshops":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return workshops

def i_core(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    core = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Core Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return core

def i_embedded(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    embedded = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Embedded Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return embedded

def i_infrastructure(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    infrastructure = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Infrastructure":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return infrastructure

def i_scientific(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    scientific = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Scientific Computing":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return scientific

def i_software(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    software = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Software Development Tools":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return software

def i_web(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    web = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Web Development":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return web

def i_workshops(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    workshops = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Intermediate":
            if section == "Workshops":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return workshops

def a_core(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    core = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Core Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return core

def a_embedded(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    embedded = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Embedded Python":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return embedded

def a_infrastructure(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    infrastructure = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Infrastructure":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return infrastructure

def a_scientific(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    scientific = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Scientific Computing":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return scientific

def a_software(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    software = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Software Development Tools":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return software

def a_web(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    web = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Web Development":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return web

def a_workshops(page):
    soup = BeautifulSoup(page)
    extras = soup.find_all('tbody')
    proposals = []
    workshops = []

    for extra in extras[::2]:
        proposals.append(extra)

    for proposal in proposals:
        detail = proposal.find_all('tr')
        level = detail[1].find_all('td')[5].string
        section = detail[1].find_all('td')[3].string
        if level == "Advanced":
            if section == "Workshops":
                temp = []
                temp.append(detail[1].find_all('td')[1].string)
                temp.append(detail[1].find_all('td')[6].string)
                core.append(temp)
    return workshops

