```javascript
const iscube = (a) => {
  if(a === 0) return true;
  let b = Math.abs(a);
  for(let i = 0; i*i*i <= b; i++){
    if(i*i*i === b) return true;
  }
  return false;
}
```