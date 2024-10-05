    if (strings.empty()){
        return NULL;
    }
B:
    string longest = strings[0];
    for (int i=0; i<strings.size(); i++){
        if (strings[i].length() > longest.length()){
            longest = strings[i];
        }
    }
    return longest;
}

int main() {
    vector<string> strings = {"a", "bb", "ccc"};
    printf("%s\n", longest(strings).c_str());
    return 0;
}

Output:
ccc

*/

