    int count = 0;
    int len = substring.length();
    for(int i = 0; i <= str.length() - len; i++){
        if(str.substr(i, len) == substring){
            count++;
        }
    }
    return count;
}
int main(){
    string str,substring;
    cout << "Enter the string: ";
    cin >> str;
    cout << "Enter the substring: ";
    cin >> substring;
    printf("The substring '%s' appears %d times in the string.\n", substring.c_str(), how_many_times(str, substring));
    return 0;
}
