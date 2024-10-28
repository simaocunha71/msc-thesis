    int count = 0;
    string::size_type start = 0, end = 0;
    while (end != string::npos){
        end = S.find('.', start);
        string temp = S.substr(start, end - start);
        if (temp[0] == 'I')
            count++;
        start = end != string::npos ? end + 1 : string::npos;
    }
    start = 0, end = 0;
    while (end != string::npos){
        end = S.find('?', start);
        string temp = S.substr(start, end - start);
        if (temp[0] == 'I')
            count++;
        start = end != string::npos ? end + 1 : string::npos;
    }
    start = 0, end = 0;
    while (end != string::npos){
        end = S.find('A', start);
        string temp = S.substr(start, end - start);
        if (temp[0] == 'I')
            count++;
        start = end != string::npos ? end + 1 : string::npos;
    }
    return count;
}

