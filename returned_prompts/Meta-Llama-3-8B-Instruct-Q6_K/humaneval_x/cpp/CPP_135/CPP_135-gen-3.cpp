    int n = arr.size();
    int res = -1;
    for(int i=1; i<n; i++){
        if(arr[i-1] <= arr[i]){
            res = i-1;
            break;
        }
    }
    return res;
}

int main(){
    vector<int> arr = {1,2,4,3,5};
    printf("Largest index of an element which is not greater than or equal to the element immediately preceding it: %d\n", can_arrange(arr));
    return 0;
}

