/*--------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/energys';
    let insertedCount = 0;
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        data.energys.reverse().forEach(item => {
          if (insertedCount < 20) { // Limita 20 linhas para aparecer
            insertList(item.name, item.heef, item.coef);
            insertedCount++;
          }
        })
      })
      .catch((error) => {
        console.error('Error:', error);
        //alert('Não foi possível se comunicar com a base.');
      });
  }

// Chamada da função para carregamento inicial dos dados
getList();

/*--------------------------------------------------------------------------------------
    Função para inserir items na tabela apresentada
  --------------------------------------------------------------------------------------*/
const insertList = (name, heef, coef) => {
    var item = [name, heef, coef]
    var table = document.getElementById('tabela');
    var row = table.insertRow();
  
    for (var i = 0; i < item.length; i++) {
      var cel = row.insertCell(i);
      cel.textContent = item[i];
    }

    insertButton(row.insertCell(-1))
    removeElement();
  }

/*  --------------------------------------------------------------------------------------
    Função para pegar nome do item na tabela para pesquisa
  --------------------------------------------------------------------------------------*/
document.addEventListener('DOMContentLoaded', (event) => {
  const tabela = document.getElementById('tabela');

    tabela.addEventListener('click', (event) => {
      const linha = event.target.closest('tr');
        if (linha && linha.parentNode.tagName.toLowerCase() === 'tbody') {
            const primeiraColuna = linha.querySelector('td');
            const primeiroValor = primeiraColuna ? primeiraColuna.textContent : null;
            console.log(primeiroValor);
            if(primeiroValor)
            {
              // Aqui você pode fazer algo com o primeiro valor, como exibi-lo em um alerta
              document.getElementById("nome").value = primeiroValor; 
              getValues(primeiroValor);
            }
          }
      });
  });
  
/*  --------------------------------------------------------------------------------------
  Função para obter as informações existentes de um item específico do servidor via requisição GET
  --------------------------------------------------------------------------------------*/

const getValues = async (nomequery) => {
  let url = 'http://127.0.0.1:5000/energy?name=' + nomequery;
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      insertValues(data.name, data.comp, data.surf,
                   data.wall, data.roof, data.heig,
                   data.orie, data.gare, data.gdis,                 
                   data.held, data.cold, data.heef, data.coef 
      );
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Não foi possível encontrar o item desejado.');
    });
  }

/*  --------------------------------------------------------------------------------------
    Função para inserir items nos componentes da tela 
  --------------------------------------------------------------------------------------*/
  const insertValues = (name, comp, surf,
                        wall, roof, heig,
                        orie, gare, gdis,                 
                        held, cold, heef, coef ) => {

      // Envia valores recebidos para os campos na tela
      document.getElementById("nome").value = name; 
      document.getElementById("compacidade").value = comp; 
      document.getElementById("superficie").value = surf;
      document.getElementById("parede").value = wall; 
      document.getElementById("telhado").value = roof; 
      document.getElementById("altura").value = heig;
      document.getElementById("orientacao").value = orie; 
      document.getElementById("envidracamento").value = gare; 
      document.getElementById("distribuicao").value = gdis;                 
      document.getElementById("cgaquecimento").value = held; 
      document.getElementById("cgresfriamento").value = cold; 
      document.getElementById("efaquecimento").value = heef; 
      document.getElementById("efresfriamento").value = coef;

      // Atualiza o estilo do input baseado no valor de heef
      const efaquecimentoInput = document.getElementById("efaquecimento");
      
      if (heef === "Alta") {
        efaquecimentoInput.style.backgroundColor = "green";
        efaquecimentoInput.style.color = "black";
      }
      else if (heef === "Média") {
        efaquecimentoInput.style.backgroundColor = "yellow";
        efaquecimentoInput.style.color = "black";
      } else {
        efaquecimentoInput.style.backgroundColor = "red";
        efaquecimentoInput.style.color = "yellow";
      }

      // Atualiza o estilo do input baseado no valor de heef
      const efresfriamentoInput = document.getElementById("efresfriamento");
      
      if (coef === "Alta") {
        efresfriamentoInput.style.backgroundColor = "green";
        efresfriamentoInput.style.color = "white";
      }
      else if (coef === "Média") {
        efresfriamentoInput.style.backgroundColor = "yellow";
        efresfriamentoInput.style.color = "black";
      } else {
        efresfriamentoInput.style.backgroundColor = "red";
        efresfriamentoInput.style.color = "yellow";
      }
  }

/*--------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
--------------------------------------------------------------------------------------*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*--------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove();
        deleteItem(nomeItem);      
      }
    }
  }
}

/*--------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via método DELETE
--------------------------------------------------------------------------------------*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/energy?nome=' + item;

  fetch(url, {
    method: 'delete'
  })
    .then((response) => 
      { response.json();
        if (response.status === 200)
          { alert('Item removido com sucesso!');

            // Apaga valores dos campos da tela
            document.getElementById("nome").value = ' '; 
            document.getElementById("compacidade").value = ' '; 
            document.getElementById("superficie").value = ' ';
            document.getElementById("parede").value = ' '; 
            document.getElementById("telhado").value = ' '; 
            document.getElementById("altura").value = ' ';
            document.getElementById("orientacao").value = ' '; 
            document.getElementById("envidracamento").value = ' '; 
            document.getElementById("distribuicao").value = ' ';                 
            document.getElementById("cgaquecimento").value = ' '; 
            document.getElementById("cgresfriamento").value = ' '; 
            document.getElementById("efaquecimento").value = ' '; 
            document.getElementById("efresfriamento").value = ' ';
          }
      })
    .catch((error) => {
      console.error('Error:', error);
      alert('Não foi possível remover o item.');
    });
}

/*--------------------------------------------------------------------------------------
  Função para abrir tela de novo cadastro
--------------------------------------------------------------------------------------*/
function openPopup(url) {
  const width = 750;
  const height = 800;
  const popupWindow = window.open(url, 'popupWindow', `width=${width},height=${height},resizable=yes,scrollbars=yes`);

  //verifica se o pup foi fechado para atualizar tela inicial
  const timer = setInterval(function() {
    if (popupWindow.closed) {
      clearInterval(timer);
      location.reload();
    }
  }, 500);
}

/*--------------------------------------------------------------------------------------
  Função para pesquisar item cadastrado ao pressionar botão
  --------------------------------------------------------------------------------------*/
function Pesquisar() {
  
  //Apaga todos os elementos da tabela
  const tableBody = document.getElementById('tabela').getElementsByTagName('tbody')[0];
  while (tableBody.rows.length > 1) {tableBody.deleteRow(1);}

  //Preenche com resultado da pesquisa
  getQuery(document.getElementById("pesquisa").value);
}

/*--------------------------------------------------------------------------------------
  Função para pesquisar item cadastrado ao pressionar tecla enter
  --------------------------------------------------------------------------------------*/
document.getElementById('pesquisa').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    Pesquisar();
  }
});

/*--------------------------------------------------------------------------------------
  Função para obter resultado da pesquisa do servidor via requisição GET
  --------------------------------------------------------------------------------------*/
const getQuery = async (nomequery) => {
  let url = 'http://127.0.0.1:5000/energy?name=' + nomequery;
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      insertList(data.name, data.heef, data.coef);
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Não foi possível encontrar o item informado!');
    });
  }

 /*--------------------------------------------------------------------------------------
  Função para atualizar registro de energy
  --------------------------------------------------------------------------------------*/
const Atualizar = () => {
      //Pega informações da tela
      let inputname = document.getElementById("nome").value;
      let inputcomp = document.getElementById("compacidade").value;  
      let inputsurf = document.getElementById("superficie").value; 
      let inputwall = document.getElementById("parede").value;
      let inputroof = document.getElementById("telhado").value;   
      let inputheig = document.getElementById("altura").value; 
      let inputorie = document.getElementById("orientacao").value;  
      let inputgare = document.getElementById("envidracamento").value;
      let inputgdis = document.getElementById("distribuicao").value;                  
  
      //Realiza requisição PUT
      putItem(inputname, inputcomp, inputsurf,
              inputwall, inputroof, inputheig,
              inputorie, inputgare, inputgdis);        
  }
  
/*--------------------------------------------------------------------------------------
   Função para atualizar registro de item especifico usando o método PUT
--------------------------------------------------------------------------------------*/
  const putItem = async (inputname, inputcomp, inputsurf,
                         inputwall, inputroof, inputheig,
                         inputorie, inputgare, inputgdis) => {
  
      //Pega dados para enviar a base
      const formData = new FormData();
      formData.append("name",inputname);
      formData.append("comp",inputcomp);  
      formData.append("surf",inputsurf); 
      formData.append("wall",inputwall);
      formData.append("roof",inputroof);   
      formData.append("heig",inputheig); 
      formData.append("orie",inputorie);  
      formData.append("gare",inputgare);
      formData.append("gdis",inputgdis); 
    
      //Aplica rota para requisição de serviço
      let url = 'http://127.0.0.1:5000/energy';
      fetch(url, {
          method: 'put',
          body: formData
          })
          .then((response) => 
            { response.json();
              if (response.status === 200)
                { 
                  alert('Item atualizado com sucesso!');

                  //Atualiza objetos na tela
                  getValues(inputname);

                  //Apaga todos os elementos da tabela
                  const tableBody = document.getElementById('tabela').getElementsByTagName('tbody')[0];
                  while (tableBody.rows.length > 1) {tableBody.deleteRow(1);}

                  //Atualiza tabela
                  getList();
              }
            })
          .catch((error) => {
            console.error('Error:', error);
            alert('Não foi possível atualiza o item.');
          });
    }


