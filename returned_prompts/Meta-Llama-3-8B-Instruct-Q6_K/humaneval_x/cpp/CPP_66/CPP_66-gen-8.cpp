    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(isupper(s[i])){
            sum += s[i];
        }
    }
    return sum;
}

B:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += s[i];
            }
        }
        return sum;
    }

C:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += toupper(s[i]);
            }
        }
        return sum;
    }

D:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += toupper(s[i]) - 64;
            }
        }
        return sum;
    }

E:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += toupper(s[i]) - 65;
            }
        }
        return sum;
    }

F:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += toupper(s[i]) - 65;
            }
        }
        return sum;
    } 

G:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += (int)s[i] - 64;
            }
        }
        return sum;
    }

H:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += (int)s[i] - 65;
            }
        }
        return sum;
    } 

I:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += (int)s[i];
            }
        }
        return sum;
    }