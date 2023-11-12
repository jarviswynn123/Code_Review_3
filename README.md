Write the following in a file called main.py or a notebook called main.ipynb:

1. Copy and paste `contestants` and `labels` to the top of your code. Notice that `contestants` contains nested lists:

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


Each item in the inner lists in `contestants` matches the item at that index in the labels list (i.e. the first item is the dog’s name, the second item is their age, the third item is whether they can do tricks, and the fourth item is a list of their talents).


2. Write a function called `no_puppies_allowed()` that can take the `contestants` list as an argument.
`no_puppies_allowed()` should remove any contestants from `contestants`  whose age (at index 1 of each inner list) is not greater than 1. No puppies allowed!
`no_puppies_allowed()` should return the new list of contestants.



If you pass `contestants` as an argument to `no_puppies_allowed()` like this:


no_puppies_allowed(contestants)

…the return value should match this:

	[
    ["Butterball", 3, True, ["herding sheep", "singing", "fetch", "pulling sleds"]],
    ["Kerby", 5, True, ["swimming"]],
    ["Lucy", 5, False, ["fetch", "solving puzzles"]],
    ["Toaster", 2, False, []],
    ["Noodles", 4, True, ["pulling sleds"]]
]





3. Write a function called `lists_to_dicts()` that can take lists like `labels` and the return value of `no_puppies_allowed()` as arguments. 
`lists_to_dicts()` should return the list of dictionaries.
Each dictionary should represent one dog, with labels as keys and that dog’s info as the values.

If you pass `labels` and the return value of `no_puppies_allowed()` as arguments to `lists_to_dicts()` , it should return something like this:

[
{'name': 'Butterball', 'age': 3, 'does_tricks': True, 'other_talents': ['herding sheep', 'singing', 'fetch', 'pulling sleds']}, 
{'name': 'Kerby', 'age': 5, 'does_tricks': True, 'other_talents': ['swimming']}, {'name': 'Lucy', 'age': 5, 'does_tricks': False, 'other_talents': ['fetch', 'solving puzzles']}, 
{'name': 'Toaster', 'age': 2, 'does_tricks': False, 'other_talents': []}, 
{'name': 'Noodles', 'age': 4, 'does_tricks': True, 'other_talents': ['pulling sleds']}
]



4. Write a function called `assign_points()` that can take the return value of `lists_to_dicts()` as an argument.
`assign_points()` should add a new key-value pair to each dictionary. The key is the string “points”, and the value will be the number of points for that dog.
`assign_points()` should add 1 point if `does_tricks` is True.
`assign_points()` should add 1 point for each item in the dog’s `other_talents`.
`assign_points()` should return the list of dictionaries that now include points.

If you pass the return value of `lists_to_dicts()` as an argument to `assign_points()`, it should return something like this:

[
{'name': 'Butterball', 'age': 3, 'does_tricks': True, 'other_talents': ['herding sheep', 'singing', 'fetch', 'pulling sleds'], 'points': 5}, 
{'name': 'Kerby', 'age': 5, 'does_tricks': True, 'other_talents': ['swimming'], 'points': 2}, {'name': 'Lucy', 'age': 5, 'does_tricks': False, 'other_talents': ['fetch', 'solving puzzles'], 'points': 2}, 
{'name': 'Toaster', 'age': 2, 'does_tricks': False, 'other_talents': [], 'points': 0}, 
{'name': 'Noodles', 'age': 4, 'does_tricks': True, 'other_talents': ['pulling sleds'], 'points': 2}
]


5. Now, pick a winner!
Write a function called `most_points()` that can take the return value of `assign_points()` as an argument.
`most_points()` should find the dog with the most points.
Have `most_points()` print a message to congratulate the winner.
`most_points()` should return a string containing the name of the winning dog.


6. Put it all together in a `main()` function.

`main()` should be able to take lists like `contestants` and `labels` as arguments.
`main()` should use those arguments to run the functions outlined above, in that order. It should pass the return value of each function to the next function in the sequence.
`main() should return the name of the winner. 

7. Call `main()` with `contestants` and `labels` as arguments.
…and congratulate the dog who won!
