    for i := len(word) - 1; i > 0; i-- {
        if !isVowel(word[i]) && isVowel(word[i-1]) && isVowel(word[i+1]) {
            for j := i - 1; j > 0; j-- {
                if !isVowel(word[j]) && isVowel(word[j-1]) && isVowel(word[j+1]) {
                    if word[i] > word[j] {
                        return string(word[i])
                    } else {
                        return string(word[j])
                    }
                }
            }
        }
    }
    return ""
}

func isVowel(b byte) bool {
    return bytes.Contains([]byte("aeiouAEIOU"), []byte{b})
}
```

## コメント

このコードは、与えられた単語の右端から最も近い位置にある、2つの子音の間にある母音を見つけようとしています。

関数`GetClosestVowel`は、与えられた単語の右端から順に文字をチェックし、母音であり、左右の文字として子音があるかどうかを確認します。

この条件に当てはまる最初の母音を見つけた場合、その母音が与えられた単語の中で最も右にあるかどうかをチェックします。