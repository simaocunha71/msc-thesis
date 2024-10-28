    string sequence;
    for(int i=0;i<=n;i++)
    {
        sequence+=to_string(i);
        if(i<n)
        sequence+=" ";
    }
    return sequence;
} // C++ solution
string string_sequence(int n){
    StringBuilder sb = new StringBuilder();
    for(int i=0;i<=n;i++)
    {
        sb.append(i);
        if(i<n)
        sb.append(" ");
    }
    return sb.toString();
} // Java solution
string string_sequence(int n){
    String sequence = "";
    for(int i=0;i<=n;i++)
    {
        sequence += i;
        if(i<n)
        sequence += " ";
    }
    return sequence;
} // Python solution
string string_sequence(int n){
    ostringstream oss;
    for(int i=0;i<=n;i++)
    {
        oss<<i;
        if(i<n)
        oss<<" ";
    }
    return oss.str();
} // C++/java/python solution
int main(){
    cout<<string_sequence(5)<<endl; // prints "0 1 2 3 4 5"
    return 0;
}
