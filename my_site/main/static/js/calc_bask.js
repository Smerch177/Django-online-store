const d = document;
let tb = d.querySelector('tbody'),
    cartItems = tb.querySelectorAll('tr.product');

cartItems.forEach(element => {
    element.querySelector('input').addEventListener('input', function() {
        let price = Number(element.querySelector('#price').innerText),
        count = Number(element.querySelector('#count').value),
        limit = 10000000;

        if (count < 0) {
            element.querySelector('#count').value = 0;
        }

        if (price * count < 0) {
            element.querySelector('#amount').innerHTML = 0;
        } else if(price * count > limit){
        element.querySelector('#amount').innerHTML = Math.floor(limit / price) * price;
        element.querySelector('#count').value = Math.floor(limit / price);
        } else {
            element.querySelector('#amount').innerHTML = price * count;
        }
        all_prices = document.querySelectorAll('td#amount');
        full_price = 0;
        for (let i of all_prices) {
            full_price += Number(i.innerText);
        }

        document.querySelector('#full_amount').innerHTML = full_price;
        document.querySelector('#hidden_full_amount').value = full_price;

        const cartInfoJson = {};
        cartItems.forEach(element => {
            let item = element.querySelector('#item_name').innerText,
                count = element.querySelector('#count').value,
                amount = element.querySelector('#amount').innerText;
            if (count > 0) {
                cartInfoJson[item] = [count, amount];
            }
        })

        document.querySelector('#hidden_all_info_json').value = JSON.stringify(cartInfoJson);
        console.log(document.querySelector('#hidden_all_info_json').innerText);
    });
});