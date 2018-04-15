from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def scraper(max_pages):
	for i in range(1,max_pages):
		my_url='https://www.monster.com/jobs/search/?q=Software-Engineer&where=USA&intcid=skr_navigation_nhpso_searchMain&jobid=0a71a749-66d0-49d5-9dd8-40599a4337b3&page='+str(i)
	#Opening up connection, grabbing the content from the 

	uClient = uReq(my_url)
	page_html=uClient.read()
	uClient.close()

	#HTML parser
	page_soup=soup(page_html,"html.parser")

	#Grabs each job post
	containers=page_soup.findAll("section",{"class":"card-content"})

	filename="Jobs.csv"
	f=open(filename,"w")

	headers="Jobs, Comapny, Location\n"

	f.write(headers)

	for container in containers[1:]:
		job=container.a.text.replace("\r\n","")
		company=container.find("div",{"class":"company"}).span.text
		location=container.find("div",{"class":"location"}).span.text.replace("\r\n","")

		print("Job: "+job)
		print("Comapany: "+company)
		print("Location: "+location)

		f.write(job +","+ company +","+ location+"\n")
	f.close()

pages=input("How many page data you want? = ")
print("Scrapping the data from given website, Please wait")
scraper(int(pages))
print("\n\n\nScrapping is Done, Please check Output on Jobs.csv file\n\n")

