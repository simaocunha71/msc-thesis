    if (arr.size()==0) return true;
    int i,j;
    for (i=0;i<arr.size()-1;i++)
    {
        for (j=i+1;j<arr.size();j++)
        {
            if (arr[i]>arr[j])
                return false;
        }
    }
    return true;
} 
//or
bool move_one_ball(vector<int> arr){
    for(int i = 0; i < arr.size() - 1; i++){
        if(arr[i] > arr[i + 1])
            return false;
    }
    return true;
} 
//or
bool move_one_ball(vector<int> arr){
    for(int i = 0; i < arr.size() - 1; i++){
        if(arr[i] > arr[(i+1)%arr.size()])
            return false;
    }
    return true;
} 



