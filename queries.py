# =========================
# FUNCIONÁRIOS
# =========================

LISTAR_FUNCIONARIOS = """
SELECT
    id,
    nome,
    cargo,
    percentual_comissao
FROM funcionarios
ORDER BY nome;
"""

INSERIR_FUNCIONARIO = """
INSERT INTO funcionarios (
    nome,
    cargo,
    percentual_comissao
)
VALUES (%s, %s, %s)
RETURNING id;
"""


# =========================
# VENDAS
# =========================

INSERIR_VENDA = """
INSERT INTO vendas (
    carro_id,
    comprador_id,
    funcionario_id,
    forma_pagamento_id,
    valor_venda,
    percentual_desconto,
    data_venda
)
VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE)
RETURNING id;
"""


# =========================
# COMISSÕES
# =========================

INSERIR_COMISSAO = """
INSERT INTO comissoes (
    venda_id,
    valor_comissao
)
VALUES (%s, %s);
"""


# =========================
# RELATÓRIOS
# =========================

RELATORIO_VENDAS = """
SELECT
    v.id AS venda_id,
    b.nome AS comprador,
    f.nome AS vendedor,
    m.nome AS marca,
    mo.nome AS modelo,
    v.valor_venda,
    v.percentual_desconto,
    c2.valor_comissao,
    fp.descricao AS forma_pagamento,
    v.data_venda
FROM vendas v
JOIN compradores b ON v.comprador_id = b.id
JOIN funcionarios f ON v.funcionario_id = f.id
JOIN carros c ON v.carro_id = c.id
JOIN modelos mo ON c.modelo_id = mo.id
JOIN marcas m ON mo.marca_id = m.id
JOIN formas_pagamento fp ON v.forma_pagamento_id = fp.id
LEFT JOIN comissoes c2 ON c2.venda_id = v.id
ORDER BY v.id;
"""

RELATORIO_COMISSOES = """
SELECT
    f.id AS funcionario_id,
    f.nome AS vendedor,
    COUNT(c.id) AS total_vendas,
    COALESCE(SUM(c.valor_comissao), 0) AS total_comissao
FROM funcionarios f
LEFT JOIN vendas v ON v.funcionario_id = f.id
LEFT JOIN comissoes c ON c.venda_id = v.id
GROUP BY f.id, f.nome
ORDER BY total_comissao DESC;
"""
