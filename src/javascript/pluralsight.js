

  
function write(message) {
  console.log(message);
  document.getElementById('code').innerHTML += message + '<br/>';
}

//___________________________________________

console.clear();

//___________________________________________


//eval is evil:
//eval("alert('Hello World'')");

//___________________________________________

write("");
write("*** JSON vs XML ***");

var input = '{"books":[{"title":"Frankenstein","author":"Mary Shelley"}]}';

var withJson2 = JSON.parse(input);
write("parsed with json2: " + withJson2.books[0].title + " by " + withJson2.books[0].author);
write("JSON.stringify(): " + JSON.stringify(withJson2));



//___________________________________________


write("");
write("*** DATES ***");

var from = new Date();
for (var i = 0; i < 10000000; i++ ) {
  var result = Math.sqrt(i);
}
var to = new Date();
var elapsed = to - from;
write("Calculating the square root of 10,000,000 numbers took: " + elapsed + " milliseconds" );




//___________________________________________



write("");
write("*** REGULAR EXPRESSIONS ***");
write("abcde".search(/d/));
var input = "Text with some <strong>highlighted</strong> parts/";
var expression = /<strong>(.*)<\/strong>/;
var results = expression.exec(input);
write("matched substring: " + results[0]);
write("first capture group: " + results[1]);

var s = "abc4de";
var containsANumber = /\d/.test(s);
write(s + " contains a number: " + containsANumber);

expression = /(\w+) (\w+)/g;
var updated = "Fred Brooks".replace(expression, function (match, capture1, capture2) {
  return capture2.toUpperCase() + ", " + capture1;
});
write("Fred Brooks -> " + updated);


//___________________________________________

write("");
write("*** UNDERSCORE ***");

var numbers = [1, 2, 3, 4];

_.each(numbers, function (num) {
  //write(num);
});

_(numbers).each(function (num) {
  //write(num);
});


var doubled = _(numbers).map(function (num) {
  return num * 2;
});
write(numbers + " doubled = " + doubled);

var total = _(numbers).reduce(function (memo, num) {
  return memo+=num;
}, 0);
write(numbers + " reduced = "+total);

//select
var evens = _(numbers).select(function(num) {
  return num %2 === 1;
});
write(numbers + " selected = " + evens);

//all
var allNumbers = _(numbers).all(function (item) {
  return typeof item == "number";
});
write (numbers + " all = " + allNumbers);

numbers2 =_(numbers).push("a");
allNumbers= _(numbers2).all(function (item) {
  return typeof item == "number";
});
write (numbers2 + " all = " + allNumbers);

write(numbers + " includes 4 =  " + _(numbers).include(4));


//___________________________________________

write("");
write("*** ARRAYS ***");

var arr = ['m', 'a', 'x', ' ', 'p', 'l', 'a', 'n', 'k'];

write('arr='+arr);
write('arr.slice(1,3)='+arr.slice(1,3));
write('arr='+arr);
write('arr.splice(1,3)='+arr.splice(1,3));
write('arr='+arr);
write('arr.reverse()='+arr.reverse());
write('arr='+arr);
write('arr.sort()='+arr.sort());
write('arr='+arr);


//___________________________________________

write (" ");
write ("*** EXCEPTIONS ***");

function fibonachi(n) {
  if (n<1) {
    throw {
      name: "fibonachi: out of range error",
      message: "expected parameter greater than 0, received "+n
    };
  } 
  else if (n==1 || n==2) {
    return 1;
  }
  else {
    return fibonachi(n-1) + fibonachi(n-2);
  }
}

try {
  write("the 6th Fibonachi is "+fibonachi(6));
  write(fibonachi(-4));
} catch(e) {
  write (e.name + ": " + e.message);
}

//___________________________________________

/*

write (" ");
write ("*** OBJECTS ***");

//objects are passed by reference
var whom = {name: "Max Plank"};
function reversePersonsName(p) {
  p.name = reverse(p.name);
  return p;
}

write(whom.name);
var newname = reversePersonsName(whom);
write(whom.name);

//___________________________________________

//alert("Line one\nLine two")

write("\u00A9");

write((0.1+0.2).toFixed(1));
write((0.1*10+0.2*10)/10);

var collection = ['a', 1, /3/, {}];
write(collection[0]);
write(collection.length);



//___________________________________________

function add() {
  var total = 0;
  for (var i = 0; i<arguments.length; i++) {
    total += arguments[i];
  }
  return total;
}

write (" ");
write ("*** arguments ***");
write(add());
write(add(1,2,3,4));

//___________________________________________

var object = {name: "anon"};
object.hi = function hello(who) {
  write("Hello "+who);
};

var sq = function square(x) {
  return x*x;
};
 
object.square =sq;
write (" ");
write ("*** object functions ***");
write(object.square(6));
write(object.hi("Patrick"));



//___________________________________________

var tom = {
  name: "Thomas",
  age: 70
};

for (var prop in tom) {
  write(prop + "=" + tom[prop]);
}



//___________________________________________

*/


