    for i := 2; i < len(sentence); i++ {
        if len(sentence) % i == 0 {
            return WordsInSentence(sentence[:len(sentence)-1])
        }
    }
    if len(sentence) == 1 {
        return ""
    }
    if len(sentence) == 2 {
        return sentence
    }
    return sentence[strings.Index(sentence, " ")+1:]
}

func main() {
    fmt.Println(WordsInSentence("This is a test")) // should return "is"
    fmt.Println(WordsInSentence("lets go for swimming")) // should return "go for"
}
```

## 解析

我们被要求从给定的句子中提取长度为质数的单词。

我们需要首先创建一个函数来检查一个数字是否为质数。

在 `WordsInSentence` 函数中，我们通过从右到左检查每个字符来确定句子是否可以被2到句子长度减1之间的任何数字整除。如果可以整除，我们将递归调用 `WordsInSentence` 函数，但这次我们将删除句子末尾的字符。如果不能整除，我们检查句子长度是否为1或2。如果是1，我们返回空字符串，如果是2，我们返回句子本身。

如果句子的长度既不为1也不为2，我们使用 `strings.Index` 函数找到空格的索引，并返回从空格索引到句子末尾的子字符串。

在 `main` 函数中，我们使用给定的句子调用 `WordsInSentence` 函数，并打印结果。

该解决方案的时间复杂度为 O(n)，其中 n 是句子的长度，因为我们需要遍历句子中的每个字符。空间复杂度为 O(n)，因为我们使用递归调用堆栈来解决问题。

## 运行代码

要运行代码，你需要在本地设置 Go 环境。一旦设置好了