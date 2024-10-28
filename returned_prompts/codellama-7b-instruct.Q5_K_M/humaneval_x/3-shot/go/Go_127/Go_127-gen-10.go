    if (interval1[0] < interval2[1] && interval1[1] > interval2[0]) {
        if (interval1[1] - interval1[0] == 1) {
            return "NO"
        }
        if (interval1[1] - interval1[0] > 1) {
            if (math.Mod(interval1[1]-interval1[0], 2) != 0) {
                return "YES"
            }
        }
    }
    return "NO"
}



