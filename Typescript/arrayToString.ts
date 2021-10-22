// Convert array of strings to single string
function getArrayAsString(
  arrayOfStrings: string[],
  separator: string = ', '
): string {
  return arrayOfStrings.filter((str) => str).join(separator);
}
