    if(array.size()==0)
    {
        return array;
    }
    int mid=array.size()/2;
    vector<int> left_array;
    vector<int> right_array;
    left_array=sort_array(array);
    right_array=sort_array(array);
    vector<int> result_array;
    int index_left=0,index_right=0;
    if((array[mid]+array[mid-1])%2==0)
    {
        while(index_left<left_array.size()&&index_right<right_array.size())
        {
            if(left_array[index_left]<right_array[index_right])
            {
                result_array.push_back(left_array[index_left]);
                index_left++;
            }
            else
            {
                result_array.push_back(right_array[index_right]);
                index_right++;
            }
        }
        while(index_left<left_array.size())
        {
            result_array.push_back(left_array[index_left]);
            index_left++;
        }
        while(index_right<right_array.size())
        {
            result_array.push_back(right_array[index_right]);
            index_right++;
        }
    }
    else
    {
        while(index_left<left_array.size()&&index_right<right_array.size())
        {
            if(left_array[index_left]>right_array[index_right])
            {
                result_array.push_back(left_array[index_left]);
                index_left++;
            }
            else
            {
                result_array.push_back(right_array[index_right]);
                index_right++;
            }
        }
        while(index_left<left_array.size())
        {
            result_array.push_back(left_array[index_left]);
            index_left++;
        }
        while(index_right<right_