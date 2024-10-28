    result = ""
    i = 0
    while i < len(text):
        if text[i] == " ":
            if i + 1 < len(text) and text[i + 1] == " ":
                result += "-"
                while i < len(text) and text[i] == " ":
                    i += 1
            else:
                result += "_"
                i += 1
        else:
            result += text[i]
            i += 1
    return result

