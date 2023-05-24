def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    new_list = []
    for name in names:
        new_list.append(badge_maker(name))
    return new_list

def assign_rooms(names):
    new_list = []
    for name in names:
        new_list.append(f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!")
    return new_list

def printer(names):
    for name in names:
        print(badge_maker(name))
    for name in names:
        print(f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!")
