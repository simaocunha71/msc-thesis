    vector<float> positive;
    for (int i = 0; i < l.size(); i++){
        if (l[i] > 0){
            positive.push_back(l[i]);
        }
    }
    return positive;
}

int main()
{
    vector<float> v1 = {-1, 2, -4, 5, 6};
    vector<float> v2 = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    vector<float> pos1, pos2;
    pos1 = get_positive(v1);
    pos2 = get_positive(v2);
    for (int i = 0; i < pos1.size(); i++){
        printf("%.0f ", pos1[i]);
    }
    printf("\n");
    for (int i = 0; i < pos2.size(); i++){
        printf("%.0f ", pos2[i]);
    }
    printf("\n");
    return 0;
}

```

This program will filter out the negative numbers from the input vector and return only the positive ones. It uses a for loop to iterate over each element in the input vector, checks if the number is positive, and if so, adds it to a new vector.

The main function tests the get_positive function with two different input vectors, and then prints out the resulting vectors. The output of this program will be the positive numbers from the input vectors, separated by spaces.
