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
}  // Not exactly what I wanted, but it's close. If I want to insert the delimiter between the elements, I can do that like this:
    // vector<int> result;
    // for(int i = 0; i < numbers.size(); i++)
    // {
    //     if(i > 0)
    //     {
    //         result.push_back(delimeter);
    //     }
    //     result.push_back(numbers[i]);
    // }
    // return result;  // This will insert the delimeter between each element.  // Not exactly what I wanted, but it's close. If I want to insert the delimiter between the elements, I can do that like this:
    // vector<int> result;
    // for(int i = 0; i < numbers.size(); i++)
    // {
    //     if(i > 0)
    //     {
    //         result.push_back(delimeter);
    //     }
    //     result.push_back(numbers[i]);
    // }
    // return result;  // This will insert the delimeter between each element.  // Not exactly what I wanted, but it's close. If I want to insert the delimeter between the elements, I can do that like this:
    // vector<int> result;
    // for(int i = 0; i < numbers.size(); i++)
    // {
    //     if(i > 0)
    //     {
    //         result.push_back(delimeter);
    //     }
    //     result.push_back(numbers[i]);
    // }
    // return result;  // This will insert the delimeter between each element.  // Not exactly what I wanted, but it's close. If I want to insert the delimiter between the elements, I can do that like this:
    // vector<int> result;
    // for(int i = 0; i < numbers.size(); i++)
    // {
    //     if(i > 0)
    //     {
    //         result.push_back(delimeter);
    //     }
    //     result.push_back(numbers[i]);
    // }
    // return result;  // This will insert the delimeter between each element.  // Not exactly