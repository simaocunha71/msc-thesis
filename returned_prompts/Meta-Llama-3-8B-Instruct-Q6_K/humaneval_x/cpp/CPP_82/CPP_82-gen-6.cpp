bool prime_length(string str)
{
    int len = str.length();
    if(len <= 1) return false;
    for(int i = 2; i * i <= len; i++){
        if(len % i == 0) return false;
    }
    return true;
}

B:
bool prime_length(string str){
    int len = str.length();
    if(len <= 1) return false;
    for(int i = 2; i <= len; i++){
        if(len % i == 0 && isPrime(i)) return false;
    }
    return true;
}

C:
bool prime_length(string str){
    int len = str.length();
    if(len <= 1) return false;
    for(int i = 2; i <= len; i++){
        if(len % i == 0) return false;
    }
    return true;
}

isPrime:
bool isPrime(int n)
{
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

D:
bool prime_length(string str){
    int len = str.length();
    return isPrime(len);
}

isPrime:
bool isPrime(int n)
{
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

E:
bool prime_length(string str){
    int len = str.length();
    if(len <= 1) return false;
    return isPrime(len);
}

isPrime:
bool isPrime(int n)
{
    if(n <= 1) return false;
    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) return false;
    }
    return true;
}

F:
bool prime_length(string str){
    int len = str.length();
    if(len <= 1) return false;
    int count = 0;
    for(int i = 2; i <= len; i++){
        if(len % i == 0) count++;
    }
    return count == 0;
}

G:
bool prime_length(string str){
    int len = str.length();
    if(len <= 1) return false;
    for(int i = 2; i <= len; i++){
        if(len % i == 0