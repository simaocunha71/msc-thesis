
// create a variable to store the filtered list
    var filteredStrings []string

// iterate over the input list
    for _, str := range strings {
        // check if the string starts with the prefix
        if strings.HasPrefix(str, prefix) {
            // if it does, add it to the filtered list
            filteredStrings = append(filteredStrings, str)
        }
    }

    // return the filtered list
    return filteredStrings
}

// end

```


### 3. Create a function to reverse a string.

