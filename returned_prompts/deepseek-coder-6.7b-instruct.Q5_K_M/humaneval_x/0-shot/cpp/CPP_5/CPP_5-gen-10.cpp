    vector<int> interspersed;
    for(int i=0; i<numbers.size(); i++){
        interspersed.push_back(numbers[i]);
        if(i<numbers.size()-1)
            interspersed.push_back(delimeter);
    }
    return interspersed;
}

int main(){
    vector<int> numbers = {1, 2, 3};
    int delimeter = 4;
    vector<int> interspersed = intersperse(numbers, delimeter);
    for(int i=0; i<interspersed.size(); i++){
        printf("%d ", interspersed[i]);
    }
    return 0;
}

// Explanation:
// We iterate through the input vector `numbers` and for each element, we add it to a new vector `interspersed`.
// If the current element is not the last element in `numbers`, we also add `delimeter` to `interspersed`.
// Finally, we return `interspersed`.

// Note:
// This solution assumes that the input vector `numbers` is not empty.
// If the input vector `numbers` can be empty, you should add a check for this before the loop.
// If the input vector `numbers` is empty, the function will return an empty vector.
// This is because there are no elements to intersperse, so the function will not add the delimeter.
// If you want to handle this case differently, you can add a special case for it.

// Also,
// This solution assumes that the type of the elements in the input vector `numbers` is int.
// If the type of the elements in the input vector `numbers` is not int, you will need to adjust the solution accordingly.
// For example, if the type is double, you should change the type of the variable `numbers` to vector<double>, and so on.
// Also, if the type is a user-defined type, you will need to overload the << operator for that type to be able to print it.
// If the type is a complex type, you