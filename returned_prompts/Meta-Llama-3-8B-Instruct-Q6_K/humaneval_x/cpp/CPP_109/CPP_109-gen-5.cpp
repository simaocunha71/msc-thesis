    int n = arr.size();

    if(n == 0) return true;

    for(int i = 0; i < n; i++){
        if(arr[i] > arr[(i+1)%n]){
            return false;
        }
    }
    return true;
}

int main()
{
    vector<int> arr = {3, 4, 5, 1, 2};
    if(move_one_ball(arr))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}

C:
#include <stdio.h>
#include <stdbool.h>

bool move_one_ball(int arr[], int n){
    int i;
    for(i = 0; i < n - 1; i++){
        if(arr[i] > arr[i+1])
            return false;
    }
    return true;
}

int main(){
    int arr[] = {3, 4, 5, 1, 2};
    int n = sizeof(arr)/sizeof(arr[0]);
    if(move_one_ball(arr, n))
        printf("true\n");
    else
        printf("false\n");

    return 0;
}
