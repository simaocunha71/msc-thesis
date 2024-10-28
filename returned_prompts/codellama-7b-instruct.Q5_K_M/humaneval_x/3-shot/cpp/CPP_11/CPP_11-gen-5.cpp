    string result="";
    int carry=0;
    int i;
    for (i=0;i<a.length();i++)
    {
        int sum=carry;
        sum+=int(a[i])^int(b[i]);
        carry=sum/2;
        result+=to_string(sum%2);
    }
    if (carry)
    result+=to_string(carry);
    reverse(result.begin(),result.end());
    return result;
}



