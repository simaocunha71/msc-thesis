    int count = 0;
    vector<bool> visited(128,false);
    for(int i=0; i<str.size(); i++){
        if(visited[tolower(str[i])]==false){
            visited[tolower(str[i])]=true;
            count++;
        }
    }
    return count;
}
int main(){
    printf("%d\n",count_distinct_characters("xyzXYZ"));
    printf("%d\n",count_distinct_characters("Jerry"));
    return 0;
}

This program firstly initialize a count variable to 0 to record the number of distinct characters. It then initializes a vector visited to record whether a character has been visited.

For each character in the string, if it hasn't been visited, it is marked as visited and the count is increased by 1.

The function tolower is used to make the character comparison case-insensitive.

Finally, it returns the count.

The main function tests the count_distinct_characters function with "xyzXYZ" and "Jerry" and prints the result.

This program assumes that the string only consists of ASCII characters. If the string can contain Unicode characters, a different approach should be used.

Time complexity: O(n)
Space complexity: O(1), as the size of the visited array is constant.
*/
```

### C++ (STL)
```c++
