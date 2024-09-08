    string s = "";
    for(int i = 0; i <= n; i++){
        s += to_string(i) + " ";
    }
    return s.substr(0, s.size()-1); // remove the last space
}

main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%s\n", string_sequence(n).c_str());
}
