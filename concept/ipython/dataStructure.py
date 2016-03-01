__author__ = 'tpham'
#To change this template use Tools | Templates.

#list
shopping_list = []
#add items to list
shopping_list.append("milk")
shopping_list.append("cheese")
shopping_list.append("bread")
print(shopping_list)
#remove item from list
shopping_list.remove("milk")
print(shopping_list)
#dictionaries
food ={}
food["banana"] = "A delicious and tasty treat"
food["dirt"] = "Not delicious. Not tasty. DO NOT EAT!"
print(food)
print(food["banana"])
del food["dirt"]
print(food)
#add dictionaries to lists:
europe = []
germany = {"name":"Germany", "population":"81000000"}
europe.append(germany)
print(europe)