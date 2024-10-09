# In this file, I will initially fetch all the mdedical records from the test api provided by hackerrank and display it to user

import requests

def getAllMedicalRecords():
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    response = requests.get(base_url).json() #This returns everything from the API including thre data, page no, per_page, etc
    data = response['data'] #This returns the data in a list(array)
    
    # print(f'API response: {response}')
    print(f'Data: {data}')
    

getAllMedicalRecords()
    