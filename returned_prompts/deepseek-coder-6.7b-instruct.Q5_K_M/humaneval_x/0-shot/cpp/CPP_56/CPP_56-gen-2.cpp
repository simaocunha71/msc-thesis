    int count = 0;
    for(char c : brackets){
        if(c == '<'){
            count++;
        }
        else if(c == '>'){
            if(count == 0){
                return false;
            }
            count--;
        }
        else{
            return false;
        }
    }
    return count == 0;
}

int main() {
    printf("%d\n", correct_bracketing("<"));
    printf("%d\n", correct_bracketing("<>"));
    printf("%d\n", correct_bracketing("<<><>>"));
    printf("%d\n", correct_bracketing("><<>"));
    return 0;
}
```

## 解析
この問題の目標は、与えられた文字列が正しく括られているかどうかを判定することです。

解答は、カウンタ変数 count を用いて実装されています。この変数は、開き括弧 '<' をカウントします。

文字列の各文字について、
- 開き括弧 '<' の場合、count をインクリメントします。
- 閉じ括弧 '>' の場合、count が 0 の場合、つまり開き括弧がない場合、false を返します。それ以外の場合は、count をデクリメントします。
- それ以外の文字の場合