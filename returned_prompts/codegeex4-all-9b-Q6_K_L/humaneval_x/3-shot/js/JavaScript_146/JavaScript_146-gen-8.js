
You are missing a semicolon after your if statement:
if (num > 10) {
  let firstDigit = Math.floor(Math.abs(num) / 10);
  let lastDigit = Math.floor(Math.abs(num) % 10);
  if (firstDigit % 2 == 1 && lastDigit % 2 == 1) {
    count += 1;
  }
} // <-- Missing semicolon here

The semicolon is necessary to end the if statement and start the next line of code.