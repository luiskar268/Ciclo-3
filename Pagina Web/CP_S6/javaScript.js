function validar_formulario(){
    var nombre = document.getElementById('nombre');
    var apellido = document.getElementById('apellido');
    var email = document.getElementById('email');
    var contraseña = document.getElementById('contraseña');
    if(nombre.classList.length < 8){
        alert('El nombre debe contener al menos 5 caracteres');
        return false;
    }
    if(apellido.value.length < 5){
        alert('El apellido debe contener al menos 5 caracteres');
        return false;
    }

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if(!email.value.match(formato_email)){
        alert('No es un email válido');
        return false;
    }
    if(contraseña.value.length < 5){
        alert('La contraseña debe contener al menos 5 caracteres');
        return false;
    }
}