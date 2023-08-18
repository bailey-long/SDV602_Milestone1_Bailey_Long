_player_inventory = set()


def collect_item(item_name):
    _player_inventory.add(item_name)
    print(f"You got the {item_name}")


def remove_item(item_name):
    _player_inventory.remove(item_name)


def has_item(item_name):
    return item_name in _player_inventory