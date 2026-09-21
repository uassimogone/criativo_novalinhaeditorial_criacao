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
