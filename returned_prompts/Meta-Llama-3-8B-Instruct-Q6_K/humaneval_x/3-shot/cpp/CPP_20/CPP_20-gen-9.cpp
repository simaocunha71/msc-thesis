    float min_diff=float("inf");
    float closest_pair[2];
    int i,j;
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    {
        if (abs(numbers[i]-numbers[j])<min_diff)
        {
            min_diff=abs(numbers[i]-numbers[j]);
            closest_pair[0]=numbers[i];
            closest_pair[1]=numbers[j];
        }
    }
    return vector<float>(closest_pair, closest_pair+2);
} // end of function find_closest_elements
//  This function returns a vector of two elements. The first element is the first closest number and the second element is the second closest number. The numbers are in ascending order. //end of comment



