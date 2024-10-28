
/*

The above solution will fail for a large input because it sorts the string every time.
We can improve the solution by only sorting the string once.

*/

#include<bits/stdc++.h>
using namespace std;

string sort_numbers(string numbers) {
    map<string, int> m;
    m["zero"] = 0;
    m["one"] = 1;
    m["two"] = 2;
    m["three"] = 3;
    m["four"] = 4;
    m["five"] = 5;
    m["six"] = 6;
    m["seven"] = 7;
    m["eight"] = 8;
    m["nine"] =