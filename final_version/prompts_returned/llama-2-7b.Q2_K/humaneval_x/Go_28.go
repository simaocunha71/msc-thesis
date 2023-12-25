
// Concatenate list of strings into a single string
// >>> Concatenate([])
// ''
// >>> Concatenate(['a', 'b', 'c'])
// 'abc'
func Concatenate(strings []string) string {
    if strings == nil || len(strings) == 0 {
        return ""
    } else if strings != nil && len(strings) > 1 {
        tmp := strings[0]
        for i, v := range strings[1:] {
            str := fmt.Sprintf("%s%v", tmp, v)
            tmp = str
        }
        return tmp
    } else if strings != nil && len(strings) == 1 {
        return strings[0]
    } else { // i.e. strings = nil || len(strings) == 0
        return ""
    }
}
