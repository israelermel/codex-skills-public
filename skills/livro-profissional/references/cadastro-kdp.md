# Textos e cadastro do eBook no Amazon KDP

Prepare um pacote completo de publicação, com redação real baseada na edição aprovada. O destino é o **Kindle Direct Publishing (KDP)**. Diferencie cadastro da conta, cadastro da obra e submissão para análise/publicação. Um pacote pronto não significa que o livro está à venda.

## Fontes e dados necessários

Leia manuscrito, capa, metadados do EPUB, decisões do autor e registro de produção. Use os mesmos título, subtítulo, nome autoral e edição em todos os lugares. Preserve o nome literário aprovado; dados legais da conta não devem substituí-lo no livro por dedução.

Pergunte somente o que não puder ser obtido dos arquivos e decisões existentes. Continue redigindo descrição e metadados enquanto houver decisões comerciais pendentes. Não exija senha, código de autenticação, dados bancários ou informações fiscais no chat. O titular preenche os dados sensíveis diretamente no site; o guia pode indicar quais etapas faltam sem armazenar seus valores.

## Entrega pronta para copiar

Use `entrega/kdp/` ou pasta equivalente já estabelecida:

| Arquivo | Conteúdo |
|---|---|
| `titulo.txt` e `subtitulo.txt` | Valores exatos aprovados; subtítulo só quando existir |
| `descricao.txt` | Texto comercial integral, sem comentários internos |
| `descricao.html` | A mesma descrição com formatação simples suportada pelo KDP |
| `palavras-chave.txt` | Uma frase por linha, na ordem dos campos do formulário, sem números/rótulos incorporados |
| `cadastro-kdp.md` | Guia campo a campo com valores, categorias, decisões pendentes, anexos e sequência de envio |
| `biografia-autor.txt` | Texto aprovado para página do autor ou uso editorial, quando houver informações; não é campo obrigatório da aba de detalhes do eBook |

No guia, separe o **valor para colar** de justificativas, contagens e instruções. Campos opcionais sem conteúdo devem indicar “deixar em branco” no guia, sem colocar essa frase no formulário. Não entregue apenas um template quando for possível preencher a partir do livro. Se faltar dado obrigatório, marque a pendência no guia, jamais disfarce um placeholder como texto final.

## Redação comercial e limites

Abra a descrição com uma pergunta ou apresentação concreta ligada ao tema. Desenvolva premissa, experiência de leitura, assuntos centrais e público, com linguagem envolvente e fiel à obra. Encerre com um convite à leitura sem prometer resultados ou esconder o gênero. Para ficção, evite spoilers; para ensaios, preserve a distinção entre hipótese e fato. Não copie automaticamente a descrição do YouTube, que tem outra finalidade.

Referências verificadas em 13/09/2026; conferir requisitos atuais antes da entrega:

- Título e subtítulo combinados devem ter **menos de 200 caracteres**, corresponder à capa e não receber palavras de busca artificiais. Descrição KDP não deve incluir URLs, contato, preços, promoções, depoimentos, pedidos de avaliação ou listas de tags. [KDP — metadados](https://kdp.amazon.com/en_US/help/topic/G201097560).
- Descrição: até **4.000 caracteres**. Valide tanto o texto simples quanto o código HTML final, incluindo a marcação no orçamento, e confira no editor da plataforma. Use somente tags suportadas, como `<p>`, `<br>`, `<b>` e `<i>`; sem CSS, scripts, imagens ou links. Renderize a versão HTML para verificar parágrafos, acentos e hierarquia. [KDP — descrição do livro](https://kdp.amazon.com/en_US/help/topic/G201189630).
- Prepare até **sete palavras-chave ou frases curtas**, distintas e pertinentes. Confira o limite exibido em cada campo; não use nomes de concorrentes, alegações de ranking, marcas sem autorização ou termos de programas Amazon para atrair buscas. Não prometa posição nas pesquisas. Registre a razão editorial das escolhas separadamente. [KDP — palavras-chave](https://kdp.amazon.com/en_US/help/topic/G201298500).
- Sugira até **três categorias**, adequadas ao conteúdo, público e loja principal. Verifique os caminhos na taxonomia atual do KDP para eBook e no marketplace escolhido; não apresente códigos BISAC ou categorias de outra loja como opções confirmadas. Sem acesso à lista atual, identifique sugestões como “a confirmar no formulário”. [KDP — categorias](https://kdp.amazon.com/en_US/help/topic/G200652170).

## Guia campo a campo

Organize `cadastro-kdp.md` pelas telas atuais. Para cada campo, registre valor proposto/confirmado, fundamento e situação (`pronto`, `não aplicável`, `decisão do autor` ou `verificação no site`). Se o formulário atual exibir novos campos, acrescente-os; não trate esta lista como substituto da interface vigente.

### Conta do titular

Indique acesso/criação da conta e conclusão do perfil, identidade, recebimento e entrevista fiscal quando a plataforma solicitar. Não preencha dados inventados, não aceite termos em nome do autor por inferência e não inclua informações sensíveis no pacote editorial. Se a conta já estiver pronta, não repita o processo. O nome da conta e a autoria literária são dados distintos.

### Detalhes do eBook

Relacione idioma; título; subtítulo opcional; série/número se houver; número da edição quando aplicável; autor; colaboradores reais com função; descrição; direitos de publicação; público/pergunta de conteúdo explícito e idade de leitura quando aplicáveis; loja principal; palavras-chave; categorias; opção de lançamento/pré-venda e datas que o formulário solicitar.

Não invente série, tradutor, ilustrador humano, edição nova ou coautoria da IA. Não marque domínio público só porque o livro ainda não foi publicado. Direitos e loja principal devem ser confirmados com o autor quando não houver decisão registrada. [KDP — criação de um livro](https://kdp.amazon.com/en_US/help/topic/G202172740).

### Conteúdo do eBook

Manter o interior do livro limpo conforme [o padrão editorial](publicacao.md#interior-limpo-e-informações-confirmadas). Os registros técnicos e declarações de IA ficam neste guia/formulário externo, sem acrescentar esses avisos às páginas visíveis do EPUB ou do miolo. Continuar respondendo com veracidade às exigências da plataforma.

Relacione caminho exato e hash do EPUB final e da capa Kindle; resultado da prévia; DRM como decisão registrada do autor; informações de acessibilidade; declaração de uso de IA; ISBN e editora, se aplicáveis; demais campos apresentados pelo KDP.

O eBook Kindle **não exige ISBN**. Deixe o campo opcional em branco quando não houver número válido; não reutilize por suposição o ISBN de outro formato e não invente ASIN. Editora é opcional e deve ser real; não use Amazon/KDP como editora. Mantenha a capa sem quadro de ISBN e código de barras. [KDP — identificação e editora](https://kdp.amazon.com/en_US/help/topic/G201097560).

Prepare a resposta sobre IA com base no processo documentado. Texto escrito pelo autor e apenas revisado com IA é diferente de texto gerado por IA; capa/ilustrações geradas continuam sendo imagens geradas, mesmo quando o texto é autoral. A política atual exige declarar conteúdo gerado por IA, inclusive imagens, e diferencia assistência de geração. Responda por tipo/alcance e demais detalhes solicitados, sem esconder o processo nem classificar tudo automaticamente da mesma forma. [KDP — conteúdo e IA](https://kdp.amazon.com/en_US/help/topic/G200672390).

Declare acessibilidade de acordo com o EPUB realmente inspecionado, especialmente alternativas textuais para imagens informativas. Não marque presença de descrições em todas as imagens sem conferência. Registre resultados e pendências do arquivo, não uma promessa genérica de acessibilidade. [KDP — recursos de acessibilidade](https://kdp.amazon.com/en_US/help/topic/GSKNDYRASGAUS98L).

### Preço e distribuição

Liste a decisão de adesão ou não ao KDP Select, territórios de distribuição de acordo com os direitos reais, loja/moeda base, preço de lista, plano de royalties e condições de lançamento. Preço, exclusividade, DRM e territórios não são textos promocionais para a IA escolher silenciosamente.

Se o autor pedir recomendação de preço, consulte condições atuais da loja, royalties, tamanho do arquivo e custos aplicáveis; apresente estimativas como estimativas e solicite a decisão que faltar. Não fixe taxas ou elegibilidade universais nesta skill. Antes de adesão ao Select, confira os termos vigentes de exclusividade do eBook considerando a distribuição pretendida. Não confunda automaticamente vídeo/audiobook com distribuição do arquivo do eBook.

## Revisão do pacote e publicação

Confira consistência com capa, folha de rosto, EPUB e registro editorial; contagem de caracteres; HTML; palavras-chave; categorias; ausência de dados fictícios e de placeholders nos arquivos para colar. Submeta os textos ao autor para observações e aplique os ajustes antes de fechar o pacote.

Entregue a sequência operacional: acessar KDP → criar eBook Kindle → preencher detalhes → enviar EPUB/capa e conferir prévia → definir preço/distribuição → revisar e submeter quando autorizado. Consulte a interface atual para os nomes dos botões; não afirme ter preenchido, enviado ou publicado sem execução real.

Preparar o cadastro não autoriza publicação automática. Se o usuário pedir operação no site, execute o trabalho reversível autorizado, respeite decisões já aprovadas e pergunte apenas o que ainda for necessário. Após submissão, diferencie “em análise”, “publicando” e “disponível para compra”. Registre URL/ASIN somente quando existirem e tiverem sido verificados; depois atualize o link do livro nos textos do YouTube, se essa atualização estiver no escopo.

Se também houver cadastro de edição física no KDP, reaproveite os textos editoriais consistentes e acrescente os campos próprios de impressão e ISBN válido conforme a modalidade. A escolha de impressão não altera a regra de entregar capa sem quadro de ISBN; a inserção cabe ao fornecedor.

## Operação com a skill complementar

Quando o pedido incluir upload/submissão real dos eBooks de Israel, ler [kdp-publicar-livros](../../kdp-publicar-livros/SKILL.md) e seu procedimento, se a skill estiver instalada. Reutilizar o pacote desta etapa, com arquivos/hashes e fatos da obra, e aplicar o perfil comercial e as dispensas de aprovação específicos da rotina de publicação. Não duplicar essas escolhas nesta referência nem tratar preparação de materiais como pedido de publicar. Para outro autor, as autorizações pessoais de Israel não se aplicam.
