const cycpatternCheck = (a, b) => {
let result = false;
for (let i = 0; i < a.length; i++) {
for (let j = 0; j < b.length; j++) {
if (a.slice(i, i + b.length).includes(b)) {
result = true;
break;
}
}
if (result) {
break;
}
}
return result;
}

/*

  