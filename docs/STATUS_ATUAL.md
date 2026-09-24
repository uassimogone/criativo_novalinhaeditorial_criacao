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
