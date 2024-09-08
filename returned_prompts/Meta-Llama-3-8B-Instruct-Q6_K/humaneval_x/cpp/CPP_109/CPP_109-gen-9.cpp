    if(arr.empty())return true;
    int n=arr.size();
    int x=0;
    for(int i=1;i<n;i++){
        if(arr[i-1]>arr[i]){
            x++;
        }
    }
    if(x>0)return false;
    else return true;
}

int main()
{
    vector<int> arr={3, 4, 5, 1, 2};
    printf("%d",move_one_ball(arr));
    return 0;
}
//Output: 1

