    int ans = 0;
    int prod = 1;
    int sum = 0;

    if(arr.size() == 0) return -32768;

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] == 0) prod = 0;
        else if(arr[i] < 0) prod = prod * -1;
        else prod = prod * 1;
        sum = sum + abs(arr[i]);
    }

    if(prod == -1){
        ans = ans + sum;
    }
    else{
        ans = ans - sum;
    }

    return ans;
}

int main(){
    vector<int> arr = {1, 2, 2, -4};
    printf("%d", prod_signs(arr));
    return 0;
}



