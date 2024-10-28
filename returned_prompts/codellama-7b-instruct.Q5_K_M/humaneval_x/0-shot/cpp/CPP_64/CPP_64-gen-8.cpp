    return count(s.begin(), s.end(), 'a') + count(s.begin(), s.end(), 'e') + count(s.begin(), s.end(), 'i') + count(s.begin(), s.end(), 'o') + count(s.begin(), s.end(), 'u') + count(s.begin(), s.end(), 'y');
}

int main()
{
    string word = "abcde";
    int ans = vowels_count(word);
    printf("ans: %d", ans);
    return 0;
}
