import textrazor


textrazor.api_key = "96ef2e58adcedc20c7b199c1603265255f4a17711bcc36c6d88e25e1"
client = textrazor.TextRazor(extractors=["entities", "topics","relations"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")

for entity in response.entities():
	print entity.matched_text