    dot_index  := strings.Index(file_name, ".")
    if dot_index  != -1  &&  strings.Count(file_name, ".")  == 1  {
        first_part  := file_name[:dot_index]
        second_part  := file_name[dot_index+1:]
        if (first_part[0] >= 'a'  &&  first_part[0] <= 'z')  || (first_part[0] >= 'A'  &&  first_part[0] <= 'Z')  &&  strings.Count(first_part, "") <= 3  {
            if second_part == "txt"  || second_part == "exe"  || second_part == "dll"  {
                return "Yes"
            }
        }
    
    }
    return "No"
}



