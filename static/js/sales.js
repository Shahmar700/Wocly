$('.plus-cart').click(function () {
    // console.log("salam")
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    console.log(id);
    $.ajax(
        {
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log(data);
                eml.innerText = data.quantity;
                
                
                console.log(data.amount)
                document.getElementById("amount").innerText = data.amount.toFixed(2);
                document.getElementById("totalamount").innerText = data.totalamount.toFixed(2);
                document.getElementById("amount_base").innerText = data.amount;
                document.getElementById("quant-"+id).innerText = data.quantity.toFixed(2);
                document.getElementById("quant_base-"+id).innerText = data.quantity.toFixed(2);
                document.getElementById("amounts-"+id).innerText = data.tempamount.toFixed(2);
            }
        })
});

$('.minus-cart').click(function () {
    // console.log("salam")
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2];
    // console.log("salam")
    $.ajax(
        {
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            
            success: function (data) {
                console.log(data)
                eml.innerText = data.quantity;
                
                document.getElementById("amount").innerText = data.amount.toFixed(2);
                document.getElementById("totalamount").innerText = data.totalamount.toFixed(2);
                document.getElementById("amount_base").innerText = data.amount;
                document.getElementById("quant-"+id).innerText = data.quantity.toFixed(2);
                document.getElementById("quant_base-"+id).innerText = data.quantity.toFixed(2);

                document.getElementById("amounts-"+id).innerText = data.tempamount.toFixed(2);
                
            }
        })
});

$('.remove-cart').click(function () {
    var id = $(this).attr("pid").toString();
    var elm = this;
    $.ajax(
        {
            type: "GET",
            url: "/removecart",
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log(data)
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("amount_base").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
                elm.parentNode.parentNode.remove()
            }
        })
});
