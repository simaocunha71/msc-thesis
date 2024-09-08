    for(int i=0;i<arr.size();i++){
        if(arr[i]<arr[(i+1)%arr.size()])return true;
    }
    return false;
}
int main(){
    vector<int> v={3,4,5,1,2};
    printf("%d\n",move_one_ball(v));
    return 0;
}
