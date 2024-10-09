# In this file, I will initially fetch all the mdedical records from the test api provided by hackerrank for a given user id which will be passed as a parameter

import requests

def getAllMedicalRecordsForUser(userId):
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    current_page = 1
    timeout_limit = 5
    allUserRecords = []
    
    while True:
        url = f"{base_url}?userId={userId}&page={current_page}"
        print(current_page)
        try:
            response = requests.get(url, timeout=timeout_limit)
            # if status code for response is 200 then store all user data
            if response.status_code == 200:
                responseData = response.json()
                allUserRecords.extend(responseData['data'])
                if current_page >= responseData['total_pages']:
                    break
                current_page += 1
            else:
                print(f"Error fetching data at {current_page}")
                break
        except requests.exceptions.Timeout:
            print("Timeout error")
            break
        except requests.exceptions.RequestException as reqError:
            print(f"Request related error: {str(reqError)}")
            break
    print(f"Total medical records fetched for user {userId}: {len(allUserRecords)}")
    return allUserRecords  # Return the fetched records    
    

testUserId = 2
getAllMedicalRecordsForUser(testUserId)
    