import random

def reverse_lists(self):
    output = []
    for number in self: # for loop adds the object of the list before the given index in the output list, therefore changing the position of the first numbers with the lasts.
        output.insert(0, number)
    print(output)

list_tobe_reversed = list(range(0, (random.randint(0, 10)))) #creates a random list.

reverse_lists(list_tobe_reversed)
