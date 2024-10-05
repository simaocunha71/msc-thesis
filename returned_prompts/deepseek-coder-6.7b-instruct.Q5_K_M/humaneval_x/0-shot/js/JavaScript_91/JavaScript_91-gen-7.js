  let sentences = S.split(/\.|\?|!/);
  let count = 0;
  
  for(let i = 0; i < sentences.length; i++){
    if(sentences[i][0] === 'I'){
      count++;
    }
  }
  
  return count;
}

module.exports = isBored;
```

# 2. 문제 풀이

```javascript
