    for(int i=0;i<arr.size();i++){
        if(arr[i]>arr[i+1]){
            // printf("%d\n",arr[i]);
            return false;
        }
    }
    return true;
}
int main(){
    vector<int> arr={3, 4, 5, 1, 2};
    if(move_one_ball(arr))printf("true");
    else printf("false");
    return 0;
}
