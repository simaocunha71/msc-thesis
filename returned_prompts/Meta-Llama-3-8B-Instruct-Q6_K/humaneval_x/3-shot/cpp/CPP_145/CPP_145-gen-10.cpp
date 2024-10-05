    vector<pair<int,int>> points;
    int i;
    for (i=0;i<nums.size();i++)
    {
        points.push_back(make_pair(i,sum_digits(nums[i])));
    }
    sort(points.begin(),points.end());
    vector<int> result;
    for (i=0;i<points.size();i++)
    {
        result.push_back(nums[points[i].first]);
    }
    return result;
}

int sum_digits(int num)
{
    int sum=0;
    while(num>0)
    {
        sum+=num%10;
        num=num/10;
    }
    return sum;
}