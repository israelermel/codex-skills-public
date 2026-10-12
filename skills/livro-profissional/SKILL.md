---
name: livro-profissional
description: Produza livros a partir de fotos, manuscritos, PDFs ou Markdown, com revisão editorial e aprovação do autor. Inclui EPUB Kindle, miolo e capas de impressão, ilustrações, audiobook em português brasileiro, vídeo e legendas/textos para YouTube e cadastro/publicação de eBook no Amazon KDP. Não acione para revisão avulsa de mensagens sem finalidade de livro.
---

# Livro profissional

Conduza uma produção editorial com participação do autor. Preserve sua voz, organize uma fonte textual única e entregue arquivos verificáveis para os formatos solicitados. Esta skill orienta o trabalho; geração de imagem, voz e vídeo depende das ferramentas realmente disponíveis.

## Começar ou retomar

1. Leia as instruções do projeto, o registro de produção, as aprovações e os arquivos atuais antes de fazer perguntas. Não presuma que todas as etapas precisam ser refeitas.
2. Identifique fontes originais, transcrição, manuscrito vigente e derivados. Data de modificação ou nome “final” não comprova aprovação. Em divergências, use a decisão mais recente do autor e registre a escolha.
3. Confirme somente lacunas relevantes à etapa: título/autor, público, gênero, intensidade da revisão e entregas desejadas. Dados de gráfica são necessários ao fechamento técnico, não para começar a revisão.
4. Para produção nova, adapte [o registro de produção](assets/producao-template.md) em `~/.Codex/specs/<slug-especifico-do-livro>/producao.md`. Atualize `spec_location.md` no projeto e na memória do projeto quando disponível, preservando referências existentes. Se já houver registro, atualize-o em vez de criar outro concorrente.
5. Trabalhe apenas no escopo pedido. Criar esta skill não inicia a revisão nem a regeneração de um livro existente. Pedir somente uma capa ou correção não autoriza produzir todos os formatos.

Para aproveitar a experiência que originou esta skill, consulte [as lições do projeto](references/licoes-do-projeto.md). Os caminhos e números desse caso são referências históricas, não dependências para novos livros.

## Aprovação do autor

Por padrão, use a sequência abaixo. Um pedido atual explícito pode alterar a ordem ou dispensar uma aprovação específica; registre isso. Não interprete “faça tudo” como dispensa automática das revisões do autor.

| Etapa | Material que o autor recebe | Condição para continuar |
|---|---|---|
| Transcrição e revisão editorial | Markdown revisado, parecer, mudanças relevantes e dúvidas localizadas | Aprovação do texto e resolução das dúvidas que afetam seu sentido |
| Capa | Frente Kindle, estudo de contracapa/lombada e prova legível | Aprovação do conceito e dos textos da capa |
| Ilustrações | Piloto de estilo; depois sequência de cenas com quantidade variável por capítulo | Aprovação do piloto antes do lote e do conjunto antes da montagem final |
| Projeto do miolo e EPUB | Amostra diagramada e provas dos formatos solicitados | Aprovação da prova e conferência técnica antes de fechar a edição |
| Narração | Amostra de 60–90 segundos com a voz escolhida e direção expressiva | Aprovação da voz, ritmo, pronúncias e interpretação antes do lote |
| Vídeo ilustrado | Trecho piloto com áudio, imagens e títulos; efeitos somente quando pedidos | Aprovação antes de renderizar a edição integral |
| Textos para YouTube | Título, descrição final, capítulos e créditos prontos para colar | Aprovação dos textos; envio ao canal depende do pedido do autor |
| Cadastro do eBook no KDP | Descrição comercial e todos os textos/campos aplicáveis, com arquivos e decisões de publicação | Aprovação do pacote; submissão depende do pedido do autor |

Depois de texto → capa → ilustrações, a diagramação e a amostra de voz podem avançar conforme o pedido; a montagem final do vídeo depende das ilustrações e do áudio aprovados. A capa aberta só se torna final depois da paginação final do miolo.

Em cada ponto de aprovação:

- Termine todo o trabalho autorizado que torna a decisão concreta. Mostre links/arquivos, versão, o que mudou e pendências, com imagens e áudio reproduzíveis quando aplicável.
- Faça uma pergunta breve, por exemplo: “Você aprova esta versão do texto ou quer ajustar algum trecho?” O autor pode responder livremente, anotar no arquivo ou usar `capítulo + trecho + alteração desejada`; nenhum formulário é obrigatório.
- Aplique as observações, apresente a versão seguinte com resumo das mudanças e repita até haver aprovação explícita. “Gostei, mas altere o final” ainda exige o ajuste; “ajuste X e pode seguir” autoriza continuar após X.
- Registre etapa, versão, caminhos, SHA-256 dos arquivos aprovados, data e a resposta real do autor. Não fabrique aprovação nem trate silêncio como consentimento. Se apenas alguns capítulos forem aprovados, mantenha o restante pendente; não declare o livro inteiro aprovado.
- Sem resposta, salve a etapa como `aguardando autor` e encerre com a pergunta. Uma skill não agenda retomadas por si só. Retome da mesma etapa quando a resposta chegar.
- A aprovação limita-se ao material apresentado. Não volte a perguntar sobre uma decisão que permanece válida. Se precisar aguardar por esta regra, identifique e vincule este `SKILL.md` e cite brevemente a instrução relevante, explicando que implementa o fluxo solicitado pelo autor.

Se o texto mudar depois de aprovado, preserve a edição anterior e avalie os derivados afetados: EPUB/PDF, paginação e lombada, roteiro, áudio, legendas e horários. Marque-os como desatualizados e regenere os dependentes. Não substitua uma capa aprovada por nova arte por causa de uma correção textual.

## Execução por etapa

### 1. Imagens e originais → Markdown → revisão

Leia [transcrição e revisão editorial](references/editorial.md). Separe `transcricao.md` fiel aos originais de `livro.md` revisado. Confira a cobertura de todas as páginas, marque ilegíveis e lacunas e preserve a rastreabilidade. Faça revisão ortográfica, gramatical, de concordância verbal/nominal, pontuação, clareza e consistência, sem descaracterizar o autor.

Entregue o parecer com o [modelo de revisão](assets/revisao-template.md). Alterações de tese, estrutura ou fatos precisam ser visíveis ao autor. Não avance à criação de capa com texto ainda aguardando aprovação, salvo autorização explícita para um estudo independente.

**Mínimo de páginas antes dos derivados:** quando a produção completa inclui livro físico no KDP, pagine um miolo provisório em formato aceito pela plataforma antes de fechar a revisão. Para brochura em preto e branco, confira o mínimo vigente de **24 páginas**; outras modalidades podem exigir mais. Se o PDF ficar abaixo do mínimo, **bloqueie o fechamento e a geração de derivados**, releia a obra e amplie automaticamente o conteúdo com cenas, desenvolvimento ou explicações pertinentes, dentro do escopo editorial autorizado. Não complete a contagem com páginas vazias, repetição ou alterações artificiais de fonte/margens. Regenere e conte o PDF até atingir o mínimo real; registre os acréscimos e siga as aprovações/dispensas válidas. Se o pedido limitar a revisão ou proibir acréscimos, respeite-o e esclareça a incompatibilidade. Consulte [a barreira de paginação](references/publicacao.md#barreira-de-paginação-para-livro-físico-no-kdp). Esse mínimo não se aplica ao EPUB Kindle.

### 2. Capa e imagens dos capítulos

**Capas com IA local — escolha de Israel em 11/10/2026:** usar por padrão o ComfyUI com Qwen Image 2.1 UC Q6_K também para gerar novas capas e estudos de renovação, conforme [o fluxo de capas locais](references/comfyui-local.md#capas-locais). Ler primeiro os briefings e registros do livro, o manuscrito e a frase de divulgação vigente. Manter acabamento realista cinematográfico, composição e legibilidade; preservar capas aprovadas até autorização de substituição. Não acionar geração de imagens do ChatGPT para capas sem pedido específico do autor. A preferência local não dispensa inspeção, aprovação nem as condições de licença já registradas.

**Geração local dos capítulos, escolha de Israel em 11/10/2026:** usar ComfyUI com o Qwen Image 2.1 UC Q6_K já existente quando a geração local for solicitada, conforme [o pipeline local](references/comfyui-local.md). Para esse fluxo, a quantidade pode superar duas ou três imagens por capítulo, conforme momentos narrativos distintos; o pedido de mais imagens substitui a faixa abaixo no fluxo local. Preservar artes aprovadas e validar um piloto antes do lote. Registrar a licença Qwen Research e a necessidade de autorização comercial separada; a escolha técnica do autor não equivale a permissão do licenciante. Não declarar instalação funcional sem teste real de geração.

Leia [capas, diagramação e formatos](references/publicacao.md). Desenvolva identidade adequada ao gênero e ao público; capa profissional exige composição, tipografia e leitura em miniatura, além de arte bonita. Use a skill/ferramenta de geração de imagem disponível quando houver criação ou edição de arte raster. Inspecione as referências antes de editá-las.

**Padrão visual das próximas capas:** use a capa de *Pedágio do Tempo* indicada por Israel em 05/10/2026 como referência de qualidade para YouTube, PDF e EPUB: arte cinematográfica de alta fidelidade, cena que desperta curiosidade com fidelidade à obra, luz e sombras com profundidade, contraste forte e título grande e legível em miniatura. Consulte [a referência e os critérios de qualidade](references/qualidade-capas.md) antes de criar ou renovar capas. Adapte gênero, personagens, paleta e composição ao livro; gere versões próprias vertical e horizontal. A referência define o acabamento esperado, não uma obrigação de copiar a cena ou garantia de desempenho. Preserve capas já aprovadas, salvo pedido de renovação.

**Texto da frente de capa — regra de Israel, 11/10/2026:** a capa de PDF/EPUB e a miniatura do YouTube devem conter somente o título da obra, uma frase de impacto fiel à história e, embaixo, o nome do autor **Vorne Ermel**. Não colocar “Livro 1”, número de volume, gênero (“conto”, “romance”), chamadas de formato ou outros textos na frente. Para autoria diferente explicitamente confirmada, usar o nome confirmado, sem copiar Vorne Ermel. Na miniatura do YouTube, a frase deve ser exatamente a do `titulo.txt`; aplicar a mesma frase na frente vertical quando houver título de divulgação definido. Identificação de volume/subtítulo e outros dados editoriais permanecem na folha de rosto e nos metadados quando pertinentes. Ao corrigir uma capa, preservar a cena aprovada, conferir a grafia e a autoria no rodapé e atualizar/verificar sua incorporação efetiva no PDF e no EPUB; autoria apenas na folha de rosto não satisfaz esta regra.

**Nunca desenhe quadro de ISBN, retângulo branco, código de barras, ISBN fictício ou texto “ISBN aqui” na capa. A gráfica acrescentará esse elemento.** Quando houver área técnica prevista pelo fornecedor, preserve o fundo contínuo e mantenha textos essenciais fora dela, sem torná-la um quadro visível.

Após aprovação da capa, gere um piloto de estilo. Para as imagens do vídeo, a preferência atual é **alta fidelidade visual e fotorrealismo nos personagens e ambientes**, com aparência natural e consistência entre cenas. Leia cada capítulo inteiro e escolha **duas ou três imagens no total por capítulo**, conforme os acontecimentos; não são imagens adicionais a uma primeira imagem. Reutilize artes adequadas ao estilo e não refaça capítulos já aprovados retroativamente. Cada imagem deve representar um momento distinto, sem variações de enquadramento usadas apenas para preencher quantidade. Esta faixa substitui o teto anterior de quatro imagens; mudanças dependem de pedido explícito do autor.

Registre o roteiro por cena, sua ligação com o trecho do capítulo e a justificativa da quantidade antes de gerar o lote, seguindo [o planejamento visual](references/publicacao.md#ilustrações-de-capítulos). A aprovação do piloto confirma o estilo, não limita o capítulo a uma imagem. Preserve artes válidas ao ampliar uma sequência. Registre se as imagens entram no miolo/EPUB, no vídeo ou em ambos; não acrescente páginas ilustradas ao impresso silenciosamente, pois isso altera custo e lombada.

### 3. Kindle e livro físico

Gere EPUB de texto fluido, capa Kindle separada, PDF do miolo e PDF de capa aberta conforme o destino. Se solicitado, exporte PDF de leitura em tela separadamente. Não trate o PDF impresso como substituto do EPUB.

**Interior limpo:** use somente informações editoriais essenciais e confirmadas. Por padrão, não inclua avisos de revisão/geração por IA, ferramentas, fontes tipográficas, licenças, processo de produção, “edição independente”, editora não fornecida, ISBN ausente ou textos técnicos genéricos no livro. Mantenha esses registros e declarações aplicáveis fora do conteúdo visível ao leitor, no pacote de produção/cadastro; preserve licenças e obrigações reais. Veja [o padrão de interior limpo](references/publicacao.md#interior-limpo-e-informações-confirmadas).

Use a skill de PDF quando disponível, com renderização e inspeção visual; para DOCX, use a skill de documentos apenas se esse formato for pedido. Descubra dependências locais em vez de fixar caminhos de runtimes de outra máquina. Siga [a conferência de publicação](references/publicacao.md) e registre o que foi efetivamente validado.

Para entrega destinada à publicação no Kindle, inclua o [pacote de cadastro Amazon KDP](references/cadastro-kdp.md), com descrição comercial, metadados e guia campo a campo. A produção de um EPUB para Kindle inclui esses textos; o usuário não precisa pedi-los novamente. Respeite pedidos limitados a uma correção específica em arquivos já existentes.

### 4. Narração → audiobook → vídeo no Filmora

No fluxo local Qwen, permitir perfis carla/bruna com --voice na skill narracao-livro. Manter padrao local na ausencia de escolha. Uma nova referencia nao substitui a voz existente; avaliar amostra antes de aprovar novo perfil.

**Perfil local atualizado, 11/10/2026:** Israel aprovou Qwen3-TTS 0.6B Base com Carla. Usar a skill narracao-livro e scripts/narrar_qwen.py, referencia/transcricao locais aprovadas, MP3 256 kbps em blocos separados/numerados para Filmora, sem aceleracao posterior. Substitui o perfil MOSS local abaixo; nao substitui audio anterior nem ElevenLabs solicitado. Kokoro foi desinstalado; nao reinstalar ou trocar modelo automaticamente.

**Fluxo local MOSS-TTS para Filmora, escolhido por Israel em 11/10/2026:** quando a narracao solicitada for local, usar a skill complementar [narracao-livro](../narracao-livro/SKILL.md). Manter a referencia feminina brasileira ja aprovada na configuracao local, sem trocar voz ou pedir nova selecao. Entregar MP3 192 kbps em blocos maiores (aproximadamente 1000 caracteres, com cortes somente entre frases), separados e numerados por capitulo, com manifesto de texto/duracao/hash. Agrupar paragrafos e falas curtas para reduzir emendas; montagem e ajustes das juncoes ficam no Filmora. Nao concatenar automaticamente nem gerar um capitulo inteiro em uma unica chamada. Usar otimizacao de cache da referencia e liberacao da GPU pelo codec, sem reduzir codebooks ou alterar a precisao/sampling aprovados. Preservar trechos validos e audio anterior. Este fluxo complementa o ElevenLabs abaixo; nao substitui narracoes ElevenLabs ja aprovadas nem autoriza regeneracao automatica. Se a skill local nao estiver instalada, informar a dependencia e instalar/configurar dentro do pedido antes de executar, sem inventar a referencia aprovada.

Leia [narração e vídeo](references/audiovisual.md) e, para montagem/exportação, [o fluxo Filmora](references/filmora.md). As preferências atuais de Israel para novas produções são **ElevenLabs em pt-BR, modelo Eleven v4 (`eleven_v4`), com a voz `rwMvgbQxwV0LJTium7sd` (Lucy Fennek — Immersive and Inviting), Filmora desktop no Mac ou no Windows, imagens estáticas e cortes diretos**, visando reutilização e menor custo. Use a plataforma disponível no computador de execução, identificando o sistema e a versão instalada antes de operar; adapte caminhos, atalhos e ferramentas de controle conforme [a operação e a transferência de projetos](references/filmora.md#operação-do-aplicativo). Essa voz foi escolhida pelo usuário em 05/10/2026 e reafirmada em 11/10/2026 junto ao modelo v4; a combinação é o padrão para novas narrações. Não solicite novamente a escolha da voz ou do modelo. Verifique compatibilidade e use os parâmetros aceitos pelo endpoint v4; não substitua voz/modelo silenciosamente. Decisões explícitas do projeto prevalecem; preserve voz e materiais já aprovados em trabalhos anteriores. A amostra continua necessária para avaliar ritmo, pronúncias e interpretação em português brasileiro. Escolhas específicas já registradas para A Água do Despertar e A Casa Onde Guardamos o Amanhã (`mPDAoQyGzxBSkE0OAOKw` com v4) permanecem restritas a esses projetos.

**Lista de personagens — regra de Israel, 11/10/2026:** a apresentação/lista de personagens é apoio de leitura e permanece somente no livro (Markdown, PDF, EPUB e impresso). Não narrar nem exibir essa seção no vídeo ou no roteiro de narração destinado a ele. Começar com identificação breve da obra ou diretamente pela narrativa, conforme a edição escolhida pelo autor, para não atrasar o início da história. Preservar todas as cenas, falas e menções aos personagens dentro da narrativa. Ao remover a seção de um projeto existente, fechar o espaço vazio em todas as faixas e recalcular legendas e capítulos, conforme [a regra de abertura audiovisual](references/audiovisual.md#abertura-sem-lista-de-personagens).

Prepare roteiro derivado do texto aprovado, direção calorosa e expressiva, pronúncias e amostra. Após aprovação, mantenha áudios por blocos/capítulos; não exija concatenar todos em um arquivo antes de importar no Filmora. Preserve a narração completa do roteiro audiovisual, respeitando a exclusão da lista de personagens. Entregue projeto editável, MP4, títulos e os arquivos do YouTube; publicar, enviar à gráfica ou contratar serviços exige pedido correspondente.

### 5. Textos para publicar no YouTube

**Artes limpas:** nunca inserir “narração sintética”, “voz sintética” ou avisos de IA nas capas/miniaturas, aberturas e cartelas do vídeo. Usar título, autor e informações de formato confirmadas; manter créditos técnicos e declarações aplicáveis fora dessas artes, sem inventar um narrador humano.

**Frase de impacto na miniatura:** nunca colocar “Audiolivro completo”, “Audiobook completo” ou chamadas equivalentes de formato na capa/miniatura do YouTube. Nesse espaço, usar a **mesma frase de impacto que consta no título de divulgação do vídeo**, entre o nome do livro e o autor, para despertar curiosidade com fidelidade à história. Ler `titulo.txt` vigente, preservar a frase inteira e ajustar somente caixa, quebra de linhas e composição para manter a leitura no celular. Se a frase do título mudar, atualizar a miniatura correspondente. Informações de formato podem ficar na descrição e nas tags pertinentes.

Na produção de vídeo do audiobook para YouTube, inclua o pacote de publicação descrito em [textos para YouTube](references/youtube.md): **capa/miniatura própria do vídeo, bonita e fiel ao livro**, título recomendado, descrição completa, capítulos com horários reais, créditos, **tags do vídeo em `tags.txt`**, metadados e **legendas completas em SRT sincronizado para upload**, com VTT alternativo. Gere as tags em toda entrega, sem esperar pedido adicional, prontas para copiar no campo Tags do YouTube. Cartelas e capítulos da descrição não substituem as legendas da fala; não espere um pedido adicional de SRT. Entregue arquivos prontos para copiar e colar, além das observações de cadastro em arquivo separado. Também atenda pedidos apenas desses textos usando os materiais já aprovados; não regenere áudio ou vídeo sem necessidade.

Para o título de divulgação dos livros de Vorne Ermel, use como padrão **frase curta e chamativa que represente a história | Vorne Ermel**, sem o nome do livro no título do vídeo. Mantenha o nome da obra na descrição e na miniatura. Para outra autoria confirmada, aplique **frase | nome do autor**. A frase deve comunicar uma mensagem da obra e despertar curiosidade com fidelidade ao texto. Consulte os critérios e o exemplo em [redação para YouTube](references/youtube.md#redação); escolhas explícitas do autor prevalecem.

### 6. Cadastro e textos comerciais do eBook no Amazon KDP

Leia [cadastro do eBook](references/cadastro-kdp.md). Prepare os textos efetivos com base no livro aprovado, em formatos prontos para colar, e relacione todos os campos do cadastro: preenchidos, não aplicáveis ou dependentes de decisão do autor. Inclua título/subtítulo, autoria, descrição em texto e HTML, sete campos de palavras-chave quando pertinentes, categorias verificadas, dados da edição, direitos, acessibilidade, declaração de uso de IA e decisões comerciais. Não transforme o pedido desses materiais em submissão automática ao site.

Para pedidos de **upload, submissão ou publicação real no Kindle**, usar a skill complementar [kdp-publicar-livros](../kdp-publicar-livros/SKILL.md), quando instalada, lendo seu procedimento antes de operar o site. Ela aplica o perfil comercial autorizado de Israel e verifica o estado de cada obra na Biblioteca KDP. Encaminhar a edição vigente e os registros já produzidos; não repetir a produção nem pedir novamente decisões ainda válidas. O pedido atual precisa incluir publicação dos livros indicados; preparar textos ou arquivos sozinho continua sem autorizar submissão. As dispensas específicas de aprovação da rotina KDP aplicam-se ao seu escopo, sem serem estendidas a outras etapas ou projetos. As duas skills podem ser instaladas juntas pelo repositório público; se a complementar estiver ausente, informar isso e preservar o trabalho preparado sem alegar que ela foi executada.

## Entrega e continuidade

- Use nomes claros e mantenha somente a edição vigente em `entrega/`, preservando versões anteriores em `historico/`. Respeite a estrutura já estabelecida ao retomar um projeto.
- Inclua os fontes editáveis, os formatos solicitados, prompts/direção visual e de voz, manifesto com hashes e relatório dos checks realmente executados. Crie somente pastas necessárias à fase atual.
- Atualize o registro global após cada aprovação, alteração importante ou conclusão. O estado final deve distinguir `gerado`, `validado`, `aprovado pelo autor` e `publicado`.
- Não declare padrão profissional apenas porque o arquivo abriu: a qualidade editorial, a inspeção visual e a escuta precisam ter evidências. Se faltarem dados da gráfica, voz disponível ou ferramenta de validação, entregue as provas possíveis e nomeie precisamente a pendência.

## Manutenção e sincronização desta skill

Regra permanente de Israel: toda alteração nesta skill, incluindo referências, modelos, scripts e assets, deve ser publicada também em `https://github.com/israelermel/codex-skills-public`, branch `main`, pasta `skills/livro-profissional`, antes de declarar a atualização concluída. O pedido de editar a skill inclui autorização para esse commit e push; não pedir novamente confirmação para sincronizar.

- Verificar os estados Git da origem e do repositório público; incluir somente mudanças desta skill em commits pequenos e focados, preservando alterações de outros trabalhos.
- Sincronizar o pacote completo, incluindo remoções intencionais. Adaptar caminhos absolutos locais para referências portáteis; em `references/licoes-do-projeto.md`, manter os caminhos históricos sob `<pasta-do-livro>/` na cópia pública. Não publicar credenciais, manuscritos ou arquivos de projetos de livros.
- Validar estrutura e links da skill; executar checks apropriados aos scripts alterados. Fazer commit e push da origem quando versionada e da cópia pública, e verificar o commit remoto.
- Se o envio falhar, registrar a pendência e reportar a falha; não declarar o repositório público atualizado sem confirmação remota.

Essa sincronização mantém a versão disponível no GitHub. A instalação no outro computador precisa ser atualizada a partir desse repositório; não presumir que ela se atualiza sozinha.
