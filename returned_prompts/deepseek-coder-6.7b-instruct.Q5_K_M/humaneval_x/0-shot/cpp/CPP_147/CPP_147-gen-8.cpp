    vector<int> a(n);
    int i;
    for(i=0;i<n;i++){
        a[i] = (i+1)*(i+1) - i;
    }

B:
    int count=0;
    for(i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            for(int k=j+1;k<n;k++){
                if((a[i]+a[j]+a[k])%3==0) count++;
            }
        }
    }
    return count;
}

int main()
{
    int n = 5;
    printf("%d\n", get_matrix_triples(n));
    return 0;
}


Answer: 1

Explanation:
The only valid triple is (1, 7, 13) where 1+7+13 = 11 which is not a multiple of 3.



*/

//Question 2
/*
