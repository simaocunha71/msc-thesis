import (
    "fmt"
    "strconv"
)

// Given a positive integer N, return the total sum of its digits in binary.
// 
// Example
// For N = 1000, the sum of digits will be 1 the output should be "1".
// For N = 150, the sum of digits will be 6 the output should be "110".
// For N = 147, the sum of digits will be 12 the output should be "1100".
// 
// Variables:
// @N integer
// Constraints: 0 ≤ N ≤ 10000.
// Output:
// a string of binary number
func Solve(N int) string {
    var i, j int = 0, k, ret string //k stores the sum of digits in decimal form
    
    str := "0"

    for N > 1 { //if N is odd then it should be added to the rightmost digit.
        tmpStr := "" //tmpStr stores the sum of digits in binary form.
        
        ret += "," + strconv.Itoa(N%1) + " = ?b"
        for j < 8 && N > 0 { //while N is less than 2^8, it should be divided by 2
            tmpStr = ""
            
            if i == 7 || (i == 6 && k == "") {    //leftmost digit is the rightmost digit or no digits are there.
                n := 0
                
                for j < 8 && N > 0 {     //while N is less than 2^8, it should be divided by two so that i can store only decimal number in variable n till index of i = n % 10. The value of i will always remain 7 or 6
                    if str[i] == '9' || str[i] == '8', { //leftmost digit is the rightmost digit or no digits are there.
                        tmpStr += ",b" + strconv.Itoa(N%2)
                        
                        N = N / 2 //divide by two, so that it will store only binary value till index of