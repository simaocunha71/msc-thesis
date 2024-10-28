
const fileNameCheck = (file_name) => {
  const file_name_array = file_name.split(".");
  return (file_name_array.length === 2 && file_name.match(/[a-z]/i) && file_name_array[1] === "txt" || "exe" || "dll") ? "Yes" : "No";
};

