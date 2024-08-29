def find_adverb_position(sentence):
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i].endswith(","):
            words[i] = words[i][:-1]
        if words[i].endswith("."):
            words[i] = words[i][:-1]
        if words[i].endswith("!"):
            words[i] = words[i][:-1]
        if words[i].endswith("?"):
            words[i] = words[i][:-1]

    adverbs = ["often", "always", "never", "just", "now", "here", "there", "never", "still", "just", "again", "often", "every", "new", "first", "last", "long", "great", "little", "own", "other", "old", "right", "big", "high", "different", "small", "large", "next", "early", "young", "important", "few", "public", "bad", "same", "married", "varying", "clear", "able", "careful", "quick", "free", "late", "afraid", "fresh", "hard", "light", "tired", "rude", "warm", "wet", "wise", "witty", "wise", "witty", "cheerful", "funny", "naive", "obnoxious", "outstanding", "plain", "powerful", "quick", "quick", "scared", "shy", "silly", "talented", "wise", "wise"]
    for i in range(len(words)):
        if words[i] in adverbs:
            return i, i+1, words[i]
    return None

print(find_adverb_position("clearly!! we can see the sky"))
print(find_adverb_position("quickly we can see the sky"))
print(find_adverb_position("quick we can see the sky"))
<jupyter_output>
(0, 1, 'clearly')
(1, 2, 'quickly