for i, v := range arr[:k] {
    if v > 9 {
        arr[i+1] += v / 10
    }
}

B:
res := 0
for _, v := range arr[:k] {
    if v > 10 {
        res += v / 100
    }
}

C:
return res
}
