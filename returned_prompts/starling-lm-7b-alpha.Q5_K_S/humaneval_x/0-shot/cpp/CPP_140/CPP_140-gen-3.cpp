    int len = text.length();
    for(int i=0;i<len;i++)
    {
        if(text[i]==' ')
        {
            if(i+1<len && text[i+1]==' ')
            {
                if(i+2<len && text[i+2]==' ')
                {
                    text[i]='-';
                    text[i+1]='-';
                    text[i+2]='-';
                    i+=2;
                }
                else
                {
                    text[i]='-';
                    text[i+1]='-';
                }
            }
            else
                text[i]='_';
        }
    }
    return text;
}

int main()
{
    printf("%s\n",fix_spaces("Example"));
    printf("%s\n",fix_spaces("Example 1"));
    printf("%s\n",fix_spaces(" Example 2"));
    printf("%s\n",fix_spaces(" Example   3"));
    return 0;
}


*/








































































































































































































































