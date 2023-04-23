import requests
import argparse
import json

# Print banner
print('')
print('---------------------------------------------- ')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('▓▓▓▓▓▓▓▓▓▓▓²²²²╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('▓▓▓▓▓▓ ▓▓▓▓▓▓  ╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('▓▓▓▓▓▓  ▓▓▓▓▓   ````````````````````````` ▓▓▓▓ ')
print('▓▓▓▓▓    ▓▓▓▓    ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ ')
print('▓▓▓▓▓─   ▓▓      ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ ')
print('▓▓▓▓▓─                                    ▓▓▓▓ ')
print('▓▓   ─           ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ ')
print('▓▓ ▓▓─   ▓▓▓     ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ ')
print('▓▓▓▓▓▓  ▓▓▓▓▓                             ▓▓▓▓ ')
print('▓▓▓▓▓▓ ▓▓▓▓▓▓                             ▓▓▓▓ ')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓   ▓▓▓   ▓▓  ▓▓▓▓▓ ')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('                                               ')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('▓ ▓ ▓ ▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓▓▓▓                 ▓▓ ')
print('▓ ▓▓▓ ▓▓▓▓   ▓▓▓ ▓▓▓▓▓   ▓▓  G  Y  V  E  R  ▓▓ ')
print('▓ ▓▓▓ ▓▓▓▓ ▓ ▓▓▓▓  ▓▓▓▓▓▓▓▓                 ▓▓ ')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('                                               ')
print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ')
print('++++++++++++++++++++++++++++++++++++++++++++++ ')
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ')
print('')
# Parse command line arguments
parser = argparse.ArgumentParser(description='Retrieve MAC/OUI info from macaddress.io API')
parser.add_argument('--mac', help='MAC address or OUI to search for', required=True)
args = parser.parse_args()

# Load API key from config.json file
with open('config.json') as f:
    config = json.load(f)
    api_key = config['api_key']

# Set API endpoint and parameters
url = 'https://api.macaddress.io/v1'
params = {
    'apiKey': api_key,
    'output': 'json',
    'search': args.mac,
}

# Make API request
response = requests.get(url, params=params)

# Check for errors
if response.status_code != 200:
    print('Error: could not retrieve MAC address information')
    print('HTTP status code:', response.status_code)
    exit()

# Parse JSON response
data = response.json()

# Display vendor name or full MAC address information
if 'vendor' in data:
    print('Vendor:', data['vendor'])
else:
    print('MAC address information:')
    for key, value in data.items():
        print(key + ':', value)
