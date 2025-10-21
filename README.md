<!-- O projeto é sobre um sistema que gerencia produtos de uma loja. Permite cadastrar produtos, ver o estoque e atualizar a quantidade -->
<!-- Para isso será utilizado uma API RESTful com a FastAPI 
utilizando pastas como back-end
banco de dados
• Consumir a API via aplicativo Streamlit (front-end).
• Garantir tratamento de erros, validação e
documentação da API.

Estrutura:
Pasta back-end e front-end separadas.
Utilizar todas as boas praticas como git, gitignore,
requirements, env e etc.. -->

<!-- Etapas do Desenvolvimento -->

<!-- Funcionalidades: -->
<!-- • Adicionar produto -->
<!-- • Listar todos -->
<!-- • Atualizar preço ou quantidade -->
<!-- • Excluir produto -->
<!-- • Mostrar valor total em estoque (no Streamlit) -->

A ideia era criar um sistema que gerencia os produtos de uma loja. Então, basicamente, dá pra cadastrar produtos, ver o estoque, atualizar a quantidade ou o preço, excluir e também ver o valor total de tudo que tá no estoque.

Pra fazer isso, eu usei a FastAPI pra criar uma API RESTful. Separei tudo certinho: backend ficou numa pasta, frontend em outra. No backend também tem o banco de dados, e o frontend eu fiz com Streamlit, que é o que a gente usou pra consumir a API e mostrar os dados de forma visual.

A API tem tratamento de erros, validação certinha dos dados e também tá documentada (aquela doc automática da FastAPI ajuda bastante nisso). Coloquei tudo que precisava: .gitignore, requirements.txt, variáveis de ambiente com .env, e fui usando o Git desde o começo pra organizar o projeto direitinho.

As funcionalidades principais são:

Adicionar um novo produto no estoque

Listar todos os produtos que já foram cadastrados

Atualizar o preço ou a quantidade de algum produto

Excluir um produto do sistema

Mostrar o valor total do estoque direto no app do Streamlit

No geral, foi um projeto legal de fazer porque deu pra treinar tanto o backend com FastAPI quanto o frontend com Streamlit, além de pensar na organização do código e nas boas práticas.
]

a função deletar está funcionando só na api, no streamlit não roda, irei rever 
