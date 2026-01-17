import json

def lambda_handler(event, context):
    """
    Simula o processamento de um pedido na farmácia.
    """
    # 1. Recebe os dados do pedido (Simulado)
    nome_produto = event.get('produto', 'Medicamento Genérico')
    preco_base = event.get('preco', 0.0)
    
    # 2. Lógica de negócio: Desconto para compras acima de R$ 100
    if preco_base > 100.0:
        desconto = 0.10  # 10% de desconto
        preco_final = preco_base * (1 - desconto)
        mensagem = f"Desconto de 10% aplicado ao produto: {nome_produto}"
    else:
        preco_final = preco_base
        mensagem = "Preço mantido (sem descontos aplicáveis)."

    # 3. Retorno para o sistema de checkout
    return {
        'statusCode': 200,
        'body': json.dumps({
            'produto': nome_produto,
            'preco_original': preco_base,
            'preco_final': round(preco_final, 2),
            'status': mensagem
        })
    }
