import os
import json
from decimal import Decimal

from db import get_connection
from queries import (
    LISTAR_FUNCIONARIOS,
    INSERIR_FUNCIONARIO,
    INSERIR_VENDA,
    INSERIR_COMISSAO,
    RELATORIO_VENDAS,
    RELATORIO_COMISSOES
)

# =========================
# UTILITÁRIOS
# =========================

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\n🔎 Pressione ENTER para continuar...")


def validar_int_positivo(valor):
    valor = int(valor)
    if valor <= 0:
        raise ValueError("Digite um número inteiro positivo.")
    return valor


def validar_float_positivo(valor):
    valor = float(valor)
    if valor < 0:
        raise ValueError("Digite um valor maior ou igual a zero.")
    return valor


# =========================
# FUNCIONÁRIOS
# =========================

def listar_funcionarios():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(LISTAR_FUNCIONARIOS)
    funcionarios = cursor.fetchall()

    print("\n📋 FUNCIONÁRIOS\n")
    for f in funcionarios:
        print(
            f"ID: {f['id']} | "
            f"Nome: {f['nome']} | "
            f"Cargo: {f['cargo']} | "
            f"Comissão: {f['percentual_comissao']}%"
        )

    cursor.close()
    conn.close()


def cadastrar_funcionario():
    nome = input("Nome: ").strip()
    cargo = input("Cargo: ").strip()
    percentual = validar_float_positivo(
        input("Percentual de comissão (%): ")
    )

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        INSERIR_FUNCIONARIO,
        (nome, cargo, percentual)
    )

    funcionario_id = cursor.fetchone()["id"]
    conn.commit()

    print(f"\n✅ Funcionário cadastrado com ID {funcionario_id}")

    cursor.close()
    conn.close()


# =========================
# VENDAS
# =========================

def cadastrar_venda():
    carro_id = validar_int_positivo(input("ID do carro: "))
    comprador_id = validar_int_positivo(input("ID do comprador: "))
    funcionario_id = validar_int_positivo(input("ID do vendedor: "))
    forma_pagamento_id = validar_int_positivo(
        input("ID da forma de pagamento: ")
    )

    valor_venda = validar_float_positivo(
        input("Valor da venda: ")
    )
    percentual_desconto = validar_float_positivo(
        input("Percentual de desconto (%): ")
    )
    percentual_comissao = validar_float_positivo(
        input("Percentual de comissão (%): ")
    )

    conn = get_connection()
    cursor = conn.cursor()

    # Inserir venda
    cursor.execute(
        INSERIR_VENDA,
        (
            carro_id,
            comprador_id,
            funcionario_id,
            forma_pagamento_id,
            valor_venda,
            percentual_desconto
        )
    )

    venda_id = cursor.fetchone()["id"]

    # Calcular comissão
    valor_liquido = valor_venda - (valor_venda * percentual_desconto / 100)
    valor_comissao = valor_liquido * (percentual_comissao / 100)

    cursor.execute(
        INSERIR_COMISSAO,
        (venda_id, valor_comissao)
    )

    conn.commit()

    print(f"\n✅ Venda registrada (ID {venda_id})")
    print(f"💰 Comissão: R$ {valor_comissao:.2f}")

    cursor.close()
    conn.close()


# =========================
# RELATÓRIOS
# =========================

def relatorio_vendas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(RELATORIO_VENDAS)
    vendas = cursor.fetchall()

    print("\n📊 RELATÓRIO DE VENDAS\n")

    for v in vendas:
        print(
            f"Venda #{v['venda_id']} | "
            f"{v['marca']} {v['modelo']} | "
            f"Vendedor: {v['vendedor']} | "
            f"Valor: R$ {v['valor_venda']:,.2f}"
        )

    cursor.close()
    conn.close()


def relatorio_vendas_json():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(RELATORIO_VENDAS)
    vendas = cursor.fetchall()

    print(
        json.dumps(
            vendas,
            indent=4,
            ensure_ascii=False,
            default=lambda x: float(x) if isinstance(x, Decimal) else x
        )
    )

    cursor.close()
    conn.close()


def relatorio_comissoes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(RELATORIO_COMISSOES)
    comissoes = cursor.fetchall()

    print("\n💰 RELATÓRIO DE COMISSÕES\n")
    for c in comissoes:
        print(
            f"Vendedor: {c['vendedor']} | "
            f"Vendas: {c['total_vendas']} | "
            f"Comissão Total: R$ {c['total_comissao']:,.2f}"
        )

    cursor.close()
    conn.close()


# =========================
# MENU PRINCIPAL
# =========================

def menu():
    while True:
        limpar_tela()

        print("==============================")
        print("🚗 SISTEMA DA CONCESSIONÁRIA")
        print("==============================")
        print("1 - Listar funcionários")
        print("2 - Cadastrar funcionário")
        print("3 - Cadastrar venda")
        print("4 - Relatório de vendas")
        print("5 - Relatório de vendas (JSON)")
        print("6 - Relatório de comissões")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        try:
            if opcao == "1":
                listar_funcionarios()
                pausar()

            elif opcao == "2":
                cadastrar_funcionario()
                pausar()

            elif opcao == "3":
                cadastrar_venda()
                pausar()

            elif opcao == "4":
                relatorio_vendas()
                pausar()

            elif opcao == "5":
                relatorio_vendas_json()
                pausar()

            elif opcao == "6":
                relatorio_comissoes()
                pausar()

            elif opcao == "0":
                print("\n👋 Encerrando sistema.")
                break

            else:
                print("\n❌ Opção inválida.")
                pausar()

        except Exception as e:
            print(f"\n❌ Erro: {e}")
            pausar()


# =========================
# START
# =========================

if __name__ == "__main__":
    menu()
