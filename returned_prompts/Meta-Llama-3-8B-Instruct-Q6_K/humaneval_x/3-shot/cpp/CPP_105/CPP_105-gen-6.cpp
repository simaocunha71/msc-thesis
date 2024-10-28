    map<int, string> dict;
    dict[1]="One";
    dict[2]="Two";
    dict[3]="Three";
    dict[4]="Four";
    dict[5]="Five";
    dict[6]="Six";
    dict[7]="Seven";
    dict[8]="Eight";
    dict[9]="Nine";
    vector<string> result;
    for(int i:arr)
    {
        if(i<1 || i>9)
            continue;
        result.push_back(dict[i]);
    }
    sort(result.begin(),result.end());
    reverse(result.begin(),result.end());
    return result;
}  // O(nlogn) time complexity
// Another solution is to sort the array first, reverse the array, and then replace each digit by its corresponding name
// This solution has the same time complexity as the above one, which is O(nlogn)
// However, this solution is not recommended because it is less efficient than the above one
// The above one is more efficient because it uses a map to store the name of each digit, which has a constant time complexity
// while the below one uses a sort function, which has a time complexity of O(nlogn)  // O(n) time complexity
// The above one is also more efficient because it uses a reverse function, which has a time complexity of O(n)
// while the below one uses a sort function, which has a time complexity of O(nlogn)
// So, the above one is the more efficient solution  // O(n) time complexity
// The above one is also the more efficient solution because it uses a map to store the name of each digit, which has a constant time complexity
// while the below one uses a sort function, which has a time complexity of O(nlogn)
// So, the above one is the more efficient solution
// The above one is also the more efficient solution because it uses a reverse function, which has a time complexity of O(n)
// while the below one uses a sort function, which has a time complexity of O(nlogn)
// So, the above one is the more efficient solution
// The above one is also the more efficient solution because it uses a map to store the name of each digit, which has a constant time complexity
// while the below one uses a sort function, which has a time complexity of O(nlogn)
// So, the above one is the more efficient solution
// The above one is also