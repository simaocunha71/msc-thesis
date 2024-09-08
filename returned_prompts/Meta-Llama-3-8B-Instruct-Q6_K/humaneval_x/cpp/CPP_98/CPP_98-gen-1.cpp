    int count=0;
    for(int i=0;i<s.length();i++){
        if(i%2==0 && isupper(s[i])){
            count++;
        }
    }
    return count;
}  // Write your code here

int main()
{
    string s;
    printf("Enter a string: ");
    getline(cin, s);
    cout << "Number of uppercase vowels in even indices: " << count_upper(s) << endl;
    return 0;
}
```

Solution:
```c
#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;
int count_upper(string s){
    int count=0;
    for(int i=0;i<s.length();i++){
        if(i%2==0 && isupper(s[i])){
            switch(s[i]){
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                    count++;
                    break;
            }
        }
    }
    return count;
}
int main()
{
    string s;
    printf("Enter a string: ");
    getline(cin, s);
    cout << "Number of uppercase vowels in even indices: " << count_upper(s) << endl;
    return 0;
}
```
Explanation:
In the given problem, we need to count the number of uppercase vowels in even indices of a given string. 

To solve this, we iterate over the string using a for loop. We check if the current index is even (i%2==0) and if the character at that index is uppercase (isupper(s[i])). 

If both conditions are met, we check if the character is a vowel. We do this by using a switch statement and checking if the character is 'A', 'E', 'I', 'O', or 'U'. 

If the character is a vowel, we increment the count. 

Finally, we return the count. 

In the main function, we take a string input from the user and call the count_upper function with this string. We then print the result. 

Note: The original problem statement asks to count the number of uppercase vowels in even indices, which means only 'A', 'E', 'I', 'O', 'U' are considered as vowels. However, the problem statement does not explicitly mention that. Therefore, the solution provided here considers only 'A', 'E', 'I', 'O', 'U' as vowels. If the problem statement intended to consider all uppercase vowels, the