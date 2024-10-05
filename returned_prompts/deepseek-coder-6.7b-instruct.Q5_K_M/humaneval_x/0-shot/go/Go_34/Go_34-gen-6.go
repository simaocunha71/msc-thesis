     var u []int
     m := make(map[int]bool)
     for _, item := range l {
         if _, ok := m[item]; !ok {
             m[item