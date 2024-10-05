    max := l[0]
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
} // Time complexity: O(n), where n is the length of the list. Space complexity: O(1) since we are using a constant amount of space.