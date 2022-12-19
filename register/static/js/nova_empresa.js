const cnpj = document.querySelector("#id_cnpj");

cnpj.addEventListener('keypress', () => {
    let cnpjLength = cnpj.value.length

    if (cnpjLength === 2 || cnpjLength === 6) {
        cnpj.value += '.'
    } else if (cnpjLength === 10) {
        cnpj.value += '/'
    } else if (cnpjLength === 15) {
        cnpj.value += '-'
    }

    if (cnpjLength >= 18) {
        cnpj.value = cnpj.value.substring(0, 17);
    }
})