import csv
import scrapy

class Get_Poems(scrapy.Spider):
	name = "poems"
	durations = [ [1050,1375] , [1375,1700], [1700,1900] , [1900, 2020]  ]
	author_name_to_era = {}

	start_urls = ["https://kavitakosh.org/kk/index.php"]
	# start_urls = ["https://kavitakosh.org/kk/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%B0%E0%A4%B2"]
	# start_urls = ["https://kavitakosh.org/kk/%E0%A4%B5%E0%A4%A4%E0%A4%A8_%E0%A4%B9%E0%A4%AE%E0%A4%BE%E0%A4%B0%E0%A4%BE_/_%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%B0%E0%A4%B2"]
	# start_urls = ["https://kavitakosh.org/kk/%E0%A4%95%E0%A4%BE%E0%A4%81%E0%A4%9F%E0%A5%87_%E0%A4%85%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%BE%E0%A4%B0%E0%A5%87_%E0%A4%B2%E0%A4%BF%E0%A4%96%E0%A4%A4%E0%A4%BE_%E0%A4%B9%E0%A5%82%E0%A4%81_/_%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%B0%E0%A4%B2"]
	def parse123(self, response):
		authors = response.css("div.poet-list-section")
		file = open('dataset.csv', mode='w')
		poem_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

		author_links = response.css('div.poet-list-section a::attr(href)').getall()
		for author_link in author_links:
			complete_link = "https://kavitakosh.org" + author_link
			yield scrapy.Request(complete_link, self.parse_authors)

	def parse(self, response):
		author_info = response.css('div.kkparichay-box li a::attr(href)').getall()
		author_name = response.css('span#kkparichay-name::text').get()
		author_date = response.css('div.kkparichay-box table.wikitable td::text')[0].get().split()[-1]
		author_name = author_name.strip()
		self.author_name_to_era[author_name] = author_date

		with open("yoyo.txt", 'a') as file:
			file.write(" hello ")
			file.write(author_name + "~" + author_date +"\n")
		
		poem_of_author_links = response.css('li a::attr(href)').getall()
		for poem_link in poem_of_author_links:
			complete_link = "https://kavitakosh.org" + poem_link
			with open("crawled.txt", 'a') as file:
				file.write(complete_link +"\n")
			yield scrapy.Request(complete_link, self.parse_poems)

	def parse_poems(self, response):
		author_poem = response.css('h1.firstHeading span::text').get()
		if( author_poem is not None ):
			author_poem = author_poem.split('/', 2)

			if( len(author_poem) > 1 ):
				author_name = author_poem[1]
				poem_name = author_poem[0]
				
				author_name = author_name.strip()
				poem_name = poem_name.strip()

				with open("eng.txt", 'a') as file:
					file.write(poem_name + "~" + author_name + "\n")
				
				does_poem_exist = response.css('div.poem').get()
				if does_poem_exist is not None:
					with open("hi.txt", 'a') as file:
						file.write(poem_name + "~" + author_name + "\n")
					poem_lines = response.css('div.poem p::text').getall()
					poem = ""
					if poem_lines is not None:
						for line in poem_lines:
							line = line.strip()
							poem += line
						poem = poem.strip()

						if poem != "":
							with open("poems_collection.txt", 'a') as file:
								file.write(author_name  + "~"+ self.author_name_to_era[author_name]  + "~" + poem_name + "~" + poem +"~" + "\n")
