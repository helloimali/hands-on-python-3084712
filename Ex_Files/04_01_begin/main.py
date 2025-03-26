import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
  if not year["value"]:
    continue
  display_width = year["value"] // 10_000_000 #floor my a 10 milli
  print(f"{year['date']}: ", display_width*"=")
  