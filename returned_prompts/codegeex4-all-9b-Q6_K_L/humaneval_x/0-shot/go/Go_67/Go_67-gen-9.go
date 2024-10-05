```go
func FruitDistribution(s string,n int) int {
  fruitMap := make(map[string]int)
  fruits := strings.Fields(s)
  for _, fruit := range fruits {
    if _, ok := fruitMap[fruit]; !ok {
      fruitMap[fruit] = 0
    }
    if _, err := strconv.Atoi(fruit); err == nil {
      fruitMap[fruit] += 1
    }
  }
  return n - fruitMap["apples"] - fruitMap["oranges"]
}
```
B:
```go
func FruitDistribution(s string,n int) int {
  fruitMap := make(map[string]int)
  fruits := strings.Fields(s)
  for _, fruit := range fruits {
    if _, ok := fruitMap[fruit]; !ok {
      fruitMap[fruit] = 0
    }
    if _, err := strconv.Atoi(fruit); err == nil {
      fruitMap[fruit] += 1
    }
  }
  return n - fruitMap["apples"] - fruitMap["oranges"] - fruitMap["mango"]
}
```
C:
```go
func FruitDistribution(s string,n int) int {
  fruitMap := make(map[string]int)
  fruits := strings.Split(s, " ")
  for _, fruit := range fruits {
    if _, ok := fruitMap[fruit]; !ok {
      fruitMap[fruit] = 0
    }
    if _, err := strconv.Atoi(fruit); err == nil {
      fruitMap[fruit] += 1
    }
  }
  return n - fruitMap["apples"] - fruitMap["oranges"]
}
```
D:
```go
func FruitDistribution(s string,n int) int {
  fruitMap := make(map[string]int)
  fruits := strings.Fields(s)
  for _, fruit := range fruits {
    if _, ok := fruitMap[fruit]; !ok {
      fruitMap[fruit] = 0
    }
    if _, err := strconv.Atoi(fruit); err == nil {
      fruitMap[fruit] += 1
    }
  }
  return n - fruitMap["apples"] - fruitMap["oranges"] - fruitMap["mango"] - fruitMap["pears"]
}
```
E:
```go
func FruitDistribution(s string,n int) int {
  fruitMap := make(map[string]int)
  fruits := strings.Fields(s)
  for _, fruit := range fruits {
    if _, ok