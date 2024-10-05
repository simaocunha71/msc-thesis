    int count = 0, a = 0;
    size_t found = str.find(substring, a);
    while (found != string::npos){
        a = found+1;
        found = str.find(substring, a);
        count++;
    }
    return count;
}

int main(){
    printf("%d\n",how_many_times("","a"));
    printf("%d\n",how_many_times("aaa","a"));
    printf("%d\n",how_many_times("aaaa","aa"));
    return 0;
}

