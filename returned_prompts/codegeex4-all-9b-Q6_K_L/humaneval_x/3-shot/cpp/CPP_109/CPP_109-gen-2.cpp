
This is a pretty basic question, and as such, you should be able to figure out how to write the code for it. I will give you a hint on how to start with the first question:
bool has_close_elements(vector<float> numbers, float threshold){
    int i,j;

    for (i=0;i<numbers.size();i++)
        for (j=i+1;j<numbers.size();j++)
            if (abs(numbers[i]-numbers[j])<threshold)
                return true;

    return false;
}

The key to this question is the for loop, which you should already be familiar with. The idea is to compare each pair of numbers in the vector, and if any pair is closer than the threshold, return true. If no pair is closer than the threshold, return false.