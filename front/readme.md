## localStorage
Despues de hacer la peticion se guarda el token en el localStorage
localStorage.setItem('Token', "aghdkjfhgaskdjfhg")

## VUE
Templates 


# Obtener token de local storage
localStorage.getItem('token');

# para el cierre de sesion
Se elimina el token del localStorage
handleCloseSession() {
    localStorage.removeItem('Token');
    window.location.reload();
}