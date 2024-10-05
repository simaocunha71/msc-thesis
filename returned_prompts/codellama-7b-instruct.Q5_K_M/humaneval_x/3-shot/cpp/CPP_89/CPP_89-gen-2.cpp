    string encrypted;
    int i;
    for (i=0;i<s.length();i++)
    {
        switch (s[i])
        {
            case 'a':
            encrypted+='c';
            break;
            case 'b':
            encrypted+='d';
            break;
            case 'c':
            encrypted+='e';
            break;
            case 'd':
            encrypted+='f';
            break;
            case 'e':
            encrypted+='g';
            break;
            case 'f':
            encrypted+='h';
            break;
            case 'g':
            encrypted+='i';
            break;
            case 'h':
            encrypted+='j';
            break;
            case 'i':
            encrypted+='k';
            break;
            case 'j':
            encrypted+='l';
            break;
            case 'k':
            encrypted+='m';
            break;
            case 'l':
            encrypted+='n';
            break;
            case 'm':
            encrypted+='o';
            break;
            case 'n':
            encrypted+='p';
            break;
            case 'o':
            encrypted+='q';
            break;
            case 'p':
            encrypted+='r';
            break;
            case 'q':
            encrypted+='s';
            break;
            case 'r':
            encrypted+='t';
            break;
            case 's':
            encrypted+='u';
            break;
            case 't':
            encrypted+='v';
            break;
            case 'u':
            encrypted+='w';
            break;
            case 'v':
            encrypted+='x';
            break;
            case 'w':
            encrypted+='y';
            break;
            case 'x':
            encrypted+='z';
            break;
            case 'y':
            encrypted+='a';
            break;
            case 'z':
            encrypted+='b';
            break;
        }
    }
    return encrypted;
}


