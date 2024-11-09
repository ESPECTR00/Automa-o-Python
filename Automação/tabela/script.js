function addProduct() {
    // Pegar os valores dos campos do formulário
    const codigo = document.getElementById("company-codigo").value;
    const marca = document.getElementById("marca").value;
    const tipo = document.getElementById("tipo").value;
    const categoria = document.getElementById("categoria").value;
    const precoUnitario = document.getElementById("preco_unitario").value;
    const custo = document.getElementById("custo").value;
    const obs = document.getElementById("obs").value;

    // Pegar a tabela
    const table = document.getElementById("productTable").getElementsByTagName('tbody')[0];

    // Criar uma nova linha
    const newRow = table.insertRow();

    // Inserir células na nova linha
    newRow.insertCell(0).textContent = codigo;
    newRow.insertCell(1).textContent = marca;
    newRow.insertCell(2).textContent = tipo;
    newRow.insertCell(3).textContent = categoria;
    newRow.insertCell(4).textContent = precoUnitario;
    newRow.insertCell(5).textContent = custo;
    newRow.insertCell(6).textContent = obs;

    // Limpar o formulário após a inserção
    document.getElementById("productForm").reset();
}
