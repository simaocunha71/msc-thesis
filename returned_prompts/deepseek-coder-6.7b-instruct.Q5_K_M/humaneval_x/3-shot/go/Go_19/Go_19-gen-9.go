    num_map := map[string]string {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    }

    num_arr := strings.Split(numbers, " ")
    sort.Slice(num_arr, func(i, j int) bool {
        return num_map[num_arr[i]] < num_map[num_arr[j]]
    })

    return strings.Join(num_arr, " ")
}



