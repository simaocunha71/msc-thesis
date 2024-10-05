    int mango=0;
    int i,j;
    for (i=0;i<s.length();i++)
    {
        j=i;
        while (j<s.length() && s[j]!=' ')
        j++;
        string fruit=s.substr(i,j-i);
        if (fruit!="apples" && fruit!="oranges")
        {
            mango=n-atoi(s.substr(0,j).substr(strspn(s.substr(0,j).c_str(),"0123456789"),s.substr(0,j).length()));
            return mango;
        }
    }
    return 0;
}

int main() {
    cout << fruit_distribution("5 apples and 6 oranges", 19) << endl;
    cout << fruit_distribution("0 apples and 1 oranges", 3) << endl;
    cout << fruit_distribution("2 apples and 3 oranges", 100) << endl;
    cout << fruit_distribution("100 apples and 1 oranges", 120) << endl;
    return 0;
}
