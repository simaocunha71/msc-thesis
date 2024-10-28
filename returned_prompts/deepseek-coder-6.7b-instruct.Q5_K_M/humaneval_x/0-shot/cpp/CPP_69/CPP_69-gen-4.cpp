    int max=0;
    int count=0;
    for(int i=0; i<lst.size(); i++){
        if(lst[i] > max){
            max = lst[i];
        }
    }

    for(int i=0; i<lst.size(); i++){
        if(lst[i] == max){
            count++;
        }
    }
    if(count == max){
        return max;
    }else{
        return -1;
    }
}

int main(){
    vector<int> v = {4, 1, 2, 2, 3, 1};
    printf("%d\n", search(v));
    return 0;
}

//The solution provided by the user is not correct as the problem statement is not clear about how to handle the case when the frequency of the max number is equal to the max number itself.
//If the frequency of the max number is equal to the max number itself, then the function should return the max number, else it should return -1.
//However, the solution provided by the user returns the max number if the count of the max number in the list is greater than the max number itself, which is not correct.
//The correct solution should be:

```cpp
#include<bits/stdc++.h>
using namespace std;

int search(vector<int> lst){
    unordered_map<int, int> freq;
    for(int i=0; i<lst.size(); i++)
        freq[lst[i]]++;
    for(int i=lst.size(); i>0; i--)
        if(freq[i] >= i)
            return i;
    return -1;
}

int main(){
    vector<int> v = {4, 1, 2, 2, 3, 1};
    cout<<search(v)<<endl;
    return 0;
}
```

This solution creates a frequency map and then iterates from the size of the vector to 1 checking if the frequency of the current number is greater than or equal to the current