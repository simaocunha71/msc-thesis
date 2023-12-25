// Out of list of strings, return the Longest one. Return the first one in case of multiple
// strings of the same length. Return nil in case the input list is empty.
// >>> Longest([])
// nil
// >>> Longest(['a', 'b', 'c'])
// 'a'
// >>> Longest(['a', 'bb', 'ccc'])
// 'ccc'
func Longest(strings []string) interface{}{
    if strings == nil || len(strings) < 1 {
        return nil
    } else {
      for i, s := range strings {
          if v, ok := strings[len(strings)-1]; ok && s != "" && s > v {
              return s
          }
      }
      return strings[0]
  }
}