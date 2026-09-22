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
- Pauta 3: criativo aprovado; intenção de publicação em 24/09/2026 às 07:00. O publicador já suporta scheduled_for, mas o envio dos arquivos finais à fila ainda precisa ser concluído para o agendamento ficar efetivo.
- Pauta 4: pendente de produção/refação.
- Pauta 5: pendente de roteiro + texto para teleprompter.
- fila atual: vazia;
- itens QUEUED: 0.

A fila só passa a representar um agendamento efetivo quando os arquivos finais estiverem no GitHub e o item correspondente constar como QUEUED com scheduled_for.

## 7. AUTOMAÇÕES ATIVAS RELACIONADAS

- Radar editorial: sábado às 06:00 de Brasília.
- Publicador da Nova Linha Editorial: diariamente às 07:00 de Brasília.
- Regra do publicador: máximo de 1 conteúdo por dia, somente itens QUEUED e somente quando scheduled_for já tiver chegado.
