    vector<string> prefixes;
    string prefix = "";
    for(int i=0; i<str.size(); i++){
        prefix += str[i];
        prefixes.push_back(prefix);
    }
    return prefixes;
}

int main(){
    vector<string> prefixes = all_prefixes("abc");
    for(int i=0; i<prefixes.size(); i++){
        printf("%s\n", prefixes[i].c_str());
    }
    return 0;
}

*/

/*
Answer:
The question is asking to return all the prefixes of a given string. A prefix is a sequence of characters at the start of a string. The prefixes of "abc" are "a", "ab", "abc". 

This code defines a function, all_prefixes(), which takes a string as an argument and returns a vector of strings. It uses a for loop to iterate over each character in the string, adding each character to a prefix string and pushing the prefix string onto a vector. This continues until all characters in the string have been added to the vector.

The main function then calls this function with the string "abc" and prints the resulting prefixes to the console.
*/

//Q2:
/*
