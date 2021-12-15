import requests
import json
import webbrowser

import argparse
import pprint
import sys
import urllib

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
#### Client ID:
#### API Key:
API_KEY= 'Enter Your Key'
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  
DEFAULT_TERM = ''
DEFAULT_LOCATION = 'Ann Arbor, MI'
SEARCH_LIMIT = 50
SEARCH_OFFSET = 950

def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()

def search(api_key, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'offset': SEARCH_OFFSET
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location)
    with open("Yelp_950_1000.json", "w") as outfile:
        json.dump(response, outfile)
    #print(response)
    businesses = response.get('businesses')
    #print(businesses)
    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print(u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id))

    response = get_business(API_KEY, business_id)

    print(u'Result for business "{0}" found:'.format(business_id))
    #pprint.pprint(response, indent=2)



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

main()


#print(data)

dict_all = []
with open('Yelp_0_50.json') as f:
    data1 = json.load(f)
    item1 = data1["businesses"]

with open('Yelp_50_100.json') as f:
    data2 = json.load(f)
    item2 = data2["businesses"]

with open('Yelp_100_150.json') as f:
    data3 = json.load(f)
    item3 = data3["businesses"]

with open('Yelp_150_200.json') as f:
    data4 = json.load(f)
    item4 = data4["businesses"]

with open('Yelp_200_250.json') as f:
    data5 = json.load(f)
    item5 = data5["businesses"]

with open('Yelp_250_300.json') as f:
    data6 = json.load(f)
    item6 = data6["businesses"]

with open('Yelp_300_350.json') as f:
    data7 = json.load(f)
    item7 = data7["businesses"]

with open('Yelp_350_400.json') as f:
    data8 = json.load(f)
    item8 = data8["businesses"]

with open('Yelp_400_450.json') as f:
    data9 = json.load(f)
    item9 = data9["businesses"]

with open('Yelp_450_500.json') as f:
    data10 = json.load(f)
    item10 = data10["businesses"]

with open('Yelp_500_550.json') as f:
    data11 = json.load(f)
    item11 = data11["businesses"]

with open('Yelp_550_600.json') as f:
    data12 = json.load(f)
    item12 = data12["businesses"]

with open('Yelp_600_650.json') as f:
    data13 = json.load(f)
    item13 = data13["businesses"]

with open('Yelp_650_700.json') as f:
    data14 = json.load(f)
    item14 = data14["businesses"]

with open('Yelp_700_750.json') as f:
    data15 = json.load(f)
    item15 = data15["businesses"]

with open('Yelp_750_800.json') as f:
    data16 = json.load(f)
    item16 = data16["businesses"]

with open('Yelp_800_850.json') as f:
    data17 = json.load(f)
    item17 = data17["businesses"]

with open('Yelp_850_900.json') as f:
    data18 = json.load(f)
    item18 = data18["businesses"]

with open('Yelp_900_950.json') as f:
    data19 = json.load(f)
    item19 = data19["businesses"]

with open('Yelp_950_1000.json') as f:
    data20 = json.load(f)
    item20 = data20["businesses"]

dict_all = dict_all + item1 + item2 + item3 + item4 + item5 + item6 + item7 + item8 + item9 + item10 + item11 + item12 + item13 + item14 + item15 + item16 + item17 + item18 + item19 + item20


with open("Yelp_Combined.json", "w") as outfile:
    json.dump(data, outfile)

'''
'''
with open("Yelp_0_50.json") as f:
    data = json.load(f)

list = data['businesses']
print(list)
i = 0
for item in list:
    i += 1

print(i)
