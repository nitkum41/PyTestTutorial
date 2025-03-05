import requests

database ={
    1:"Nitesh",
    2:"Rajiv",
    3:"Shubham"
}


def get_user_from_db(user_id):
    return database[user_id]

def get_users():
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code==200:
        return response.json()
    raise requests.HTTPError