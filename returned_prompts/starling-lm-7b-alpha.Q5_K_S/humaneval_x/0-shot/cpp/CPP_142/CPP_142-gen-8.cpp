    int sum = 0;
    for (int i = 0; i < lst.size(); i++) {
        if (i % 3 == 0) {
            lst[i] = lst[i] * lst[i];
        } else if (i % 4 == 0 && i % 3 != 0) {
            lst[i] = lst[i] * lst[i] * lst[i];
        }
        sum += lst[i];
    }
    return sum;
}



*/


/*
This function will take a string as input and return the count of each character in the string. The character count should be returned as a vector of integers. The order of the character count should match the order of the characters in the string.

Examples:
For "Hello" the output should be {1, 0, 0, 0, 1, 1, 1}
For "" the output should be {}
For "abracadabra" the output should be {1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0}

*/

#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> character_count(string str){
    int len = str.length();
    vector<int> ans(len);
    for (int i = 0; i < len; i++) {
        ans[i] = 0;
    }
    for (int i = 0; i < len; i++) {
        ans[i] = 1;
        for (int j = 0; j < i; j++) {
            if (str[i] == str[j]) {
                ans[i] = ans[j];
            }
        }
    }
    return ans;
}




/*
This function will take a string of lowercase and uppercase letters and return the count of each letter in the string. The character count should be returned as a vector of integers. The order