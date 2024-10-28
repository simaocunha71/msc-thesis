    transform(text.begin(), text.end(), text.begin(), [](unsigned char c){
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            return ' ';
        }
        return c;
    });

    text.erase(remove(text.begin(), text.end(), ' '), text.end());
    return text;
}

