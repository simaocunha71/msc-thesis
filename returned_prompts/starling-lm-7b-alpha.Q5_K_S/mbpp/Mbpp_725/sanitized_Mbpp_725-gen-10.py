def extract_quotation(sentence):
    quote_list = []
    while " " in sentence:
        start = sentence.index(" ")
        end = sentence.rindex(" ")
        quote_list.append(sentence[start+1:end])
        sentence = sentence[end+1:]
    return quote_list