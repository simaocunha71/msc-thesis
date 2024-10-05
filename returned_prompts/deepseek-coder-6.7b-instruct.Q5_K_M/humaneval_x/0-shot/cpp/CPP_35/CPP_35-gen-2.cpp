    float max = -INFINITY;
    for(int i=0; i<l.size(); i++)
        if(l[i] > max)
            max = l[i];
    return max;
}
int main() {
    vector<float> l1 = {1, 2, 3};
    printf("%f\n", max_element(l1));

    vector<float> l2 = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    printf("%f\n", max_element(l2));

    return 0;
}

The code above defines a function that iterates through the given vector and returns the maximum value. It then tests the function with two vectors, printing the maximum values of each. 

