    int n = brackets.length();
    int count = 0;
    for(int i = 0; i < n; i++){
        if(brackets[i] == '<'){
            count++;
        }
        else{
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}

int main(){
    printf("%d\n", correct_bracketing("<"));
    printf("%d\n", correct_bracketing("<>"));
    printf("%d\n", correct_bracketing("<<><>>"));
    printf("%d\n", correct_bracketing("><<>"));
    return 0;
}
```

## プログラム解説

このプログラムは、与えられた文字列の全ての括弧が正しく閉じられているかどうかを判定するプログラムです。

このプログラムでは、スタックを使っています。このスタックの中に、'<'という文字があるかどうかを確認していきます。

'<'という文字がある場合は、'>'という文字が続くことを期待しています。

'>'という文字が出てきた場合は、'<'という文字がある必要があります。

最後に、スタッ