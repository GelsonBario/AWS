# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS
### Data: 17/01/2026 Empresa: Farmácia Vida & Saúde (Fictícia) Responsável: Gelson Bario

### Introdução
. Este relatório apresenta o processo de implementação de ferramentas na empresa Farmácia Vida & Saúde, realizado por Gelson. O objetivo do projeto foi elencar 3 serviços AWS com a finalidade de realizar a migração de servidores locais para a nuvem, focando na diminuição de custos operacionais e alta disponibilidade.

Etapa 1: AWS Lambda (Processamento Serverless de Pedidos)
Ferramenta: AWS Lambda.

Foco da ferramenta: Execução de lógica de negócio orientada a eventos com custo zero em tempo ocioso.

Descrição de caso de uso: A implementação utiliza uma função Lambda escrita em Python para processar as regras de negócio da farmácia no momento do checkout. O script atua da seguinte forma:

Gatilho (Trigger): É acionado via API Gateway sempre que um cliente finaliza uma compra.

Lógica: O código verifica o valor total do carrinho; se exceder R$ 100,00, aplica automaticamente um desconto de 10% antes de enviar o valor para o processador de pagamentos.

Eficiência de Custo: Diferente de um servidor tradicional que cobraria pela disponibilidade 24/7, o Lambda cobra apenas pelos milissegundos de execução do script. Para uma farmácia com picos de acesso (como períodos de promoção), isso elimina o custo de manter servidores superdimensionados para momentos de baixa demanda.

Exemplo entrada (JSON):
{
  "produto": "Vitamina C",
  "preco": 120.00
}

Exemplo saida (JSON):
{
  "statusCode": 200,
  "body": {
    "produto": "Vitamina C",
    "preco_original": 120.00,
    "preco_final": 108.00,
    "status": "Desconto de 10% aplicado ao produto: Vitamina C"
  }
}

Etapa 2: Amazon S3 (Armazenamento de Dados e Receitas Digitais)
Ferramenta: Amazon S3 (Simple Storage Service).

Foco da ferramenta: Armazenamento de objetos com alta durabilidade, escalabilidade e gerenciamento de ciclo de vida.

Descrição de caso de uso: A farmácia lida com um grande volume de imagens de produtos e, principalmente, fotos de receitas médicas enviadas pelos clientes para validação.

Organização em Camadas (Tiering): Arquivos de acesso frequente (fotos do site) ficam na camada Standard. Receitas médicas, que precisam ser guardadas por motivos legais mas raramente são acessadas após a venda, são movidas automaticamente para o S3 Glacier após 30 dias.

Segurança e Conformidade: Utilização de criptografia de ponta a ponta e políticas de acesso (IAM) para garantir que apenas farmacêuticos autorizados visualizem as receitas, atendendo a normas de proteção de dados.

Redução de Custos: Ao mover arquivos antigos para o Glacier, o custo de armazenamento cai drasticamente (até 90% de economia por GB), permitindo que a empresa mantenha um histórico imenso de documentos sem sobrecarregar o orçamento.
"Configurada regra de ciclo de vida para mover objetos do prefixo receitas/ para a classe GLACIER_INSTANT_RETRIEVAL após 90 dias de criação, otimizando o custo de armazenamento de longo prazo."

Etapa 3: AWS Budgets & Cost Explorer (Governança e Controle Financeiro)
Ferramenta: AWS Budgets.

Foco da ferramenta: Monitoramento proativo de custos e previsão de gastos.

Descrição de caso de uso: Para evitar surpresas na fatura mensal da farmácia, foram implementados mecanismos de controle financeiro:

Criação de Alertas: Configuramos um orçamento mensal de (exemplo) $50.00 USD. Caso o gasto real ou a previsão de gastos atinja 80% desse valor, um alerta automático é enviado por e-mail para o responsável pelo projeto.

Visibilidade com Cost Explorer: A ferramenta permite visualizar quais serviços estão consumindo mais recursos (ex: processamento do Lambda vs. armazenamento do S3), facilitando ajustes finos na arquitetura para manter o custo baixo.

Benefício Imediato: Garante a previsibilidade financeira da empresa, permitindo que a farmácia escale seus serviços na nuvem de forma sustentável e segura, sem riscos de ultrapassar o orçamento aprovado pela diretoria.

Conclusão
A implementação de ferramentas na empresa Farmácia Vida & Saúde tem como esperado uma redução de custos operacionais em até 60% e a eliminação total de gastos com hardware físico, o que aumentará a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias, como o AWS CloudFront, para melhorar ainda mais o tempo de carregamento do site em diferentes regiões.
