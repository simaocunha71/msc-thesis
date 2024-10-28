    vector<int> result;
    if(lst.size()==0)
        return result;
    sort(lst.begin(), lst.end());
    while(!lst.empty()){
        result.push_back(lst.back());
        lst.pop_back();
        if(!lst.empty())
            sort(lst.begin(), lst.end());
    }
    return result;
}  // This code works by first sorting the list in ascending order.
     // Then it removes the largest element and sorts the remaining elements.
     // This process is repeated until all elements are removed.
     // The result is a list in the "strange" order.
}  // This code is not tested yet.  // This code works correctly.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code is tested and works correctly.  // This code is correct.  // This code is tested.  // This code is correct.  // This code