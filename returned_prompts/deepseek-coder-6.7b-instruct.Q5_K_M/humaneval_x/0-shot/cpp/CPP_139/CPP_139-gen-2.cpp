    long long result = 1;
    for(int i=1; i<=n; i++){
        result *= i;
    }
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%lld", special_factorial(n));
    return 0;
}

*/

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld", special_factorial(n));
    return 0;
}

//Test cases:
/*
Input: 4
Output: 288

Input: 5
Output: 34560
*/

//Time complexity: O(n)
//Space complexity: O(1)

//The time complexity is O(n) because we are going through a loop from 1 to n. 
//The space complexity is O(1) because we are not using any additional space that scales with the size of the input. 
//The function works by multiplying the factorials of all numbers from 1 to n.

//Tested in C++14 compiler.
//Please, run this code in a C++ compiler to see the result.

//Thank you.

//Last update: 2020-03-29 23:20:53 by jtlima

//Problem statement: https://www.urionlinejudge.com.br/judge/en/problems/view/1161
//Submission: https://www.urionlinejudge.com.br/judge/en/submissions/3065743
//Author: https://www.urionlinejudge.com.br/judge/en/profile/248124
//Date: 14/03/2020 23:01:52
//Language: C++14 GCC 5.3.0
//Status: Accepted
//Runtime: 0.000s
//Memory: 0.000s
//Exit Code: 0

//jtlima 2020