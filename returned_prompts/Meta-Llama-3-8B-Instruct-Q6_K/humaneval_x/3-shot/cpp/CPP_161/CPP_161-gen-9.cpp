    string result;
    for (char c : s)
    {
        if (isalpha(c)) {
            result += (islower(c) ? toupper(c) : tolower(c));
        } else {
            result += c;
        }
    }
    reverse(result.begin(), result.end());
    return result;
}