#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int sum = 0;
    int i = 0;
    int j = arr.size() - 1;
    while(i <= j){
        if(arr[i] != arr[j]){
            sum++;
        }
        i++;
        j--;
    }
    return sum;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 3, 2, 2};
    int res = smallest_change(arr);
    printf("smallest_change(%d) = %d\n", arr.size(), res);
    return 0;
}
B:
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int sum = 0;
    int i = 0;
    int j = arr.size() - 1;
    while(i < j){
        if(arr[i] != arr[j]){
            sum++;
        }
        i++;
        j--;
    }
    return sum;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 3, 2, 2};
    int res = smallest_change(arr);
    printf("smallest_change(%d) = %d\n", arr.size(), res);
    return 0;
}
C:
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int sum = 0;
    int i = 0;
    int j = arr.size() - 1;
    while(i < j){
        if(arr[i] == arr[j]){
            sum++;
        }
        i++;
        j--;
    }
    return sum;
}
int main(){
    vector<int> arr = {1, 2, 3, 4, 3, 2, 2};
    int res = smallest_change(arr);
    printf("smallest_change(%d) = %d\n", arr.size(), res);
    return 0;
}
D:
#include<stdio.h>
#include<vector>
using namespace std;
int smallest_change(vector<int> arr){
    int sum = 0;
    int i = 0;
    int j = arr.size() - 1;
    while(i < j){
        if(arr[i] != arr[j]){
            sum++;
        }
        i++;
        j--;
    }
    return sum;
}
int main(){
    vector<int> arr =