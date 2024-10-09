# In this file, I will initially fetch all the mdedical records of users from the test api provided by hackerrank who has the same doctor which will be passed as a parameter

import requests

def getAllMedicalRecordsByDoctor(doctorId):
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    current_page = 1
    timeout_limit = 5
    allRecordsByDoctor = []
    while True:
        url = f"{base_url}?doctor={doctorId}&page={current_page}"
        print(current_page)
        try:
            response = requests.get(url, timeout_limit)
            if response.status_code == 200:
                responseData = response.json()
                allRecordsByDoctor.extend(responseData['data'])
                if current_page >= responseData['total_pages']:
                    break
                current_page += 1
            else:
                print(f"Error fetching data at page {current_page}")
                break
        except requests.exceptions.Timeout:
            print("Timeout error")
            break
        except requests.exceptions.RequestException as ReqError:
            print(f"Request related error: {ReqError}")
    print(f"Total number of records for doctor {doctorId} = {len(allRecordsByDoctor)}")
    return(str(allRecordsByDoctor))

doctorId = 2
getAllMedicalRecordsByDoctor(doctorId)
    