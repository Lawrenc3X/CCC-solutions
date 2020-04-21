from typing import Generator

num_of_boards = int(input())
boards = [int(i) for i in input().split(" ")]
seen_lengths =[]
fence_lengths = []

def sack_explore(length:int, istart:int, jstart:int) -> Generator[int, None, None]:
    pass

for index, board_1 in enumerate(boards[:-1]):
    for jindex, board_2 in enumerate(boards[index + 1:]):
        current_length = board1 + board2

        if current_length not in seen_lengths:
            seen_lengths.append(current_length)
            
            longest_fence = 0
            for fence_length in sack_explore(current_length, index, jindex):
                if fence_length > longest_fence:
                    longest_fence = fence_length

            fence_lengths.append(longest_fence)
