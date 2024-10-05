  let seq = [3, 2, 8];
  if (n < 3) return seq.slice(0, n + 1);
  let a = 3, b = 2, c = 8;
  for (let i = 3; i < n; i++) {
    let temp = a;
    a = b;
    b = c;
    c = temp + b + seq[i - 1];
    seq.push(c);
  }
  return seq;
}
tri(3);
tri(4);
tri(5);
tri(6);
tri(7);
tri(8);
tri(9);
tri(10);
tri(11);
tri(12);
tri(13);
tri(14);
tri(15);
tri(16);
tri(17);
tri(18);
tri(19);
tri(20);
tri(21);
tri(22);
tri(23);
tri(24);
tri(25);
tri(26);
tri(27);
tri(28);
tri(29);
tri(30);
tri(31);
tri(32);
tri(33);
tri(34);
tri(35);
tri(36);
tri(37);
tri(38);
tri(39);
tri(40);
tri(41);
tri(42);
tri(43);
tri(44);
tri(45);
tri(46);
tri(47);
tri(48);
tri(49);
tri(50);

This is the code that I wrote, but it's not working as expected. I have to calculate the Tribonacci sequence up to 50.
Could you help me to fix the code?
I'm sorry, but I didn't find anything wrong with the code.

A: Your function is not correctly implementing the Tribonacci sequence. The problem lies in the line where you calculate c:
c = temp + b + seq[i - 1];

You'