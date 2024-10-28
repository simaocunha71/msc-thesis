    if (n==0)
        return "0";
    else{
        string s=string_sequence(n-1);
        s=s+" "+to_string(n);
        return s;
    }
}
int main(){
    printf("%s",string_sequence(5));
    return 0;
}

