from re import findall

numOfPg = int(input())
pages = {}

def path(p1, p2):
	crawlQ = pages[p1]
	if p2 in crawlQ:
            return True

	while crawlQ:
		prefix = []

		newPage = False
		if crawlQ[0] in pages: #if link has listing in pages
			for j in pages[crawlQ[0]]: #links in first element of crawlQ
				if not(j in pages[p1]):
					newPage = True 
					prefix.append(j)
					pages[p1].append(j)
					if j == p2: return True

		if newPage:
			crawlQ = prefix + crawlQ
		else:
			del crawlQ[0]
	return False

#something wrong here?
while numOfPg: #going through pages
    title = input()

    pages[title] = []
    while 1: #exploring page
        _in = input()

        if findall("</HTML>", _in): #end of page
            numOfPg -= 1
            break
        
        links = findall("<A HREF=\"[^>]+\">", _in) #links in input, change to dmoj specifications?
        if links: #any links?
            for i in links: #print and append links
                link_name = i[9:len(i) - 2]
                pages[title].append(link_name)
                print("Link from {0} to {1}".format(title, link_name))

while 1:
    page1 = input()
    if page1 == "The End":
        break

    page2 = input()
    if path(page1, page2):
        print("Can surf from {0} to {1}.".format(page1, page2))
    else:
        print("Can't surf from {0} to {1}.".format(page1, page2))
