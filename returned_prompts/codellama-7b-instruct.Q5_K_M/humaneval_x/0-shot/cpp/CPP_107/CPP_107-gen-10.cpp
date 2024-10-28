    vector<int> res(2,0);
    int max_palindrome = 10000;
    int min_palindrome = 10000;
    int max_palindrome_even = 0;
    int max_palindrome_odd = 0;
    int min_palindrome_even = 0;
    int min_palindrome_odd = 0;
    int max_palindrome_even_count = 0;
    int max_palindrome_odd_count = 0;
    int min_palindrome_even_count = 0;
    int min_palindrome_odd_count = 0;
    for(int i=1;i<=n;i++){
        //string s = to_string(i);
        string s = to_string(i);
        int len = s.length();
        bool is_even = true;
        for(int j=0;j<len/2;j++){
            if(s[j] != s[len-j-1]){
                is_even = false;
                break;
            }
        }
        if(is_even){
            if(s[0] == '1'){
                min_palindrome_odd++;
                min_palindrome_odd_count++;
            }else{
                if(s[0] == '0'){
                    min_palindrome_even++;
                    min_palindrome_even_count++;
                }else{
                    min_palindrome_even++;
                    min_palindrome_odd++;
                    min_palindrome_even_count++;
                    min_palindrome_odd_count++;
                }
            }
        }else{
            if(s[0] == '1'){
                max_palindrome_odd++;
                max_palindrome_odd_count++;
            }else{
                if(s[0] == '0'){
                    max_palindrome_even++;
                    max_palindrome_even_count++;
                }else{
                    max_palindrome_