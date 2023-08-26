_player_inventory = set() #Create a set that holds the player inventory

#Function to add an item to the inventory
def collect_item(item_name):
    _player_inventory.add(item_name)
    print(f"You got the {item_name}")

#Function to remove an item from the inventory
def remove_item(item_name):
    _player_inventory.remove(item_name)

#Check if the player has an item in the inventory
def has_item(item_name):
    return item_name in _player_inventory

def contents():
    return _player_inventory

#Function to clear inventory if the player dies
def reset():
    _player_inventory = set()