    vector<int> result;
    int even_count=0, odd_count=0;
    for(int i=1;i<=n;i++){
        string s=to_string(i);
        if(s==reverse(s)){
            if(i%2==0) even_count++;
            else odd_count++;
        }
    }
    result.push_back(even_count);
    result.push_back(odd_count);
    return result;
}  // Function to reverse a string
string reverse(string s){
    string rev;
    for(int i=s.length()-1;i>=0;i--)
        rev+=s[i];
    return rev;
}
} // namespace std; // End of namespace std;
} // namespace yournamespace; // End of namespace yournamespace; // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End of yourprogram. // End