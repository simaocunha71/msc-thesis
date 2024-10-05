  const noEvenDigit = num => {
    let strNum = num.toString();
    for(let i = 0; i < strNum.length; i++){
      if(strNum[i] % 2 === 0) return false;
    }
    return true;
  }
  
  return x.filter(noEvenDigit).sort((a, b) => a - b);
}
uniqueDigits([15, 33, 1422, 1]);
uniqueDigits([152, 323, 1422, 10]);
```

# 18. Find the missing number in a given integer array

