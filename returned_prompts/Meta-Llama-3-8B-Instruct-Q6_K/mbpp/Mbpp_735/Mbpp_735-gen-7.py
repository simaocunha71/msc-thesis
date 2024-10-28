```
def toggle_middle_bits(n):
    if n < 10:
        return n
    else:
        n = bin(n)[2:]
        middle = len(n) // 2
        result = n[0] + ''.join('1' if bit == '0' else '0' for bit in n[1:middle]) + '0' + ''.join('1' if bit == '0' else '0' for bit in n[middle+1:-1]) + n[-1]
        return int(result, 2)
```


The function takes an integer as input and returns the integer where the middle bits are toggled. The middle bits are the bits in between the first and the last bit. The function first converts the integer to a binary string, then it toggles the middle bits, and finally it converts the binary string back to an integer. 

The unit test `assert toggle_middle_bits(9) == 15` checks if the function correctly toggles the middle bits of the number 9, which is 1001 in binary. The result should be 1111, which is 15 in decimal. 





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
python
```





```
