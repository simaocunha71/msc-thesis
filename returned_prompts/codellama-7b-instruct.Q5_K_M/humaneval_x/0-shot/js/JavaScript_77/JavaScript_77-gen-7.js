const iscube = (a) => a === Math.cbrt(a) ** 3;

B:
const iscube = a => a === Math.cbrt(a) ** 3;

C:
const iscube = (a) => a === (a ** (1/3));

D:
const iscube = a => a === (a ** (1/3));

E:
const iscube = a => a === Math.pow(a, 1/3);

F:
const iscube = a => a === Math.cbrt(a);

G:
const iscube = a => a === (a ** (1/3)) || a === Math.cbrt(a);

H:
const iscube = a => a === Math.pow(a, 1/3) || a === Math.cbrt(a);

I:
const iscube = a => a === (a ** (1/3)) || a === Math.cbrt(a) || a === Math.pow(a, 1/3);

J:
const iscube = a => a === Math.cbrt(a) || a === Math.pow(a, 1/3);

K:
const iscube = a => a === Math.cbrt(a) || a === Math.pow(a, 1/3) || a === (a ** (1/3));
