#include <bits/stdc++.h>
using namespace std;
int can_arrange(vector<int> arr){
    int n = arr.size();
    int max_idx = -1;
    for(int i = 1; i < n; i++){
        if(arr[i] >= arr[i-1]){
            max_idx = i;
        }
    }
    return max_idx;
}
/*
    if(max_idx != -1){
        return max_idx;
    }
    else{
        return -1;
    }
}
*/
int main(){
    vector<int> arr = {1,2,4,3,5};
    cout<<can_arrange(arr);
    return 0;
}

B:
#include <bits/stdc++.h>
using namespace std;
int can_arrange(vector<int> arr){
    int n = arr.size();
    int max_idx = -1;
    for(int i = 1; i < n; i++){
        if(arr[i] >= arr[i-1]){
            max_idx = i;
        }
    }
    return max_idx;
}
/*
    if(max_idx != -1){
        return max_idx;
    }
    else{
        return -1;
    }
}
*/
int main(){
    vector<int> arr = {1,2,4,3,5};
    cout<<can_arrange(arr);
    return 0;
}

C:
#include <bits/stdc++.h>
using namespace std;
int can_arrange(vector<int> arr){
    int n = arr.size();
    int max_idx = -1;
    for(int i = 1; i < n; i++){
        if(arr[i] >= arr[i-1]){
            max_idx = i;
        }
    }
    return max_idx;
}
/*
    if(max_idx != -1){
        return max_idx;
    }
    else{
        return -1;
    }
}
*/
int main(){
    vector<int> arr = {1,2,4,3,5};
    cout<<can_arrange(arr);
    return 0;
}

D:
#include <bits/stdc++.h>
using namespace std;
int can_arrange(vector<int> arr){
    int n = arr.size();
    int max_idx = -1;
    for(int i = 1; i < n; i++){
        if(arr[i] >= arr[i-1]){
            max_idx = i;
        }
    }
    return max_idx;
}
/*
    if(max_idx != -1){
        return max_idx;
    }
