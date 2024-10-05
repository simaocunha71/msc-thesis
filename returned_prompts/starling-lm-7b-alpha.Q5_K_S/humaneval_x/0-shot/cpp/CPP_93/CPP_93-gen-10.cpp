    string s = "";
    for(int i = 0; i < message.length(); i++)
    {
        char c = message[i];
        if(c >= 'a' && c <= 'z')
        {
            s += toupper(c);
        }
        else if(c >= 'A' && c <= 'Z')
        {
            s += tolower(c);
        }
        else
        {
            continue;
        }
    }
    int n = s.length();
    for(int i = 0; i < n; i++)
    {
        if(s[i] == 'a')
        {
            s[i] = 'c';
        }
        else if(s[i] == 'e')
        {
            s[i] = 'g';
        }
        else if(s[i] == 'i')
        {
            s[i] = 'k';
        }
        else if(s[i] == 'o')
        {
            s[i] = 'u';
        }
        else if(s[i] == 'u')
        {
            s[i] = 'w';
        }
    }
    return s;
}

int main()
{
    string message = "This is a message";
    printf("%s\n", encode(message).c_str());
    return 0;
}














































































































































































