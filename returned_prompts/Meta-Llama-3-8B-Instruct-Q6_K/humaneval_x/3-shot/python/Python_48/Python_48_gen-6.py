    text = text.lower().replace(' ', '')  # normalize the text
    return text == text[::-1]  # check if the text is equal to its reverse


