    var even_count int = 0
    for _, num := range lst1 {
        if num%2 == 0{
            even_count += 1
        }
    }

    if even_count == len(lst1){
        return "YES"
    }

    for _, num := range lst2 {
        if num%2 == 0 {
            even_count -= 1
        }
    }

    if even_count == 0 {
        return "YES"
    }

    return "NO"
}



