
The first function is correct. Your second function has an off-by-one error in the last line. You want to subtract the count of the first character from the total count of the string. Your current code is subtracting the count of the whole string. It should be:

return len(strings.ToLower(str)) - len(strings.Replace(strings.ToLower(str), strings.ToLower(str)[0:1], "", -1))

The third function is also correct.