    for _, v := range sentence {
        if v == ' ' {
            continue
        }
        if v < 'a' || v > 'z' {
            break A
        }
    }

    words := strings.Split(sentence, " ")
    result := []string{}

    for _, word := range words {
        if word == "" {
            continue
        }
        if IsPrime(len(word)) {
            result = append(result, word)
        }
    }

    return strings.Join(result, " ")
}

func IsPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

```

# 题目解析

这道题目要求我们对字符串进行操作。

给定一个字符串`sentence`，其中包含一些由空格分隔的单词。我们需要返回一个字符串，该字符串包含原始句子中长度为质数的单词。单词的顺序应与原始句子相同。

我们需要编写一个辅助函数`IsPrime`来判断一个数是否为质数。

然后，我们将句子分割为单词，并对每个单词检查其长度是否为质数。如果是，我们将该单词添加到结果中。最后，我们将结果作为字符串返回。

# 代码解析

这段代码首先检查输入的`sentence`是否只包含小写字母。如果包含其他字符，它会立即返回一个空字符串。

然后，它使用`strings.Split`函数将句子分割为单词。然后，它遍历每个单词，并使用`IsPrime`函数检查其长度是否为质数。如果是，它将该单词添加到结果切片中。

最后，它使用`strings.Join`函数将结果切片中的单词连接成一个字符