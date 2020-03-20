#    from time import sleep

cases = int(input())
nums = [int(input()) for i in range(cases)]

for num in nums:
    undefeated = num
    one_loss = 0
    eliminated = 0

    r = 0
    print(f"Round 0: {undefeated} undefeated, 0 one-loss, 0 eliminated")
    while True:
        r += 1

        new_undefeated = undefeated
        new_losses = 0
        new_eliminations = 0

        if undefeated > 1:
            eliminations = undefeated //2
            new_undefeated -= eliminations
            new_losses += eliminations
        if one_loss > 1 and undefeated >= 1:
            eliminations = one_loss //2
            new_losses -= eliminations
            new_eliminations += eliminations
        
        if undefeated == 1 and one_loss == 1:
            new_undefeated -= 1
            new_losses += 1
        elif undefeated == 0 and one_loss == 2:
            one_loss -= 1
            eliminated += 1
            print(f"Round {r}: 0 undefeated, 1 one-loss, {eliminated} eliminated")
            break

# Round 0: 3 undefeated, 0 one-loss, 0 eliminated
# Round 1: 2 undefeated, 1 one-loss, 0 eliminated
# Round 2: 1 undefeated, 2 one-loss, 0 eliminated
# Round 3: 0 undefeated, 2 one-loss, 1 eliminated
# Round 4: 0 undefeated, 1 one-loss, 2 eliminated
# There are 4 rounds.
        
        undefeated = new_undefeated
        one_loss += new_losses
        eliminated += new_eliminations

        print(f"Round {r}: {undefeated} undefeated, {one_loss} one-loss, {eliminated} eliminated")

#         sleep(1)

    print(f"There are {r} rounds.")
