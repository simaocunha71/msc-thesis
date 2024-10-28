    length := len(l)

    if length < 3 {
        return false
    }

    sort.Ints(l)

    for i := 0; i < length - 2; i++ {
        if l[i] > 0 {
            return false
        }

        j := i + 1
        k := length - 1

        while j < k {
            sum := l[i] + l[j] + l[k]

            if sum < 0 {
                j += 1
            } else if sum > 0 {
                k -= 1
            } else {
                return true
            }
        }
    }

    return false
}



