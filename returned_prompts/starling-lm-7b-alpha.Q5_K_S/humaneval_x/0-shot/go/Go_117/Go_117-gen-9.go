    var res []string
    var word []byte
    var consonants = []byte{'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    for _, r := range strings.Split(s, " ") {
        for _, c := range r {
            if !contains(consonants, c) {
                word = append(word, c)
            }
        }
        if len(word) == n {
            res = append(res, string(word))
        }
        word = []byte{}
    }
    return res

selectWords("Mary had a little lamb", 4) ==> ["little"]
selectWords("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
selectWords("simple white space", 2) ==> []
selectWords("Hello world", 4) ==> ["world"]
selectWords("Uncle sam", 3) ==> ["Uncle"]

selectWords("Mary had a little lamb", 1) ==> []
selectWords("Mary had a little lamb", 2) ==> ["Mary", "little"]
selectWords("simple white space", 1) ==> []
selectWords("Hello world", 2) ==> ["Hello"]
selectWords("Uncle sam", 1) ==> ["Uncle"]

selectWords("Mary had a little lamb", 0) ==> []
selectWords("Mary had a little lamb", 2) ==> ["Mary", "little"]
selectWords("simple white space", 0) ==> []
selectWords("Hello world", 2) ==> []
selectWords("Uncle sam", 0) ==> []

selectWords("Mary had a little lamb", 5) ==> []
selectWords("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
selectWords("simple white space", 3) ==> []
selectWords("Hello world", 