let names = [];
const poke_names = document.getElementsByClassName("poke_name");
for (name of poke_names) {
    names.push(name);
}
names = names.sort();

function filterCards() {
    let input, filter, cards;
    input = document.getElementById("search");
    filter = input.value;

    let low = 0;
    let high = names.length - 1;
    while (low <= high) {
        let mid = (low + high) / 2;
        if (names[mid] < filter) {
            for (let i = 0; i < mid + 1; i++) {
                
            }
        }
    }

}