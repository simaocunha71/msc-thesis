    int n = lst.size();
    int freq[n+1] = {0};

B:
    for(int i=0; i<n; i++)
        freq[lst[i]]++;

C:
    for(int i=n; i>0; i--)
        if(freq[i] >= i)
            return i;

D:
    return -1;
}

*/

#include<bits/stdc++.h>
using namespace std;

int search(vector<int> lst){
    int n = lst.size();
    int freq[n+1] = {0};

    for(int i=0; i<n; i++)
        freq[lst[i]]++;

    for(int i=n; i>0; i--)
        if(freq[i] >= i)
            return i;

    return -1;
}

int main(){
    vector<int> vec = {4, 1, 2, 2, 3, 1};
    cout<<search(vec)<<endl; // Output: 2
    return 0;
}
```
This code will solve the problem in C++. It uses an array of frequency counters to count the number of occurrences of each integer in the vector. It then iterates through the array in reverse order, and returns the first integer that has a frequency that is greater than or equal to its value. If no such integer is found, it returns -1.

Please note that this code assumes that all elements in the vector are positive integers and that the size of the vector is less than or equal to the maximum integer value. This is because it uses an array of size n+1 to count the frequency of each integer, where n is the size of the vector. If these assumptions are not true, the code may not work correctly.

The time complexity of this code is O(n), where n is the size of the vector. The space complexity is also O(n), because of the frequency counter array.

This code is a direct translation of the given pseudocode into C++ code. It does not include any error checking or optimization