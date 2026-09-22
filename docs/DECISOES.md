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
