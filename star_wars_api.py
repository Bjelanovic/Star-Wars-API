import requests

def fetch_data(option, count): # Function that is fetching data based on count
  result = []
  
  
  
  url = f"https://swapi.dev/api/{option}/"
  while len(result) < count:
    try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()
      result.extend(data["results"]) #Extened the data with key "results"
      print(f"Number of entries: {len(result)}") # Number of Entries 
      url = data["next"]

    except requests.HTTPError as e:
      return None

    if url is None:
      break
  return result[:count] #This will slice the list to specifed count

count = int(input("Download number of entities:")) # input for user
result = fetch_data("people", count) #Function that calls after user inputs data

if result: 
    for entity in result:
      print(entity["name"])
else:
    print("Unable to download data")  
