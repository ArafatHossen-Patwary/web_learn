
// Console used for show something on console.
console.log("Hello");
// Document used for show something on browser. 
document.write("Hello");

// ..............................
// Variable
var name="Arafat";
console.log(name);

let age= 30;
console.log(age);

let Aname="Arafat";
console.log(Aname);

const PI = 3.1415;
// Type of data
console.log(typeof PI)



// Comparison operator
let x="20";
if(x===20){
    console.log("X is equal to 20");
}else{
    console.log("x is not equal to 20");
}

// Js object
let studentInfo={
    name:"Arafat",
    Age:"25",
    Batch:77,
    comment :"Good Student"

}

// Array Data type
let Array =["apple","Banana"]

console.log(typeof Array);
console.log(typeof studentInfo);
console.log(studentInfo);
console.log(Array);


// Conditional Statement

let day = 2;

if(day==1){
    console.log("saturday");
}else if(day==2){
    console.log("Sunday");
}else if(day==3){
    console.log("Monday");
}else{
    console.log("Invalid Day");
}

// Use switch Statement
let Day=3;
switch(Day){
    case 1:
        console.log("Saturday");
    break;
    
    case 2:
        console.log("Sunday");
    break;

    case 3:
        console.log("Monday");
    break;

    default:
        console.log("Day not found");
    
    
}

// Looop

// loop is same to c++ or c