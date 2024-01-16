from urllib import request
import json
import sys

def checker(domain):
    """Checker used to gather subdomain in crt.sh and processes it.
    :param domain: string - the domain in subdomain.
    :returns: None.

    This function gets json, processes it and stores the subdomain.
    """

    url = 'https://crt.sh/?q='+ domain + '&output=json'
    print(url)
    
    def get_json(url):
        """Import json file from crt.sh
        :param url: string - the url of the site.
        :return: None.

        This function takes one string (url) and returns crt.sh data in json format.
        """
        with request.urlopen(url) as response:
            if response.getcode() == 200:
                html = response.read().decode("utf-8")
                file = open("crt.json","w", encoding='utf-8')
                file.write(str(html))
                file.close
            else: print("Request error : ", response.getcode())

    def process_json():
        """Process the json file and stores it into the text file.
        :return: None.
        
        This function processes the json string returned from get_json function and stores the subdomain.
        """
        with open("crt.json", "r") as file:
            data = json.load(file)
            new_file = open("subdomain.txt","w")
            subdata = []
            for i in range(len(data)):
                new_data = data[i]["common_name"]
                if new_data not in subdata:
                    subdata.append(new_data)
            [new_file.write(i + '\n') for i in subdata]
            new_file.close()
    
    def check_status(sub_file):
        """Check the status code.
        :param sub_file: string - Subdomains to be checked (file).
        :return: None.
        
        This function checks all subdomain status code.
        """
        # sub_db = {}
        # for x in open(sub_file, "r"):
        #     url = 'https://' + x
        #     print(url)
        #     with request.urlopen(url) as response:
        #         html = response.read()
        #         code = response.getcode()
        #         print("Subdomain : %S", (x,code))

    # run the program.
    get_json(url)
    process_json()
    # check_status("subdomain.txt")


if __name__ == "__main__":
    checker(sys.argv[1])