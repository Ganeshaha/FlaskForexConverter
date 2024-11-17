$("#converter-form").on("submit",
    async function handleFormSubmit(event) {
        event.preventDefault();
   
        console.log(event.target);
        
        validResponse = await axios.post('/submit',
           {fromValue: event.target[0].value,
            toValue: event.target[1].value,
            amountValue: event.target[2].value}
        ).then(response => savedReponse =response);
    
        console.log(savedReponse)
     
        if(savedReponse.data.result != undefined){
            $('body').append(`  
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                <strong>Result: ${savedReponse.data.result}</strong> 
                <button type="button" class="close btn-close" data-bs-dismiss="alert" aria-label="Close">
                <span aria-hidden="true"></span>
                </button>
                </div> `);
    
        }
       

        if (savedReponse.data.hasOwnProperty("error")){
            //$('#error').text(`Error: ${savedReponse.data.error.info}`);
            $('body').append(`  
                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>${savedReponse.data.error.info}</strong> 
                <button type="button" class="close btn-close" data-bs-dismiss="alert" aria-label="Close">
                <span aria-hidden="true"></span>
                </button>
                </div> `);
                    }
        

        //if (savedReponse.data.success == "false"){

          //  $('body').append(`<p>${savedReponse.data.error.info} </p>`)
        // }
        
    
    })
function closeScript(){
    console.log("testing");
    $('.alert').remove()
}
$('.close').on("click", 
    function(event) {
        $('.alert').remove()

})
