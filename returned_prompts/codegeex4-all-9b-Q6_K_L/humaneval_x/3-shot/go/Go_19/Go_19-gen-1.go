    num_map := map[string]int{
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    num_array := strings.Split(numbers," ")
    sort.Slice(num_array, func(i, j int) bool {
        return num_map[num_array[i]] < num_map[num_array[j]]
    })
    return strings.Join(num_array," ")
}

