    sort(l.begin(), l.end());
    for(int i=0; i+l.size()-2 < l.size(); i++)
    {
        int left = i+1;
        int right = l.size()-1;
        while(left < right)
        {
            int sum = l[i] + l[left] + l[right];
            if(sum < 0)
            {
                left++;
            }
            else if(sum > 0)
            {
                right--;
            }
            else
            {
                return true;
            }
        }
    }
    return false;
}