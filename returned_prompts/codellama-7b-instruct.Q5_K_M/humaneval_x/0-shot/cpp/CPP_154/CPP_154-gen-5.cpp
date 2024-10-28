    if(a.empty() || b.empty())
        return false;
    int a_len = a.length();
    int b_len = b.length();
    if(b_len > a_len)
        return false;

    for(int i = 0; i < a_len - b_len + 1; i++){
        int j = 0;
        while(j < b_len && a[i+j] == b[j])
            j++;
        if(j == b_len)
            return true;
    }

    return false;
}

int main(){
    string a("abcd");
    string b("abd");
    printf("%d\n",cycpattern_check(a,b));
    return 0;
}
