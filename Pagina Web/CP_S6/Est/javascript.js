function cambiarColor(){
    //Capturar elementos por su id
    var div1 = document.getElementById('cambiar');
    if(div1.classList.contains('color')){
        div1.classList.remove('color');
    }else{
        div1.classList.add('color');
    }
    //Capturar elementos por nombre de clase
    //console.log(document.getElementsByClassName('clase'));
    //Capturar elemento  por atributo name
    //document.getElementsByName();
}

function validarFormulario(){
    var nombre = document.formulario.nombre;
    var email = document.formulario.email;
    if(nombre.value.length < 5){
        alert('El nombre debe contener al menos 5 caracteres');
        return false;
    }

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if(!email.value.match(formato_email)){
        alert('No es un email válido');
        return false;
    }

}