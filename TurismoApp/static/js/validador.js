/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$("#fromulario").validate({
    rules: {
        "txtCorreo": {
            required: true,
            email: true
        },
        "txtNombre": {
            required: true
        },
		"txtApellido": {
            required: true
        },
        "txtTelefono": {
            required: true,
            tel: true
        },
        "txtCiudad": {
            required: true
        },
        "txtFecha": {
            required: true
        },
        "txtRun":{
            required: true
        }
    },
    messages: {
        "txtNombre": {
            required: "Ingrese Nombre"
        },
		"txtApellido": {
            required: "Ingrese Apellido"
        },
        "txtCorreo": {
            required: "Ingrese correo",
            email: "No cumple formato"
        },
        "txtTelefono": {
            required: "Ingrese telefono",
            tel: "No cumple formato"
        },
        "txtCiudad": {
            required: "Ingrese ciudad"
        },
        "txtFecha": {
            required: "Ingrese fecha"
        },
        "txtRun": {
            required: "Ingrese run"
        }
    }
});

