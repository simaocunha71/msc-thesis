    int n = sentence.length();
    int i, j;
    char a[n];
    for(i = 0; i < n; i++) a[i] = sentence[i];
    int len = 0;
    for(i = 0; i < n; i++){
        if(a[i] == ' ') len++;
        else len++;
    }
    int *word = new int[len];
    int *len_ = new int[len];
    i = 0;
    j = 0;
    int cnt = 0;
    while(i < n){
        if(a[i] == ' '){