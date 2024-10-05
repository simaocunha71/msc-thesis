    string result="";
    for(int i=0;i<a.size();i++)
    {
        if(a[i]==b[i])
            result+='0';
        else
            result+='1';
    }
    return result;
}

int main()
{
    string a,b;
    scanf("%s %s",&a,&b);
    printf("%s",string_xor(a,b).c_str());
    return 0;
}

*/

