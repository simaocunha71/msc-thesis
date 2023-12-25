
// Filter an input list of strings only for ones that start with a given prefix.
// >>> FilterByPrefix([], 'a')
// []
// >>> FilterByPrefix(['abc', 'bcd', 'cde', 'array'], 'a')
// ['abc', 'array']
func FilterByPrefix(strings []string,prefix string) []string {
    if len(strings) == 0 {
        return nil
    }
    strings2 := append(strings, strings...)
    all := make(map[string]interface{}) // we will store everything as an interface{}
    for _, s := range strings2 {
        if prefix == "" || prefix == string(s) {
            all["s"] = s
            all["prefix"] = prefix
        } else {
            continue
        }
    }

    rr := reflect.ValueOf(all).Elem() // we take out the map[string]interface{} and work with it's value instead of the type
    switch rr.Kind() {
    case reflect.Map:
        for k, v := range all["s"].(map[string]interface{}) {
            if prefix == "" || strings.Contains(strings2[:], string(k)) { // if the key contains the prefix then
                s:=reflect.ValueOf(v).Elem()
                switch rr.Kind() {
                case reflect.Array:
                    res := make([]string, 0)
                    for j := range *(*[]interface{})(s) { // j = the index of an element (as an interface{} ) to be filtered out
                        if !strings2[j].Contains(strings[i]) { // we do not want elements with prefix (and only the elements in strings[i], which is a slice, that contains any characters from strings[j]
                            res = append(res, strings[i])
                        }
                    }
                    return append(res, strings2......) // and the rest of filtered items after the prefix (the ones not containing any characters of it)
                case reflect.Slice: // this is the slice in which we will put our elements instead of the original one because it's more efficient than a map[string]interface{}
                    out