const strongestExtension = (class_name, extensions) => {
  const strengths = extensions.map(ext => {
    const cap = ext.match(/\p{Lu}/gu).length;
    const sm = ext.match(/\p{Ll}/gu).length;
    return cap - sm;
  });
  const max = Math.max(...strengths);
  const index = strengths.findIndex(s => s === max);
  return `${class_name}.${extensions[index]}`;
};
