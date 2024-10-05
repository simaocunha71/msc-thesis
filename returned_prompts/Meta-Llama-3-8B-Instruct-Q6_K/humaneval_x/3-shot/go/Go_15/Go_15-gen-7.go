    result := ""
    for i := 0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result[:len(result)-1]
}  // Remove the extra space at the end
}  // End of function StringSequence
}  // End of package main
}  // End of import "main"


