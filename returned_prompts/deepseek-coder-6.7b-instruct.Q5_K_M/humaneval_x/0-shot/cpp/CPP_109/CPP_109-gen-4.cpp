    int n=arr.size();
    if(n==0)
        return true;

B:
    int count=0;
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1])
            count++;
    }
    if(arr[n-1]>arr[0])
        count++;

C:
    if(count>1)
        return false;
    else
        return true;
}
int main() {
    vector<int> arr = {3, 5, 4, 1, 2};
    if(move_one_ball(arr))
        printf("true");
    else
        printf("false");
    return 0;
}

*/

// C++ solution of the above problem
#include<iostream>
#include<vector>
using namespace std;

bool move_one_ball(vector<int> arr){
    int n=arr.size();
    if(n==0)
        return true;
    int count=0;
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1])
            count++;
    }
    if(arr[n-1]>arr[0])
        count++;
    if(count>1)
        return false;
    else
        return true;
}

int main() {
    vector<int> arr = {3, 5, 4, 1, 2};
    if(move_one_ball(arr))
        cout<<"true";
    else
        cout<<"false";
    return 0;
}

// This code is contributed by Aryan Singh(github.com/Aryan-Singh-24)

// This code is contributed by Aryan Singh(github.com/Aryan-Singh-24)
// This code is contributed by Aryan Singh(github.com/Aryan-Singh-24)

// This code is contributed by Aryan Singh(github.com/Aryan-Singh