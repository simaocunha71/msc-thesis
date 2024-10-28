    string result = "";
    for (int i=0;i<=n;i++)
    {
        result += to_string(i) + " ";
    }
    return result.substr(0, result.length()-1);
}
// or
string string_sequence(int n){
    string result = "";
    for (int i=0;i<=n;i++)
    {
        result += to_string(i) + " ";
    }
    return result;
} // No need to substring
// or 
string string_sequence(int n){
    string result = "";
    for (int i=0;i<=n;i++)
    {
        result += to_string(i);
        if(i<n)result+=" ";
    }
    return result;
}
// This one is more efficient and accurate. It avoids the substring operation. It also directly appends the space if it's not the last number.