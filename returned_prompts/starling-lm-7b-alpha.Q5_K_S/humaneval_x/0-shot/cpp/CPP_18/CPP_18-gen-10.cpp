    int l = 0;
    int n = 0;
    int len = substring.length();
    for(int i = 0; i < str.length(); i++) {
        if(str[i] == substring[l]) {
            l++;
            if(l == len) {
                n++;
                l = 0;
            }
        } else {
            if(l != 0)
                l = substring[0];
        }
    }
    return n;
}

int main() {
    printf("%d\n", how_many_times("aaa", "a"));
    printf("%d\n", how_many_times("aaaa", "aa"));
    printf("%d\n", how_many_times("aaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaaaxaxaaaxaaaxaaaxaxaaaxaxaaaxaxaaaxaaayaxaaayaxayaaaxayyaayayayayayayayayayayayaaayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayay