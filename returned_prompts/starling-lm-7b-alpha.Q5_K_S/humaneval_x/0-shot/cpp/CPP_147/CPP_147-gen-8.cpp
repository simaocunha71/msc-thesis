    vector<int> a(n);
    for(int i=0;i<n;i++)
        a[i]=i*i-i+1;
    int ans=0;
    for(int i=0;i<n;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            for(int k=j+1;k<n;k++)
            {
                if((a[i]+a[j]+a[k])%3==0)
                    ans++;
            }
        }
    }
    return ans;

}
int main(){
    int n;
    scanf("%d",&n);
    printf("%d",get_matrix_triples(n));
    return 0;
}




ANS:
The above code is accepted by the online judge, but I feel that it can be further optimized. Here are some optimizations:

1. If n is small, we can use a brute force approach to calculate all the possible values of a[i]+a[j]+a[k] and count the multiples of 3. This approach has a time complexity of O(n^3). However, if n is large, this approach may be inefficient.

2. We can use a dynamic programming approach to optimize the time complexity. We can pre-calculate the sum of all possible values of a[i]+a[j]+a[k] for all i, j and k, and then count the multiples of 3. This approach has a time complexity of O(n^3). However, this approach may still be inefficient for large values of n.

3. We can use a mathematical approach to optimize the time complexity. We can observe that a[i]+a[j]+a[k] can only be a multiple of 3 if at least one of a[i], a[j], and a[k] is a multiple of 3. We can calculate the number of multiples of 3 for a[i], a[j], and a[k] separately, and then multiply them together to get the total number of multiples of 3 for a[i]+a[j]+a[k]. This approach has