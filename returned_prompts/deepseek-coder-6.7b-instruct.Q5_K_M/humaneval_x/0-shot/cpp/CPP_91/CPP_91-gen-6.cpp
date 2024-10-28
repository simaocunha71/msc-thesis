int cnt = 0;
size_t found = S.find("I");
while (found != string::npos){
    cnt++;
    found = S.find("I", found+1);
}
return cnt;
}

int main(){
string s = "The sky is blue. The sun is shining. I love this weather";
printf("%d\n", is_bored(s));
return 0;
}
```

The program starts by initializing a counter `cnt` to 0 and a variable `found` to the position of the first occurrence of 'I'. Then it enters a loop where it keeps searching for the next occurrence of 'I' in the string and increments the counter whenever it finds one. Once it has finished scanning the string and hasn't found any more 'I's, it returns the counter.

The function `is_bored` takes a string `S` as an input, counts the number of occurrences of 'I' in that string and returns the count.

The main function tests `is_bored` with the string "The sky is blue. The sun is shining. I love this weather". The result is printed to the console.

The program will output `1` which indicates there is 1 boredom in the provided string.

*/

int main() {
    string s = "The sky is blue. The sun is shining. I love this weather";
    printf("%d\n", is_bored(s));
    return 0;
}

int is_bored(string S) {
    int cnt = 0;
    size_t found = S.find("I");
    while (found != string::npos) {
        cnt++;
        found = S.find("I", found+1);
    }
    return cnt;
}
```

## Output:

```
1
```

This output indicates that there is 1 boredom in the provided string.


## Complexity Analysis:

The time complexity of this program is O(n), where n is the length of the string. This is because in the worst case, we're traversing the string once. The space complexity is O(1),