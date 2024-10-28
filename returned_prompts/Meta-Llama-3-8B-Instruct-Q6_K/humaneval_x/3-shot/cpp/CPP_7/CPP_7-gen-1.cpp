    vector<string> filtered_strings;
    int i;
    for (i=0;i<strings.size();i++)
    {
        if (strings[i].find(substring)!=string::npos)
        {
            filtered_strings.push_back(strings[i]);
        }
    }
    return filtered_strings;
}  // This can be simplified using a range-based for loop and std::copy_if
// vector<string> filter_by_substring(vector<string> strings, string substring){
//     return vector<string>(std::remove_if(strings.begin(), strings.end(),[&substring](const string& s){return !s.find(substring);}), strings.end());
// }  // This is a more functional way of doing the same thing.  //  It uses the remove_if function from the algorithm library, which removes elements from a range for which a predicate is true.  The predicate is a lambda function that checks if a string contains the given substring.  The end iterator is returned, which is used to create a new vector with the remaining elements.  // This version is more concise and more efficient than the original.  //  It also uses C++11 features, so it won't work in older versions of C++.  //  It's also worth noting that the original code has a linear time complexity, while this version has a constant time complexity for the find operation, and a linear time complexity for the remove_if operation.  //  Therefore, this version is more efficient for large inputs.  //  It's also worth noting that this version creates a new vector, which can be a problem if memory is a concern.  //  In that case, the original code might be a better choice.  //  But in general, this version is a good choice for most use cases.  //  It's also worth noting that this version uses C++11 features, so it won't work in older versions of C++.  //  But if you're using a modern compiler, it should work fine.  //  It's also worth noting that this version is more idiomatic C++ than the original code.  //  It uses the standard library and the range-based for loop, which are both idiomatic C++ features.  //  So, if you're looking for a more idiomatic way to do this, this is the way to go.  //  But if you're looking for a more concise way, the original code might be a better choice.  //  It's also worth noting that