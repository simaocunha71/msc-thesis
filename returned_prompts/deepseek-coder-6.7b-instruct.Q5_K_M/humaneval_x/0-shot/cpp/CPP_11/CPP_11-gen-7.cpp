    string res = "";
    for (int i=0; i<a.length(); i++)
    {
        if(a[i]==b[i])
            res+='0';
        else
            res+='1';
    }
    return res;
}

int main(){
    string a = "010";
    string b = "110";
    printf("%s",string_xor(a,b).c_str());
    return 0;
}
```

## 运行代码

通过编译和运行代码，可以得到输入字符串"010"和"110"的XOR结果为"100"。

## 代码说明

给定的代码接受两个二进制字符串作为输入，并对它们执行XOR操作。XOR操作是逐位进行的，如果两个位相同，则结果为0，如果位不同，则结果为1。

代码从左到右遍历每个字符串的位，然后检查两个位是否相同。如果相同，则追加'0'到结果字符串中，否则追加'1'。

最后，函数返回结果字符串。

请注意，该代码假设输入字符串的长度相等。如果长度不同，您需要在使用此代码之前添加一些错误检查。

## 时间复杂度

时间复杂度为O(n)，其中n是输入字符串的长度。这是因为我们需要遍历两个字符串的每个字符一次。

## 空间复杂度

空间复杂度为O(n)，因为我们需要存储结果字符串，其长度与输入字符串相等。

## 注意

请确保输入字符串的长度相等。如果长度不同，您需要在使用此代码之前添加一些错误检查。

## 参考资料

1. [Bitwise Operations](https://en.wikipedia.org/wiki/Bitwise_operation)
2. [Binary XOR](https://en.wikipedia.org/wiki/Exclusive_or)

</div>
</