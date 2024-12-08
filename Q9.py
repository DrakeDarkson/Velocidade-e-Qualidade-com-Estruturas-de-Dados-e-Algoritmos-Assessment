# Hashtable
user_profiles = {
    "alice123": {"name": "Alice", "age": 25, "location": "São Paulo"},
    "douglas69": {"name": "Douglas", "age": 30, "location": "Rio de Janeiro"},
    "charlie98": {"name": "Charlie", "age": 22, "location": "San Francisco"},
    "luizinha23": {"name": "Luíza", "age": 28, "location": "Brasília"}
}

def get_user_profile_from_hashtable(username):
    return user_profiles.get(username, "Profile not found")

# Lista Sequencial
user_profiles_list = [
    {"username": "alice123", "name": "Alice", "age": 25, "location": "São Paulo"},
    {"username": "douglas69", "name": "Douglas", "age": 30, "location": "Rio de Janeiro"},
    {"username": "charlie98", "name": "Charlie", "age": 22, "location": "San Francisco"},
    {"username": "luizinha23", "name": "Luíza", "age": 28, "location": "Brasília"}
]
 
def find_profile_in_list(username, profiles):
    for profile in profiles:
        if profile["username"] == username:
            return profile
    return "Profile not found"

username_to_find = "charlie98"

# Hashtable
profile_from_hashtable = get_user_profile_from_hashtable(username_to_find)
print(f"Using hashtable - Profile for {username_to_find}: {profile_from_hashtable}")

# Lista Sequencial
profile_from_list = find_profile_in_list(username_to_find, user_profiles_list)
print(f"Using list - Profile for {username_to_find}: {profile_from_list}")
