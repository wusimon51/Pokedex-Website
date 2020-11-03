function filterCards() {
    let input, filter, cards;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    cards = document.getElementsByClassName("card-text");

    console.log(cards[0]);
}