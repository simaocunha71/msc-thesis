const strlen = (string) => string.length;

B:
const strlen = (string) => string.toString().length;

C:
const strlen = (string) => string.length || 0;

D:
const strlen = (string) => string.toString().length || 0;

E:
const strlen = (string) => string.length > 0 ? string.length : 0;

F:
const strlen = (string) => string.toString().length > 0 ? string.length : 0;

G:
const strlen = (string) => string.length > 0 ? string.length : string.toString().length;
