    transform(text.begin(),text.end(),text.begin(),[](char x)->char{
        if (x=='a'||x=='e'||x=='i'||x=='o'||x=='u'||x=='A'||x=='E'||x=='I'||x=='O'||x=='U')
        return ' ';
        return x;
    });
    text.erase(remove(text.begin(),text.end(),' '),text.end());
    return text;
}


