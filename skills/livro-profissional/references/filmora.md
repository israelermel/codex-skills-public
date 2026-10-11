# Montagem do audiobook no Filmora e entrega para YouTube

Aplicar a novas produções de Israel como preferência consolidada em Luz de Cristal, salvo decisão explícita diferente. Não iniciar geração nem publicação quando o pedido for somente atualizar a skill. Para os números e resultados daquele livro, consultar [as lições](licoes-do-projeto.md).

## Materiais, custo e retomada

- Inventariar manuscrito vigente, capa, imagens aprovadas, áudios, alinhamentos e projetos salvos antes de produzir algo. Preservar aprovações e hashes; retomar do ponto real.
- Reutilizar artes adequadas. Para novos capítulos, duas ou três imagens no total, escolhidas pela narrativa, com personagens e ambientes fotorrealistas de alta fidelidade. Essa faixa substitui o teto anterior de quatro. Não refazer capítulos anteriores já aprovados para obedecer retroativamente ao teto. Destino das imagens é explícito: em Luz de Cristal, somente vídeo, sem ilustrações internas no EPUB/PDF.
- Manter áudios separados por bloco/capítulo, com IDs e ordem. Não exigir MP3 único: o Filmora aceita a sequência na faixa de áudio. A duração final reúne os blocos sem exigir um intermediário concatenado.
- Preferir estrutura simples: `entrega/filmora/01-audios`, `02-imagens`, `03-titulos`, projeto `.wfp`, `plano-timeline.json`, MP4 e relatório; `entrega/youtube` contém textos e SRT/VTT.
- Cópias ou hard links podem organizar as mídias no mesmo volume; registrar quando arquivos compartilham dados. Não editar uma cópia presumindo independência de um hard link. Preservar caminhos de origem necessários para reabrir o projeto.

## Plano de montagem

Guardar tempos em segundos na timeline pública, com `fps`, `duration_seconds` e listas:

- `audio`: `id`, `file`, `start_seconds`, `end_seconds`, duração original e quantidade de quadros.
- `scenes`: ID, arquivo, trecho/âncora narrativa e início/fim reais.
- `titles`: número do capítulo, texto/arquivo e início/fim.

Usar os alinhamentos do áudio aprovado para localizar a fala associada a cada cena. Não distribuir imagens igualmente pela duração por conveniência. Conferir identidade do texto antes de utilizar seus tempos.

No projeto de referência, cada bloco foi arredondado **para cima** ao quadro completo a 25 fps; a diferença vira apenas o silêncio final tecnicamente necessário. Usar o início efetivo de cada bloco na timeline para legendas e marcadores. A soma das durações MP3 originais pode divergir da duração renderizada; não usar essa soma para sincronizar o final do livro.

Garantir ordem e continuidade das faixas: sem lacunas visuais, sobreposição acidental de falas, truncamento da última palavra ou repetição de trecho. Cobrir abertura/personagens com a capa ou arte aprovada e cobrir o último áudio até o fim. Nunca aplicar `-shortest` para esconder divergências.

## Aparência aprovada

Abertura e cartelas devem conter apenas identificação da obra e informações de formato confirmadas. Nunca inserir “narração sintética”, “voz sintética” ou avisos de IA na imagem. Ao corrigir uma arte já usada, atualizar a mídia do projeto, reabrir e salvar no Filmora, reexportar os vídeos afetados e conferir o quadro resultante; trocar somente o PNG não corrige um MP4 existente.

**Padrão atual: imagens estáticas e cortes diretos, sem pan, zoom, dissoluções ou transições.** Não criar efeitos extras; foram dispensados para reduzir tempo de exportação. Música apenas se pedida/aprovada.

No início de cada capítulo, exibir cartela sobre a imagem com:

1. `CAPÍTULO 01` — número visível, pequeno, em dourado discreto.
2. Título real do capítulo — serifado maior em branco/creme.
3. Traço curto dourado e `NOME DO LIVRO · NOME DO AUTOR` em corpo menor.

Composição alinhada à esquerda na parte inferior, fundo/degradê escuro discreto para contraste, margem segura e sem cortar texto. Referência do caso: overlay PNG transparente em 1920×1080, 12 segundos por cartela, sem fades na edição simplificada. Ajustar tamanho/quebra de títulos longos e duração ao livro; 12 s não é requisito rígido. Usar título/autor reais de cada obra, não copiar “Vorne Ermel” automaticamente.

Cartela de capítulo, marcadores da descrição e legendas da fala são três entregas distintas. O texto narrado completo também deve ter **SRT externo para o YouTube**, sem gravá-lo na imagem por padrão.

## Operação do aplicativo

Usar o **Filmora desktop no Mac ou no Windows**, conforme o computador disponível. Identificar o sistema operacional, a versão instalada e as ferramentas de controle acessíveis antes de começar; obter esses dados do ambiente quando possível, sem exigir uma escolha de plataforma já evidente. Abrir, montar/salvar e exportar no aplicativo, entregando `.wfp` editável. Utilizar as ferramentas de controle de app disponíveis nessa plataforma; inspecionar o estado antes de agir e após alterações. Se o controle não estiver disponível, preparar as mídias e o plano e dizer exatamente qual passo requer ajuda, sem afirmar que operou o Filmora ou substituir silenciosamente o aplicativo por outro editor.

- Preferir elementos de acessibilidade e diálogos nativos. Não reutilizar índices de outra captura. Se ações no canvas/arraste não responderem, confirmar o resultado antes de repetir.
- Após uma tentativa e uma alternativa sem efeito, solicitar a menor ajuda manual concreta: por exemplo, selecionar arquivos e clicar Abrir. Registrar o que foi importado; ao receber “importei”, conferir e continuar, sem reiniciar o projeto.
- No Mac, usar os diálogos nativos e, quando disponível, `⌘⇧G` para informar o caminho completo; salvar com `⌘S` ou o menu correspondente. No Windows, usar o campo de nome/caminho ou a barra de endereços do diálogo observado; salvar com `Ctrl+S` ou o menu correspondente. Conferir os atalhos configurados no aplicativo; não traduzir todos os atalhos do Mac para Windows por mera troca de teclas. [Atalhos do Filmora](https://filmora.wondershare.com/basic-video-editing/video-editing-keyboard-shortcuts.html).
- Descobrir caminhos e runtimes locais. Nos scripts, usar construção de caminhos adequada ao sistema, como `pathlib.Path`; em comandos, respeitar o shell disponível, incluindo PowerShell no Windows. Usar caminhos reais, incluindo espaços e acentos, sem escapes de outra plataforma. Não salvar por cima do original ao testar uma montagem.
- Alterar o texto aparente de um campo de exportação não comprova que o Filmora aceitou o destino. No caso histórico do Mac, a exportação foi para `~/Movies/Wondershare Filmora Mac/Output` apesar da alteração visível; esse caminho não é padrão universal nem deve ser imposto ao Windows. Conferir o destino efetivo e o arquivo real após concluir e só então organizar a entrega.
- Scripts podem preparar mídias, cartelas, plano e cópias do projeto; não apresentar um MP4 produzido fora do app como exportação do Filmora. FFmpeg/ffprobe podem inspecionar os resultados e gerar provas técnicas sem substituir a edição solicitada.

### Continuar em outro computador ou sistema

Usar **Arquivo → Arquivar projeto / File → Archive Project** quando disponível para reunir projeto e mídias; copiar todo o pacote gerado, não apenas um `.wfp` que ainda dependa dos caminhos da máquina original. A extensão e a organização do arquivo de transferência podem variar pela versão. Consultar o fluxo da edição instalada: [Windows](https://filmora.wondershare.com/guide/move-projects.html) e [Mac](https://filmora.wondershare.com/guide-mac/move-projects.html).

Antes de transferir entre Mac e Windows, conferir compatibilidade das versões e preferir a mesma versão nos dois computadores; não prometer compatibilidade apenas pela extensão. A orientação oficial de [transferência Windows → Mac](https://support.wondershare.com/how-tos/filmora/can-i-open-the-project-created-by-windows-version-on-mac.html) exige verificar a versão e arquivar o projeto. Não atualizar o aplicativo nem contratar licença ou recursos pagos sem autorização correspondente.

No destino, abrir uma cópia pelo Filmora, relocalizar mídias ausentes e conferir fontes, cartelas, efeitos utilizados, áudio, duração e cortes. Salvar uma nova cópia e exportar um piloto para validar a retomada antes da edição integral. Preservar o projeto e os arquivos de origem. Registrar sistema/versão de origem e destino e o resultado da transferência; distinguir pacote preparado de projeto efetivamente aberto e validado no outro computador.

### Cópia nativa `.wfp` como recuperação de automação

Usar somente quando houver um projeto real salvo/importado pelo próprio Filmora e for possível validar a cópia no aplicativo. O formato é interno e depende de versão: não inventar um `.wfp` ou presumir compatibilidade.

No Filmora 15.6.4 observado, `.wfp` era ZIP com `ProjectFolder/project_info.json`, `ProjectFolder/Medias/<UUID>/timeline.wesproj`, `medias_info.json` e `media.json` por mídia. A timeline usava ticks de 100 ns (`10.000.000/s`; `400.000/quadro` a 25 fps), campos `inPoint/outPoint/tlBegin/tlEnd` e IDs importados. **`medias_info.json` continha chaves `media_item` repetidas**: um parse/serialize JSON comum pode perder mídias. Preservar estrutura e metadados originais; tratar isso como observação da versão, não API estável.

Preparar uma cópia, preservar originais, abrir e salvar pelo Filmora, conferir contagem/arquivos/tempos no salvo e exportar piloto real. Falha nessa validação impede alegar que o projeto é utilizável. Não repetir tentativas cegas de edição interna.

## Piloto e exportação

- Piloto curto de aproximadamente 60–90 segundos contendo narração, imagem e ao menos uma cartela. Mostrar arquivo reproduzível e registrar a aprovação. Reaproveitar piloto/aprovação válidos; um pedido explícito para remover efeitos e seguir permite a versão simplificada, sem nova barreira artificial.
- Perfil de referência: MP4/H.264, 1920×1080, 25 fps constantes, SDR Rec.709, cerca de 8 Mb/s; AAC estéreo 44,1 kHz/192 kb/s no caso de origem. Ajustar ao projeto/fontes/destino; não exigir resampling ou reencodificação sem motivo. Não confundir esse perfil com requisitos universais de YouTube.
- Usar aceleração de GPU quando disponível/estável. Auto Highlight, compressão avançada e backup automático em nuvem desativados, salvo pedido específico; não criar resumo automático no lugar do audiobook integral.
- Conferir duração total e espaço em disco antes de exportar. O tamanho real é medido depois; não prometer que outro livro terá 19 GB ou o mesmo prazo.
- Mostrar progresso real do aplicativo com percentuais/ETA quando disponíveis, sem inventar evolução. Evitar polling frenético e tentativas simultâneas na UI. Enquanto exporta, preparar textos/SRT usando a timeline vigente.
- Declarar exportado somente após confirmação do aplicativo e existência do arquivo íntegro. Preservar o original; organizar a cópia/hard link final depois do término.

## Conferência e entrega

1. Projeto: contagem/ordem de áudios, cenas e cartelas contra o plano; mídias presentes; tempos contínuos; efeitos correspondentes ao pedido.
2. MP4: duração de áudio/vídeo e da timeline, resolução/fps/codecs, decodificação do áudio e análise de clipping. Média/pico de `volumedetect` não são LUFS. Hash do áudio recodificado em AAC não deve ser comparado byte a byte com MP3.
3. Visual: abertura, cartelas de todos os capítulos, encerramento e cortes de cenas; ampliar títulos longos e verificar contraste, recorte e marca d’água. Se a revisão foi amostral, declarar quantos quadros e quais fronteiras foram examinadas. Não alegar escuta integral ou decodificação de todos os quadros sem realizá-las.
4. YouTube: MP4 + `.wfp`/mídias + SRT sincronizado (VTT alternativo) + textos/horários/créditos/tags/cadastro + miniatura aprovada ou pendência explícita + manifesto de hashes. Produzir uma miniatura própria, bonita e representativa do livro, seguindo [a direção de capa do vídeo](youtube.md#capa-ou-miniatura-do-vídeo). Reutilizar uma arte compatível como base quando isso funcionar; não considerar a capa vertical ou um frame aleatório como miniatura final automaticamente.
5. Vincular SRT e capítulos ao hash da edição exata do MP4. Alterações de ordem/pausas/cortes exigem recalcular tempos; simples entrega de SRT não exige renderizar novamente.
6. Atualizar o registro global e entregar links claros, distinguindo gerado, validado, aprovado e publicado. Preparar tudo localmente não autoriza upload, agendamento ou publicação.
