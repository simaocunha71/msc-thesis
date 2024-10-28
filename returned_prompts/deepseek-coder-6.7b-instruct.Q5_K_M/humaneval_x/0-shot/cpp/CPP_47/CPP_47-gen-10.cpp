    sort(l.begin(), l.end());
    if(l.size()%2 == 0)
        return (l[l.size()/2 - 1] + l[l.size()/2]) / 2;
    else
        return l[l.size()/2];
}

int main(){
    vector<float> l = {3, 1, 2, 4, 5};
    printf("%f\n", median(l));
    l = {-10, 4, 6, 1000, 10, 20};
    printf("%f\n", median(l));
    return 0;
}

*/

/*
E:
This function works by sorting the vector l in ascending order. Then, if the size of the vector is even, it returns the average of the two middle elements. If the size of the vector is odd, it returns the middle element. The result is the median of the vector.
*/

// 4. Write a function that takes a string and a character as input and counts the number of occurrences of that character in the string.
/*
