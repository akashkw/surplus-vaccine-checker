import smtplib
from selenium import webdriver
from time import sleep

carriers = {
	'att':    '@mms.att.net',
	'tmobile':' @tmomail.net',
	'verizon':  '@vtext.com',
	'sprint':   '@page.nextel.com'
}

def send(number, message):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = '{}{}'.format(number, carriers['att'])
	auth = ('email', 'password')

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)

some_text = "ATTENTION: Sign up for vaccines now!"

numbers = ["5557777"]

vacc_url = "vaccurl.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver=webdriver.Chrome(chrome_options=chrome_options)

print("Running Vaccine Checker")
while True:
    try:
        driver.get(vacc_url)
        driver.switch_to.frame(0)
        contents = str(driver.page_source)
        if ("No services were set up." in contents) or ("No spots available" in contents):
            sleep(10)
        else:
            print("Vaccines available")
            for number in numbers:
                send(number, some_text)
            sleep(120)
    except Exception as e:
        print("ERROR:", e)
        sleep(20)

driver.quit()


