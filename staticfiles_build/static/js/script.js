let submitBtn = document.getElementById('submitBtn');
let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];
let fileName;
let imagesDiv = document.getElementById('imagesDiv');
let imageHeadingDiv = document.getElementById('imageHeadingDiv');

// data.append('')

let createWatermark = () => {
    imageHeadingDiv.style.display = 'block';
    let form = document.getElementById('form');
    let data = new FormData(form);
    let url = window.location.href;
    console.log(url);
    fetch(url,
        {
            method: 'POST',

            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken.value,
            },
            body: data
        }

    ).then(response => response.json()).then(data => {
        console.log(data);
        data = JSON.parse(data);
        if (data['status'] == 200) {
            tempStr = ``;
            for (let path of data['paths']) {
                // fileName = path.split('/').slice(-1)[0];
                tempStr += `
                <div class="card p-2 mb-3">
                    <div class="  d-flex  no-wrap justify-content-between align-items-center">
                        <div class="imageDiv">
                            <img src=${path} alt=${path}>
                        </div>
                    
                        <div class="">
                            <a href=${path} class="btn btn-primary" download>Download</a>
                        </div>
                    </div>
                </div>
                `
            }
        }
        else {
            tempStr = '<h4 class="text-danger">Someting Error Occoured!</h4>';
        }
        imagesDiv.innerHTML = tempStr;

    })
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
        submitBtn.addEventListener('click', event => {
            event.preventDefault();
            if (!form.checkValidity()) {
                event.stopPropagation();
            }
            else{
                createWatermark();
            }
            form.classList.add('was-validated')
        }, false)
    })
})()