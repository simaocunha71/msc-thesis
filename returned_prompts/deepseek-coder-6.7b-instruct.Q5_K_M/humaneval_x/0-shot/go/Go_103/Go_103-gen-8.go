    if n > m {
        return -1
    }

B:
    avg := math.Round(float64(n+m) / 2)
    bin := fmt.Sprintf("%b", int(avg))

C:
    return bin
}

func main() {
    fmt.Println(RoundedAvg(1, 5))
    fmt.Println(RoundedAvg(7, 5))
    fmt.Println(RoundedAvg(10, 20))
    fmt.Println(RoundedAvg(20, 33))
}
```

## 解析

まず、与えられたnがmより大きい場合に-1を返します。次に、平均値を計算して四捨五入します。最後に、平均値を二進数形式に変換して返します。

## テスト

```
func TestRoundedAvg(t *testing.T) {
    type args struct {
        n int
        m int
    }
    tests := []struct {
        name string
        args args
        want interface{}
    }{
        {"1", args{1, 5}, "0b11"},
        {"2", args{7, 5}, -1},
        {"3", args{10, 20}, "0b1111"},
        {"4", args{20, 33}, "0b11010"},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            if got := RoundedAvg(tt.args.n, tt.args.m); !reflect.DeepEqual(got, tt.want) {
                t.Errorf("RoundedAvg() = %v, want %v", got, tt.want)
            }