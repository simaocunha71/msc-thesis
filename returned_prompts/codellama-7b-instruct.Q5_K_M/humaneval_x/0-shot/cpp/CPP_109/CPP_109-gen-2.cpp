    if(arr.size()==0) return true;
    if(arr.size()==1) return true;
    int i=0;
    int j=arr.size()-1;
    while(i<j){
        if(arr[i]>arr[j]) return false;
        i++;
        j--;
    }
    if(arr[i]>arr[j]) return false;
    int temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
    j--;
    i++;
    while(i<j){
        if(arr[i]>arr[j]) return false;
        i++;
        j--;
    }
    if(arr[i]>arr[j]) return false;
    temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
    j--;
    i++;
    while(i<j){
        if(arr[i]>arr[j]) return false;
        i++;
        j--;
    }
    if(arr[i]>arr[j]) return false;
    temp=arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
    return true;
}
int main(int argc, char** argv) {

    vector<int> arr={3, 4, 5, 1, 2};
    printf("The given vector is %d \n",move_one_ball(arr));
    return 0;
}











































































































































