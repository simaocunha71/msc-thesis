    int mangoes=n;
    int i;
    int pos=s.find("apples");
    int num_apples=0;
    int num_oranges=0;
    if (pos!=-1)
    {
        for (i=pos+8;i<s.length();i++)
        {
            if (s[i]>='0'&&s[i]<='9')
                num_apples=num_apples*10+(s[i]-'0');
        }
    }
    pos=s.find("oranges");
    if (pos!=-1)
    {
        for (i=pos+7;i<s.length();i++)
        {
            if (s[i]>='0'&&s[i]<='9')
                num_oranges=num_oranges*10+(s[i]-'0');
        }
    }
    mangoes=n-num_apples-num_oranges;
    return mangoes;
}  // end of function
// test the function
int main()
{
    printf("%d\n",fruit_distribution("5 apples and 6 oranges",19)); // prints 8
    printf("%d\n",fruit_distribution("0 apples and 1 oranges",3)); // prints 2
    printf("%d\n",fruit_distribution("2 apples and 3 oranges",100)); // prints 95
    printf("%d\n",fruit_distribution("100 apples and 1 oranges",120)); // prints 19
    return 0;
}
// end of main function
// end of program
*/  // end of comment
