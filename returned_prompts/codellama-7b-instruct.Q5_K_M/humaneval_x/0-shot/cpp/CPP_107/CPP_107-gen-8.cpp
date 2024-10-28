    return vector<int> ();
}

int main() {
    int n = 12;
    vector<int> result = even_odd_palindrome(n);
    for(int i=0;i<result.size();i++){
        printf("%d\n",result[i]);
    }
    return 0;
}