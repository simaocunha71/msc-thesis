    string result;
    string words[100];
    int i,j;
    int count=0;
    int temp;
    for (i=0;i<sentence.length();i++)
    {
        if (sentence[i]==' ')
        {
            temp=i;
        }
    }
    for (i=0;i<sentence.length();i++)
    {
        if (i==temp)
        {
            words[count]=string(sentence.begin()+i+1,sentence.begin()+temp);
            count++;
        }
    }
    for (i=0;i<count;i++)
    {
        for (j=2;j<=sqrt(words[i].length());j++)
        {
            if (words[i].length()%j==0)
                break;
        }
        if (j>sqrt(words[i].length()))
            result+=words[i]+" ";
    }
    return result;
} // end of function
int main()
{
    string s="lets go for swimming";
    cout<<words_in_sentence(s)<<endl;
    return 0;
}
