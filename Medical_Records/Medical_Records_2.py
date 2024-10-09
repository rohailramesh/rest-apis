# In this file, I will initially fetch all the mdedical records from the test api provided by hackerrank and use pagination and timeout techniques too

import requests

def getAllMedicalRecords():
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    time_out_limit = 5
    current_page = 1
    all_records_data = []
    while True: #from page 1 to the last page
        url = f"{base_url}?page={current_page}"
        print(current_page)
        try:
            respone = requests.get(url, timeout=time_out_limit)
            if respone.status_code == 200:
                response_data = respone.json()
                all_records_data.extend(response_data['data'])
                if current_page >= response_data['total_pages']:
                    break
                else:
                    current_page += 1
            else:
                print(f"Error fetching data at {current_page}: {respone.status_code}")
        except requests.exceptions.Timeout:
            print(f"Timeout error")
        except requests.exceptions.RequestException as error:
            print(f"Request related error: {str(error)}")
    # print(f"Total records fetched {len(all_records_data)}")
    # print(str(all_records_data))
    

getAllMedicalRecords()
    