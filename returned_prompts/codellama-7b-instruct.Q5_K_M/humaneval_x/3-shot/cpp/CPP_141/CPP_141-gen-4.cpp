    int dot_cnt=0;
    int num_cnt=0;
    int i;
    bool valid_pre_dot=false;
    bool valid_post_dot=false;
    bool valid_name=true;
    for (i=0;i<file_name.length();i++)
    {
    if (file_name[i]>='0'&&file_name[i]<='9')
    num_cnt+=1;
    if (file_name[i]=='.')
    dot_cnt+=1;
    if (file_name[i]>='A'&&file_name[i]<='Z')
    valid_pre_dot=true;
    if (file_name[i]>='a'&&file_name[i]<='z')
    valid_pre_dot=true;
    if (file_name[i]=='txt'||file_name[i]=='exe'||file_name[i]=='dll')
    valid_post_dot=true;
    }
    if (num_cnt>3)
    valid_name=false;
    if (dot_cnt>1)
    valid_name=false;
    if (!valid_pre_dot)
    valid_name=false;
    if (!valid_post_dot)
    valid_name=false;
    if (valid_name)
    return "Yes";
    else
    return "No";
}


