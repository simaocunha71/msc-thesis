    float max = l[0];
    for(int i = 1; i<l.size(); i++){
        if(max < l[i]){
            max = l[i];
        }
    }
    return max;
}

int main(){
    vector<float> l = {1, 2, 3};
    printf("%f\n", max_element(l));
    return 0;
}


/*
To solve this, we need to find the maximum element in a given vector. This can be achieved by iterating through the vector and comparing each element with the current maximum element. If an element is found to be greater than the current maximum, then that element becomes the new maximum.

In the above code, the max_element function takes a vector of floats as its parameter. It initializes the max variable to the first element of the vector. Then, it iterates through the remaining elements of the vector, comparing each element with the current maximum. If an element is found to be greater than the current maximum, then the max variable is updated to the new maximum. After iterating through all the elements, the max variable will hold the maximum element of the vector.

Finally, the main function creates a vector l with elements {1, 2, 3}. It then calls the max_element function with the vector l as its argument and prints the result using the printf function.

The output of the program will be the maximum element of the vector, which in this case is 3.

Note: The code provided is a solution to the given problem and may not be the most efficient or optimal solution.


*/


















































































































































