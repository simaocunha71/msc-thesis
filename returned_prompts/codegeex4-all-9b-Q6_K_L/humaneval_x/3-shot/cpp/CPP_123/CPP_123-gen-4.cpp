    int i,j;
    
    for (i=0;i<numbers.size();i++)
    for (j=i+1;j<numbers.size();j++)
    if (abs(numbers[i]-numbers[j])<threshold)
    return true;

    return false;
}

The function name is not very descriptive. It is better to have a name that describes what the function does. Also, the parameter names are not very good. They should describe the parameter itself, not the type of the parameter. The function should check if there are two elements in the vector that are closer than the given threshold. So a good name would be something like close_elements_in_vector.
The function has a lot of code in the function body. It is better to have the code in separate functions. This makes it easier to understand what the function does.
The function doesn't do anything with the given vector. It just checks if there are two elements in the vector that are closer than the given threshold. It would be better if the function would return the two elements that are closer than the given threshold. This would make it easier to understand what the function does.
The function doesn't check if the vector is empty. It would be