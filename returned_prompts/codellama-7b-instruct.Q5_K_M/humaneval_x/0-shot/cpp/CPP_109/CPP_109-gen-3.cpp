    if(arr.size()==0)
        return true;
    for(int i=0;i<arr.size()-1;i++){
        if(arr[i]>arr[i+1]){
            int j=i;
            while(j>0){
                swap(arr[j],arr[j-1]);
                j--;
            }
            arr[arr.size()-1]=arr[0];
            goto A;
        }
    }
    return false;
}
int main(){
    vector<int>arr={3, 4, 5, 1, 2};
    if(move_one_ball(arr)){
        cout<<"true"<<endl;
    }
    else{
        cout<<"false"<<endl;
    }
    return 0;
}
