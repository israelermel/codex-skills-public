# Legendas, textos e cadastro do vídeo no YouTube

Entregue textos completos baseados no livro, na narração e na montagem aprovados. Não entregue apenas orientações ou modelos vazios quando houver conteúdo suficiente. Se o pedido for somente atualizar a skill, registre este fluxo sem iniciar a publicação de um livro.

## Arquivos de entrega

Use `entrega/youtube/` ou a pasta de publicação já existente no projeto:

| Arquivo | Conteúdo |
|---|---|
| `titulo.txt` | Uma única linha com o título recomendado, pronto para colar |
| `descricao.txt` | Descrição integral, com créditos e capítulos, sem instruções internas |
| `capitulos.txt` | Horários e títulos extraídos da timeline final |
| `tags.txt` | Obrigatório em toda entrega: tags pertinentes em uma linha, separadas por vírgulas, prontas para o campo Tags do vídeo |
| `cadastro-youtube.md` | Alternativas de título, contagem de caracteres, arquivos a enviar, decisões de cadastro e pendências |
| `<livro>-pt-BR.srt` | Legendas completas com marcação de tempo, para upload no campo Legendas do YouTube |
| `<livro>-pt-BR.vtt` | Versão alternativa das mesmas legendas |
| `manifesto.json` | Hash do MP4 e hashes/versões dos textos, horários e legendas |
| `miniatura-youtube.jpg` ou `.png` | Capa própria do vídeo, bonita, representativa do livro e legível em tamanho pequeno |

Para capítulos publicados individualmente, prepare título/descrição próprios por vídeo quando essa entrega for solicitada. Mantenha o título no padrão **frase | nome do autor**; identifique capítulo e livro na descrição e use somente links confirmados para a série ou vídeo completo, salvo escolha explícita diferente do autor.

## Capa ou miniatura do vídeo

Aplicar [a referência de qualidade das capas](qualidade-capas.md), compartilhada com PDF e EPUB. Manter acabamento, personagens e identidade do livro em uma composição horizontal própria, conferida também em 320×180 e 160×90.

Manter a arte limpa: título, autoria e frase de impacto do título de divulgação. Nunca escrever “Audiolivro completo”, “Audiobook completo” ou chamadas equivalentes de formato na miniatura/capa do YouTube. Também não inserir “narração sintética”, “voz sintética” ou avisos de IA na miniatura, capa do vídeo ou abertura. Créditos técnicos e declarações aplicáveis ficam nos arquivos de produção/cadastro; não atribuir a narração a uma pessoa que não a realizou.

**Gerar uma capa própria para o vídeo em toda produção completa para YouTube**, sem esperar novo pedido. O objetivo é representar muito bem a obra e despertar interesse com uma composição bonita, fiel ao gênero, à atmosfera e ao conflito central. Consultar o manuscrito/sinopse e as decisões visuais antes de escolher a cena; não reduzir o livro a um objeto chamativo sem relação com sua história.

- Criar uma composição horizontal 16:9, com um foco visual claro, boa luz, contraste e hierarquia. Perfil de trabalho inicial: 1920×1080; exportar JPEG/PNG e conferir limites vigentes de tamanho/formato no envio.
- Para as novas produções deste fluxo, usar personagens e ambientes realistas, de alta fidelidade, coerentes com as referências das cenas do vídeo. Se houver elementos extraordinários no livro, representá-los conforme a narrativa e a direção aprovada, sem mudar o gênero da obra.
- Incluir nome do livro em destaque e autoria legível; no espaço secundário, usar a **mesma frase de impacto do título do vídeo**, lida de `titulo.txt` antes do separador final ` | ` que antecede a autoria. No padrão `frase | Vorne Ermel`, a frase é o trecho à esquerda. Preservar suas palavras: pode alterar caixa e dividir em duas linhas, sem trocar a frase por outra chamada. Ela deve despertar curiosidade sem spoiler e representar a história. Se ainda não houver título definido, preparar primeiro o título no padrão da seção Redação e então aplicar sua frase de impacto na miniatura. Conferir acentos, grafia, margens e leitura em tamanho pequeno, especialmente no celular. Se a frase do título for alterada, revisar a miniatura para manter a correspondência.
- Usar arte existente como base quando ela for adequada e compor a miniatura para esse formato. Não esticar a capa vertical, não entregar apenas uma captura aleatória e não confundir a primeira cartela do vídeo com a miniatura externa. Se faltar uma base adequada, gerar uma nova arte com a ferramenta de imagem disponível, respeitando o orçamento e as aprovações vigentes.
- A capa do vídeo é um arquivo separado; não entra na contagem de duas ou três cenas por capítulo. Não regenerar capítulos ou alterar capa de EPUB/impresso para criar essa miniatura.
- Inspecionar anatomia, identidade dos personagens, ambiente, fidelidade narrativa e legibilidade antes de mostrar a prévia. Evitar spoilers decisivos, promessas enganosas e imagens que prometam uma história diferente apenas para atrair cliques. Não garantir views ou taxa de cliques.
- Entregar o arquivo pronto e registrar fonte da arte, versão/hash e aprovação em `cadastro-youtube.md`. Se a geração estiver impedida, identificar a pendência explicitamente; não declarar a capa pronta sem arquivo e inspeção.

Pedidos restritos a tags, textos ou SRT de um vídeo existente não autorizam gerar uma nova miniatura nem refazer mídia. Atualizar a skill também não inicia a criação da capa de um livro.

## Legendas completas da narração

**SRT faz parte da entrega padrão de vídeo para YouTube; não espere o autor lembrar de pedi-lo.** São as legendas que o espectador ativa/desativa. Entregue o arquivo externo com marcações de tempo para o campo Legendas; VTT como alternativa. Não queime o texto na imagem, não remultiplexe nem reexporte um MP4 pronto apenas para entregar esse arquivo. Uma escolha explícita por legendas sempre visíveis altera esse padrão.

Não confundir:
- Cartelas: número/título do capítulo, nome do livro e autor sobre a imagem.
- Capítulos da descrição: navegação por horários.
- SRT/VTT: **todo o texto falado**, incluindo abertura, personagens e narração, sincronizado.

### Sincronização sem nova geração de voz

Reutilize os alinhamentos já salvos pelo ElevenLabs. Para cada bloco, confira texto/hash e três vetores de igual tamanho: `characters`, `character_start_times_seconds`, `character_end_times_seconds`. Some a cada tempo local o **início efetivo desse bloco na timeline final**. Não use duração estimada de leitura, divisão uniforme por capítulo ou apenas a soma de MP3: pausas e arredondamento por quadro podem acumular diferença. Se a fala foi cortada/acelerada na edição, transformar os alinhamentos pela edição ou realinhar o áudio final; não aplicar offsets simples a material retimado.

Sem alinhamentos válidos, utilizar transcrição/alinhamento da gravação existente e conferir com o texto aprovado. Não regenerar áudio pago só para obter tempos nem criar tempos fictícios. Distinguir alinhamento do provedor de transcrição independente e de escuta humana.

O script portátil [gerar_legendas_alinhadas.py](../scripts/gerar_legendas_alinhadas.py) usa somente a biblioteca padrão Python e o esquema do fluxo Filmora:

```bash
python3 scripts/gerar_legendas_alinhadas.py --project "/caminho/do/livro" --basename "Nome-do-Livro-pt-BR"
```

Executar a partir da pasta da skill ou resolver o caminho absoluto do script. Entradas esperadas no projeto: `entrega/filmora/plano-timeline.json` (lista `audio` com ID/início/fim), `entrega/audiobook-elevenlabs/roteiro.json` (lista `blocks` com ID/texto) e `entrega/audiobook-elevenlabs/blocos/<id>.json` (alignment/text_sha256). `--output` permite escolher pasta de saída; padrão `entrega/youtube`. O script não acessa API, chave ou rede e não altera voz/vídeo. Para outro esquema, adaptar a leitura e validar; não copiar arquivos de Luz de Cristal para outro livro.

### Leitura e verificações

- Gerar UTF-8, índices SRT crescentes, `HH:MM:SS,mmm --> HH:MM:SS,mmm`; VTT começa com `WEBVTT` e usa ponto nos milissegundos.
- Segmentar por palavras/frases, preferindo pontuação e evitando cortar unidades de sentido. Referência de composição: até duas linhas de 42 caracteres; duração em torno de 1–7 s e velocidade de leitura próxima de até 20–21 caracteres/s. Não cortar palavras/texto para atingir esses números; inspecionar exceções.
- Conferir início/fim dentro do vídeo, tempos crescentes, ausência de sobreposição, preservação da ordem e de todos os tokens do roteiro falado. Inspecionar começo/fim e fronteiras dos blocos/capítulos para detectar deslocamento acumulado.
- Verificar leitura do SRT por um parser (ex.: ffprobe) e registrar contagem, cobertura, duração, hashes e limitações. Não chamar isso de escuta integral.
- Vincular a versão do SRT ao hash do MP4 exato. Se o vídeo ainda renderiza, indicar validação final pendente; depois comparar duração e atualizar o manifesto.

### Envio quando solicitado

Orientação: YouTube Studio → Legendas → selecionar vídeo → Português (Brasil) → Adicionar → Fazer upload do arquivo. O SRT já contém os tempos; quando houver escolha, usar **com marcação de tempo**. Conferir a prévia antes de salvar/publicar. Não orientar colar o SRT na descrição nem usar sincronização automática sobre tempos já conferidos. [YouTube — adicionar legendas](https://support.google.com/youtube/answer/2734796?hl=pt-BR).

Entregar o arquivo e a orientação não autoriza operar/publicar no canal. Se o autor pedir apenas as legendas de um vídeo existente, gerar o SRT/VTT e atualizar o registro, preservando o MP4 e o projeto de edição.

## Redação

Use como padrão a estrutura **frase curta e chamativa que represente a história | Vorne Ermel** para os livros desse autor, com um único separador ` | `. O nome do livro fica na descrição e na miniatura, sem entrar no título de divulgação do vídeo. Para outra autoria confirmada, use **frase | nome do autor**. A frase deve comunicar uma mensagem da obra e despertar curiosidade a partir de seu conflito, vínculo ou promessa principal. Escolha palavras concretas e emocionais, fiéis ao manuscrito ou à sinopse aprovados, sem revelar o desfecho nem criar suspense enganoso.

Exemplo aplicado a esta preferência: `Uma promessa mais forte que o sangue | Vorne Ermel`, para *O Pacto do Dedinho*. Use a mensagem desse exemplo apenas para essa obra; escolha uma frase própria para cada livro. Esse é o título de divulgação do vídeo, sem alterar o título oficial do livro, a capa ou os metadados editoriais. Esta preferência foi atualizada por Israel em 10/10/2026 e substitui o padrão anterior que incluía o nome do livro no título do vídeo.

Informações de formato, como “audiolivro completo ilustrado”, podem entrar na descrição e nas tags pertinentes quando corresponderem ao conteúdo. A miniatura usa a frase de impacto do título, sem chamadas de formato. Ofereça até duas alternativas em `cadastro-youtube.md`, mantendo uma escolha clara em `titulo.txt`, dentro do limite de caracteres conferido. Respeite um título ou estrutura escolhidos explicitamente pelo autor. Não invente promessas, resultados, fama, prêmios ou sucesso de vendas, nem garanta visualizações.

Estruture a descrição com:

1. Abertura curta que desperte curiosidade, identifique o nome do livro e explique o que o ouvinte encontrará.
2. Sinopse fiel ao gênero e ao público, sem revelar desfechos relevantes.
3. Créditos reais de autoria e produção; identifique o provedor/voz realmente utilizados como narração sintética, sem atribuir a autoria à voz. Não copiar Thalita para créditos de um vídeo narrado com ElevenLabs.
4. Capítulos com marcações de tempo do vídeo final.
5. Links existentes e confirmados do livro, autor ou playlist, se fornecidos ou verificados. Sem página Amazon publicada, omita a linha de compra do texto final e registre a pendência no cadastro; nunca invente ASIN ou URL.
6. Convite discreto para acompanhar o canal/comentar e poucas hashtags pertinentes, se úteis ao público. Não repita palavras de busca em excesso.

O texto deve ficar pronto para colar: não inclua rótulos como “introdução aqui”, instruções de revisão, caminhos locais, placeholders ou contadores dentro de `descricao.txt`.

## Tags do vídeo

Gere `tags.txt` automaticamente junto com título, descrição, capítulos e legendas, sem exigir que o autor peça novamente. Entregue o conteúdo efetivo, não uma lista de orientações ou placeholders.

- Objetivo pedido pelo autor: selecionar tags com potencial de aumentar a descoberta e as visualizações por pessoas interessadas no conteúdo. Antes de escolher, pesquisar consultas atuais no idioma/mercado do público usando fontes acessíveis: termos de pesquisa do próprio canal quando disponíveis, sugestões de busca do YouTube e tendências relevantes. Registrar fonte e data em `cadastro-youtube.md`; não alegar pesquisa ou volume de buscas que não foram observados.
- Priorizar aderência ao livro e intenção de busca, combinando identificação da obra/autor, consultas de formato e idioma (por exemplo, “audiobook completo em português”, somente quando completo) e expressões específicas de gênero/tema. Sinais observados de procura ajudam a priorizar; popularidade isolada não justifica uma tag irrelevante. Não rotular termos como “alto volume” ou “baixa concorrência” sem dados que sustentem isso.
- Use título do livro, nome do autor, formato (audiobook, audiolivro, livro narrado), idioma, gênero e temas que o conteúdo realmente aborda. Priorize termos específicos da obra e evite uma lista inflada de termos genéricos.
- Escreva uma única linha, com tags separadas por vírgulas, sem `#`, aspas, marcadores de lista ou duplicatas. Hashtags da descrição são outro campo e não substituem esse arquivo.
- Não invente popularidade, prêmios, nomes de outros autores, temas ou palavras em alta sem relação com o vídeo. Não prometa alcance ou posição em buscas.
- Registre em `cadastro-youtube.md` o arquivo a usar no campo Tags e a contagem de caracteres do conjunto. Confira o limite vigente na etapa de envio e reduza termos menos relevantes se necessário.
- Ao revisar título, autoria, gênero ou escopo do vídeo, revise também as tags. Um pedido apenas de tags não exige gerar voz, imagens, legendas ou vídeo novamente.

O YouTube informa que título, miniatura e descrição têm mais peso na descoberta e que tags costumam contribuir pouco, salvo quando ajudam com grafias pesquisadas incorretamente. Tratar “alto potencial” como objetivo de seleção, não garantia de views. No pacote completo, manter título, miniatura e descrição coerentes com a intenção de busca, sem excesso de palavras-chave; não alterar automaticamente materiais aprovados em um pedido restrito às tags. Quando não houver dados acessíveis, entregar uma seleção editorial pertinente e identificar a ausência de validação de demanda. [YouTube — tags e descoberta](https://support.google.com/youtube/answer/146402?hl=pt-BR), consultado em 26/09/2026.

## Limites e conferência

Referências de limites, capítulos e upload de legendas verificadas em 26/09/2026; confirme mudanças ao preparar uma publicação:

- Título: até **100 caracteres**. Descrição: até **5.000 caracteres**, contando espaços, quebras de linha, URLs, créditos e hashtags. Conte os arquivos finais e ajuste sem cortar palavras no meio. [YouTube — configurações do vídeo](https://support.google.com/youtube/answer/57404?hl=pt-BR).
- Capítulos manuais: começar em `00:00`, incluir pelo menos três marcações crescentes e duração mínima de dez segundos por capítulo. Confira também o último intervalo até o fim do vídeo. Se seções curtas não atenderem, agrupe somente os marcadores da descrição, preservando a narração. Sem duração/timeline real, deixe o pacote como provisório, sem inventar horários. [YouTube — capítulos](https://support.google.com/youtube/answer/9884579?hl=pt-BR).
- Teste correspondência de títulos, duração, créditos, links e miniatura. Salve hash/versão do vídeo ao qual a descrição pertence; alteração na montagem exige recalcular horários.

No arquivo de cadastro, registre idioma, categoria sugerida, playlist quando conhecida, miniatura, legendas disponíveis e decisões pendentes sobre público infantil, licença, visibilidade e agendamento. Examine a regra vigente de conteúdo alterado/sintético conforme o material real; não escolha automaticamente a resposta só por existir TTS.

Apresente título e descrição ao autor para observações e aprovação. Preparar esses arquivos não publica nem agenda o vídeo. Se o usuário pedir envio, use as ferramentas disponíveis, confirme somente decisões ainda pendentes e registre o resultado real e a URL após a operação autorizada.
