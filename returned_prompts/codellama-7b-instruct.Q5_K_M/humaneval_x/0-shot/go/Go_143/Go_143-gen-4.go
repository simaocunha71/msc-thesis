for i, w := range strings.Split(sentence, " ") {
    if !isPrime(len(w)) {
        continue A
    }
    return w
}
return ""
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

func TestWordsInSentence() {
    {
        s := "This is a test"
        expected := "is"
        actual := WordsInSentence(s)
        if actual != expected {
            t.Errorf("Test %v Failed, Expected %v but got %v", s, expected, actual)
        }
    }
    {
        s := "lets go for swimming"
        expected := "go for"
        actual := WordsInSentence(s)
        if actual != expected {
            t.Errorf("Test %v Failed, Expected %v but got %v", s, expected, actual)
        }
    }
}



