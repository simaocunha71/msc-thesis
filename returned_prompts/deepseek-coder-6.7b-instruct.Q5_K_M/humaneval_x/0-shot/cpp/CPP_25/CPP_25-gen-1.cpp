    vector<int> factors;
    for(int i = 2; i <= n; i++){
        while(n%i == 0){
            factors.push_back(i);
            n /= i;
        }
    }
    return factors;
}

int main(){
    vector<int> factors = factorize(70);
    for(int factor : factors){
        printf("%d ", factor);
    }
    return 0;
}
*/

