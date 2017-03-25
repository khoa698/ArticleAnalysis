import textrazor

textrazor.api_key = "6d70afc03f0bf77ec27fe30686bcfb685cfa324d233d81dce3e99066"

client = textrazor.TextRazor(extractors=["entities", "topics"])
response = client.analyze_url("http://www.bbc.co.uk/news/uk-politics-18640916")

for entity in response.entities():
    print entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types