    float max = -INFINITY;
    for(int i=0; i<l.size(); i++){
        if(l[i] > max)
            max = l[i];
    }
    return max;
}

// Testing code
int main(){
    vector<float> l1 = {1, 2, 3};
    vector<float> l2 = {5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10};
    printf("%f\n", max_element(l1)); // should print 3.000000
    printf("%f\n", max_element(l2)); // should print 123.000000
    return 0;
}

*/

/*
