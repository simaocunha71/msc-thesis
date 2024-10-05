	// 1. split sentence into words
	words := strings.Split(sentence, " ")

	// 2. filter words by length
	// 3. join filtered words into a new sentence
	return strings.Join(words, " ")

}

