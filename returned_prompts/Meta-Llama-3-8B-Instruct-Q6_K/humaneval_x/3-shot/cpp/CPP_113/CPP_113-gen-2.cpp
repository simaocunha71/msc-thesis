    vector<string> result;
    for (int i=0;i<lst.size();i++)
    {
        int count=0;
        for (int j=0;j<lst[i].size();j++)
        {
            if (lst[i][j]-'0'%2==1)
                count++;
        }
        result.push_back(string("the number of odd elements ") + to_string(count) + "n the str" + to_string(i+1) + "ng " + to_string(i+1) + " of the " + to_string(i+1) + "nput.");
    }
    return result;
}  // This function takes vector of strings as an input and returns a vector of strings
// where each element is a string describing the number of odd digits in the corresponding string of the input. 
// For example, if the input is {"1234567"}, the output should be {"the number of odd elements 4 in the string 4 of the input."}. 
// The function loops over each string in the input, then over each character in the string, checks if the character is odd, and 
// if it is, increments a counter. After going over all characters in the string, it constructs a string describing the number of odd digits 
// in the string and adds it to the output vector. 
// The function then returns the output vector. 
// The result vector will have the same number of elements as the input vector, and each element in the result vector will be a string 
// describing the number of odd digits in the corresponding string of the input. 
// For example, if the input is {"3","11111111"}, the output should be 
// {"the number of odd elements 1 in the string 1 of the input.", "the number of odd elements 8 in the string 8 of the input."}. 
// The function uses the modulo operator '%' to check if a digit is odd. 
// The function uses the to_string function to convert the counter to a string. 
// The function uses the string constructor to construct the result string. 
// The function returns the result vector. 
// The function loops over each string in the input, and for each string, it loops over each character in the string. 
// The function uses the size function to get the size of the string. 
// The function uses the push_back function to add an element to the result vector. 
// The function uses the string constructor to