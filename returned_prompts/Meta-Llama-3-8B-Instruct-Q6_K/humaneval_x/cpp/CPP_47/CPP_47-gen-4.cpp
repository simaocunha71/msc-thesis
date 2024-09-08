    sort(l.begin(), l.end());  // sort the vector
    int n = l.size();          // get the size of the vector
    if(n % 2 == 0){            // if the size is even
        return (l[n/2 - 1] + l[n/2]) / 2.0;  // return the average of two middle elements
    }
    else{                      // if the size is odd
        return l[n/2];          // return the middle element
    }
}

int main() {
    vector<float> l = {3, 1, 2, 4, 5};
    printf("Median: %f\n", median(l));
    return 0;
}

