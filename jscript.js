var myObj = {
  gift: "pony",
  pet: "kitten",
  bed: "sleigh"
};

function checkObj(checkProp) {
  // Only change code below this 
  if (myObj.hasOwnProperty(checkProp)) {
    return myObj[checkProp]; 
  } else {
    return "Not Found"
  }
  // Only change code above this line
}
console.log(checkObj("joe"));

//checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "gift") should return "pony".
checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "pet") should return "kitten".
Passed
checkObj({gift: "pony", pet: "kitten", bed: "sleigh"}, "house") should return "Not Found".
checkObj({city: "Seattle"}, "city") should return "Seattle".
Passed
checkObj({city: "Seattle"}, "district") should return "Not Found".
