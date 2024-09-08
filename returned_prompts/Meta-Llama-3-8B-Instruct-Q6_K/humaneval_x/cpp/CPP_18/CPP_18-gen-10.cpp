    int count = 0;
    int i = 0;
    int j = 0;
    while(i < str.length()) {
        if(str[i] == substring[j]) {
            i++;
            j++;
            if(j == substring.length()) {
                count++;
                j = 0;
            }
        } else {
            i = i - j + 1;
            j = 0;
        }
    }
    return count;
}

int main() {
    string str = "aaaa";
    string substring = "aa";
    printf("The substring %s appears %d times in the string %s.\n", substring.c_str(), how_many_times(str, substring), str.c_str());
    return 0;
}
B:
    int how_many_times(string str,string substring){
        int count = 0;
        int pos = 0;
        while((pos = str.find(substring, pos)) != string::npos){
            count++;
            pos += substring.length();
        }
        return count;
    }
    int main() {
        string str = "aaaa";
        string substring = "aa";
        printf("The substring %s appears %d times in the string %s.\n", substring.c_str(), how_many_times(str, substring), str.c_str());
        return 0;
    }
C:
    int how_many_times(string str,string substring){
        int count = 0;
        size_t pos = 0;
        while((pos = str.find(substring, pos)) != string::npos){
            count++;
            pos += substring.length();
        }
        return count;
    }
    int main() {
        string str = "aaaa";
        string substring = "aa";
        cout << "The substring " << substring << " appears " << how_many_times(str, substring) << " times in the string " << str << "." << endl;
        return 0;
    }
D:
    int how_many_times(string str,string substring){
        int count = 0;
        for(int i = 0; i <= str.length() - substring.length(); i++){
            if(str.substr(i, substring.length()) == substring)
                count++;
        }
        return count;
    }
    int main() {
        string str = "aaaa";
        string substring = "aa";
        cout << "The substring " << substring << " appears " << how_many_times(str, substring) << " times in the string " << str << "." << endl;
        return 0