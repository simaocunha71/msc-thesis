    m := make(map[int]bool)
    for _, val := range l {
        m[val] = true
    }
    var result []int
    for k := range m {
        result = append(result, k)
    }
    sort.Ints(result)
    return result
}
// or
func Unique(l []int) []int {
    m := make(map[int]bool)
    for _, val := range l {
        m[val] = true
    }
    var result []int
    for k := range m {
        result = append(result, k)
    }
    return result
} // if you don't care about the order of the result
} // end of Unique function
// or
func Unique(l []int) []int {
    result := make([]int, 0)
    for _, val := range l {
        found := false
        for i := 0; i < len(result); i++ {
            if result[i] == val {
                found = true
                break
            }
        }
        if !found {
            result = append(result, val)
        }
    }
    sort.Ints(result)
    return result
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique function
} // end of Unique