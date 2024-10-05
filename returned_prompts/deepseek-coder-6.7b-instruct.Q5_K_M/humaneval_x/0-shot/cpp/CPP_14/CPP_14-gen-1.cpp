vector<string> prefixes;
B:
for(int i=0; i<str.size(); i++){
    C:
    string prefix = str.substr(0,i+1);
    D:
    prefixes.push_back(prefix);
}
E:
return prefixes;
}


A: Create an empty vector of strings named prefixes
B: Iterate over the length of the input string
C: Create a substring from the input string starting at index 0 and ending at the current index plus one
D: Add the new substring to the prefixes vector
E: Return the prefixes vector
*/

