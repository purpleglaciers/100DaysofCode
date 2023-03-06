import requests
import datetime

USERNAME = "purpleglaciers (enter your own Pixela username)"
TOKEN = "YOUR_TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

practicegraph_endpoint = "https://pixe.la/v1/users/purpleglaciers/graphs/practicegraph"

# TODO 1: Create a graph with desired params using the pixe.la API
graph_params = {
    "id": "practicegraph",
    "name": "Miles_Walked_Per_Day",
    "unit": "mile",
    "type": "float",
    "color": "ajisai",
    "timezone": "US/Mountain",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# TODO 2: Retrieve needed variables (today's date, user input for miles walked.)
today = datetime.date.today()

graph_update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": float(input("How many miles did you walk today? "))
}

# TODO 3: post today's data to the pixe.la graph I created using the pixe.la API
response = requests.post(url=practicegraph_endpoint, json=graph_update_config, headers=headers)
print(response.text)

# TODO 4: Practice using HTTP put requests by updating a piece of data in my graph
# put_response = requests.put(url=f"{practicegraph_endpoint}/20230305", json={"quantity": "5"}, headers=headers)
# print(put_response.text)

# TODO 5: Practice using HTTP delete requests by deleting a piece of data from my graph
# delete_response = requests.delete(url=f"{practicegraph_endpoint}/20230305", headers=headers)
# print(delete_response.text)
