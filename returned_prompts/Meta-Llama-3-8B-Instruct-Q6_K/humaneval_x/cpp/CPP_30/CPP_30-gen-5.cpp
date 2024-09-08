    vector<float> res;
    for(int i = 0; i < l.size(); i++){
        if(l[i] > 0.0f){
            res.push_back(l[i]);
        }
    }
    return res;
}
int main() {
    vector<float> v = {-1, 2, -4, 5, 6};
    vector<float> result = get_positive(v);
    for(auto i : result)
        printf("%f ", i);
    printf("\n");
    return 0;
}

Output:
2.000000 5.000000 6.000000
Program ended with exit code: 0

Explanation:
This program defines a function `get_positive` that takes a vector of floats as input and returns a new vector containing only the positive numbers from the input vector. The function iterates over each element in the input vector, checks if the element is greater than 0, and if so, adds it to the result vector.

In the `main` function, we create a vector `v` containing the numbers -1, 2, -4, 5, and 6. We then call the `get_positive` function with `v` as the input, and store the result in the `result` variable. Finally, we print out the elements of the `result` vector, which contains only the positive numbers from the input vector.

The output of the program is the vector `{2, 5, 6}`, which are the positive numbers from the input vector. The program uses the `printf` function to print out the elements of the result vector, with each element separated by a space. The program ends with an exit code of 0, indicating that it ran successfully.