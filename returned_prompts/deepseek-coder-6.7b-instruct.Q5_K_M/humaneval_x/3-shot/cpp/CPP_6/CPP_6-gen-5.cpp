    vector<int> levels;
    int current_level = 0;
    int max_level = 0;

    for(char c : paren_string) {
        if (c == '(') {
            current_level++;
            if (current_level > max_level)
                max_level = current_level;
        }
        if (c == ')')
            current_level--;
    }

    levels.push_back(max_level);
    return levels;
}

