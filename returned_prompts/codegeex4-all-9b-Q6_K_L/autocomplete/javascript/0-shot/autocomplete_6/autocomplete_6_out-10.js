  
      if(token == tokens2[j]) {
        tokens2.splice(j, 1);
        continue outer;
      }
    }
    values += token + ' ';
  }

  return values.trim();
}
```


  outer:
  for(var i = 0; i < tokens1.length; i++) {
    var token = tokens1[i];
    for(var j = 0; j < tokens2.length; j++) {  
      if(token == tokens2[j]) {
        tokens2.splice(j, 1);
        continue outer;
      }
    }
    values += token + ' ';
  }

  return values.trim();
```

  for(var i = 0; i < tokens2.length; i++) {
    var token = tokens2[i];
    values += token + ' ';
  }

  return values.trim();
```