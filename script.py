import requests

# Define the router's API endpoint and credentials
router_ip = "192.168.1.1"  # Replace with the router's IP address
username = "your_username"  # Replace with your router's username
password = "your_password"  # Replace with your router's password

# Set up authentication
auth = (username, password)

# Define the base URL for the router's RESTCONF API
base_url = f"https://{router_ip}/restconf/data/"

# Define the path to retrieve the IOS-XE version
version_url = f"{base_url}Cisco-IOS-XE-device-hardware:device-hardware/data"

# Make the API request to retrieve the IOS-XE version
response = requests.get(version_url, auth=auth, headers={"Accept": "application/yang-data+json"})

if response.status_code == 200:
    version_data = response.json()
    ios_xe_version = version_data["Cisco-IOS-XE-device-hardware:device-hardware"]["version"]
    print(f"The IOS-XE version running on the router is: {ios_xe_version}")
else:
    print(f"Failed to retrieve the IOS-XE version. Status code: {response.status_code}")
