    int n = arr.size();
    if(n == 0)
        return true;
    int i = 0;
    while(i < n - 1){
        if(arr[i] > arr[i + 1]){
            //shift the array
            for(int j = 0;j < n;j++){
                if(j == i + 1)
                    arr.push_back(arr[j]);
                else if(j == 0)
                    arr[0] = arr[i + 1];
                else
                    arr[j] = arr[j - 1];
            }
            n++;
            i = 0;
        }
        else
            i++;
    }
    if(arr[0] <= arr[1])
        return true;
    else
        return false;
}
int main(){
    vector<int> arr = {3, 4, 5, 1, 2};
    if(move_one_ball(arr))
        printf("true\n");
    else
        printf("false\n");
    return 0;
}
