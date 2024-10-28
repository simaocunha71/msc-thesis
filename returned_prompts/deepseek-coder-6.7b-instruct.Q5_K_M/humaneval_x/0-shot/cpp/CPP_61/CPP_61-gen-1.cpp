    int count = 0;
    for(char& c : brackets){
        if (c == '(') {
            count++;
        } else if (c == ')') {
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    return (count == 0);
}

int main() {
    printf("%d\n", correct_bracketing("("));
    printf("%d\n", correct_bracketing("()"));
    printf("%d\n", correct_bracketing("(()())"));
    printf("%d\n", correct_bracketing(")(()"));
    return 0;
}
```

### 解説

この問題では、与えられた括弧文字列が正しく括られているかどうかを判定する。正しく括られているとは、すべての開き括弧に対応する閉じ括弧があることを言う。

解答では、与えられた文字列を順に読み、開き括弧が出てきたらカウンターを1増やし、閉じ括弧が出てきたらカウンターを1減らしていく。もし、閉じ括弧が出てきたがカウンターが0だったら、開き括弧がないため、正しく括られていないと判断してfalseを