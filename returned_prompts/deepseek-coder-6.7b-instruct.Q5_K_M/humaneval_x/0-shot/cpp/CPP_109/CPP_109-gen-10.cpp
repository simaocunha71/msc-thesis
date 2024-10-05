    int count = 0;
    int n = arr.size();
    for(int i = 0; i < n - 1; i++){
        if(arr[i] > arr[i+1]){
            count++;
        }
    }
    if(arr[n-1] > arr[0]){
        count++;
    }
    if(count > 1){
        return false;
    }
    return true;
}


int main(){
    vector<int> arr = {3, 5, 4, 1, 2};
    if(move_one_ball(arr)){
        printf("True");
    }else{
        printf("False");
    }
    return 0;
}

