    text.erase(remove(text.begin(), text.end(), 'a'), text.end());
    text.erase(remove(text.begin(), text.end(), 'e'), text.end());
    text.erase(remove(text.begin(), text.end(), 'i'), text.end());
    text.erase(remove(text.begin(), text.end(), 'o'), text.end());
    text.erase(remove(text.begin(), text.end(), 'u'), text.end());
    return text;
}


