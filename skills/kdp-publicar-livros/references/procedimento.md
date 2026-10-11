# Procedimento real de cadastro Kindle

## Materiais e fatos por livro

Prefira a estrutura do projeto: `entrega/livro/*.epub`, `entrega/capa/capa-kindle*.jpg`, `entrega/livro.md`, `entrega/kdp/` e `editorial/`. Leia `spec_location.md` e o registro de produção quando existirem. Relacione a fonte, o EPUB e a capa escolhidos; registre SHA-256. Não suba arquivos de `historico/` por terem nome parecido com o vigente.

Confira o EPUB com validação estrutural disponível (por exemplo, EPUBCheck), capa e autoria, sumário navegável, texto/acentos e alternativas textuais de imagens. Use relatórios existentes quando correspondam aos hashes atuais. Corrija apenas defeitos técnicos reversíveis que preservem a edição; se o problema exigir conteúdo/arte novos, marque o livro afetado e continue o lote.

Prepare descrições fiéis ao manuscrito, sem spoilers desnecessários, preços, URLs, tags, alegações de ranking ou depoimentos inventados. Descrição de até 4.000 caracteres, incluindo HTML; até sete palavras-chave curtas e distintas; até três categorias da taxonomia atual da Amazon.com.br. Se os limites da interface mudarem, use os limites atuais. Categorias de um livro não são padrão dos demais. Título/subtítulo devem corresponder ao EPUB/capa; não use a chamada promocional do YouTube como título bibliográfico.

Não crie ISBN, ASIN, editora, série, número de edição ou colaboradores fictícios. O ISBN Kindle é opcional; deixe em branco sem número válido. Não insira avisos técnicos de IA no interior do livro.

## Acesso e retomada

Use ferramentas de navegador/UI permitidas no ambiente, respeitando a documentação da ferramenta. Se houver ferramenta nativa ou connector adequado, prefira-o. Não acesse cookies, perfis do navegador, senhas ou sessões por rotas não autorizadas. O usuário autentica diretamente no site se necessário.

Na Biblioteca, verifique título + subtítulo + autoria e, quando disponível, ID registrado. Retome o rascunho correto. Homônimos ou outro formato não são automaticamente o mesmo eBook. Um título em análise ou à venda não deve ser recriado. Registro local diz “não enviado” mas Biblioteca diz “Em revisão”: reconcilie com o estado atual, sem novo envio.

Preencha pela interface observada. Obtenha estado atualizado após alterações que mudem o formulário; índices de elementos são transitórios. Se a página ficar em branco, tente recarregar ou reabrir a URL observada em uma nova aba e então retome o mesmo ID. Não recrie o livro por uma falha de navegação.

## Detalhes

Preencha idioma, título, subtítulo, autoria, descrição, direitos próprios e Amazon.com.br. Use o nome literário real, não o nome legal da conta por dedução. Série, edição e colaboradores apenas quando presentes e confirmados nos materiais. Conteúdo explícito e faixa etária dependem do livro; não copie “Não” nem idade de outro projeto sem examinar o conteúdo.

Selecione as palavras-chave e categorias adequadas ao livro nas opções atuais. Salve e reabra para conferir texto, acentos e opções persistidas. Em ferramentas nativas, uma operação de digitação pode corromper acentos; use o setter de campo quando disponível e confira o resultado real. Para HTML, use o modo Fonte se necessário e verifique a descrição renderizada.

## Conteúdo

1. Envie o EPUB e aguarde a confirmação de upload, processamento e verificação do manuscrito. Envie a frente Kindle e aguarde sua confirmação. Não avance com erro de processamento.
2. Selecione **sem DRM**, incluindo a permissão EPUB/PDF quando o KDP a oferecer. Não basta a opção estar visualmente vazia: confira que a seleção foi aplicada e salva.
3. Responda sobre IA a partir do processo real de **cada livro**. Conteúdo redigido/ilustrado/traduzido pela IA é gerado mesmo após edição. Revisão de conteúdo criado pelo autor é assistência. Declare tipo, alcance e ferramentas comprovados; não invente os nomes nem copie o alcance de outro livro. Uma capa gerada conta como imagem gerada. Se faltar informação indispensável, registre o impedimento da obra.
4. Declare acessibilidade conforme o EPUB inspecionado. Marque alternativas textuais em todas as imagens informativas somente se efetivamente conferidas. Não confunda validação estrutural com auditoria completa.
5. Na prévia KDP, confira capa inteira, sumário/navegação, início, ponto intermediário e fim; use as visualizações Kindle, tablet e celular disponíveis. Registre amostragem e problemas observados, sem alegar leitura integral. Corrija defeitos reais antes de submeter. Não registre URLs temporárias autenticadas de prévia.
6. Ao retornar da prévia, confira novamente DRM, declaração de IA e acessibilidade: autosave pode não preservar uma seleção. Salve antes de prosseguir.

## Condições comerciais e envio

Marque **KDP Select** e **70%**. Em territórios, selecione **Territórios individuais**, use **Nenhum** para limpar a seleção inicial e marque **Brasil**. Confira que o resumo contém exatamente **um território: Brasil**. A lista inicial pode apresentar todos os países já selecionados; clicar em territórios individuais sozinho não limita a distribuição.

Insira **R$ 5,99** na Amazon.com.br. Deixe a plataforma calcular os preços de outras lojas quando o formulário exigir; isso não muda o território Brasil selecionado. Confira preço, plano, Select e território após salvar/reabrir. Receitas líquidas variam com custos e condições: não copie a estimativa de R$ 4,15 observada em Ecos da Névoa para outro livro.

Verifique requisitos atuais de preço/royalties e Select. A opção de 70% no Brasil depende de Select e dos demais critérios vigentes. A exclusividade do Select se aplica ao eBook digital; verifique eventuais registros concretos de distribuição EPUB/PDF integral fora da Amazon. Vídeo/audiobook não provam, por si, distribuição concorrente do eBook. Não exija nova declaração de exclusividade por rotina: a adesão já foi autorizada; só peça resolução se encontrar incompatibilidade real.

Com os campos e arquivos conferidos, execute **Publicar** conforme autorizado no SKILL.md, sem pedir outra confirmação. Aguarde a confirmação identificando o título certo e preço. Feche a confirmação e leia o estado na Biblioteca. Se houver aviso concreto ou bloqueio, resolva o que estiver no escopo; caso precise do titular, preserve o cadastro e continue os outros livros.

Não repita o botão de submissão após timeout sem verificar a Biblioteca. Se o envio foi confirmado e o título está “Em revisão”, esse livro está concluído para a etapa de envio; registre e avance ao próximo. Análise posterior da Amazon não precisa bloquear os demais.

## Registro e conclusão do lote

Grave por livro: pasta, título/autoria, paths/hashes enviados, ID e URLs estáveis, escolhas aplicadas, perfil de autorização `kdp-publicar-livros` (10/10/2026), pedido de execução atual, upload/processamento, prévia amostrada, confirmação de envio, status e timestamp com fuso. Grave ASIN/link de compra somente quando exibidos/verificados. Preserve pacotes e manifestos anteriores; o registro operacional fica fora de `entrega/`.

Atualize o checkpoint do lote após cada título. Em uma nova execução, consulte esse registro e confirme o estado vivo da obra antes de agir. Registros antigos do pacote editorial podem dizer “não enviado”; o registro operacional atual e a Biblioteca resolvem esse histórico. Não atualize memória global sem pedido do usuário.

## Fontes oficiais

Referências consultadas em 10/10/2026. Reconsulte durante a execução quando a decisão depender de regra vigente ou quando a interface apresentar mudança:

- [KDP Select e exclusividade](https://kdp.amazon.com/pt_BR/select).
- [Royalties de eBooks](https://kdp.amazon.com/pt_BR/help/topic/G200644210).
- [Requisitos de preço](https://kdp.amazon.com/pt_BR/help/topic/G200634560).
- [Metadados](https://kdp.amazon.com/pt_BR/help/topic/G201097560).
- [Conteúdo gerado ou assistido por IA](https://kdp.amazon.com/pt_BR/help/topic/G200672390).

Estas são condições da plataforma; o padrão comercial do autor continua o mesmo até alteração expressa. Se uma condição atual impedir esse padrão, não converta silenciosamente para 35%, aumente preço ou amplie territórios.
