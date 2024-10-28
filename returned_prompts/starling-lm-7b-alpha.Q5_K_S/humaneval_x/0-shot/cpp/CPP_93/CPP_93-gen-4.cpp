    string result="";
    for(int i=0;i<message.length();i++)
    {
        if(message[i]>='a'&&message[i]<='z')
        {
            result.push_back(message[i]-'a'+'A');
        }else if(message[i]>='A'&&message[i]<='Z')
        {
            result.push_back(message[i]-'A'+'a');
        }else if(message[i]=='a')
        {
            result.push_back('c');
        }else if(message[i]=='e')
        {
            result.push_back('g');
        }else if(message[i]=='i')
        {
            result.push_back('k');
        }else if(message[i]=='o')
        {
            result.push_back('s');
        }else if(message[i]=='u')
        {
            result.push_back('w');
        }else if(message[i]=='A')
        {
            result.push_back('C');
        }else if(message[i]=='E')
        {
            result.push_back('G');
        }else if(message[i]=='I')
        {
            result.push_back('K');
        }else if(message[i]=='O')
        {
            result.push_back('S');
        }else if(message[i]=='U')
        {
            result.push_back('W');
        }
    }
    return result;
}

int main()
{
    string str="This is a message";
    printf("%s\n",encode(str).c_str());
    return 0;
}

*/









































































