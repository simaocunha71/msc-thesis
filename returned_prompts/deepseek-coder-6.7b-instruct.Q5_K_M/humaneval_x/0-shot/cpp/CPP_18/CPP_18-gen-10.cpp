    int str_length = str.size();
    int substring_length = substring.size();
    int count = 0;
    for(int i=0; i <= (str_length - substring_length); i++){
        for(int j=0; j < substring_length; j++){
            if(str[i+j] != substring[j]){
                break;
            }
            if(j == substring_length - 1){
                count++;
            }
        }
    }
    return count;
}
int main(){
    printf("%d\n", how_many_times("", "a"));    // 0
    printf("%d\n", how_many_times("aaa", "a"));  // 3
    printf("%d\n", how_many_times("aaaa", "aa")); // 3
    return 0;
}
```

This C++ program works by iterating over the given string, and for each character, checking if the following characters match the characters of the substring. If they do, it increments a counter. Finally, it returns the counter.

If the substring is empty, it returns 0, because there are no substrings to look for in the string. If the string is "aaa" and the substring is "a", it will return 3 because there are three instances of "a" in "aaa". If the string is "aaaa" and the substring is "aa", it will return 3 because there are three instances of "aa" in "aaaa".

This code is case sensitive. If you want to ignore case, you would need to add additional code to convert both the string and the substring to lower or upper case before comparing them.
*/


int how_many_times(string str,string substring){
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    transform(substring.begin(), substring.end(), substring.begin(), ::tolower);

    int str_length = str.size();
    int substring_length = substring.size();
    int count = 0;
    for(int i=0; i <= (str_length -