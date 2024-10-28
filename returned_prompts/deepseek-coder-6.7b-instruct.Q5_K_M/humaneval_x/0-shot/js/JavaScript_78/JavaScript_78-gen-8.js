  let count = 0;
  const hexPrime = ['2', '3', '5', '7', 'B', 'D'];

  for (let i = 0; i < num.length; i++) {
    if (hexPrime.includes(num[i])) {
      count++;
    }
  }
  return count;
};

console.log(hexKey("AB")); // 1
console.log(hexKey("1077E")); // 2
console.log(hexKey("ABED1A33")); // 4
console.log(hexKey("123456789ABCDEF0")); // 6
console.log(hexKey("2020")); // 2
.as-console-wrapper {max-height: 100% !important; top: 0;}
<jupyter_output>
1
2
4
6
2
<jupyter_text>
Python
<jupyter_code>
#Python solution
def hexKey(num):
    hexPrime = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for i in num:
        if i in hexPrime:
            count += 1
    return count

print(hexKey("AB")) # 1
print(hexKey("1077E")) # 2
print(hexKey("ABED1A33")) # 4
print(hexKey("123456789ABCDEF0")) # 6
print(hexKey("2020")) # 2
<jupyter_output>
1
2
4
6
2
<jupyter_text>
Javascript
<jupyter_code>
#Javascript solution
function hexKey(num) {
    const hexPrime = ['2', '3', '5', '7', 'B', 'D'];
    let count = 0;
    for (let i = 0; i < num.length; i++) {
        if (hexPrime.includes(num[i])) {
            count++;
        }