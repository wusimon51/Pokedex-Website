function filterCards() {
    let input, filter, cards;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    cards = document.getElementsByClassName("card");

    for (let i = 0; i < cards.length; i++) {
        let card = cards[i];
        let cardText = card.innerText;
        if (cardText.toUpperCase().indexOf(filter) > -1) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    }
}