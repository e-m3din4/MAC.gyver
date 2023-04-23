# MAC.gyver
### Retrieve MAC address vendor info or a full profile in json format.

            ---------------------------------------------- 
		▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
		▓▓▓▓▓▓▓▓▓▓▓²²²²╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
		▓▓▓▓▓▓ ▓▓▓▓▓▓  ╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
		▓▓▓▓▓▓  ▓▓▓▓▓   ````````````````````````` ▓▓▓▓ 
		▓▓▓▓▓    ▓▓▓▓    ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ 
		▓▓▓▓▓─   ▓▓      ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ 
		▓▓▓▓▓─                                    ▓▓▓▓ 
		▓▓   ─           ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ 
		▓▓ ▓▓─   ▓▓▓     ▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓▓ ▓▓▓▓    ▓▓▓▓ 
		▓▓▓▓▓▓  ▓▓▓▓▓                             ▓▓▓▓ 
		▓▓▓▓▓▓ ▓▓▓▓▓▓                             ▓▓▓▓ 
		▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓   ▓▓▓   ▓▓  ▓▓▓▓▓ 
		▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
				                               
		▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
		▓▓ ▓ ▓▓▓▓▓▓ ▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
		▓ ▓ ▓ ▓▓▓▓ ▓ ▓▓▓ ▓▓▓▓▓▓▓▓▓▓                 ▓▓ 
		▓ ▓▓▓ ▓▓▓▓   ▓▓▓ ▓▓▓▓▓   ▓▓  G  Y  V  E  R  ▓▓ 
		▓ ▓▓▓ ▓▓▓▓ ▓ ▓▓▓▓  ▓▓▓▓▓▓▓▓                 ▓▓ 
		▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
				                               
		▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
		++++++++++++++++++++++++++++++++++++++++++++++ 
		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

		usage: MACgyver.py [-h] --mac MAC

		Retrieve MAC/OUI info from macaddress.io API

		options:
		  -h, --help  show this help message and exit
		  --mac MAC   MAC address or OUI to search for

### About...
This Python script retrieves information from basic vendor lookup to a comprehensive profile related to a MAC address, used to identify which device is which on your local network. MAC addresses are always a 12 digit hexadecimal number, 
with the numbers separated every two digits by a colon or hyphen.  
The script takes a MAC address as an argument and retrieves the API key from a config.json 
file located in the same directory as the script.

### Requirements

To run the script, you will need Python 3 and the requests module installed. You can install the module using pip:

pip3 install requests

### Usage

To run the script, open a terminal in the directory containing the script and the config.json file, and run the following command:


python3 MACgyver.py --mac [OUI]


The script will send a request to the macaddress.io API and print the response.

You can also use the -h or --help argument to see the help menu:

### Configuration

The config.json file should contain your macaddress.io API key in the following format:


{
    "api_key": "your_api_key_here"
}

Replace your_api_key_here with your actual Documentos-RapidAPI key.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
