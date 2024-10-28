
```c
unsigned int left_rotate(unsigned int num, int d)
{
    return (num << d) | (num >> (32-d));
}
```
