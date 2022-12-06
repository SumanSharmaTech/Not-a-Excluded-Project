// Simple Algorithm to find the nth number of the fibonacci sequence.
function fib(nth) {
    var firstN = 0;
    var secondN = 1;
    
    if(nth < 1) {
    	throw "invalid nth num";
    }
    if(nth == 1) {
      return 0;
    } else if (nth == 2) {
      return 1;
    } else {
      for(var i = nth-2; i > 0; i--) {
        var tempN = firstN + secondN;
        firstN = secondN;
        secondN = tempN;
      }
      return secondN;
    }
    
}
