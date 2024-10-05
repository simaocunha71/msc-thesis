    int result = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] >= 'A' && s[i] <= 'Z'){
            result += s[i];
        }
    }
    return result;
}
int main(){
    printf("%d", digitSum("abAB"));
    return 0;
}


Ans:
    int result = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] >= 'A' && s[i] <= 'Z'){
            result += s[i];
        }
    }
    return result;
}
