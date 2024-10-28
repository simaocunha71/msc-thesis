    int n = l.size();

    if (n < 3) return false;

    sort(l.begin(), l.end());

    for (int i = 0; i < n - 1; i++){

        int a = l[i];
        int start = i + 1;
        int end = n - 1;

        while (start < end){

            int b = l[start];
            int c = l[end];

            if (a + b + c == 0){
                return true;
            }

            else if (a + b + c < 0){
                start += 1;
            }

            else{
                end -= 1;
            }
        }
    }
    return false;
}

int main(){
    vector<int> l = {2, 4, -5, 3, 9, 7};
    printf("%d\n", triples_sum_to_zero(l));
    return 0;
}
```

## References
- [Triplet Sum to Zero](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [Triplet Sum to Zero](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [Triplet Sum to Zero](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [Triplet Sum to Zero](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [Triplet Sum to Zero](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [Triplet Sum to Zero](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
- [Triplet Sum