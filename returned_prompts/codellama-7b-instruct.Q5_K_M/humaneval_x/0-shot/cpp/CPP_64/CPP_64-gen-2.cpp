    int count = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'){
            count++;
        }
        if(s[i] == 'y' && i == s.size()-1){
            count++;
        }
    }
    return count;
}

// 测试代码
int main(int argc, char** argv){
    printf("%d\n", vowels_count("abcde"));
    printf("%d\n", vowels_count("ACEDY"));
    return 0;
}

