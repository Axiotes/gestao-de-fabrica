$(
    function()
    {
        $("#form-login").on("submit", function(event)
        {
            event.preventDefault();

            let emailValue = $("#email").val();
            console.log(emailValue)

            let senhaValue = $("#senha").val();
            console.log(senhaValue)
            
            if (emailValue == ""){
                alert("Informe seu email");
                return
            } 
            if (senhaValue == ""){
                alert("Informe sua senha");
                return
            }

            $.ajax({
                method: "POST",
                url: "http://127.0.0.1:8000/login",
                data: {email: emailValue, senha: senhaValue},
                crossDomain: true,
                dataType: "json",
                headers: {
                    "accept": "application/json",
                    //"Access-Control-Allow-Origin": "*"
                }
            })
            .done(function(resp){
                if (resp == false){
                    alert("Email ou senha inválido")
                }
                else {
                    location.replace("dashboard.html")
                }
            }); //.done(function(resp)
            
        }); //$("#form-login").on("submit", function(event)
    } //function()
) //$(