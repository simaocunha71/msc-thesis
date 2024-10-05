
// Concatenate list of strings into a single string
// >>> Concatenate([])
// ''
// >>> Concatenate(['a', 'b', 'c'])
// 'abc'
func Concatenate(strings []string) string {
	var sb strings.Builder
	for _, s := range strings {
		sb.WriteString(s)
	}
	return sb.String()
}

