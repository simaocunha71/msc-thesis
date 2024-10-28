    result = ""
    for i in range(len(text)):
        if text[i] == " ":
            result += "_"
        elif text[i] == " " and text[i-1] == " ":
            result += "-"
        else:
            result += text[i]

    return result

