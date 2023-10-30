def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    i = 1
    new_l = []
    while i < 9:
        for name in names:
            new_l.append(f"Hello, {name}! You'll be assigned to room {i}!")
            i += 1
    return new_l

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for s in badges: print(s)
    for s in rooms: print(s)