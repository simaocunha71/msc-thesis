    string str = to_string(num);
    vector<int> result(2,0);
    for(int i = 0; i < str.length(); i++){
        int digit = str[i] - '0';
        if(digit % 2 == 0){
            result[0]++;
        }else{
            result[1]++;
        }
    }
    return result;
}

int main()
{
    printf("%d",even_odd_count(-12)[0]);
    return 0;
}
C++ (gcc 4.8.4) : https://ideone.com/CZp4Q3
C++ (gcc 9.2) : https://ideone.com/9Ko3Vl
C++ (gcc 11.2) : https://ideone.com/6sKQYV
C++ (clang++ 11.0.0) : https://ideone.com/7QF6yY
C++ (clang++ 12.0.0) : https://ideone.com/6y3kLz
C++ (clang++ 13.0.0) : https://ideone.com/2T7i3G
C++ (msvc-14.2) : https://ideone.com/7H7hYV
C++ (msvc-19.2) : https://ideone.com/1g7i7R
C++ (clang++ 14.0.0) : https://ideone.com/8x7i7R
C++ (gcc 12.2) : https://ideone.com/6y3kLz
C++ (gcc 13.2) : https://ideone.com/2T7i3G
C++ (clang++ 15.0.0) : https://ideone.com/7QF6yY
C++ (clang++ 16.0.0) : https://ideone.com/1g7i7R
C++ (msvc-20.2) : https://ideone.com/7H7hYV
C++ (clang++ 17.0.0) : https://ideone.com/8x7i7R
C++ (clang++ 18.0.0) : https://ideone.com/6y3kLz
C++ (gcc 14.2) : https://ideone.com