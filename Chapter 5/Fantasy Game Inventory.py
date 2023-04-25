inv = {
    'rope': 2,
    'torch': 1,
    'gold coin': 10
}


dragonLoot = ['gold coin', 'gold coin', 'dragon horn', 'dragon scale', 'dragon scale']

def addToInventory(inventory, addedItems):
    inv1 = inventory.copy()
    lootInv = {}
    
    for item in inventory.keys():    
        for loot in addedItems: # Loop the elements in dragonLoot
            if loot == item: #if loot in inventory.keys():
                inv1[loot] +=1 # N.B.* Advantage of using dictionaries is that you can access a value with a specific and unique word.
            elif loot not in inventory: # can't use 'else' here because it will set existing items in the inventory to zero. This line of code checks for the item in the existing inventory. 
                lootInv.setdefault(loot, 0)
    for lootItem in lootInv.keys():
        for loot in addedItems:
            if loot == lootItem:
                lootInv[lootItem] += 1
                
    updatedInv = inv1 | lootInv 
    return updatedInv # N.B.* Must return a value if part of the source code utilizes the output     
    """ '|' is one way of combining the elements of a dictionary. This will ensure that the new loot items will be added to the updated inventory."""

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0 # Is there another way to track a count beside assigning a variable to 0?
    for item, quantity in inventory.items():
        item_total += quantity
        print(str(quantity) + " " + item)
    print("Total number of items: " + str(item_total))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
