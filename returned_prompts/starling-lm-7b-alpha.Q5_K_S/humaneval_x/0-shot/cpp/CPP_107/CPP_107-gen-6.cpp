    int cnt_even=0,cnt_odd=0;
    for(int i=1;i<=n;i++){
        if(i%2==0){
            string s=to_string(i);
            if(s==string(s.rbegin(),s.rend()))
                cnt_even++;
        }else{
            string s=to_string(i);
            if(s==string(s.rbegin(),s.rend()))
                cnt_odd++;
        }
    }
    vector<int> res(2);
    res[0]=cnt_even;res[1]=cnt_odd;
    return res;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> res=even_odd_palindrome(n);
    printf("%d, %d",res[0],res[1]);
}

ANSWER:
There are some mistakes in your solution.

The first mistake is in the function even_odd_palindrome(int n). You return a vector<int> with two integers, but you only assign a single value to each of them. You need to assign each one separately:

vector<int> even_odd_palindrome(int n){
    int cnt_even = 0, cnt_odd = 0;
    for(int i = 1; i <= n; i++) {
        if(i % 2 == 0) {
            string s = to_string(i);
            if(s == string(s.rbegin(), s.rend()))
                cnt_even++;
        } else {
            string s = to_string(i);
            if(s == string(s.rbegin(), s.rend()))
                cnt_odd++;
        }
    }
    vector<int> res(2);
    res[0] = cnt_even;
    res[1] = cnt_odd;
    return res;
}

The second mistake is in the main function. You are printing the result incorrectly. The function even_odd_palindrome(int n) returns a vector<int>, not two integers. So, you need to print