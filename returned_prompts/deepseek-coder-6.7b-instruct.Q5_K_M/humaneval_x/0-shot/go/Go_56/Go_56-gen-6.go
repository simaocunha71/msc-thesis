  if brackets == ""{
    return true
  }

B:
  if len(brackets) % 2 != 0 {
    return false
  }

C:
  stack := []rune{}
  for _, bracket := range brackets {
    switch bracket {
    case '<':
      stack = append(stack, bracket)
    case '>':
      if len(stack) == 0 || stack[len(stack)-1] != '<' {
        return false
      }
      stack = stack[:len(stack)-1]
    default:
      return false
    }
  }

  return len(stack) == 0
}
```

## 2.1.4. 코드 설명

코드는 하나의 함수로 구성되어 있으며, 이 함수는 brackets라는 문자열을 매개변수로 받습니다. 함수는 두 가지 조건을 확인합니다:

1. 빈 문자열인지 확인: 만약 빈 문자열이면 함수는 true를 반환합니다. 이는 빈 문자열은 올바르게 괄호가 될 수 있기 때문입니