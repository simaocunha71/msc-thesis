    int x=arr[0];
    for(int i=1;i<arr.size();i++){
        if(arr[i]<x){
            return false;
        }
        x=arr[i];
    }
    return true;
}
int main(){
    vector<int> arr={3, 5, 4, 1, 2};
    bool ans=move_one_ball(arr);
    if(ans){
        printf("true");
    }else{
        printf("false");
    }
    return 0;
} 
