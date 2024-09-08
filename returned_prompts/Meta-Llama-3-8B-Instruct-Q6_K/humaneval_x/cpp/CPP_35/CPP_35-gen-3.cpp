    float max = l[0];
    for(int i = 1; i < l.size(); i++) {
        if(l[i] > max) {
            max = l[i];
        }
    }
    return max;
}

int main() {
    vector<float> v = {1, 2, 3};
    printf("%f", max_element(v));
    return 0;
}

S:
The function max_element takes a vector of floats as an argument and returns the maximum element in the vector.

The function iterates over the vector, comparing each element with the current maximum. If it finds a larger element, it updates the maximum.

In the main function, a vector of floats is created and the max_element function is called with this vector as an argument. The result is printed to the console.

Note: This function does not handle the case where the input vector is empty. If you want to handle this case, you can add a check at the beginning of the function to return a special value (e.g. -INFINITY) if the vector is empty.