/*
You are given a string S. Your task is to find the number of distinct characters in it.

Input Format

A single line containing string S.

Constraints

0 < length(S) <= 10000
Output Format

Output the number of distinct characters in string S.

Sample Input 0

qA2z%5
Sample Output 0

6
Explanation 0

String S='qA2z%5' has the following distinct characters: q, A, 2, z, %, 5.

Sample Input 1

hackerrank
Sample Output 1

9
Explanation 1

String S='hackerrank' has the following distinct characters: h, a, c, k, e, r, n.
*/
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    string s;
    cin >> s;
    int count = 0;
    unordered_map<char, bool> unique;
    for (int i = 0; i < s.length(); i++) {
        unique[s[i]] = true;
    }
    for (auto it : unique) {
        count++;
    }
    cout << count << endl;
    return 0;
}