
// You are given 2 words. You need to return true if the second word or any of its rotations is a substring in the first word
// CycpatternCheck("abcd","abd") => false
// CycpatternCheck("hello","ell") => true
// CycpatternCheck("whassup","psus") => false
// CycpatternCheck("abab","baa") => true
// CycpatternCheck("efef","eeff") => false
// CycpatternCheck("himenss","simen") => true
func CycpatternCheck(a , b string) bool {
	if len(b) == 0 || a[len(b)-1] < 'e' && a[len(b)-1:] != ""{
    return false
} else if b == "" || a[:len(b)] == ""{
    return true
} else {
	for i:=1;i<len(b);i++{
		if a[i] >= 'e' &&a[i-1:] != ""{
		if (b[i:i+len(b)-i] == b[:i]) || (!isRotation(a,b)) { return false } else  if !isRotation(a,b) {return true}
		}
	}
   
} return true
}
func isRotation(a , b string){
for i :=1; i<len(b);i++{
if a[:i] == (a[i-1:])||(!isStringLetter(b[i])){
return false}}return true
}

	