     sort.Strings(words)

B:
     max := 0
     maxWord := ""

C:
     for _, word := range words {
     D:
         unique := make(map[rune]struct{})

     E:
         for _, char := range word {
             unique[char] = struct{}{}
         }

     F:
         if len(unique) > max {
             max = len(unique)
             maxWord = word
         }
     }

     return maxWord
}
`

	expect := `import (
	"sort"
)

func FindMax(words []string) string {
	sort.Strings(words)

	max := 0
	maxWord := ""

	for _, word := range words {
		unique := make(map[rune]struct{})

		for _, char := range word {
			unique[char] = struct{}{}
		}

		if len(unique) > max {
			max = len(unique)
			maxWord = word
		}
	}

	return maxWord
}`

	actual := CommentedCode(input)

	if expect != actual {
		t.Errorf("\nExpected: %s\nActual: %s", expect, actual)
	}
}

func TestCommentedCode_TwoLoops(t *testing.T) {
	input := `
