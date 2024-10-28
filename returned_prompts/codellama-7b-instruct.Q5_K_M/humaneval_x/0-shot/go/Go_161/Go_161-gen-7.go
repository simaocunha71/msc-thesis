
// 1st try
func Solve(s string) string {
	var ans string
	for i := range s {
		if s[i] >= 'a' && s[i] <= 'z' {
			ans += string(s[i] - 'a' + 'A')
		} else if s[i] >= 'A' && s[i] <= 'Z' {
			ans += string(s[i] - 'A' + 'a')
		} else {
			ans += string(s[i])
		}
	}
	return ans
}

// 2nd try
func Solve(s string) string {
	var ans string
	for i := range s {
		if s[i] >= 'a' && s[i] <= 'z' {
			ans += string(s[i]-'a'+'A')
		} else if s[i] >= 'A' && s[i] <= 'Z' {
			ans += string(s[i]-'A'+'a')
		} else {
			ans += string(s[i])
		}
	}
	return ans
}

// 3rd try
func Solve(s string) string {
	var ans string
	for i := range s {
		if s[i] >= 'a' && s[i] <= 'z' {
			ans += string(s[i] - 'a' + 'A')
		} else if s[i] >= 'A' && s[i] <= 'Z' {
			ans += string(s[i] - 'A' + 'a')
		} else {
			ans += string(s[i])
		}
	}
	return ans
}

// 4th try
func Solve(s string) string {
	var ans string
	for i := range s {
		if s[i] >= 'a' && s[i] <= 'z' {
			ans += string(s[i]-'a'+'A')
		