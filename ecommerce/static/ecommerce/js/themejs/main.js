$('.nav-market').addClass('active');
function change_price(price_product, price_sup, percentage) {
    price_sup = parseFloat(price_sup);
    price_product = parseFloat(price_product);
    percentage = parseFloat(percentage);
    var price;
    if(isNaN(percentage )){
         price = price_product + price_sup;
        $('#price_new_2').html('$' + price.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1 "));
    }
    else{
        price = price_product + price_sup;
        $('#price_old_1').html('$' + price.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1 "));
        price = price - ((price * percentage) / 100);
        $('#price_new_1').html('$' + price.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1 "));
    }
}