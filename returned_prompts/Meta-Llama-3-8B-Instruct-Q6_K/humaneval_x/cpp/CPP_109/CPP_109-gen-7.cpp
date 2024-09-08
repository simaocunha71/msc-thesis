    if(arr.empty())
        return true;
    int n=arr.size();
    for(int i=1;i<n;i++){
        if(arr[i-1]>arr[i]){
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> arr = {3, 5, 4, 1, 2};
    if(move_one_ball(arr))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}
