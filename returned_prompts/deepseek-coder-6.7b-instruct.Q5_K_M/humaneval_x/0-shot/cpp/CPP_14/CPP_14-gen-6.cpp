vector<string> res;
B:
for(int i = 0; i < str.size(); i++){
C:
string prefix = str.substr(0, i+1);
D:
res.push_back(prefix);
E:
}
F:
return res;
}
int main(){
G:
string test = "abc";
H:
vector<string> prefixes = all_prefixes(test);
I:
for(string s : prefixes){
J:
printf("%s\n", s.c_str());
K:
}
L:
return 0;
}

This program is written in C++.

In the program, we start by declaring a vector of strings named res. Afterwards, we loop over all characters in the input string. For each iteration, we create a substring of the input string from the start to the current index and push this substring into the res vector. Finally, we return the res vector.

In the main function, we create a test string and call the all_prefixes function with this string as input. The function returns a vector of all prefixes of the test string. We then loop over this vector and print each prefix to the console.

This program should print the following output:

a
ab
abc
*/

```

## Python Solution

```python
# 