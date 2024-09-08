    int num_apples = 0, num_oranges = 0;
    int i = 0;
    while(i < s.size()) {
        if(s[i] == 'a') {
            while(i < s.size() && s[i] != ' ') {
                i++;
            }
            i++; // skip the 'and'
            while(i < s.size() && s[i] != ' ') {
                if(s[i] == 'p') {
                    num_apples++;
                    while(i < s.size() && s[i] != ' ') {
                        i++;
                    }
                    i++; // skip the 's'
                }
                i++;
            }
        } else if(s[i] == 'o') {
            while(i < s.size() && s[i] != ' ') {
                i++;
            }
            i++; // skip the 'and'
            while(i < s.size() && s[i] != ' ') {
                if(s[i] == 'r') {
                    num_oranges++;
                    while(i < s.size() && s[i] != ' ') {
                        i++;
                    }
                    i++; // skip the 's'
                }
                i++;
            }
        }
    }
    return n - num_apples - num_oranges;
}

int main(){
    printf("%d\n",fruit_distribution("5 apples and 6 oranges",19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n",fruit_distribution("2 apples and 3 oranges",100));
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}

B:
    int fruit_distribution(string s, int n) {
        size_t found;
        int num_apples = 0, num_oranges = 0;
        found = s.find("apples");
        while(found != string::npos) {
            num_apples++;
            found = s.find("apples", found + 1);
        }
        found = s.find("oranges");
        while(found != string::npos) {
            num_oranges++;
            found = s.find("oranges", found + 1);
        }
        return n - num_apples - num_oranges;
    }
int main() {
    printf("%d\n",fruit_distribution("5 apples and 6 oranges",19));
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3));
    printf("%d\n