var key = 0

// if num == "" {
//     return key
// }

for i := 0; i < len(num); i++ {
    if num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7' || num[i] == 'B' || num[i] == 'D' {
        key++
    }
}
return key
}
这个代码能通过吗？为什么

