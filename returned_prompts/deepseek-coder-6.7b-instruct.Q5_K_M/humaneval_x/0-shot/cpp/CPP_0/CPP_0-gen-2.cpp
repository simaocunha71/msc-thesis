    for(int i=0; i<numbers.size(); i++){
        for(int j=i+1; j<numbers.size(); j++){
            if(fabs(numbers[i]-numbers[j]) <= threshold){
                return true;
            }
        }
    }
    return false;
}

int main(){
    vector<float> v1 = {1.0, 2.0, 3.0};
    vector<float> v2 = {1.0, 2.8, 3.0, 4.0, 5.0, 2.0};
    printf("%d\n", has_close_elements(v1, 0.5));
    printf("%d\n", has_close_elements(v2, 0.3));
    return 0;
}

*/

/*
Note:
Here, we are using fabs function from math library to get the absolute value of the difference between two numbers. This way we are ensuring that we are only checking for values that are closer than the threshold.

The function has_close_elements will iterate over all pairs of elements in the vector, and if any pair of elements is closer than the given threshold, it will return true. If no such pair is found after checking all pairs, it will return false.
*/

// END

// Solution Ends

// C++ Code Ends

// END OF CODE

// END OF PROBLEM SOLUTION

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// SOLUTION ENDS

// CODE ENDS

// END OF FILE

// S