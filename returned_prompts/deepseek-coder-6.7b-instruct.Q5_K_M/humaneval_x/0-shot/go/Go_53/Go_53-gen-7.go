
// Return the result of addition of x and y
return x + y

}


```

# 3. 条件语句

条件语句用于基于一些条件来执行不同的代码块。Go语言提供了以下几种条件语句：

- if 语句
- if else 语句
- switch 语句
- select 语句

## 3.1 if 语句

if 语句用于基于条件来执行代码块。

```go
if 条件 {
  // 代码块
}
```

示例：

```go
if x > y {
  fmt.Println("x is greater than y")
}
```

## 3.2 if else 语句

if else 语句用于在条件为真时执行一个代码块，在条件为假时执行另一个代码块。

```go
if 条件 {
  // 代码块1
} else {
  // 代码块2
}
```

示例：

```go
if x > y {
  fmt.Println("x is greater than y")
} else {
  fmt.Println("y is greater than x")
}
```

## 3.3 switch 语句

switch 语句用于基于不同条件来执行不同的代码块。

```go
switch 变量 {
case 值1:
  // 代码块1
case 值2:
  // 代码块2
default:
  // 默认代码块
}
```

示例：

```go
switch x {
case 1:
  fmt.Println("x is 1")
case 2:
  fmt.Println("x is 2")
default:
  fmt.Println("x is not 1 or 2")
}
```

# 4. 循环语句

循环语句用于重复执行一段代码，直到满足某个条件为止。Go语言提供了以下几种循环语句：

- for 循环
- while 循环
- do while 循环

## 4.1 for 循环