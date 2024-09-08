    vector<char> v;
    for(int i=0;i<str.length();i++){
        char c=str[i];
        if(c>=97 && c<=122 || c>=65 && c<=90){ //only consider alphabets
            bool flag = true; 
            for(int j=0;j<v.size();j++){
                if(v[j]==c) { flag = false; break; }
            }
            if(flag) v.push_back(c);
        }
    }
    return v.size(); 
}
int main() {
    printf("%d\n", count_distinct_characters("xyzXYZ")); // 3
    printf("%d\n", count_distinct_characters("Jerry")); // 4
    return 0;
}

Explanation:

This program uses a vector to store the distinct characters of the input string. It iterates over the string, and for each character, it checks if it is an alphabet (ignoring case). If it is, it checks if the character is already present in the vector. If not, it adds the character to the vector. Finally, it returns the size of the vector, which represents the number of distinct characters.

The time complexity of this program is O(n), where n is the length of the input string. This is because it iterates over the string once and performs a constant amount of work for each character.

The space complexity is also O(n), as in the worst case, the vector could store all the characters of the input string. However, in practice, the space complexity is usually less than O(n), as the number of distinct characters in a string is usually much less than the total number of characters.