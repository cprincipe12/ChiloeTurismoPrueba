function revisarDigito(dvr)
{
    dv = dvr + ""
    if (dv != '0' && dv != '1' && dv != '2' && dv != '3' && dv != '4' && dv != '5' && dv != '6' && dv != '7' && dv != '8' && dv != '9' && dv != 'k' && dv != 'K')
    {
        alert("Debe ingresar un digito verificador valido");
        window.document.formulario.txtRun.focus();
        window.document.formulario.txtRun.select();
        return false;
    }
    return true;
}
function revisarDigito2(ctxtRun)
{
    largo = ctxtRun.length;
    if (largo < 2)
    {
        alert("Debe ingresar el Run completo")
        window.document.formulario.txtRun.focus();
        window.document.formulario.txtRun.select();
        return false;
    }
    if (largo > 2)
        txtRun = ctxtRun.substring(0, largo - 1);
    else
        txtRun = ctxtRun.charAt(0);
    dv = ctxtRun.charAt(largo - 1);
    revisarDigito(dv);
    if (txtRun == null || dv == null)
        return 0
    var dvr = '0'
    suma = 0
    mul = 2
    for (i = txtRun.length - 1; i >= 0; i--)
    {
        suma = suma + txtRun.charAt(i) * mul
        if (mul == 7)
            mul = 2
        else
            mul++
    }
    res = suma % 11
    if (res == 1)
        dvr = 'k'
    else if (res == 0)
        dvr = '0'
    else
    {
        dvi = 11 - res
        dvr = dvi + ""
    }
    if (dvr != dv.toLowerCase())
    {
        alert("EL Run es incorrecto")
        window.document.formulario.txtRun.focus();
        window.document.formulario.txtRun.select();
        return false
    }
    return true
}
function Rut(texto)
{
    var tmpstr = "";
    for (i = 0; i < texto.length; i++)
        if (texto.charAt(i) != ' ' && texto.charAt(i) != '.' && texto.charAt(i) != '-')
            tmpstr = tmpstr + texto.charAt(i);
    texto = tmpstr;
    largo = texto.length;
    if (largo < 2)
    {
        alert("Debe ingresar el Run completo")
        window.document.formulario.txtRun.focus();
        window.document.formulario.txtRun.select();
        return false;
    }
    for (i = 0; i < largo; i++)
    {
        if (texto.charAt(i) != "0" && texto.charAt(i) != "1" && texto.charAt(i) != "2" && texto.charAt(i) != "3" && texto.charAt(i) != "4" && texto.charAt(i) != "5" && texto.charAt(i) != "6" && texto.charAt(i) != "7" && texto.charAt(i) != "8" && texto.charAt(i) != "9" && texto.charAt(i) != "k" && texto.charAt(i) != "K")
        {
            alert("El valor ingresado no corresponde a un R.U.T valido");
            window.document.formulario.txtRun.focus();
            window.document.formulario.txtRun.select();
            return false;
        }
    }
    var invertido = "";
    for (i = (largo - 1), j = 0; i >= 0; i--, j++)
        invertido = invertido + texto.charAt(i);
    var dtexto = "";
    dtexto = dtexto + invertido.charAt(0);
    dtexto = dtexto + '-';
    cnt = 0;
    for (i = 1, j = 2; i < largo; i++, j++)
    {
        //alert("i=[" + i + "] j=[" + j +"]" );		
        if (cnt == 3)
        {
            dtexto = dtexto + '.';
            j++;
            dtexto = dtexto + invertido.charAt(i);
            cnt = 1;
        } else
        {
            dtexto = dtexto + invertido.charAt(i);
            cnt++;
        }
    }
    invertido = "";
    for (i = (dtexto.length - 1), j = 0; i >= 0; i--, j++)
        invertido = invertido + dtexto.charAt(i);

    window.document.formulario.txtRun.value = invertido.toUpperCase()
    if (revisarDigito2(texto))
        return true;
    return false;
}