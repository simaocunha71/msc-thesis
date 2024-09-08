    int max_index=-1;
    for(int i=1;i<arr.size();i++){
        if(arr[i-1]<=arr[i]){
            max_index=i;
        }
    }
    return max_index;
}

int main(){
    vector<int> arr={1,2,4,3,5};
    printf("The largest index is: %d\n",can_arrange(arr));
    return 0;
}

