var cropper = $('#cropper').croppie(croppieOptions);


function readFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('#cropper').croppie('bind', {
                url: e.target.result
            });
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$('input#id_photo_0').on('change', function() {
    readFile(this);
});

cropper.on('update', function(cr) {
    var data = cropper.croppie('get');
    $('input#id_photo_1').val(data.points[0]);
    $('input#id_photo_2').val(data.points[1]);
    $('input#id_photo_3').val(data.points[2]);
    $('input#id_photo_4').val(data.points[3]);
});
