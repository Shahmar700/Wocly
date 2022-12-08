function addImage(){
    var image_inputs = $("input[type='file']").length



    if(image_inputs < 3){
        $("#imagesDiv").append(`
            <input type="file" name="image" accept="image/png, image/gif, image/jpeg" />
        `)
    }

    if(image_inputs >= 2){
        $("#addImageButton").css("display", "none")
    }
}