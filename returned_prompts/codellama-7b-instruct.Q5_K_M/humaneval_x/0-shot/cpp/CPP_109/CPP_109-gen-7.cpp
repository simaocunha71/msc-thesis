    if(arr.size() == 0) return true;
    if(arr.size() == 1) return true;
    if(arr.size() == 2) return (arr[0] < arr[1]);
    if(arr.size() == 3) return (arr[0] < arr[1] && arr[1] < arr[2]);

    int i = 0;
    int j = 0;
    for(i=0;i<arr.size()-1;i++){
        if(arr[i] > arr[i+1]){
            for(j=i+1;j<arr.size()-1;j++){
                if(arr[j] < arr[j+1]){
                    swap(arr[i],arr[j]);
                    goto A;
                }
            }
            swap(arr[i],arr[j]);
            goto A;
        }
    }
    return true;
}
int main(){
    vector<int> arr;
    arr.push_back(3);
    arr.push_back(4);
    arr.push_back(5);
    arr.push_back(1);
    arr.push_back(2);
    //arr.push_back(3);
    //arr.push_back(5);
    //arr.push_back(4);
    //arr.push_back(1);
    //arr.push_back(2);
    printf("%d",move_one_ball(arr));
}
