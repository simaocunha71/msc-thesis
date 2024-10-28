    int count = 0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0){
            count++;
        }
    }
    if(count==0){
        return {};
    }
    int min = arr[0];
    int index = 0;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2==0&&arr[i]<min){
            min = arr[i];
            index = i;
        }
    }
    vector<int> result;
    result.push_back(min);
    result.push_back(index);
    return result;
}
int main(){
    vector<int> arr;
    arr.push_back(4);
    arr.push_back(2);
    arr.push_back(3);
    vector<int> result = pluck(arr);
    for(int i=0;i<result.size();i++){
        printf("result[%d] = %d\n",i,result[i]);
    }
    return 0;
}
