
You are doing the right thing, but there's a small thing I would change. Instead of checking for y at the end of the string, you could check if it is the last character in the string with len(s)-1. This will make your code more efficient and easier to understand.
Also, you could use a switch statement instead of multiple if statements. This would make your code more concise and easier to read.
Here's the updated version of your function:

func VowelsCount(s string) int {
    count := 0
    vowels := "aeiou"
    for _, c := range s {
       