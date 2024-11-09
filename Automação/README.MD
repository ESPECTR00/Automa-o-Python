# Cadastro de Produtos

Este projeto é uma aplicação web simples para cadastro e visualização de produtos. Ele inclui uma funcionalidade de automação em Python, utilizando a biblioteca PyAutoGUI para preencher automaticamente os campos do formulário com dados de uma planilha CSV.
 
## Tecnologias Utilizadas
- Python
- HTML
- CSS
- JavaScript

| Blibiotecas | Significado |
|--------|-------------|
|Pandas |Usado para ler a planilha em .CSV|
|PyAutoGUI |Para automatizar o processo desde abrir o navegador até inserir os dados|
|Time|Usado para pausas curtas, assim fazendo a CPU ter tempo de processar as informações|

## Rodar o código

#### Para o Formulário
Qualquer navegador moderno para abrir o index.html.

Nele terá os seguintes campos para cadastro:
- Código do Produto
- Marca
- Tipo do Produto
- Categoria
- Preço Unitário
- Custo
- Observações

Instale as bibliotecas necessárias:
```
pip install pyautogui pandas time
```

#### Cadastro Automático com o Script Python
Certifique-se de que o arquivo produtos.csv contém os dados dos produtos a serem cadastrados.

Execute o script automacao.py:
```
python automacao.py
```
 
O script abrirá o navegador, acessará o formulário em index.html e preencherá automaticamente cada campo com os dados de produtos.csv. Cada cadastro é enviado individualmente, e os produtos serão exibidos na tabela.


Para usar o click do mouse recomendavel que pegue a posição dos locais da tela:
```
time.sleep(5)
print(pyautogui.position())
```