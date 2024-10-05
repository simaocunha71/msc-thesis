    if a < 0 {
        a = -a
    }

B:
    for i := 0; i <= a; i++ {
        if i * i * i == a {
            return true
        }
    }

    return false
}

func main() {

    fmt.Println(Iscube(1))     // true
    fmt.Println(Iscube(2))     // false
    fmt.Println(Iscube(-1))    // true
    fmt.Println(Iscube(64))    // true
    fmt.Println(Iscube(0))     // true
    fmt.Println(Iscube(180))   // false
}

*/

/*
