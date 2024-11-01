import requests

url = "https://poop.movie/d/vg8en99k3ufy"

def getFileName(url):
    api = "https://poopdown.com/getKey.php?id="
    
    id_video = url.split("/")[-1]
    final_api = f"{api}{id_video}"
    
    print("Final API URL:", final_api) 

    response = requests.get(final_api)

    print("Response Status Code:", response.status_code) 
    
    if response.status_code == 200:
        try:
            data = response.json()
            print("Response Data:", data)
            
            file_name = data.get("file")
            if file_name:
                direct_link(file_name)
            else:
                print("No file found in response.")
                
        except ValueError as e:
            print("Error parsing JSON:", e)
            print("Response Text:", response.text)
    else:
        print("Error:", response.status_code, response.text)

def direct_link(file_name):
    download_url = f"https://mba.dog/download.php?key={file_name}"
    
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "s",
        "content-type": "application/json",
        "origin": "https://poopdown.com",
        "priority": "u=1, i",
        "referer": "https://poopdown.com/",
        "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    
    response = requests.get(download_url, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            print("Response Data:", data) 
            direct_link = data.get("direct_link")
            if direct_link:
                print(direct_link)
            else:
                print("No file found in response.")
                
        except ValueError as e:
            print("Error parsing JSON:", e)
            print("Response Text:", response.text)
    else:
        print("Error:", response.status_code, response.text)

getFileName(url)
