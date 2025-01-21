from Patterns import *
import logging

Un = input("Enter your name for registration: ").strip()
logging.basicConfig(level=logging.INFO, filename=f"{Un}_logs.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

#Username
def validate_user_name(f):
    logging.info("Registartion attempt received")
    def helper(*x):
        logging.info("Starting username validation.")
        if re.match(Pattern_un,Un):
            logging.info("Username validated successfully")
            return f(*x)
        else:
            print("Invalid Username! Please enter valid username")
            
    return helper

#Password
def validate_password(f):
    def helper(*x):
        logging.info("Starting password validation.")
        while True:
            try:
                psw=input("Enter Password: ")
                if re.match(Pattern_psw,psw):
                    logging.info("Password validation successfull")
                    return f(*x)
                else:
                    logging.warning("Registration failed for user Password too short")
                raise ValueError("Invalid Password Format! Please Enter correct Password")
            except Exception as e:
                print(e)
    return helper

#Name
def validate_Name(f):
    def helper(*x):
        logging.info("Starting name validation.")
        while True:
            try:
                nm=input("Enter the name: ")
                if re.match(Pattern_name,nm):
                    logging.info("Name validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Name format")
                raise ValueError("Invalid Name format! Please Enter correct Name")
            except Exception as e:
                print(e)
    return helper

#Phone number
def validate_user_phone(f):
    def helper(*x):
        logging.info("Starting phoen_no validation.")
        while True:
            try:
                phn=input("Enter the 10 digit number: ")
                if re.match(Pattern_phone,phn):
                    logging.info("Phone validation successfull")
                    return f(*x) 
                else:
                    logging.warning(f"Registration failed for user Invalid phone No. format")
                    raise ValueError("Invalid Phone! Please Enter correct 10 digit phone number")
            except Exception as e:
                print(e)
    return helper

#Email
def validate_email_id(f):
    def helper(*x):
        logging.info("Starting email validation.")
        while True:
            try:
                eml=input("Enter the email: ")
                if re.match(Pattern_email,eml):
                    logging.info("Email validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid email format")
                    raise ValueError("Invalid Email! Please Enter correct Email")
            except Exception as e:
                print(e)
    return helper

#License number
def validate_Lic_no(f):
    def helper(*x):
        logging.info("Starting License number validation.")
        while True:
            try:
                Licno=input("Enter the License number: ")
                if re.match(Pattern_lic,Licno):
                    logging.info("License number validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Lic_ No format")
                raise ValueError("Invalid Lic. No! Please Enter correct Lic. No")
            except Exception as e:
                print(e)
    return helper

#Adhaar number
def validate_Adhaar_no(f):
    def helper(*x):
        logging.info("Starting adhar validation.")
        while True:
            try:
                adr=input("Enter the adhaar number: ")
                if re.match(Pattern_adhr,adr):
                    logging.info("Aadhaar number validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Adhar_No format")
                raise ValueError("Invalid Adhaar No! Please Enter correct Adhaar No.")
            except Exception as e:
                print(e)
    return helper

#City
def validate_city(f):
    def helper(*x):
        logging.info("Starting city name validation.")
        while True:
            try:
                cty=input("Enter the city name: ")
                if re.match(Pattern_city,cty):
                    logging.info("City name validated successfully")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid City format")
                raise ValueError("Invalid City name! Please Enter correct City")
            except Exception as e:
                print(e)
    return helper

#pincode
def validate_pincode(f):
    def helper(*x):
        logging.info("Starting pincode validation.")
        while True:
            try:
                pin=input("Enter the pincode: ")
                if re.match(Pattern_pincode,pin):
                    logging.info("Pin Code validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid pincode format")
                raise ValueError("Invalid Pincode! Please Enter correct Pincode")
            except Exception as e:
                print(e)
    return helper

#state
def validate_state(f):
    def helper(*x):
        logging.info("Starting state validation.")
        while True:
            try:
                stt=input("Enter the state name: ")
                if re.match(Pattern_state,stt):
                    logging.info("State name validated successfully")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid State format")
                raise ValueError("Invalid State! Please Enter correct state")
            except Exception as e:
                print(e)
    return helper

#Company name
def validate_Company_name(f):
    def helper(*x):
        logging.info("Starting Company validation.")
        while True:
            try:
                Cname=input("Enter the Company name: ")
                if re.match(Pattern_Company_name,Cname):
                    logging.info("Company name validated successfully")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Company name format")
                raise ValueError("Invalid Company Name! Please Enter correct Company name")
            except Exception as e:
                print(e)
    return helper

#Model name/number
def validate_model_no(f):
    def helper(*x):
        logging.info("Starting model name validation.")
        while True:
            try: 
                mdl=input("Enter the model name/number: ")
                if re.match(Pattern_mdl,mdl):
                    logging.info("Model name validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid model_no format")
                raise ValueError("Invalid model_no! Please Enter correct model_no")
            except Exception as e:
                print(e)
    return helper

#Color
def validate_Color(f):
    def helper(*x):
        logging.info("Starting Colour validation.")
        while True:
            try:
                clr=input("Enter the color of the car: ")
                if re.match(Pattern_Color,clr):
                    logging.info("Color validation successfull")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Colour Name format")
                raise ValueError("Invalid Colour! Please Enter correct Colour")
            except Exception as e:
                print(e)
    return helper

#Price
def validate_Price(f):
    def helper(*x):
        logging.info("Starting Price validation.")
        while True:
            try:
                prc=input("Enter the price of car: ")
                if re.match(Pattern_Price,prc):
                    logging.info("Price validated successfully")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Price format")
                raise ValueError("Invalid Price! Please Enter correct Price")
            except Exception as e:
                print(e)
    return helper

#Fuel
def validate_Fuel(f):
    def helper(*x):
        logging.info("Starting fuel type validation.")
        while True:
            try:
                fl=input("Enter the fuel type: ")
                if fl in Patter_Fuel:
                    logging.info("Registration done Successfully.")
                    return f(*x)
                else:
                    logging.warning(f"Registration failed for user Invalid Fuel type format")
                raise ValueError("Invalid Fuel_type! Please Enter correct Fuel_type")
            except Exception as e:
                print(e)
    return helper

#validation of user name
@validate_user_name
def check_username():
    pass

#validation of password
@validate_password
def check_password():
    pass

#validation of name
@validate_Name
def check_Name():
    pass

#validation of phone
@validate_user_phone
def check_phone():
    pass

#validation of email
@validate_email_id
def check_email():
    pass

#validation of license numeber
@validate_Lic_no
def check_licno():
    pass

#validation of aadhaar number
@validate_Adhaar_no
def check_Aadhaar():
    pass

#validation of city
@validate_city
def check_city():
    pass

#validation of pincode
@validate_pincode
def check_pin():
    pass

#validation if city
@validate_state
def check_state():
    pass

#validation of company name
@validate_Company_name
def check_Cname():
    pass

#validation of model number
@validate_model_no
def check_model():
    pass

#validation of color
@validate_Color
def check_color():
    pass

#validation of price
@validate_Price
def check_price():
    pass

#validation of fuel
@validate_Fuel
def check_fuel():
    pass
    print("You'r details are successfully registered")

check_username()
check_password()
check_Name()
check_phone()
check_email()
check_licno()
check_Aadhaar()
check_city()
check_pin()
check_state()
check_Cname()
check_model()
check_color()
check_price()
check_fuel()
