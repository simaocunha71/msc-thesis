// iterate through the list and check if the element is odd and its position is even
sum := 0
for i, num := range lst {
    if num%2 != 0 && i%2 == 0 {
        sum += num
    }
}
return sum
}

