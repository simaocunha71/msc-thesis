let words = s.split(" ");
    let result = [];
    for(let i = 0; i < words.length; i++){
        let chars = words[i].split("");
        chars.sort((a,b) => a.charCodeAt(0) - b.charCodeAt(0));
        result.push(chars.join(""));
    }
    return result.join(" ");
}
console.log(antiShuffle('Hi')) // 'Hi'
console.log(antiShuffle('hello')) // 'ehllo'
console.log(antiShuffle('Hello World!!!')) // 'Hello !!!Wdlor'


```

## 2. Solution

```javascript

