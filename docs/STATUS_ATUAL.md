# STATUS ATUAL — NOVA LINHA EDITORIAL

Atualizado em: 2026-09-22

Este arquivo é o ponto de entrada operacional para qualquer novo chat semanal.

## 1. FLUXO OFICIAL

Radar → aprovação no ChatGPT → criação final no ChatGPT → envio dos arquivos finais para o GitHub → fila de publicação → Instagram.

## 2. RITMO SEMANAL

### Sábado
- Radar editorial às 06:00 de Brasília.
- Seleção de até 5 pautas.
- Novo chat da semana é aberto para análise, aprovação, rejeição e ajustes das pautas.

### Sábado / Domingo
- Definição dos formatos.
- Desenvolvimento dos textos, teses, roteiros e direção visual.
- Curadoria de imagens reais quando necessário.

### Domingo / Segunda
- Criação final dos carrosséis e posts estáticos no ChatGPT.
- Cada slide de carrossel é entregue como arquivo independente.
- Após validação final no ChatGPT, os arquivos são enviados ao GitHub e entram na fila como QUEUED.

### Durante a semana
- O publicador roda diariamente às 07:00 de Brasília.
- Publica no máximo 1 conteúdo da Nova Linha Editorial por dia.
- O primeiro item QUEUED é publicado.
- Vídeos permanecem manuais.

### Encerramento da semana
- Atualizar este STATUS_ATUAL.
- Registrar decisões relevantes em docs/DECISOES.md.
- Atualizar docs/MASTER_CONTEXT.md quando houver mudança estrutural, editorial ou operacional.

## 3. REGRA PARA NOVO CHAT

Ao iniciar um novo chat semanal, consultar nesta ordem:
1. docs/STATUS_ATUAL.md
2. docs/MASTER_CONTEXT.md
3. docs/DECISOES.md
4. docs/MANUAL_VISUAL.md
5. fila do publicador: database/novalinha_posts.json

O usuário não precisa reexplicar o projeto.

## 4. ESTADO EDITORIAL ATUAL

Pautas aprovadas em 2026-09-21:
1. CARROSSEL — A ilusão da produtividade com IA: menos horas prometidas, 90 horas entregues.
2. CARROSSEL — A decisão de RH que sua empresa toma hoje e vira execução judicial amanhã.
3. CARROSSEL — Discutir redução de jornada sem falar de produtividade é conversa para boi dormir.
4. CARROSSEL — Por que o agro forte de MT está virando tijolo em Santa Catarina.
5. VIDEO_CURTO — Estar ocupado o dia todo não é sinal de competência, é sintoma de falta de método.

## 5. ESTADO VISUAL / PRODUÇÃO

- O antigo lote automático v3 das Pautas 1–4 foi retirado da fila de publicação.
- A Pauta 4 teve sua composição visual explicitamente rejeitada e precisa ser refeita.
- O renderer automático não é mais fonte da arte final.
- A criação final visual ocorre no ChatGPT.
- Prioridade: fotografia real/documental específica → tipografia → IA apenas excepcionalmente.
- Pauta 1 permanece como referência de qualidade visual/editorial, não como template obrigatório.

## 6. PUBLICAÇÕES E FILA

Estado em 2026-09-22:
- Pauta 2: publicada manualmente em 22/09/2026.
- Pauta 1: publicação manual planejada para 23/09/2026.
- Pauta 3: APROVADA e efetivamente agendada no GitHub para 24/09/2026 às 07:00 de Brasília. Cinco arquivos finais estão na fila; slide 1 usa fotografia real CC0 do Wikimedia Commons; slides 2–5 são tipográficos. Legenda registrada. Status: QUEUED.
- Pauta 4: APROVADA e efetivamente agendada para 25/09/2026 às 18:00 de Brasília. Pacote final já existente foi reutilizado; legenda registrada. Status: QUEUED.
- Pauta 5: roteiro e texto para teleprompter finalizados; gravação pelo usuário prevista para 22/09/2026. Após gravação, falta apenas legenda final e definição de publicação.
- fila atual: 2 itens;
- itens QUEUED: 2 (Pauta 3 — 24/09/2026 às 07:00; Pauta 4 — 25/09/2026 às 18:00).

A Pauta 3 já cumpre os requisitos de agendamento efetivo: arquivos finais no GitHub + status QUEUED + scheduled_for.

## 7. AUTOMAÇÕES ATIVAS RELACIONADAS

- Radar editorial: sábado às 06:00 de Brasília.
- Publicador da Nova Linha Editorial: diariamente às 07:00 de Brasília.
- Regra do publicador: máximo de 1 conteúdo por dia, somente itens QUEUED e somente quando scheduled_for já tiver chegado.


## REGRA OPERACIONAL DE AGENDAMENTO

- Não usar tarefas do ChatGPT para publicações da Nova Linha Editorial.
- Todo conteúdo aprovado entra diretamente no GitHub com `scheduled_for`.
- O GitHub Actions é o único mecanismo de disparo automático para o Instagram.

- Post de domingo (“Parabéns é depois. Apoio é durante.”): arte e legenda aprovadas; publicação será manual pelo usuário em 27/09/2026 às 13:30. Não inserir na fila automática do GitHub.


## 8. PLANEJAMENTO EM CURSO — 05/10 A 11/10/2026 (2026-09-24)

Preferência permanente: segunda, sexta e sábado concentram as pautas mais fortes e, via de regra, ficam reservados a vídeos curtos gravados manualmente. Exceções são decididas por Uassi.

Grade definida em conversa, pendente de criação final:
- 05/10 segunda: carrossel — presidente, Congresso e regras do jogo (exceção à preferência de vídeo).
- 06/10 terça: carrossel — vender muito e ficar sem dinheiro.
- 07/10 quarta: carrossel — dívida da empresa e responsabilidade do sócio.
- 08/10 quinta: post estático + legenda forte — desconto sem calcular margem.
- 09/10 sexta: vídeo — conferir e explicar respostas da IA.
- 10/10 sábado: vídeo — trabalho que entra em casa e convivência com os filhos.
- 11/10 domingo: vídeo proposto — por que líderes de empresas de IA alertam para riscos existenciais; apurar declarações e validar tese pessoal antes do roteiro.

Pauta descartada: “Se o dono precisa decidir tudo, a empresa tem um limite de crescimento”. Esta grade não equivale a criativos finalizados nem a agendamentos na fila.


## Ajuste da quinta-feira — 2026-09-24

A pauta de 08/10 sobre desconto e margem foi descartada. Quinta permanece em aberto para escolha de pauta de valores/lifestyle, em formato post estático com legenda forte. As demais escolhas da semana permanecem como planejamento editorial.


## Quinta-feira 08/10 definida — 2026-09-24

Post estático com legenda forte: “Nem tudo o que você gosta precisa virar meta.” Tema escolhido por Uassi após descartar a pauta de desconto e margem. A arte e a legenda ainda serão produzidas; não há item enfileirado para esta data.


## Produção de segunda 05/10 — 2026-09-24

Texto e direção de arte de seis slides validados por Uassi, com foto de urna no slide 2. Seis PNGs individuais, prévia conjunta e legenda/créditos produzidos para revisão visual. Estado: AVALIAÇÃO VISUAL; sem status QUEUED e sem agendamento. Não enviar ao publicador antes do feedback sobre o pacote final.


## Revisão visual do slide 2 — 2026-09-24

O primeiro slide 2 foi rejeitado por desproporção do numeral 6. Nova versão com serifa editorial e fotografia real de urna produzida e disponibilizada, aguardando feedback. Os outros cinco slides não mudaram. A pauta segue fora da fila de publicação.


## Confirmação de agendamento de segunda 05/10 — 2026-09-24

Uassi informou que já agendou a pauta do carrossel sobre Congresso. Registrar como AGENDADA PELO USUÁRIO. A plataforma, o horário, a versão final utilizada e o estado da fila do GitHub não foram informados nesta conversa; não presumir que houve inclusão pelo ChatGPT na fila. Não agendar novamente sem solicitação expressa. As notas anteriores de avaliação visual e ausência de agendamento descrevem apenas o estado antes desta confirmação.


## Revisão da pauta de terça 06/10 — 2026-09-24

Uassi descartou a pauta de fluxo de caixa/vendas. Nova proposta editorial: carrossel de sete slides sobre por que os irmãos Joesley e Wesley Batista negociaram a aquisição da estrutura operacional da Avibras apesar da crise e das dívidas históricas. Texto em elaboração e sujeito à aprovação expressa antes de criar arte ou legenda. Precisão factual: a compra anunciada é de 100% da Nova AVB, controladora da Avibras Aeroco, via Globe Investimentos; a antiga Avibras Indústria Aeroespacial permanece em recuperação judicial. A referência a mais de R$ 394 milhões deve ser contextualizada como dívida histórica atribuída à empresa antiga, não como passivo atual integralmente assumido pelo comprador; há fontes com cifras distintas. Patentes específicas ainda sem confirmação documental. Nenhum criativo ou agendamento desta pauta.


## Direção de arte e fechamento da terça 06/10 — 2026-09-24

Uassi pediu fechamento mais objetivo e impactante, com mensagem de que nos negócios cada detalhe importa. Exigiu fotografia real em todos os sete slides: slide 1 Avibras; slide 2 outra foto da empresa; slide 3 Joesley e Wesley Batista; slide 4 míssil real; slides 5 a 7 fotografia real relevante ao conteúdo. A peça continua somente em fase de texto e direção visual: não criar slides ou legenda antes de aprovação expressa do texto. Archivo Black é fonte aprovada para títulos e manchetes. Buscar imagens específicas com licença adequada antes da criação.


## Consolidação final da semana 05/10–11/10/2026 — 2026-09-24

A grade atualizada está em [PAUTA_SEMANAL_2026-10-05_A_11.md](PAUTA_SEMANAL_2026-10-05_A_11.md). Os blocos anteriores nesta seção registram etapas históricas, substituídas pela grade consolidada.

- Segunda 05/10: carrossel Congresso, agendado pelo usuário.
- Terça 06/10: carrossel Avibras, sete slides com fotos reais, produzido e agendado pelo usuário. Não agendar novamente; plataforma e horário não informados.
- Quarta 07/10: responsabilidade do sócio por dívida da empresa, carrossel pendente de desenvolvimento.
- Quinta 08/10: “Nem tudo o que você gosta precisa virar meta”, post estático + legenda forte pendentes.
- Sexta 09/10: explicação das respostas da IA, vídeo pendente.
- Sábado 10/10: trabalho que invade a casa e convivência com filhos, vídeo pendente.
- Domingo 11/10: reflexão sobre alertas de riscos extremos da IA, vídeo pendente de apuração e tese.
