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
        if element[1] > 1:
            parent_list.append(element)
    return parent_list



no_pups = no_puppies_allowed(contestants)

def list_to_dict(lst1, lst2):
    for i in lst1:
        new_dict = dict(zip(lst2, i))
        parent_list_2.append(new_dict)
    return parent_list_2



dict_created = list_to_dict(no_pups, labels)



def assign_points(lst):
    for i in lst:
        i["points"] = 0
        if i["does_tricks"] == True:
            i["points"] += 1
        i["points"] += len(i["other_talents"])
        parent_list_3.append(i)
    return parent_list_3


points_assigned = assign_points(dict_created)




def most_points(lst):
    max_points = 0
    winning_dog = None
    for i in lst:
        if i["points"] > max_points:
            max_points = i["points"]
            winning_dog = i["name"]
    return winning_dog

winner_winner_chicken_dinner = most_points(points_assigned)



def main(*args):
    no_pups = no_puppies_allowed(contestants)
    dict_created = list_to_dict(no_pups, labels)
    points_assigned = assign_points(dict_created)
    return f"Congratulations {most_points(points_assigned)}, You have won this contest!"
main(contestants,labels)










