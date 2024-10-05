
    for i := 0; i < len(l); i++ {
        for j := i+1; j < len(l); j++ {
            if l[i] + l[j] == 0 {
                return true
            }
        }
    }
    return false
}



```

## 3. 

```python
def PairsSumToZero(l):
    n = len(l)
    for i in range(n):
        for j in range(i+1, n):
            if l[i] + l[j] == 0:
                return True
    return False
```

## 4. 

```javascript
function PairsSumToZero(l) {
    for (let i = 0; i < l.length; i++) {
        for (let j = i+1; j < l.length; j++) {
            if (l[i] + l[j] === 0) {
                return true;
            }
        }
    }
    return false;
}
```

## 5. 

```ruby
def pairs_sum_to_zero(l)
    for i in 0...l.length
        for j in (i+1)...l.length
            if l[i] + l[j] == 0
                return true
            end
        end
    end
    return false
end
```

## 6. 

```php
function pairsSumToZero($l) {
    for ($i = 0; $i < count($l); $i++) {
        for ($j = $i+1; $j < count($l); $j++) {
            if ($l[$i] + $l[$j] == 0) {
                return true;
            }
        }
    }
    return false;
}
```

## 7. 

```swift
func pairsSumToZero(l: [Int]) -> Bool {
    for i in 0..<l.count {
        for j in (i+1)..<l.count {
            if l[i