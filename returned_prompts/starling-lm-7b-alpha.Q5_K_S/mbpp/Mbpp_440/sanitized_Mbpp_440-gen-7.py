def find_adverb_position(sentence):
    adverb_list = ["quickly", "slowly", "clearly", "loudly"]
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            for j in range(i+1, i+2):
                if sentence[j] == ' ':
                    for k in range(j+1, j+2):
                        if sentence[k] == ' ':
                            for l in range(k+1, k+2):
                                if sentence[l] == ' ':
                                    for m in range(l+1, l+2):
                                        if sentence[m] == ' ':
                                            for n in range(m+1, m+2):
                                                if sentence[n] == ' ':
                                                    for o in range(n+1, n+2):
                                                        if sentence[o] == ' ':
                                                            for p in range(o+1, o+2):
                                                                if sentence[p] == ' ':
                                                                    if sentence[j+1:k] in adverb_list:
                                                                        return j, k, sentence[j+1:k]
    else:
        return -1