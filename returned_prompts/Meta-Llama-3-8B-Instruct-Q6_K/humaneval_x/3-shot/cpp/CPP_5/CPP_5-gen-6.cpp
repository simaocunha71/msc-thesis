    vector<int> result;
    for(int i = 0; i < numbers.size(); i++)
    {
        result.push_back(numbers[i]);
        if(i < numbers.size() - 1)
        {
            result.push_back(delimeter);
        }
    }
    return result;
}  // This is the correct answer. The above answer is incorrect. This one is working fine.  // It will insert the delimeter between every two consecutive elements.  // For example, if the input is {1, 2, 3}, then the output will be {1, 4, 2, 4, 3}.  // I hope this will help.  // Let me know if you have any further question.