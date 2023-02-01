function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

function quicksort(table) {
    if (table.length < 2) return table;
    let pivot = table[0];
    let rightSide = [];
    let leftSide = [];
    for (let i = 1; i < table.length; i++) {
        if (table[i] < pivot) {
            leftSide.push(table[i]);
        } else {
            rightSide.push(table[i]);
        }
    }
    return [...quicksort(leftSide), pivot, ...quicksort(rightSide)];
}

function main() {
    let table = [];
    let len = 10;
    for (let i = 0; i < len; i++) {
        table.push(getRandomInt(1, 100000));
    }
    console.log("Not sorted table : ", table);
    let sorted = quicksort(table);
    console.log("Sorted : ", sorted);
}

main();