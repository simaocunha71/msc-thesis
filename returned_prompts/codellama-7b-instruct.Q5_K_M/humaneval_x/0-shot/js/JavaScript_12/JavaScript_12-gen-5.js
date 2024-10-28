const longest = (strings) => {
const max = Math.max(...strings.map(s => s.length));
return strings.find(s => s.length === max);
}

B:
const longest = (strings) => {
const maxLength = strings.reduce((max, s) => Math.max(max, s.length), 0);
return strings.find(s => s.length === maxLength);
}

C:
const longest = (strings) => {
if (strings.length === 0) {
return null;
}
const maxLength = strings.reduce((max, s) => Math.max(max, s.length), 0);
return strings.find(s => s.length === maxLength);
}

D:
const longest = (strings) => {
if (strings.length === 0) {
return null;
}
const maxLength = Math.max(...strings.map(s => s.length));
return strings.find(s => s.length === maxLength);
}

E:
const longest = (strings) => {
if (strings.length === 0) {
return null;
}
const maxLength = Math.max(...strings.map(s => s.length));
return strings.find(s => s.length === maxLength);
}