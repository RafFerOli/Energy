/*--------------------------------------------------------------------------------------
  Função para cadastrar registro de item
 --------------------------------------------------------------------------------------*/
const novoItem = () => {
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
      postItem(inputname, inputcomp, inputsurf,
              inputwall, inputroof, inputheig,
              inputorie, inputgare, inputgdis);        
  }
  
/* --------------------------------------------------------------------------------------
   Função para atualizar registro de item especifico usando o método POST
--------------------------------------------------------------------------------------*/
const postItem = async (inputname, inputcomp, inputsurf,
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
          method: 'post',
          body: formData
          })
          .then((response) => 
            { response.json();
              if (response.status === 200)
                { alert('Item cadastrado com sucesso!');}
            })
          .catch((error) => {
            console.error('Error:', error);
            alert('Não foi possível cadastrar o item.');
          });
  }