    int cnt = 0;
    for(int i = 1; i <= n; ++i){
        if(i % 3 == 1){
            for(int j = 1; j <= n; ++j){
                if(j % 3 == 2){
                    for(int k = 1; k <= n; ++k){
                        if(k % 3 == 0 && i + j + k % 3 == 0){
                            ++cnt;
                        }
                    }
                }
            }
        }
    }
    return cnt;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", get_matrix_triples(n));
    return 0;
}



ANSWER:
No
*/


/*
You are given a positive integer n. You have to create an integer vector a of length n.
    For each i (1 ≤ i ≤ n), the value of a{i} = i * i - i + 1.
    Return the number of triples (a{i}, a{j}, a{k}) of a where i < j < k, 
and a[i] + a[j] + a[k] is a multiple of 3.

Example :
    Input: n = 5
    Output: 1
    Explanation: 
    a = {1, 3, 7, 13, 21}
    The only valid triple is (1, 7, 13).












































































































































