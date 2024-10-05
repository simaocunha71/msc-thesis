    int i,digit_count=0;
    for (i=0;i<file_name.length();i++)
    if (file_name[i]>='0'&&file_name[i]<='9')
        digit_count+=1;
    if (digit_count>3)
        return "No";
    for (i=0;i<file_name.length();i++)
    if (file_name[i]=='.')
        break;
    if (i==file_name.length())
        return "No";
    if (i==0||file_name[i-1]<'a'||file_name[i-1]>'z'||file_name[i-1]<'A'||file_name[i-1]>'Z')
        return "No";
    if (file_name.length()-i<=4||file_name[i+1]!='.'||file_name[i+2]!='t'||file_name[i+3]!='x'||file_name[i+4]!=' ')
        return "No";
    if (i+5<file_name.length()&&(file_name[i+5]!='e'||file_name[i+6]!='x'||file_name[i+7]!='e'))
        return "No";
    if (i+5>=file_name.length())
        return "No";
    if (file_name[i+5]!='.'||file_name[i+6]!='d'||file_name[i+7]!='l'||file_name[i+8]!='l')
        return "No";
    return "Yes";
}


