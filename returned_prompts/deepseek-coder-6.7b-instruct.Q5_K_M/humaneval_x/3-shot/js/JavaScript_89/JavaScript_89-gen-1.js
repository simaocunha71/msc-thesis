  return s.split('').map(c => String.fromCharCode(((c.charCodeAt(0) - 97 + 14) % 26) + 97)).join('');
}
```

## Python

```python
# 