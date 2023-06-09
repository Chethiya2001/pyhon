import requests
import argparse
import json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--ipaddress", help="IP Address to track")

    args = parser.parse_args()

    ip = args.ipaddress 

    #crete request
    url = "http://ip-api.com/json/"+ip

    #http://ip-api.com/json/192.168.1.1

    response = requests.get(url)
    #pass json
    data = json.loads(response.content)
    

    print("\t[+] IP\t\t\t",data["query"])
    print("\t[+] CITY\t\t",data["city"])
    print("\t[+] ISP\t\t\t",data["isp"])
    print("\t[+] LOC\t\t\t",data["country"])
    print("\t[+] REG\t\t\t",data["regionName"])
    print("\t[+] TIME\t\t",data["timezone"])
    print("\t[+] ZIP\t\t\t",data["zip"])
    print("\t[+] LAT\t\t\t",data["lat"])
    print("\t[+] LON\t\t\t",data["lon"])

