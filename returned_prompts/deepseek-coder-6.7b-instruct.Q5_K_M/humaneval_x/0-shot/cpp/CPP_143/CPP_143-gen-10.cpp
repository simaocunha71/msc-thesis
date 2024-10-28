    string result = "", word = "";
    int len = sentence.length();
    for (int i = 0; i < len; i++){
        if (sentence[i] == ' '){
            if (is_prime(word.length())){
                result += word + " ";
            }
            word = "";
        } else {
            word += sentence[i];
        }
    }
    if (is_prime(word.length())){
        result += word;
    }
    return result;
}

bool is_prime(int num){
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}
```

## 解析
给定一个字符串表示的句子，你需要返回一个字符串，其中包含原始句子中长度为质数的单词，顺序与原始句子相同。

我们将使用两个函数，一个是主函数`words_in_sentence`，另一个是辅助函数`is_prime`。`is_prime`函数用于检查一个数字是否为质数。

在`words_in_sentence`函数中，我们将遍历句子中的每个字符。每当我们遇到一个空格时，我们将当前正在形成的单词与空格连接起来，并检查它的长度是否为质数。如果是，我们将其添加到结果字符串中。

最后，我们返回结果字符串。

## 复杂度分析
这个解决方案的时间复杂度为O(n*sqrt(m))，其中n是句子中的单词数，m是每个单词的平均长度。这是因为对于每个单词，我们都要检查其长度是否为质数，这需要O(sqrt(m))的时间。

空间复杂度为O(n)，因为我们需要存储结果字符串。

## 测试
使用以下测试用例来测试这个解决方案：

```python
assert words_in_sent