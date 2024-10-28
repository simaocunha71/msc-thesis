    if (file_name.length()>3) return "No";
    if (file_name.find(".")==string::npos) return "No";
    if (file_name.find(".")==0) return "No";
    if (file_name[file_name.find(".")-1]<'a' || file_name[file_name.find(".")-1]>'z') return "No";
    if (file_name.find(".")==file_name.length()-1) return "No";
    if (file_name[file_name.find(".")+1]<'a' || file_name[file_name.find(".")+1]>'z') return "No";
    if (file_name[file_name.find(".")+1]<'A' || file_name[file_name.find(".")+1]>'Z') return "No";
    if (file_name[file_name.find(".")+2]<'0' || file_name[file_name.find(".")+2]>'9') return "No";
    return "Yes";
}

