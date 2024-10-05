    vector<int> result;
    int size = numbers.size();
    for(int i=0; i<size; i++)
    {
        if(find(result.begin(), result.end(), numbers[i]) == result.end())
        {
            result.push_back(numbers[i]);
        }
    }
    return result;
}

int main()
{
    vector<int> numbers = {1, 2, 3, 2, 4};
    vector<int> result = remove_duplicates(numbers);
    for(auto& i : result)
    {
        printf("%d ", i);
    }
    return 0;
}




/*

To solve the problem, we can follow these steps:

1. Create an empty result vector.
2. Iterate over the input vector and for each element, check if it is already present in the result vector.
3. If the element is not present in the result vector, add it.
4. At the end of the iteration, the result vector will contain all the unique elements from the input vector.
5. Return the result vector.

The time complexity of the above algorithm will be O(n), where n is the size of the input vector.

Here is the implementation of the above algorithm in C++:

*/









































































































































































































