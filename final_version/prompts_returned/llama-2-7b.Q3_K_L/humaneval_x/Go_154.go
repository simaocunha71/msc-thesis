
// You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
// CycpatternCheck("abcd","abd") => false
// CycpatternCheck("hello","ell") => true
// CycpatternCheck("whassup","psus") => false
// CycpatternCheck("abab","baa") => true
// CycpatternCheck("efef","eeff") => false
// CycpatternCheck("himenss","simen") => true
func CycpatternCheck(a , b string) bool {
	if a == "" || b == "" {
		return false;
	}
	for i := len(b)-1; i > 0 && a[i] >= 'a' && a[i] <= 'z'; i-- {
		for j := i + 1; j < len(a); j++ {
			if a[i]+" "+a[j-1] == b {
				return true;
			}
		}
	}
	return false;
}