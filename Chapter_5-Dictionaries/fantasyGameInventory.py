'''fantasyGameInventory'''

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(stuff):
    print("Inventory:")
    item_total = 0
    for k, v in stuff.items():
        print(f"{v} {k}")
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, lootToAdd):
    for item in lootToAdd:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
