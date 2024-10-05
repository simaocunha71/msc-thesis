vector<string> words;
string word = "";
for (int i = 0; i < s.length(); i++){
    if (s[i] == ',' || s[i] == ' '){
        if (word != ""){
            words.push_back(word);
            word = "";
        }
    }
    else{
        word += s[i];
    }
}
if (word != ""){
    words.push_back(word);
}
return words;
}
*/

int main() {
	vector<string> result = words_string("Hi, my name is John");
	for (int i = 0; i < result.size(); i++) {
		printf("%s ", result[i].c_str());
	}
	return 0;
}
```

This program will print:

```
Hi my name is John 
```

This is because the function `words_string()` is designed to split the given string `s` into words based on commas and spaces, and then it returns a vector of these words.

Please note that this program uses C++ and the `<string>` and `<vector>` standard libraries.

Also, the function `words_string()` returns a vector of strings, so you can use the `c_str()` method to convert a string to a const char* for printing purposes.

This program is a simple example of how to use C++ to split a string into words based on a delimiter. In a more complex situation, you might want to use the `<sstream>` library's `istringstream` class or the `<regex>` library to perform more advanced string manipulation.

























































































































