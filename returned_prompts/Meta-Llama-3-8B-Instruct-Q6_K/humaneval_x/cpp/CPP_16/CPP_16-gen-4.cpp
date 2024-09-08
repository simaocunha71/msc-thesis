    vector<char> charSet; 
    for(int i = 0; i < str.length(); i++) { 
        char ch = tolower(str[i]); 
        if(find(charSet.begin(), charSet.end(), ch) == charSet.end()) { 
            charSet.push_back(ch); 
        } 
    } 
    return charSet.size(); 
}
int main() { 
    string str = "xyzXYZ"; 
    cout << "Distinct characters: " << count_distinct_characters(str) << endl; 
    return 0; 
} 
