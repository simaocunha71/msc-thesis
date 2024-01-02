
// Concatenate list of strings into a single string
// >>> Concatenate([])
// ''
// >>> Concatenate(['a', 'b', 'c'])
// 'abc'
func Concatenate(strings []string) string {
    if len(strings) == 0 {
        return ""
    }
    var str = strings[0]
    for i := 1; i < len(strings); i++ {
        str += strings[i]
    }
    return str
}