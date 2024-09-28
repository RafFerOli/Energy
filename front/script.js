//Formatação de dados para inputs do sistema
function FormatInput(inputElement)
{  
    let primaryFormat = inputElement.getAttribute('data-format');
    let altFormat = inputElement.getAttribute('data-alt-format');
    let rawValue = inputElement.value;
    let value = rawValue.replace(/[^a-zA-Z0-9]/g, ''); // Remove caracteres que não são letras ou números

    // Aplica os formatos
    let formattedPrimary = applyFormat(value, primaryFormat);
    let formattedAlt = altFormat ? applyFormat(value, altFormat) : '';

    // Escolhe o melhor formato baseado na entrada
    return determineBestFormat(value, formattedPrimary, formattedAlt, primaryFormat, altFormat);
}

//Interceptação e Processamento da Entrada do Usuário
document.querySelectorAll('input[data-format]').forEach(input => {
    input.addEventListener('input', function(e) {
      let primaryFormat = this.getAttribute('data-format');
      let altFormat = this.getAttribute('data-alt-format');
      let rawValue = this.value;
      let value = rawValue.replace(/[^a-zA-Z0-9]/g, ''); // Remove caracteres que não são letras ou números
  
      // Aplica os formatos
      let formattedPrimary = applyFormat(value, primaryFormat);
      let formattedAlt = altFormat ? applyFormat(value, altFormat) : '';
  
      // Escolhe o melhor formato baseado na entrada
      this.value = determineBestFormat(value, formattedPrimary, formattedAlt, primaryFormat, altFormat);
    });
  });

  //Aplica formato
  function applyFormat(value, format) {
    let finalValue = '';
    let index = 0;
    for (let i = 0; i < format.length && index < value.length; i++) {
      if ((format[i] === '9' && /\d/.test(value[index])) || (format[i] === 'X' && /[a-zA-Z]/.test(value[index]))) {
        finalValue += value[index].toUpperCase(); // Converte letras para maiúsculas
        index++;
      } else if ((format[i] !== '9') && (format[i] !== 'X')) {
        finalValue += format[i]; // Adiciona o caractere de formatação
      } else {
        break; // Interrompe a formatação se o caractere não corresponder ao esperado na posição
      }
    }
    return finalValue;
  }

  //Determina melhor formato
  function determineBestFormat(value, primary, alternate, primaryFormat, alternateFormat) {
    let primaryConsumption = primary.replace(/[^0-9A-Z]/g, '').length;
    let alternateConsumption = alternate.replace(/[^0-9A-Z]/g, '').length;
    let valueLength = value.length;
  
    // Preferir o formato que mais se aproxima de utilizar todos os caracteres digitados
    if (alternate && alternateConsumption > primaryConsumption && alternateConsumption == valueLength) {
      return alternate;
    } else if (primaryConsumption == valueLength) {
      return primary;
    }
  
    return primaryConsumption >= alternateConsumption ? primary : alternate;
  }

