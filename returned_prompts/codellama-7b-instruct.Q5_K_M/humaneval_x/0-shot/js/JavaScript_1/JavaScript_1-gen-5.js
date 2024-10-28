const separateParenGroups = (paren_string) => {
let paren_groups = [];
let paren_group = "";
let open_parens = 0;
for (let i = 0; i < paren_string.length; i++) {
const char = paren_string[i];
if (char === "(") {
open_parens++;
paren_group += char;
} else if (char === ")") {
open_parens--;
paren_group += char;
if (open_parens === 0) {
paren_groups.push(paren_group);
paren_group = "";
}
} else {
paren_group += char;
}
}
return paren_groups;
}

