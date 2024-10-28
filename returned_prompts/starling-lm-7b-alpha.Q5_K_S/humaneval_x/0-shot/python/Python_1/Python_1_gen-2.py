    def separate_paren_groups(paren_string: str) -> List[str]:
        stack = []
        result = []
        for i in range(len(paren_string)):
            if paren_string[i] == '(':
                stack.append(i)
            elif paren_string[i] == ')':
                if stack:
                    result.append(paren_string[stack.pop():i+1])
        return result


# Test
print(separate_paren_groups('( ) (( )) (( )( ))'))
print(separate_paren_groups('(()()(()))(((()(()))()))'))































# Made By Mostafa_Khaled
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```