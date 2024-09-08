    int i = 0,j = 0;
    while(i<s0.size() && j<s1.size()){
        if(s0[i]==s1[j]){
            i++;
            j++;
        }else if(i<s0.size() && s0[i]==s1[0]){
            i++;
        }else if(j<s1.size() && s0[0]==s1[j]){
            j++;
        }else{
            return false;
        }
    }
    if(i<s0.size()){
        return false;
    }
    if(j<s1.size()){
        return false;
    }
    return true;
}
int main(){
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddeddabc"));   // true
    printf("%d\n",same_chars("abcd", "dddddddabc"));   // true
    printf("%d\n",same_chars("dddddddabc", "abcd"));   // true
    printf("%d\n",same_chars("eabcd", "dddddddabc"));   // false
    printf("%d\n",same_chars("abcd", "dddddddabce"));   // false
    printf("%d\n",same_chars("eabcdzzzz", "dddzzzzzzzddddabc"));   // false
    return 0;
}

Explanation:
The function same_chars is used to check if two given strings have the same characters. The function takes two strings s0 and s1 as input and returns true if the strings have the same characters and false otherwise.

The function works by comparing the characters of the two strings one by one. It uses two pointers i and j to traverse the strings. If the characters at the current positions of the two strings are the same, it moves both pointers to the next position. If the characters at the current position of s0 are the same as the characters at the current position of s1, it moves the pointer i to the next position. If the characters at the current position of s1 are the same as the characters at the current position of s0, it moves the pointer j to the next position. If none of the above conditions are met, it returns false.

After traversing the strings, if the function has not returned false, it checks if there are any remaining characters in the strings. If there are, it returns false. Otherwise, it returns true.

In the main function, the same_chars function is called with different input strings to check if they have the same