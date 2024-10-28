    var count int
    var index int
    for index = 0; index < len(str); index++ {
        if index+len(substring) <= len(str) {
            if str[index : index+len(substring)] == substring {
                count++
            }
        }
    }

    return count
}


// Find how many times a given substring can be found in the original string. Do not count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 2
// >>> HowManyTimes('aaaa', 'aa')
// 2
func HowManyTimes1(str string,substring string) int{
    var count int
    var index int
    for index = 0; index < len(str); index++ {
        if index+len(substring) <= len(str) {
            if str[index : index+len(substring)] == substring {
                count++
            }
        }
    }
    return count
}


// Find how many times a given substring can be found in the original string. Count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 3
// >>> HowManyTimes('aaaa', 'aa')
// 3
func HowManyTimes2(str string,substring string) int{
    var count int
    var index int
    for index = 0; index < len(str); index++ {
        if index+len(substring) <= len(str) {
            if str[index : index+len(substring)] == substring {
                count++
            }
        }
    }

    return count
}


// Find how many times a given substring can be found in the original string. Do not count overlaping cases.
// >>> HowManyTimes('', 'a')
// 0
// >>> HowManyTimes('aaa', 'a')
// 2
// >>> HowManyTimes('aaaa', 'aa')
// 2
func HowManyTimes3(str string,substring string) int{
    var count int
