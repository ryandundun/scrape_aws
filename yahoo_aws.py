#yahoo.py

from bs4 import BeautifulSoup
import subprocess
#import pyautogui
import time
import requests
import bs4
import random
import webbrowser
import csv
import threading
import os
import json
#import Tkinter as tk
import datetime
import pandas as pd
import re
import datetime
import time
from random import randint
from playwright.sync_api import sync_playwright, TimeoutError
import sys

minSleep = 7
maxSleep = 7

'''
python3 yahoo_multiple.py yahoo_mul_1.csv house+plaster 'New York'
python3 yahoo_multiple.py yahoo_mul_2.csv house+decks 'New York'
python3 yahoo_multiple.py yahoo_mul_3.csv concrete 'Fremont'
python3 yahoo_multiple.py yahoo_mul_4.csv house+abatement 'Janesville'

From Painting - garage door

Outstanding:
python3 yahoo_multiple.py yahoo_mul_1.csv house+plaster 'Bolingbrook'
python3 yahoo_multiple.py yahoo_mul_2.csv flooring 'Bend'
python3 yahoo_multiple.py yahoo_mul_3.csv handyman 'Bolingbrook'
python3 yahoo_multiple.py yahoo_mul_4.csv house+electrical 'Bolingbrook'


'''

listOfCities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Indianapolis', 'Jacksonville', 'San Francisco', 'Columbus', 'Charlotte', 'Fort Worth', 'Detroit', 'El Paso', 'Memphis', 'Seattle', 'Denver', 'Washington', 'Boston', 'Nashville-Davidson', 'Baltimore', 'Oklahoma City', 'Louisville/Jefferson County', 'Portland', 'Las Vegas', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Sacramento', 'Long Beach', 'Kansas City', 'Mesa', 'Virginia Beach', 'Atlanta', 'Colorado Springs', 'Omaha', 'Raleigh', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Cleveland', 'Wichita', 'Arlington', 'New Orleans', 'Bakersfield', 'Tampa', 'Honolulu', 'Aurora', 'Anaheim', 'Santa Ana', 'St. Louis', 'Riverside', 'Corpus Christi', 'Lexington-Fayette', 'Pittsburgh', 'Anchorage', 'Stockton', 'Cincinnati', 'St. Paul', 'Toledo', 'Greensboro', 'Newark', 'Plano', 'Henderson', 'Lincoln', 'Buffalo', 'Jersey City', 'Chula Vista', 'Fort Wayne', 'Orlando', 'St. Petersburg', 'Chandler', 'Laredo', 'Norfolk', 'Durham', 'Madison', 'Lubbock', 'Irvine', 'Winston-Salem', 'Glendale', 'Garland', 'Hialeah', 'Reno', 'Chesapeake', 'Gilbert', 'Baton Rouge', 'Irving', 'Scottsdale', 'North Las Vegas', 'Fremont', 'Boise City', 'Richmond', 'San Bernardino', 'Birmingham', 'Spokane', 'Rochester', 'Des Moines', 'Modesto', 'Fayetteville', 'Tacoma', 'Oxnard', 'Fontana', 'Montgomery', 'Moreno Valley', 'Shreveport', 'Yonkers', 'Akron', 'Huntington Beach', 'Little Rock', 'Augusta-Richmond County', 'Amarillo', 'Mobile', 'Grand Rapids', 'Salt Lake City', 'Tallahassee', 'Huntsville', 'Grand Prairie', 'Knoxville', 'Worcester', 'Newport News', 'Brownsville', 'Overland Park', 'Santa Clarita', 'Providence', 'Garden Grove', 'Chattanooga', 'Oceanside', 'Jackson', 'Fort Lauderdale', 'Santa Rosa', 'Rancho Cucamonga', 'Port St. Lucie', 'Tempe', 'Ontario', 'Vancouver', 'Cape Coral', 'Sioux Falls', 'Springfield', 'Peoria', 'Pembroke Pines', 'Elk Grove', 'Salem', 'Lancaster', 'Corona', 'Eugene', 'Palmdale', 'Salinas', 'Pasadena', 'Fort Collins', 'Hayward', 'Pomona', 'Cary', 'Rockford', 'Alexandria', 'Escondido', 'McKinney', 'Joliet', 'Sunnyvale', 'Torrance', 'Bridgeport', 'Lakewood', 'Hollywood', 'Paterson', 'Naperville', 'Syracuse', 'Mesquite', 'Dayton', 'Savannah', 'Clarksville', 'Orange', 'Fullerton', 'Killeen', 'Frisco', 'Hampton', 'McAllen', 'Warren', 'Bellevue', 'West Valley City', 'Columbia', 'Olathe', 'Sterling Heights', 'New Haven', 'Miramar', 'Waco', 'Thousand Oaks', 'Cedar Rapids', 'Charleston', 'Visalia', 'Topeka', 'Elizabeth', 'Gainesville', 'Thornton', 'Roseville', 'Carrollton', 'Coral Springs', 'Stamford', 'Simi Valley', 'Concord', 'Hartford', 'Kent', 'Lafayette', 'Midland', 'Surprise', 'Denton', 'Victorville', 'Evansville', 'Santa Clara', 'Abilene', 'Athens-Clarke County', 'Vallejo', 'Allentown', 'Norman', 'Beaumont', 'Independence', 'Murfreesboro', 'Ann Arbor', 'Berkeley', 'Provo', 'El Monte', 'Lansing', 'Fargo', 'Downey', 'Costa Mesa', 'Wilmington', 'Arvada', 'Inglewood', 'Miami Gardens', 'Carlsbad', 'Westminster', 'Odessa', 'Manchester', 'Elgin', 'West Jordan', 'Round Rock', 'Clearwater', 'Waterbury', 'Gresham', 'Fairfield', 'Billings', 'Lowell', 'San Buenaventura (Ventura)', 'Pueblo', 'High Point', 'West Covina', 'Murrieta', 'Cambridge', 'Antioch', 'Temecula', 'Norwalk', 'Centennial', 'Everett', 'Palm Bay', 'Wichita Falls', 'Green Bay', 'Daly City', 'Burbank', 'Richardson', 'Pompano Beach', 'North Charleston', 'Broken Arrow', 'Boulder', 'West Palm Beach', 'Santa Maria', 'El Cajon', 'Davenport', 'Rialto', 'Las Cruces', 'San Mateo', 'Lewisville', 'South Bend', 'Lakeland', 'Erie', 'Tyler', 'Pearland', 'College Station', 'Kenosha', 'Sandy Springs', 'Clovis', 'Flint', 'Roanoke', 'Albany', 'Jurupa Valley', 'Compton', 'San Angelo', 'Hillsboro', 'Lawton', 'Renton', 'Vista', 'Davie', 'Greeley', 'Mission Viejo', 'Portsmouth', 'Dearborn', 'South Gate', 'Tuscaloosa', 'Livonia', 'New Bedford', 'Vacaville', 'Brockton', 'Roswell', 'Beaverton', 'Quincy', 'Sparks', 'Yakima', "Lee's Summit", 'Federal Way', 'Carson', 'Santa Monica', 'Hesperia', 'Allen', 'Rio Rancho', 'Yuma', 'Orem', 'Lynn', 'Redding', 'Spokane Valley', 'Miami Beach', 'League City', 'Lawrence', 'Santa Barbara', 'Plantation', 'Sandy', 'Sunrise', 'Macon', 'Longmont', 'Boca Raton', 'San Marcos', 'Greenville', 'Waukegan', 'Fall River', 'Chico', 'Newton', 'San Leandro', 'Reading', 'Fort Smith', 'Newport Beach', 'Asheville', 'Nashua', 'Edmond', 'Whittier', 'Nampa', 'Bloomington', 'Deltona', 'Hawthorne', 'Duluth', 'Carmel', 'Suffolk', 'Clifton', 'Citrus Heights', 'Livermore', 'Tracy', 'Alhambra', 'Kirkland', 'Trenton', 'Ogden', 'Hoover', 'Cicero', 'Fishers', 'Sugar Land', 'Danbury', 'Meridian', 'Indio', 'Menifee', 'Champaign', 'Buena Park', 'Troy', "O'Fallon", 'Johns Creek', 'Bellingham', 'Westland', 'Sioux City', 'Warwick', 'Hemet', 'Longview', 'Farmington Hills', 'Bend', 'Merced', 'Mission', 'Chino', 'Redwood City', 'Edinburg', 'Cranston', 'Parma', 'New Rochelle', 'Lake Forest', 'Napa', 'Hammond', 'Avondale', 'Somerville', 'Palm Coast', 'Bryan', 'Gary', 'Largo', 'Brooklyn Park', 'Tustin', 'Racine', 'Deerfield Beach', 'Lynchburg', 'Mountain View', 'Medford', 'Bellflower', 'Melbourne', 'St. Joseph', 'Camden', 'St. George', 'Kennewick', 'Baldwin Park', 'Chino Hills', 'Alameda', 'Arlington Heights', 'Scranton', 'Evanston', 'Kalamazoo', 'Baytown', 'Upland', 'Springdale', 'Bethlehem', 'Schaumburg', 'Mount Pleasant', 'Auburn', 'Decatur', 'San Ramon', 'Pleasanton', 'Wyoming', 'Lake Charles', 'Plymouth', 'Bolingbrook', 'Pharr', 'Appleton', 'Gastonia', 'Folsom', 'Southfield', 'Rochester Hills', 'New Britain', 'Goodyear', 'Canton', 'Warner Robins', 'Union City', 'Perris', 'Manteca', 'Iowa City', 'Jonesboro', 'Lynwood', 'Loveland', 'Pawtucket', 'Boynton Beach', 'Waukesha', 'Gulfport', 'Apple Valley', 'Passaic', 'Rapid City', 'Layton', 'Turlock', 'Muncie', 'Temple', 'Missouri City', 'Redlands', 'Santa Fe', 'Lauderhill', 'Milpitas', 'Palatine', 'Missoula', 'Rock Hill', 'Franklin', 'Flagstaff', 'Flower Mound', 'Weston', 'Waterloo', 'Mount Vernon', 'Fort Myers', 'Dothan', 'Rancho Cordova', 'Redondo Beach', 'Pasco', 'St. Charles', 'Eau Claire', 'North Richland Hills', 'Bismarck', 'Yorba Linda', 'Kenner', 'Walnut Creek', 'Frederick', 'Oshkosh', 'Pittsburg', 'Palo Alto', 'Bossier City', 'St. Cloud', 'Davis', 'South San Francisco', 'Camarillo', 'North Little Rock', 'Schenectady', 'Gaithersburg', 'Harlingen', 'Woodbury', 'Eagan', 'Yuba City', 'Maple Grove', 'Youngstown', 'Skokie', 'Kissimmee', 'Johnson City', 'Victoria', 'San Clemente', 'Bayonne', 'Laguna Niguel', 'East Orange', 'Shawnee', 'Homestead', 'Rockville', 'Delray Beach', 'Janesville', 'Conway', 'Pico Rivera', 'Lorain', 'Montebello', 'Lodi', 'New Braunfels', 'Marysville', 'Tamarac', 'Madera', 'Conroe', 'Santa Cruz', 'Eden Prairie', 'Cheyenne', 'Daytona Beach', 'Alpharetta', 'Hamilton', 'Waltham', 'Coon Rapids', 'Haverhill', 'Council Bluffs', 'Taylor', 'Utica', 'Ames', 'La Habra', 'Encinitas', 'Bowling Green', 'Burnsville', 'West Des Moines', 'Cedar Park', 'Tulare', 'Monterey Park', 'Vineland', 'Terre Haute', 'North Miami', 'Mansfield', 'West Allis', 'Bristol', 'Taylorsville', 'Malden', 'Meriden', 'Blaine', 'Wellington', 'Cupertino', 'Rogers', 'St. Clair Shores', 'Gardena', 'Pontiac', 'National City', 'Grand Junction', 'Rocklin', 'Chapel Hill', 'Casper', 'Broomfield', 'Petaluma', 'South Jordan', 'Great Falls', 'North Port', 'Marietta', 'San Rafael', 'Royal Oak', 'Des Plaines', 'Huntington Park', 'La Mesa', 'Orland Park', 'Lakeville', 'Owensboro', 'Moore', 'Jupiter', 'Idaho Falls', 'Dubuque', 'Bartlett', 'Rowlett', 'Novi', 'White Plains', 'Arcadia', 'Redmond', 'Lake Elsinore', 'Ocala', 'Tinley Park', 'Port Orange', 'Oak Lawn', 'Rocky Mount', 'Kokomo', 'Coconut Creek', 'Bowie', 'Berwyn', 'Midwest City', 'Fountain Valley', 'Buckeye', 'Dearborn Heights', 'Woodland', 'Noblesville', 'Valdosta', 'Diamond Bar', 'Manhattan', 'Santee', 'Taunton', 'Sanford', 'Kettering', 'New Brunswick', 'Chicopee', 'Anderson', 'Margate', 'Weymouth Town', 'Hempstead', 'Corvallis', 'Eastvale', 'Porterville', 'West Haven', 'Brentwood', 'Paramount', 'Grand Forks', 'Georgetown', 'St. Peters', 'Shoreline', 'Mount Prospect', 'Hanford', 'Normal', 'Rosemead', 'Lehi', 'Pocatello', 'Highland', 'Novato', 'Port Arthur', 'Carson City', 'Hendersonville', 'Elyria', 'Revere', 'Pflugerville', 'Greenwood', 'Wheaton', 'Smyrna', 'Sarasota', 'Blue Springs', 'Colton', 'Euless', 'Castle Rock', 'Cathedral City', 'Kingsport', 'Lake Havasu City', 'Pensacola', 'Hoboken', 'Yucaipa', 'Watsonville', 'Richland', 'Delano', 'Hoffman Estates', 'Florissant', 'Placentia', 'West New York', 'Dublin', 'Oak Park', 'Peabody', 'Perth Amboy', 'Battle Creek', 'Bradenton', 'Gilroy', 'Milford', 'Ankeny', 'La Crosse', 'Burlington', 'DeSoto', 'Harrisonburg', 'Minnetonka', 'Elkhart', 'Glendora', 'Southaven', 'Joplin', 'Enid', 'Palm Beach Gardens', 'Brookhaven', 'Plainfield', 'Grand Island', 'Palm Desert', 'Huntersville', 'Tigard', 'Lenexa', 'Saginaw', 'Kentwood', 'Doral', 'Grapevine', 'Aliso Viejo', 'Sammamish', 'Casa Grande', 'Pinellas Park', 'West Sacramento', 'Burien', 'Commerce City', 'Monroe', 'Cerritos', 'Downers Grove', 'Coral Gables', 'Wilson', 'Niagara Falls', 'Poway', 'Edina', 'Cuyahoga Falls', 'Rancho Santa Margarita', 'Harrisburg', 'Huntington', 'La Mirada', 'Cypress', 'Caldwell', 'Logan', 'Galveston', 'Sheboygan', 'Middletown', 'Murray', 'Parker', 'Bedford', 'East Lansing', 'Methuen', 'Covina', 'Olympia', 'Euclid', 'Mishawaka', 'Salina', 'Azusa', 'Chesterfield', 'Leesburg', 'Dunwoody', 'Hattiesburg', 'Bonita Springs', 'Portage', 'St. Louis Park', 'Collierville', 'Stillwater', 'East Providence', 'Wauwatosa', 'Mentor', 'Ceres', 'Cedar Hill', 'Binghamton', "Coeur d'Alene", 'San Luis Obispo', 'Minot', 'Palm Springs', 'Pine Bluff', 'Texas City', 'Summerville', 'Twin Falls', 'Jeffersonville', 'San Jacinto', 'Altoona', 'Beavercreek', 'Apopka', 'Elmhurst', 'Maricopa', 'Farmington', 'Glenview', 'Cleveland Heights', 'Draper', 'Sierra Vista', 'Lacey', 'Biloxi', 'Strongsville', 'Barnstable Town', 'Wylie', 'Sayreville', 'Kannapolis', 'Charlottesville', 'Littleton', 'Titusville', 'Hackensack', 'Pittsfield', 'York', 'Lombard', 'Attleboro', 'DeKalb', 'Blacksburg', 'Haltom City', 'Lompoc', 'El Centro', 'Danville', 'Jefferson City', 'Cutler Bay', 'Oakland Park', 'North Miami Beach', 'Freeport', 'Moline', 'Coachella', 'Fort Pierce', 'Bountiful', 'Fond du Lac', 'Keller', 'Belleville', 'Bell Gardens', 'North Lauderdale', 'Rancho Palos Verdes', 'San Bruno', 'Apex', 'Altamonte Springs', 'Hutchinson', 'Buffalo Grove', 'Urbandale', 'State College', 'Urbana', 'Manassas', 'Kearny', 'Oro Valley', 'Findlay', 'Rohnert Park', 'Westfield', 'Linden', 'Sumter', 'Wilkes-Barre', 'Woonsocket', 'Leominster', 'Shelton', 'Brea', 'Covington', 'Rockwall', 'Riverton', 'Morgan Hill', 'Edmonds', 'Burleson', 'Beverly', 'Mankato', 'Hagerstown', 'Prescott', 'Campbell', 'Cedar Falls', 'La Puente', 'Crystal Lake', 'Fitchburg', 'Carol Stream', 'Hickory', 'Streamwood', 'Norwich', 'Coppell', 'San Gabriel', 'Holyoke', 'Bentonville', 'Florence', 'Peachtree Corners', 'Bozeman', 'New Berlin', 'Goose Creek', 'Prescott Valley', 'Maplewood', 'Romeoville', 'Duncanville', 'Atlantic City', 'The Colony', 'Culver City', 'Marlborough', 'Hilton Head Island', 'Moorhead', 'Calexico', 'Bullhead City', 'Germantown', 'La Quinta', 'Wausau', 'Sherman', 'Ocoee', 'Shakopee', 'Woburn', 'Bremerton', 'Rock Island', 'Muskogee', 'Cape Girardeau', 'Annapolis', 'Greenacres', 'Ormond Beach', 'Hallandale Beach', 'Stanton', 'Puyallup', 'Pacifica', 'Hanover Park', 'Hurst', 'Lima', 'Marana', 'Carpentersville', 'Oakley', 'Huber Heights', 'Montclair', 'Wheeling', 'Brookfield', 'Park Ridge', 'Roy', 'Winter Garden', 'Chelsea', 'Valley Stream', 'Spartanburg', 'Lake Oswego', 'Friendswood', 'Westerville', 'Northglenn', 'Phenix City', 'Grove City', 'Texarkana', 'Addison', 'Dover', 'Lincoln Park', 'Calumet City', 'Muskegon', 'Aventura', 'Martinez', 'Greenfield', 'Apache Junction', 'Monrovia', 'Weslaco', 'Keizer', 'Spanish Fork', 'Beloit', 'Panama City']


#get rid of already scraped lists
startScrapeAt = sys.argv[3]
newList = []
boolean = False
for i in range(len(listOfCities)):
	if listOfCities[i] == startScrapeAt:
		boolean = True
	if boolean:
		newList.append(listOfCities[i])
listOfCities = newList




fileName = sys.argv[1]

site = 'https://search.yahoo.com/local/s;_ylt=AwrJ61hPpq9iYz0AgzrumYlQ;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=painting+contractors+new+york&pz=15&fr=yfp-t&b=1&pz=15&xargs=0'

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=True)
page = browser.new_page()


#scraping part
def scrapePage(city, site, page, notFinished=True, iteration=1, count=0):

	while notFinished:
		try:
			html = page.content()
		except:
			try:
				print('CONNECTION ISSUE HTML')
				time.sleep(60)
				html = page.content()
			except:
				try:
					print('CONNECTION ISSUE HTML - 2')
					time.sleep(120)
					html = page.content()
				except:
					try:
						print('CONNECTION ISSUE HTML - 3')
						time.sleep(150)
						page.reload()
						time.sleep(150)
						html = page.content()
					except:
						print('CONNECTION ISSUE HTML - 4')
						time.sleep(20)
						page.close()
						time.sleep(20)
						page = browser.new_page()
						time.sleep(20)
						html = page.content()

		soup = bs4.BeautifulSoup(html, "html.parser")
		#search = soup.find_all("li", {"data-idx": "0"})

		# compName = search[0].find_all("div",{"class":"title"})[0].get_text()
		# phoneNumber = search[0].get_text()[-14:]
		# URL = str(search[0].find_all("div",{"class":"title"})[0]).split('href="')[1].split('"')[0]


		#company name & phone number
		listOfNames = []
		listOfPhoneNumbers = []
		listOfURLS = []
		emptyCount = 0
		for i in range(15):
			try:
				search = soup.find_all("li", {"data-idx": str(i)})
				compName = search[0].find_all("div",{"class":"title"})[0].get_text()
				phoneNumber = search[0].get_text()[-14:]
				#URL = str(search[0].find_all("div",{"class":"title"})[0]).split('href="')[1].split('"')[0]
				theId = str(search[0]).split('data-jxid="')[1].split('"')[0]
				URL = 'https://local.yahoo.com/info-' + str(theId)
				emptyCount = 0
			except:
				if (len(search) == 0):
					try:
						print('Length of search is 0')
						time.sleep(5)
						html = page.content()
						soup = bs4.BeautifulSoup(html, "html.parser")
						search = soup.find_all("li", {"data-idx": str(i)})
						compName = search[0].find_all("div",{"class":"title"})[0].get_text()
						phoneNumber = search[0].get_text()[-14:]
						#URL = str(search[0].find_all("div",{"class":"title"})[0]).split('href="')[1].split('"')[0]
						theId = str(search[0]).split('data-jxid="')[1].split('"')[0]
						URL = 'https://local.yahoo.com/info-' + str(theId)	
					except:
						print("")
						print('Data cannot be found... continuing. Empty Count: ' + str(emptyCount))
						print("___________________")

						emptyCount += 1
						if emptyCount > 2:
							print("EMPTY COUNT HAS MET THREASHOLD")
							break
						else:
							continue
				else:
					print("")
					print('Data cannot be found... continuing. Empty Count: ' + str(emptyCount))
					print("___________________")
					continue



			print("")
			print(compName)
			print(URL)
			print(phoneNumber)
			print("___________________")
			listOfURLS.append(URL)
			listOfNames.append(compName)
			listOfPhoneNumbers.append(phoneNumber)



		

		#write the data to a csv
		df = pd.DataFrame(listOfNames, columns= ['Company Name'])
		df["Phone Numbers"] = listOfPhoneNumbers
		df["Profile URLs"] = listOfURLS

		#Grabbing last CSV or creating new one if first time
		if (iteration == 1):
			try:
				bigDF = pd.read_csv(fileName)
				print('')
				print('the file already exists and is length:')
				print(len(bigDF))
				bigDF = bigDF.append(df, sort=False)
			except:
				bigDF = df
				print('')
				print("File does not already exist - first round, set the bigDF variable")
		else:
			print('')
			print('Length before: ' + str(len(bigDF)))
			bigDF = bigDF.append(df, sort=False)
			print('Length after: ' + str(len(bigDF)))


		#writing to the CSV
		bigDF.to_csv(fileName, index=False)
		print("Written BIG file")
		print("Iteration: " + str(iteration) + " complete. Count = " + str(count) + ". City: " + city)
		print('URL was ')
		print(site)
		lenBigDF = len(bigDF)
		print("Length of Big Dataframe is: " + str(lenBigDF))
		print(str(fileName) + ". C Type: " + str(sys.argv[2]) + ". City Start: " + str(sys.argv[3]))
		print('NEW CITY: ' + str(city))
		print("_______________________________")
		print("")
		count += 10
		iteration += 1
		

		#try to click next page
		try:
			#click to next page
			xpath = '//a[@class="next"]'
			page.click(xpath, delay = 3)
		except:
			print("")
			print("MOVING ON TO NEXT CITY")
			print("")
			notFinished = False
			continue

		#stop endless
		if iteration > 45:
			print('On iteration 35, moving on...')
			notFinished = False
			time.sleep(2)

		time.sleep(randint(minSleep, maxSleep))


#site = 'https://www.google.com/search?rlz=1C5CHFA_enUS772US775&tbs=lf:1,lf_ui:14&tbm=lcl&sxsrf=ALiCzsZf2fqGz4Xp4woZ19cHMtKEpZFc2Q:1654541970866&q=landscape+new+york+contractors&rflfq=1&num=10&sa=X&ved=2ahUKEwiB2sGTwZn4AhXaj4kEHQRaBd8QjGp6BAgCEE8&biw=1348&bih=704&dpr=2#rlfi=hd:;si:13207495435885287728,a;mv:[[40.924668499999996,-73.8808562],[40.6410396,-74.021506]]'
cityCount = 1

for i in range(len(listOfCities)):

	nextCity = listOfCities[i]
	citySplit = nextCity.split(' ')
	if len(citySplit) > 1:
		city = citySplit[0] + '+'  + citySplit[1]
	else:
		city = citySplit[0]
	#so far have done deck, window, cleaning+service, painting, fence tree+service, concrete, insulation, avac, roofing, lawn+care,
	#waste+material+remover, doors, landscaping,welder, pest+control,appliances, cabinet, moving, paving, solar, tile, cleaniing serviecs, roofing & gutters
	typeOfContractor = sys.argv[2]
	site = 'https://search.yahoo.com/local/s;_ylt=AwrJ61hPpq9iYz0AgzrumYlQ;_ylu=Y29sbwNiZjEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=' + typeOfContractor + '+contractors+' + city + '&pz=15&fr=yfp-t&b=1&pz=15&xargs=0'

	print('')
	print("####################################")
	print("####################################")
	print("#########  Now doing city: " + nextCity)
	print("#########  City count is: " + str(cityCount))
	print("####################################")
	print("####################################")
	print('')
	try:
		page.goto(site)
	except:
		try:
			print('CONNECTION ERROR')
			time.sleep(60)
			page.goto(site)
		except:
			try:
				print('CONNECTION ERROR - 2')
				time.sleep(120)
				page.goto(site)
			except:
				try:
					print('CONNECTION ERROR - 3')
					time.sleep(100)
					page.reload()
					time.sleep(100)
					page.goto(site)
				except:
					print('CONNECTION ERROR - 4')
					time.sleep(20)
					page.close()
					time.sleep(20)
					page = browser.new_page()
					time.sleep(20)
					page.goto(site)

	time.sleep(2)
	scrapePage(nextCity, site, page)
	cityCount += 1

print("")
print("SCRAPING IS COMPLETE FOR YAHOO")
print("")


'''
from playwright.sync_api import sync_playwright, TimeoutError
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto(site)
html = page.content()
soup = bs4.BeautifulSoup(html, "html.parser")
search = soup.find_all("a", {"class": "listings-item"})
search[0].find_all("div", {"class": "b_factrow"})
'''

