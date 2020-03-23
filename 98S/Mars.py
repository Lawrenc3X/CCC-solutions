excursions = int(input())

def move(steps, pos):
    if direction == 0:
        pos["ydev"] += steps
    elif direction == 1:
        pos["xdev"] += steps
    elif direction == 2:
        pos["ydev"] -= steps
    elif direction == 3:
        pos["xdev"] -= steps

for i in range(excursions):
    position = {
            "xdev" : 0,
            "ydev" : 0}
    direction = 0

    while True:
        instruction = input()

        if instruction == "0":
            break

        if direction < 0: direction += 4
        direction %= 4
        
        if instruction == "1":
            move(int(input()), position)
        elif instruction == "2":
            direction += 1
        elif instruction == "3":
            direction -= 1

    distance = abs(position["xdev"]) + abs(position["ydev"])
    print(f"Distance is {distance}")
    print(f"""xdev {position["xdev"]} ydev {position["ydev"]}""")

    if distance == 0:
        print("")
        continue

    if position["xdev"] == 0:
        print(f"ran vertical direction {direction}")
        if position["ydev"] > 0:
            right_turns = (6 - direction ) % 4
            if right_turns < 3:
                print("2\n" * right_turns, end = "")
            else:
                print("3")
            print("1")
            print(f"""{position["ydev"]}""")
        else:
            print("negative ydev")
            right_turns = 4 - direction
            if right_turns < 3:
                print("2\n" * right_turns, end = "")
            else:
                print("3")

            print("1")
            print(f"""{abs(position["ydev"])}""")

    if position["ydev"] == 0:
        print(f"ran horizontal direction {direction}")
        if position["xdev"] > 0:
            right_turns = (7 - direction) % 4
            if right_turns < 3:
                print("2\n" * right_turns, end = "")
            else:
                print("3")
            print("1")
            print(f"""{position["xdev"]}""")
        else:
            print("negative xdev")
            right_turns = (5 - direction) % 4
            print(f"right turns {right_turns}")
            if right_turns < 3:
                print("2\n" * right_turns, end = "")
            else:
                print("3")

            print("1")
            print(f"""{abs(position["xdev"])}""")

    if position["xdev"] > 0 and position["ydev"] > 0: # X+ Y+
        if direction == 0 or direction == 3: # prefer x
            pass
        else: # prefer y
            pass

    if position["xdev"] > 0 and position["ydev"] < 0: # X+ Y-
        if direction == 2 or direction == 3: # prefer x
            pass
        else: # prefer y
            pass

    if position["xdev"] < 0 and position["ydev"] > 0: # X- Y+
        if direction == 0 or direction == 1: # prefer x
            pass
        else: # prefer y
            pass

    if position["xdev"] < 0 and position["ydev"] < 0: # X- Y-
        if direction == 1 or direction == 2: # prefer x
            pass
        else: # prefer y
            pass

    print("")
