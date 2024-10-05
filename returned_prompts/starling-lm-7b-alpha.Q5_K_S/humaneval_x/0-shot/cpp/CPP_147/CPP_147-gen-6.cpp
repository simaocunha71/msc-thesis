    vector<int> arr;
    for(int i = 1; i <= n; i++)
        arr.push_back(i * i - i + 1);
    int c = 0;
    for(int i = 0; i < n; i++)
        for(int j = i + 1; j < n; j++)
            for(int k = j + 1; k < n; k++)
                if((arr[i] + arr[j] + arr[k]) % 3 == 0)
                    c++;
    return c;
}


int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", get_matrix_triples(n));
    return 0;
}


ANS:

/*
Here's a step-by-step explanation of how to solve this problem.

1. Create an array of length n such that a[i] = i * i - i + 1 for each i in the range [1..n].
2. For each i in the range [1..n], find all pairs of j (j > i) such that a[i] + a[j] is a multiple of 3. The number of such pairs is given by (n - i) / 2.
3. For each pair of i and j, find the number of k in the range [j + 1..n] such that a[i] + a[j] + a[k] is a multiple of 3. This can be calculated by taking the complement of the pairs that do not satisfy the condition.
4. Summing the result from step 2 and step 3, we get the total number of triples (a[i], a[j], a[k]) that satisfy the condition.

The complexity of this approach is O(n^2), where n is the length of the array.
*/






































































