
<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary>
    <p>O Restaurante  🍝 🦐 Chapa Quente 🍛 🥘 precisa de você para finalizar sua ferramenta de construção de cardápios. O restaurante necessita desta ferramenta para que possa, de maneira simples, gerar seus cardápios considerando possíveis restrições alimentares e também a disponibilidade dos ingredientes em estoque. Hoje, a gestão das receitas e de estoque do restaurante acontece de forma muito ineficiente através de arquivos csv e, por essa razão, as pessoas fundadoras do estabelecimento desejam melhorar esta gestão.</p>
   
🚵 Habilidades exercitadas: </br>
  - conceito de `Hashmaps` através das estruturas de dados `Dict` e `Set` do Python; </br>
  - conhecimentos de testes de software; </br>
  - conhecimentos de orientação a objetos. </br>

</details>

# Orientações

  1. Clone o repositório

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
<details>
  
  Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```tree
.
├── data
│   ├──🔸 inventory_base_data.csv
│   └──🔸 menu_base_data.csv
├── src
│   ├──🔸 __init__.py
│   ├──🔸 app.py
│   ├── models
│   │   ├──🔸 __init__.py
│   │   ├──🔸 dish.py
│   │   └──🔸 ingredient.py
│   └── services
│       ├──🔸 __init__.py
│       ├──🔹 inventory_control.py
│       ├──🔹 menu_builder.py
│       └──🔹 menu_data.py
├── tests
│   ├──🔸 __init__.py
│   ├──🔸 conftest.py
│   ├── dish
│   │   ├──🔸 __init__.py
│   │   ├──🔸 conftest.py
│   │   ├──🔸 mocks.py
│   │   └──🔹 test_dish.py
│   ├── ingredient
│   │   ├──🔸 __init__.py
│   │   ├──🔸 conftest.py
│   │   ├──🔸 mocks.py
│   │   └──🔹 test_ingredient.py
│   ├──🔸 ingredients.py
│   ├── mocks
│   │   ├──🔸 inventory_base_data.csv
│   │   ├──🔸 inventory_base_data_2.csv
│   │   └──🔸 menu_base_data.csv
│   ├──🔸 test_app.py
│   ├──🔸 test_inventory_control.py
│   ├──🔸 test_menu_builder.py
│   └──🔸 test_menu_data.py
├──🔸 README.md
├──🔸 dev-requirements.txt
├──🔸 pyproject.toml
├──🔸 requirements.txt
├──🔸 setup.cfg
├──🔸 setup.py
├──🔸 trybe-filter-repo.sh
└──🔸 trybe.yml

</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, utilizo neste projeto o linter `Flake8`.
 Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual que permite sua máquina rodar, sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  :eyes: Caso precise desativar o ambiente virtual, execute o comando "deactivate". 
  :warning: Lembre-se de ativar novamente o ambiente virtual quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

