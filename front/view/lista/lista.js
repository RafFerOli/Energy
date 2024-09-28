/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/energys';
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        data.energys.forEach(item => insertList(item.name, item.comp, item.surf,
                                                item.wall, item.roof, item.heig,
                                                item.orie, item.gare, item.gdis,                 
                                                item.held, item.cold, item.heef, item.coef))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Chamada da função para carregamento inicial dos dados
    --------------------------------------------------------------------------------------
  */
  getList();
    
  /*
    --------------------------------------------------------------------------------------
    Função para inserir items na lista apresentada
    --------------------------------------------------------------------------------------
  */
  const insertList = (name, comp, surf,
                      wall, roof, heig,
                      orie, gare, gdis,                 
                      held, cold, heef, coef) => {
    var item = [name, comp, surf,
                wall, roof, heig,
                orie, gare, gdis,                 
                held, cold, heef, coef]
    var table = document.getElementById('tabela');
    var row = table.insertRow();
  
    for (var i = 0; i < item.length; i++) {
      var cel = row.insertCell(i);
      cel.textContent = item[i];
    }
  }