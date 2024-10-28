    int count = 0;
    size_t found = str.find(substring);
    while (found != std::string::npos){
        count++;
        found = str.find(substring, found+1);
    }
    return count;
}

int main(){
    printf("%d\n", how_many_times("", "a"));
    printf("%d\n", how_many_times("aaa", "a"));
    printf("%d\n", how_many_times("aaaa", "aa"));
    return 0;
}
*/

