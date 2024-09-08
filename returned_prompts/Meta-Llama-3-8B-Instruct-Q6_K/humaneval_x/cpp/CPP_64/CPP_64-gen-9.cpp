    int count = 0;
    for(int i=0; i<s.length(); i++){
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' || (s[i]=='y' && i==s.length()-1)){
            count++;
        }
    }
    return count;
}

B:
    int vowels_count(string s){
        int count = 0;
        for(int i=0; i<s.length(); i++){
            if(isalpha(s[i]) && (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' || s[i]=='y' && i==s.length()-1)){
                count++;
            }
        }
        return count;
    }  

C:
    int vowels_count(string s){
        int count = 0;
        for(int i=0; i<s.length(); i++){
            if(isalpha(s[i]) && (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u') || i==s.length()-1 && s[i]=='y'){
                count++;
            }
        }
        return count;
    }

D:
    int vowels_count(string s){
        int count = 0;
        for(int i=0; i<s.length(); i++){
            if(isalpha(s[i]) && (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u') || s[i]=='y' && i==s.length()-1){
                count++;
            }
        }
        return count;
    }  

E:
    int vowels_count(string s){
        int count = 0;
        for(int i=0; i<s.length(); i++){
            if(isalpha(s[i]) && (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u') || (s[i]=='y' && i==s.length()-1)){
                count++;
            }
        }
        return count;
    }
    int main()
    {
        string s="abcde";
        cout<<vowels_count(s)<<" ";
        s="ACEDY";
        cout<<vowels_count(s);
        return 0;
    }
F:
    int vowels_count(string s){
