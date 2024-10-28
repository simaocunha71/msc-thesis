    int dot_index=file_name.find('.');
    if (dot_index==-1 || dot_index==0 || file_name.size()-dot_index>4)
        return "No";
    string before_dot=file_name.substr(0,dot_index);
    if (!isalpha(before_dot[0]))
        return "No";
    string after_dot=file_name.substr(dot_index+1);
    string valid_extensions[]={"txt","exe","dll"};
    bool found=false;
    for (int i=0;i<3;i++)
    {
        if (after_dot==valid_extensions[i])
        {
            found=true;
            break;
        }
    }
    if (!found)
        return "No";
    return "Yes";
}  //end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//end of Q
//end of A
//