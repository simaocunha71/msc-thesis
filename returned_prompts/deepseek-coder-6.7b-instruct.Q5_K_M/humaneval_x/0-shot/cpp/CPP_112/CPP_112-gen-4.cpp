    string res="";
    for(int i=0;i<s.size();i++){
        if(c.find(s[i])==std::string::npos){
            res+=s[i];
        }
    }
    string rev_res=res;
    reverse(rev_res.begin(),rev_res.end());
    string palindrome=(res==rev_res)?"True":"False";
    return {res,palindrome};
}
*/

// ANSWER:
// The function reverse_delete takes two strings, s and c. It iterates over the string s and checks if each character is in string c.
// If the character is not in string c, it is appended to the result string res. After that, it checks if the result string is a palindrome.
// If it is, it returns a vector containing the result string and "True". If not, it returns a vector containing the result string and "False".

// The function reverse_delete returns a vector containing the result string and a string indicating whether the result string is a palindrome or not.

// The time complexity of the function is O(n), where n is the length of the string s.
// The space complexity of the function is O(n), where n is the length of the string s.

// The function uses the STL string class and the STL algorithm library to solve the problem.

// The function uses the find method of the STL string class to check if a character is in string c.
// If the character is not in string c, the find method returns std::string::npos.

// The function uses the append method of the STL string class to add characters to the result string.

// The function uses the reverse method of the STL algorithm library to reverse the result string.

// The function uses the equality operator of the STL string class to compare the result string and its reverse.

// The function uses the ternary operator to create a string indicating whether the result string is a palindrome or not.
// If the result string is a palindrome, the ternary operator returns "True". If not, it returns "False".

// The function uses the return statement to return the result string