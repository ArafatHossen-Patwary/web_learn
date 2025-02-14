// function makingBreakfast(){
//     console.log('Making Breakfast');
//     console.log('Frying eggs');
//     console.log('Making Coffee');
//     console.log('Breakfast is ready');
// }

// console.log("Good Morning");
// makingBreakfast();
// console.log("Goodbye");

// console.log("Guest come");
// makingBreakfast();
// console.log("Goodbye");

// .............................................

// Permitter passing

// function makingBreakfast(person){
//     if(person=="Arafat"){
//         console.log('Making Breakfast');
//         console.log('Frying eggs');
//         console.log('Making Coffee');
//         console.log('Breakfast is ready'); 

//     }else if(person== "Guest"){
//         console.log('Making Breakfast');
//         console.log('Cutting Apple and Banana');
//         console.log('give biskut');
//         console.log('Making Coffee');
//         console.log('Breakfast is ready'); 
//     }
   
// }

// console.log("Good Morning");
// makingBreakfast("Arafat");
// console.log("Goodbye");

// console.log("Guest come");
// makingBreakfast("Guest");
// console.log("Goodbye");

//....................................
// Multiple permitter passing

// function sum(a,b){
//     console.log(a+b);

// }
// sum(2,3);
// sum(4,5);
//............................................

// Function passing in the function.
function BuyThinks(){
    console.log("Sugar");
    console.log("Milk");
    console.log("Apple");
    console.log("Banana");

}
function makingBreakfast(person){

       consol.log(person);
      consol.log("Doing Bazar");
      BuyThinks();
    //   console.log("Now im ready to Make breakfast");

    if(person=="Arafat"){
        console.log('Making Breakfast');
        console.log('Frying eggs');
        console.log('Making Coffee');
        console.log('Breakfast is ready'); 

    }else if(person== "Guest"){
        console.log('Making Breakfast');
        console.log('Cutting Apple and Banana');
        console.log('give biskut');
        console.log('Making Coffee');
        console.log('Breakfast is ready'); 
    }
   
}

console.log("Good Morning");
makingBreakfast("Arafat");
console.log("Goodbye");

console.log("Guest come");
makingBreakfast("Guest");
console.log("Goodbye");