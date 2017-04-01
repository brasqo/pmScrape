from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
	content = urlopen("https://www.islandrealty.com/charleston-area-vacation-rentals?avail_filter%5Brcav%5D%5Bbegin%5D=&avail_filter%5Brcav%5D%5Bend%5D=&avail_filter%5Brcav%5D%5Bflex_type%5D=d&evrn_client_2=Wild+Dunes&occ_total_numeric=&beds_min=&baths_min=&sort_by=random_seed&items_per_page=48")
	soup = BeautifulSoup(content.read(), "lxml")
	#looking for and printing all the /td tags... Try /tr also.
	print(soup.find_all('td'))

except HTTPError as err:
	print(err)

except AttributeError as atterr:
	print(atterr)
	exit()



#print(content.read())

