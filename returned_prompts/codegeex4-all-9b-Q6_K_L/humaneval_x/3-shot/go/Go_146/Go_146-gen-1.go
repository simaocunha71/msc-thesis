    var count int = 0
    for _, num := range nums {
        if num > 10 && (strconv.Itoa(num)[0:1] == "1" || strconv.Itoa(num)[0:1] == "3" || strconv.Itoa(num)[0:1] == "5" || strconv.Itoa(num)[0:1] == "7" || strconv.Itoa(num)[0:1] == "9") && (strconv.Itoa(num)[len(strconv.Itoa(num))-1:] == "1" || strconv.Itoa(num)[len(strconv.Itoa(num))-1:] == "3" || strconv.Itoa(num)[len(strconv.Itoa(num))-1:] == "5" || strconv.Itoa(num)[len(strconv.Itoa(num))-1:] == "7" || strconv.Itoa(num)[len(strconv.Itoa(num))-1:] == "9") {
            count += 1
        }
    }
    return count
}

The code seems to be correct and should work as expected.