    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(isupper(s[i])){
            sum += (int)s[i];
        }
    }
    return sum;
}

B:
    int digitSum(string s){
        int sum = 0;
        for(char c : s){
            if(isupper(c))
                sum += (int)c;
        }
        return sum;
    }

C:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] >= 'A' && s[i] <= 'Z')
                sum += (int)s[i];
        }
        return sum;
    }

D:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            sum += (int)s[i];
        }
        return sum;
    }

E:
    int digitSum(string s){
        int sum = 0;
        for(char c : s){
            if(isupper(c))
                sum += (int)c - 'A' + 65;
        }
        return sum;
    }

F:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] >= 'A' && s[i] <= 'Z')
                sum += (int)s[i] - 'A' + 65;
        }
        return sum;
    }

G:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] >= 'A' && s[i] <= 'Z')
                sum += (int)s[i];
        }
        return sum;
    }

H:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i]))
                sum += (int)s[i];
        }
        return sum;
    }

I:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(s[i] >= 'A' && s[i] <= 'Z')
                sum += (int)s[i];
        }
        return sum;
    }

J:
    int digitSum