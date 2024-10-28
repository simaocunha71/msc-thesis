    var result string
    var result_array []string

    for _, c := range s {
        if (c >= 'a' && c <= 'z') {
            result_array = append(result_array, string(c))
        }else if (c >= 'A' && c <= 'Z') {
            result_array = append(result_array, string(c))
        }else {
            continue A
        }
    }

    for i := 0; i < len(result_array); i++ {
        if (i%2==1) {
            continue A
        }
        result_array[i] = string(rune(int(result_array[i][0])+2))
    }

    result = strings.Join(result_array, "")
    return result
}



