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
    var baseSelector = 'input#id_photo_';
    for (var i = 1; i <= 4; i++) {
        $(baseSelector + i).val(data.points[i-1]);
    }
});
