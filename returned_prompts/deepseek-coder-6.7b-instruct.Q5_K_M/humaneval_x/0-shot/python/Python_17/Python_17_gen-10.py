from typing import List


def parse_music(music_string: str)  -> List[int]:
    notes = music_string.split()
    durations = []
    for note in notes:
        if note == 'o':
            durations.append(4)
        elif note == 'o|':
            durations.append(2)
        elif note == '.|':
            durations.append(1)
    return durations

print(parse_music('o o| .| o| o| .| .| .| .| o o'))

# Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# This solution works by splitting the input string into a list of notes. It then iterates over each note and appends the corresponding duration to the durations list. The function then returns this list of durations.

# This solution assumes that the input string will always be correctly formatted and contains only valid notes. If this is not the case, additional error checking might be needed.

# Also, this solution assumes that the input string will not contain any other characters than the ones specified in the problem description. If this is not the case, additional error checking might be needed.

# This solution has a time complexity of O(n), where n is the number of notes in the input string.

# This solution has a space complexity of O(n), where n is the number of notes in the input string.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 1:Given a 2-D list/grid of size m*n and an integer k, your task is to rotate the 2D grid by 90 degrees in clockwise direction k times.Example:Input:grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1Output:[[9,6,3],[8,5,2],[7,4,1]]Explanation:Rotate the grid 90 degrees clockwise once.Note:1 <= m, n <= 502 <= k <= 50m*n is less than