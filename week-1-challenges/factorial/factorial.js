exports.factorial = function(num) {
  //Base Case
  if (num === 0)
    return 1;
  //Recursive call
  return num * this.factorial(num-1);
};

//Precision of builtin integers is not enough to calculate exact factorial number.
//At large enough numbers, integers are represented in scientific notation, and eventually become Infinity
//Use of external arbitrary precision integer libraries is required for accurate calculations.

//Also, even at high nums the function was exteremely fast. I suspect Node has some optimizations under the hood. For any other recursive functions, I would probably use memoization with a cache.