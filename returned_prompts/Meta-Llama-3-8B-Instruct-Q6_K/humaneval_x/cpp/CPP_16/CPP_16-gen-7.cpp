    vector<char> characters;
    for(int i = 0; i < str.length(); i++){
        char c = tolower(str[i]); // convert to lowercase
        if(find(characters.begin(), characters.end(), c) == characters.end()){
            characters.push_back(c); // add the character to the vector
        }
    }
    return characters.size();
}
int main() {
    string s = "xyzXYZ";
    cout<<count_distinct_characters(s)<<endl; // Output: 3
    s = "Jerry";
    cout<<count_distinct_characters(s)<<endl; // Output: 4
    return 0;
}
}

