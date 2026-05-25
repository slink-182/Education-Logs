const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function askQuestion() {
    let y = 20;
    rl.question("input value for z: ", function(answer) {
        let z = Number(answer);
        if (z > y) {
            let zy_difference = z - y;
            console.log("z is greater than y by " + zy_difference + ".");
            askQuestion();
        } 
        else if (z === y) {
            console.log("z is equal to y.");
            askQuestion();
        } 
        else if (z < y) {
            console.log("z is less than y.");
            rl.close();
        };
    });
}
askQuestion();