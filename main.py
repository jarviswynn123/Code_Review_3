# print("Hello World")

contestants = [
    ["Binkie", 1, False, []],
    ["Butterball", 3, True, ["herding sheep", "singing", "fetch", "pulling sleds"]],
    ["Kerby", 5, True, ["swimming"]],
    ["Lucy", 5, False, ["fetch", "solving puzzles"]],
    ["Toaster", 2, False, []],
    ["Fifi", 1, False, []],
    ["Noodles", 4, True, ["pulling sleds"]]
]

labels = ["name", "age", "does_tricks", "other_talents"]

parent_list = []
parent_list_2 = []
parent_list_3 = []



def no_puppies_allowed(lst):
    for element in lst:
        if element[1] > 1: #The loop stops at the first item and does not return all 
            parent_list.append(element)
    return parent_list

# no_puppies_allowed(contestants)

no_pups = no_puppies_allowed(contestants)

def list_to_dict(lst1, lst2):
    for i in lst1:
        new_dict = dict(zip(lst2, i))
        parent_list_2.append(new_dict)
    return parent_list_2

# print(list_to_dict(no_pups, labels))

dict_created = list_to_dict(no_pups, labels)



# def assign_points(lst):
#     for i in lst:
#         i["points"] = 0
#         if i["does_tricks"] == True:
#             i["points"] += 1
#         i["points"] += len(i["other_talents"])
#         parent_list_3.append(i)
#     return parent_list_3
# # print(assign_points(dict_created))

# points_assigned = assign_points(dict_created)


# def most_points(lst):
#     for i in lst:
#         list_items = (list(i.items()))
#         for j in list_items:
#             print(max(j))
       

# most_points(points_assigned)
    
    














# def assign_points():
#     for element in dict1:
#         dict1["points"] = len(dict1["other_talents"])
#         print(dict1)
#         # if dict1["does_tricks"] == True:
#         #     dict1["points"] += 1
#             # print(dict1)
# assign_points()


# def assign_points():
#     dict1["points"] = 0
#     for element in dict1:
#         dict1['points'] += len(dict1['other_talents'])
#         return (dict1["points"])
# assign_points()





