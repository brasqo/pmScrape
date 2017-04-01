#need to parse the results received from IRscrape into readable format.
#Property, BRs, BAs,

import requests
from lxml import html

url = "http://www.boxofficemojo.com/monthly/?view=releasedate&chart=&month=1&yr=2006"

response = requests.get(url)
soup = html.fromstring(response.content)
result_list = []
for row in soup.xpath('//div[@id="body"]/center/table')[0].xpath('.//tr')[2:] :
    # print row.xpath()
    data = row.xpath('./td//text()')
    print data
    if len(data) >= 8 :
        print data
        result_list.append({'title' : data[1].strip(), 'gross' : data[3].strip(),
            'open' : data[7].strip(), 'close' : data[8].strip()})

print result_list