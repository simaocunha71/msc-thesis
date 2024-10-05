const vowelsCount = (s) => s.length - s.replace(/[^aeiouy]/g, "").length;

B:
const vowelsCount = (s) => s.replace(/[^aeiouy]/g, "").length;

C:
const vowelsCount = (s) => s.split("").filter(x => "aeiouyAEIOUY".includes(x)).length;
