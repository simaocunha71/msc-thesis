"""
def all_Characters_Same(s):
    return len(set(s)) == 1


"""

# Python3 program to check if all characters
# in string are same or not.

# Function to check if all characters are same
def areAllCharactersSame(s):
    return len(set(s)) == 1


# Driver code
if __name__ == "__main__":
    assert(areAllCharactersSame("python") == False)
    print("All Characters are same")

# This code is contributed by PrinciRaj11
```