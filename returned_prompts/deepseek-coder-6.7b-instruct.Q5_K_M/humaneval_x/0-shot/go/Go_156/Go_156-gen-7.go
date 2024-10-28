    // Map of roman numerals to their corresponding integer values.
    m := map[int]string{
        1000: "m",
        900:  "cm",
        500:  "d",
        400:  "cd",
        100:  "c",
        90:   "xc",
        50:   "l",
        40:   "xl",
        10:   "x",
        9:    "ix",
        5:    "v",
        4:    "iv",
        1:    "i",
    }

    // List of keys in the map in descending order.
    keys := []int{1000, 900, 500, 400,