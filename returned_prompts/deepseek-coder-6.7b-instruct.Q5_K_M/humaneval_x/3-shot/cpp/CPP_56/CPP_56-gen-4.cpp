    int count=0;
    for (auto c : brackets) {
        if (c == '<')
            count++;
        if (c == '>')
            count--;
        if (count < 0)
            return false;
    }
    return count == 0;
}

