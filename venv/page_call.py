from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time , json
from waity import wait_time

weblog = webdriver.Chrome()
url = "https://uat-id.hitpa.co.in/realms/eo2v2/protocol/openid-connect/auth?client_id=eo2m2_hitpa_client&redirect_uri=https%3A%2F%2Fuat-icms.hitpa.co.in%2Fproduct%2Fmembers&state=ca49c887-489a-4a44-a7b4-7b201846f6e4&response_mode=fragment&response_type=code&scope=openid&nonce=c9b1729c-10d8-4bc3-9da7-82adbcdaaafd&code_challenge=mVlqCqdAxULBamWHM-9QHdCUNWNdWgZ-_h1EFZl8Rm8&code_challenge_method=S256"
weblog.get(url)
inward_url = "https://uat-icms.hitpa.co.in/api/claims-service/v1/claim-inward/save-claim-inward"

# LOGIN
username = wait_time(weblog,By.ID,"username").send_keys("deepaks")
password = wait_time(weblog,By.ID,"password").send_keys("Welcome@1234")
submit = wait_time(weblog,By.NAME,"login").click()

# otp = int(input("write otp for login>"))
# sign_in = wait_time(weblog,By.ID,"kc-login").click()

weblog.maximize_window()
weblog.execute_script("document.body.style.zoom='67%'")
original_tab = weblog.current_window_handle

# waiting for site to load properly
time.sleep(4)

# getting session storage
session_storage = weblog.execute_script("""
var items = {};
for (var i = 0; i < sessionStorage.length; i++) {
    var key = sessionStorage.key(i);
    items[key] = sessionStorage.getItem(key);
}
return items;
""")

with open("session_storage.json", "r") as file:
    session = json.load(file)

access_token = session["accessToken"]

print("Session storage saved successfully.")

weblog.get("https://uat-icms.hitpa.co.in/*")

menu = wait_time(weblog,By.XPATH,'//button[.//*[contains(@data-testid,"MenuIcon")]]').click()
# claim = WebDriverWait(weblog,20).until(
#     EC.element_to_be_clickable(
#         (By.XPATH,"//div[@role='button'][.//span[normalize-space()='Claim Management']]"))).click()

inward_payload ={"senderDTO":{"senderBranchName":"HI TPA Chennai","receivedVia":"eMail","courierCompany":"","courierCompanyCode":"","senderName":"Dev Aggarwal","senderPhotoPath":"","senderPhoneNo":"9358817678","senderEmailId":"divyanshu.aggarwal@consint.ai","senderAddress1":"123, Main Street","senderAddress2":"","senderLocality":"CAT EXTENSION COUNTER","senderDistrict":"NEW DELHI","location":"NEW DELHI","senderCity":"NEW DELHI","senderState":"DELHI","senderCountry":"INDIA","senderPinCode":110001,"podNo":"","capturedImageBase64":"","imageData":None,"imageContentType":""},"documentTypeDTO":{"departmentName":"Claim","documentType":"Advice for Admission","noOfDocument":0,"documentName":""},"basicDetailsDTO":{"companyName":"HI TPA Chennai","officeCode":"06","prefix":"CHE","department":"Claim","departmentCode":"DECLA_008","inwardType":"REIMB_MAIN_CLAIM","receivedDateTime":"2026-07-15 18:24:26","modeOfReceiving":""},"validateDTO":{"isValidProvider":True,"isValidMember":True,"providerMessge":"","memberMessage":""},"claimsDTO":{"providerId":"UP011225765606","claimNo":"","claimNoExt":"","policyNo":"2400240024002400","corporateEmpId":"","uhidNo":"8261032890640","corporateName":"","patientName":"Saksham Tyagi","providerName":"Arogaya hospital - Greater Noida","providerAddress":"Milak lachi on road g-3 Gr. Noida West , Greater Noida","serviceType":"ipd","admissionDate":"2026-05-07 01:24:26","dischargeDate":"2026-05-07 10:31:00","dateOfLoss":None,"claimAmount":100,"intimatedBy":"asdas","abhaNo":"","intimateDate":"2026-07-15 18:24:26","mobileNo":"9090909090","alternativeMobileNumbers":[],"emailId":"asdads@gmail.com","isDeath":False,"isAccident":False,"deathDate":None,"firNo":"","firDate":None,"isMlcCase":False,"mlcNo":"","mlcDate":None,"ipdNo":"","lineOfTreatment":"","reasonForHospitalization":"","roomNo":"","rooms":[],"initialDiagnosis":"asdasd","doctorName":"asdads","doctorRegistration":"","doctorMobileNo":"7274964521","relationWithPatient":"RESEL_001","typeOfAdmission":"ADEME_001","systemOfMedicine":"SYALL_008","treatmentType":"TRNON_002","claimType":"REIMBURSEMENT","claimSubType":"MAIN_CLAIM","hospitalizationType":"HOSPITALIZATION","natureOfLoss":"","causeOfLoss":"","coverCode":"","coverGroup":""},"memberDTO":{"memberId":23250198,"policyNo":"2400240024002400","bonusSumInsured":0,"policyStartDate":"2026-05-01 00:00:00","policyEndDate":"2027-04-30 00:00:00","sumInsured":0,"uhidNo":"8261032890640","empCode":"","corporateName":"","patientName":"Saksham Tyagi","gender":"Male","relation":"Grandson","insuranceCode":"dqwdasd","tpaCode":"023","regionalOfficeCode":"030000"},"providerDTO":{"providerName":"Arogaya hospital - Greater Noida","providerId":"UP011225765606","address":"Milak lachi on road g-3 Gr. Noida West , Greater Noida","district":"GAUTAM BUDDHA NAGAR","city":"NEW DELHI","state":"UTTAR PRADESH","pincode":201307,"rohiniCode":"8900080400252","tpaHospitalCode":"UP011225765606","providerStatus":"Network","isPPN":"PPN"},"location":""}

headers =headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

inward = requests.request(method="POST",
    url=inward_url,
    headers=headers,
    json=inward_payload
)

print(inward.status_code)
print(inward.text)
inward_json = inward.json()

claim_no_ext = inward_json["data"]["claimsDTO"]["claimNoExt"]

print (f"claim num = {claim_no_ext}")

weblog.switch_to.new_window('tab')
weblog.get("https://uat-icms.hitpa.co.in/*")
time.sleep(2)
weblog.execute_script("document.body.style.zoom='67%'")
weblog.maximize_window()


claim_search = wait_time(weblog,By.XPATH,"//div[@role='button'][.//span[normalize-space()='Search Claim']]").click()

claim_search2 = wait_time(weblog,By.XPATH,"//div[@role='button'][.//span[normalize-space()='Claim Search']]").click()
time.sleep(3)

claim_input_search = wait_time(weblog,By.NAME,"claimNo").send_keys(claim_no_ext,Keys.Enter)
time.sleep(2)



