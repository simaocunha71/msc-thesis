
// 1. 做一个简单的检查，如果lst1中存在奇数，或者lst2中存在奇数，那么就直接返回NO
for _, v := range lst1 {
    if v%2 != 0 {
        return "NO"
    }
}

for _, v := range lst2 {
    if v%2 != 0 {
        return "NO"
    }
}

// 2. 然后我们要找到lst2中的最大元素
var max int
for _, v := range lst2 {
    if v > max {
        max = v
    }
}

// 3. 然后我们要找到lst2中的最大元素的index
var maxIndex int
for i, v := range lst2 {
    if v == max {
        maxIndex = i
    }
}

// 4. 最后我们要把lst2中的最大元素的index对应的元素移到lst1的最后
lst1 = append(lst1, lst2[maxIndex])
lst2 = append(lst2[:maxIndex], lst2[maxIndex+1:]...)

// 5. 然后我们要把lst2中的元素逐个插到lst1的最后
for i := len(lst2) - 1; i >= 0; i-- {
    lst1 = append(lst1, lst2[i])
    lst2 = append(lst2[:i], lst2[i+1:]...)
}

return "YES"
}
