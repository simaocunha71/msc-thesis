    for(int i=arr.size()-1; i>0; i--){
        if(arr[i] < arr[i-1]){
            return i;
        }
    }
    return -1;
}
int main(){
    vector<int> arr = {1,2,4,3,5};
    printf("%d", can_arrange(arr));
    return 0;
}

*/

// 2. Find the number of rotations in a sorted array
/*
