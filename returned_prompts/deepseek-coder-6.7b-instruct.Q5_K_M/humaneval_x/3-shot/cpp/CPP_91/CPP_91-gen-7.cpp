    int count = 0;
    string::size_type start = 0, end = 0;

    while (end != string::npos)
    {
        end = S.find('.', start);

        string::size_type prev = S.rfind(" I", end);

        if (prev != string::npos && prev >= start)
            ++count;

        start = end != string::npos ? end+1 : string::npos;
    }

    return count;
}


