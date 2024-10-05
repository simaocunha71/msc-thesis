    string max_string="";
    for (int i=0;i<words.size();i++)
    {
        string current_string=words[i];
        sort(current_string.begin(),current_string.end());
        if (current_string!=max_string){
            max_string=current_string;
        }
    }
    return max_string;
}

