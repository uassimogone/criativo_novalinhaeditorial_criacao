# DECISÕES DO PROJETO

## 2026-09-21

- Marca pessoal será ampliada para além do Direito.
- Direito continua como pilar de autoridade, não como prisão editorial.
- Vídeos longos de YouTube não são prioridade.
- Conteúdo curto e carrosséis são o foco inicial.
- Carrossel ideal: 5 slides; máximo: 7.
- Pelo menos 1–2 slides devem ter força visual real.
- Aprovação das pautas será feita no ChatGPT.
- Não haverá ingestão de comandos via Telegram nesta fase.
- Radar entrega pautas aos sábados.
- Criação fica em repositório separado.
- Visual inicial gerado foi rejeitado.
- Referências visuais principais aprovadas: Forbes + Tio Huli.
- O carrossel da Pauta 1 foi aprovado como protótipo editorial.
- A versão final visual da Pauta 1, em Editorial Fotográfico Escuro, foi aprovada como referência de qualidade.
- O visual da Pauta 1 NÃO será template único para as demais pautas.
- O sistema deve trabalhar com famílias visuais e variar conforme o assunto.
- Famílias aprovadas: Editorial Fotográfico Escuro; Minimalista Tipográfico; Editorial Claro/Revista; Comparação Visual; Fotografia Protagonista; Dado/Diagrama Editorial.
- Identidade deve vir de qualidade editorial, tipografia, hierarquia, margens, assinatura, paleta e tese — não da repetição de layout.
- O pipeline pode usar imagens reais licenciadas quando adequadas e fallback minimalista quando não houver imagem boa.
- O criativo aprovado no ChatGPT só deve ser enviado ao Telegram quando o pipeline do repositório conseguir reproduzir o padrão aprovado; não disparar o renderer provisório.
- Próxima prioridade técnica: substituir o renderer provisório por pipeline visual com seleção de família + imagens reais/licenciadas e/ou geração fotográfica.
- Depois de estabilizar a criação, construir repositório separado de publicação automática para carrosséis e posts estáticos.
- Vídeos continuam com gravação/publicação manual.

- Implementado pipeline principal de fotografia gerada com Gemini API; Wikimedia Commons fica como fallback.
- Revisão visual v3 das Pautas 1–4 concluída com sucesso.
- Publicador de carrosséis implementado no repositório frasesepensamentos_publicador, em pipeline isolado do Stories.
- Fonte operacional do publicador: pacotes READY_TO_PUBLISH no repositório de criação; Telegram permanece para revisão humana.
- Publicação automática exige flag aprovado=true; itens coletados entram sempre como aprovado=false.

- Horário oficial de publicação automática: 07:00 de Brasília, com no máximo 1 conteúdo por dia.

## 2026-09-22 — redefinição visual

- Carrossel deve ser entregue como slides/arquivos separados; é proibido entregar uma única imagem com vários slides em grade ou montagem.
- O radar, a aprovação e a criação final passam a acontecer no ChatGPT.
- GitHub fica orientado a ingestão, fila, status, histórico e publicação; o renderer automatizado não é a fonte preferencial da arte final.
- Prioridade visual: fotografia real/documental/editorial forte > minimalismo tipográfico > imagem gerada por IA.
- IA visual deve ser exceção, usada quando houver justificativa conceitual e sem aparência genérica.
- O feed não deve ser recheado de imagens de IA.
- Imagem real deve ter função editorial e relação concreta com a pauta; não usar foto apenas para preencher espaço.
- Evitar banco de imagem corporativo clichê: reuniões genéricas, handshake, laptop/café, pessoas apontando gráficos, corredores, balança, martelo e equivalentes.
- Nas referências, sans bold sobre fotografia funciona para notícia/análise; serif de alta presença funciona melhor para reflexão/citação/tese premium.
- Reduzir adornos editoriais artificiais, microcopy decorativa, selos e marcas gráficas sem função.
- Posts tipográficos minimalistas continuam aprovados, mas são a solução básica; pautas com imagem exigem curadoria e direção de arte superiores.
- Pauta 4 visual entregue em montagem única foi rejeitada e não deve ser publicada.
- Pauta 4 deve ser refeita em cinco arquivos separados e com pesquisa de imagens reais como primeira opção.


## 2026-09-22 — ampliação das referências visuais

- Novo lote de referências confirmou que a marca pode variar bastante de linguagem visual sem perder identidade.
- Não buscar um “estilo único” para todas as peças; buscar consistência de qualidade, tipografia, hierarquia, tratamento e tese.
- Passam a ser referências válidas, conforme a pauta: capa tipográfica; foto documental; foto histórica/cultural; foto de objeto/produto/edifício real; montagem noticiosa; contraste visual; lifestyle documental.
- Uma obra de arte ou fotografia histórica pode ser usada quando carregar significado diretamente relacionado à tese.
- Montagens e composições gráficas são permitidas em notícias/negócios quando explicam uma disputa ou transformação; não devem virar padrão.
- Lifestyle deve parecer vivido/documental, não ensaio publicitário.
- Referências políticas serão usadas somente para linguagem visual/composição, sem importar automaticamente a opinião ou tese política da peça original.
- Regra consolidada: naturalidade e especificidade da imagem têm prioridade sobre uniformidade estética.


## 2026-09-22 — fluxo oficial de publicação

- Fluxo oficial: Radar → aprovação no ChatGPT → criação final no ChatGPT → envio dos arquivos finais para o GitHub → fila de publicação → Instagram.
- Não haverá uma segunda aprovação editorial dentro da fila do GitHub.
- O conteúdo só entra na fila depois de estar finalizado e validado no ChatGPT.
- A fila é operacional: organiza, agenda, registra status e entrega ao publicador.
- Carrosséis devem entrar na fila com cada slide como arquivo independente.
- O GitHub não deve recriar ou reinterpretar o criativo final recebido do ChatGPT.


## 2026-09-22 — implementação do publicador no fluxo oficial

- Removida a coleta automática de pacotes do renderer antigo para a Nova Linha Editorial.
- Removido o workflow do coletor da Nova Linha Editorial.
- Fila antiga/rejeitada foi zerada.
- Conteúdo final enviado pelo ChatGPT entra diretamente como `QUEUED`, sem segunda aprovação.
- Destino padrão dos arquivos: `queue/novalinha/<id>/`.
- Publicador suporta carrossel (2–7 slides independentes) e post estático (1 arquivo).
- Publicação automática permanece às 07:00 de Brasília.
- O código bloqueia mais de uma publicação da Nova Linha Editorial no mesmo dia.
- Estados operacionais: `QUEUED`, `PUBLISHED`, `ERROR`.
- O pipeline de Stories existente permanece separado e preservado.


## 2026-09-22 — organização semanal dos chats

- Cada semana será tratada em um chat novo.
- Criado `docs/STATUS_ATUAL.md` como ponto de entrada operacional para novos chats.
- Em novos chats, consultar STATUS_ATUAL, MASTER_CONTEXT, DECISOES, MANUAL_VISUAL e fila do publicador antes de iniciar o trabalho.
- O usuário não deve precisar reexplicar decisões, estilo, fluxo ou estado da produção.
- STATUS_ATUAL deve ser atualizado no encerramento de cada semana.


## 2026-09-22 — agendamento por data

- Pauta 2 foi publicada manualmente em 22/09/2026.
- Pauta 1 será publicada manualmente em 23/09/2026.
- Pauta 3 foi aprovada visualmente e tem intenção de publicação em 24/09/2026 às 07:00.
- O publicador passou a exigir `scheduled_for` em cada item da fila.
- Um item `QUEUED` só é elegível quando sua data/hora programada já chegou.
- O workflow permanece diário às 07:00 de Brasília.
- A existência de intenção de data não equivale a agendamento efetivo: o item precisa estar gravado na fila com seus arquivos finais.


## 2026-09-22 — Pauta 3 aprovada e agendada

- Pauta 3 aprovada pelo usuário.
- Legenda final registrada junto ao item.
- Publicação automática agendada para 24/09/2026 às 07:00 de Brasília.
- Status operacional no publicador: `QUEUED`.
- Pacote final contém 5 slides.
- Slide 1 usa fotografia real de vaca no pasto, fonte Wikimedia Commons, obra de Gerda Arendt em CC0 1.0.
- Slides 2–5 são composições tipográficas/editoriais, sem fotografia de IA.
- Regra visual reforçada: fotografia real sempre que houver imagem; IA visual apenas quando não existir alternativa real adequada.


## 2026-09-22 — Pauta 4 aprovada e agendada

- Pauta 4 aprovada pelo usuário com o pacote visual já existente.
- Legenda final registrada.
- Publicação automática agendada para 25/09/2026 às 18:00 de Brasília.
- Status operacional no publicador: `QUEUED`.
- O workflow do publicador passou a ter também uma janela às 18:00 de Brasília.
- O publicador passou a aceitar assets remotos do repositório de criação, evitando duplicação desnecessária de arquivos binários.


## 2026-09-22 — GitHub como agenda de publicação

- Publicações da Nova Linha Editorial não usarão mais automações do ChatGPT.
- A agenda oficial fica no campo `scheduled_for` da fila do GitHub.
- Conteúdo aprovado deve ser inserido diretamente no GitHub assim que ficar pronto.
- O GitHub Actions é responsável por verificar a fila e publicar quando chegar a data/hora.
- O ChatGPT atua apenas na criação, aprovação e envio do pacote final ao GitHub.


## 2026-09-24 — prioridade de dias e formatos da semana 05/10 a 11/10

- Segunda, sexta e sábado são, em regra, os dias de pautas mais fortes e devem ser preferencialmente reservados para vídeos. Segunda 05/10 é exceção aprovada como carrossel.
- Segunda 05/10: carrossel sobre presidente, Congresso e regras que afetam a vida cotidiana.
- Terça 06/10: carrossel sobre empresa que vende muito e fica sem dinheiro.
- Quarta 07/10: carrossel sobre limites da dívida da empresa e responsabilidade do sócio.
- Quinta 08/10: post estático com legenda forte sobre desconto sem cálculo de custo e margem; transferido da proposta original de sexta.
- Sexta 09/10: vídeo sobre saber conferir e explicar a resposta da IA; transferido da proposta original de quinta.
- Sábado 10/10: vídeo sobre o trabalho que invade a casa e a convivência com os filhos; transferido da proposta original de domingo.
- Domingo 11/10: proposta de vídeo reflexivo sobre declarações dos líderes de empresas de IA a respeito de riscos catastróficos/existenciais. Exige apuração de fontes e validação do enquadramento por Uassi antes do roteiro.
- Descartada a pauta “Se o dono precisa decidir tudo, a empresa tem um limite de crescimento”.
- Esta grade é editorial; nenhum item entra na fila de publicação sem a criação e validação do conteúdo final.


## 2026-09-24 — revisão da quinta-feira 08/10

- Uassi considerou fraca e descartou a pauta “Desconto sem fazer a conta pode transformar venda em prejuízo”.
- A quinta-feira permanece em aberto para post estático com legenda forte, preferencialmente sobre valores e lifestyle. Não criar ou enfileirar a pauta anterior.


## 2026-09-24 — quinta-feira 08/10 definida

- Uassi escolheu a opção 1 para quinta-feira: “Nem tudo o que você gosta precisa virar meta.”
- Formato: post estático com legenda forte. Pilar: valores e lifestyle.
- Abordagem: hobbies, esporte, leitura ou interesses feitos pelo prazer da experiência, sem obrigação de transformá-los em desempenho, negócio ou conteúdo. Não atribuir a Uassi relato pessoal não validado.


## 2026-09-24 — segunda 05/10: texto validado e prévia visual produzida

- Uassi aprovou texto e direção de arte de seis slides para a pauta sobre Congresso Nacional, com alteração específica no slide 2: fotografia real de urna eletrônica.
- Sequência final de trabalho: capa Congresso; slide 2 seis escolhas e foto de urna; slide 3 deputados/senadores e leis; slide 4 fiscalização e sabatina pelo Senado com retratos de Lula e Alexandre de Moraes identificados por poder; slide 5 consequências duradouras; slide 6 acompanhar e cobrar representantes com foto real de manifestação.
- Foram produzidas prévias PNG separadas e legenda com cinco hashtags. Material aguarda revisão visual de Uassi. Não foi enfileirado nem agendado.


## 2026-09-24 — revisão do slide 2 da pauta de segunda

- Uassi rejeitou a primeira composição do slide 2: numeral 6 isolado e desproporcional distorceu o conteúdo.
- Nova prévia usa “são seis escolhas” em serifa editorial como manchete, mantém fotografia real de urna e reserva o fecho “Presidente é a última” à área da foto. O numeral gigante foi removido, sem esticar ou deformar a fonte.
- Slide 2 revisado aguarda avaliação; slides 1 e 3–6 mantidos. Sem agendamento/publicação.


## 2026-09-24 — agendamento de segunda 05/10 informado pelo usuário

- Uassi confirmou que já agendou a pauta sobre Congresso. Considerar a publicação agendada por ele e evitar duplicação.
- Não foram informados plataforma, horário nem qual versão do slide 2 foi usada; a confirmação não equivale a registro de envio pelo ChatGPT à fila do GitHub.
