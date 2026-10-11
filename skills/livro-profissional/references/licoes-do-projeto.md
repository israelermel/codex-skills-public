# Experiência de origem: Nem Sequer um Grão de Areia

Esta skill foi extraída em 13/09/2026 dos arquivos de `<pasta-do-livro>/nem_se_quer_um_grao`. Use a experiência abaixo em qualquer novo livro; não dependa dessa pasta nem copie seu conteúdo autoral para outro trabalho.

| Material observado | Aprendizado reutilizável |
|---|---|
| PDFs de manuscritos e `transcricao.md` organizado por página | Manter o original e sua leitura separados da edição literária; controlar cobertura e ordem |
| `livro.md`, backups de revisão científica e `revisao-argumentos.md` | Revisar linguagem, clareza, coerência e fatos em camadas; distinguir hipóteses filosóficas de afirmações científicas |
| `historico/` e versões anteriores | Uma mudança editorial não deve apagar a edição anterior nem suas provas |
| `ferramentas/build_book.py` e `merge_heads.py` | Um manuscrito abastece EPUB e PDF; paginação, cabeçalhos e fólios precisam de conferência específica |
| `ferramentas/README.md` e modo `--text-only` | Preservar arte aprovada ao corrigir texto; só preservar lombada quando a contagem final continuar compatível |
| `capas/` e `antigas-capas-nao-usar/` | Identificar a arte aprovada explicitamente, sem escolher uma imagem antiga por conveniência |
| `audiobook-thalita/gerar.py` | Thalita com trechos, pausas, cache, retries limitados, metadados e checagem de duração |
| `audiobook-text/direcao-de-voz.md` antigo | Nesse projeto Thalita prevaleceu sobre uma indicação anterior de voz masculina/ElevenLabs; isso é histórico daquele livro, não veto a novas escolhas explícitas |
| `imagens/prompts.json`, `geracao.json` | Persistir prompts e correspondência entre capítulo e imagem; manter unidade visual |
| `video/produzir.py`, `video/qa/` e timeline | Conferir todas as trocas de capítulo, duração e decodificação; preservar a narração integral |

O caso observou 20 capítulos, 24 seções narradas, 21 ilustrações e vídeo de cerca de 1h39min. Esses números são particulares do livro. Em nova produção, descubra as seções do manuscrito aprovado; não use asserts de 24 arquivos nem nomes de capítulos fixos.

O miolo documentado tinha 76 páginas, formato de 5,5 × 8,5 pol. e lombada estimada para papel branco. O registro histórico não prova conformidade com qualquer gráfica e não deve ser copiado como padrão universal. Em especial, revise o limite de páginas para texto na lombada de KDP antes de aproveitar essa solução.

As artes do caso usam azul profundo e dourado em linguagem contemplativa. Essa escolha atende aquele ensaio filosófico; outros gêneros devem receber direção própria.

O script de narração transformava tags em dois ritmos (`-8%` e `-4%`) e pausas. Isso não garante atuação expressiva. A preferência atual exige amostra avaliada, variação adequada ao texto e reconhecimento dos limites do sintetizador.

Os metadados TTS foram conferidos contra as palavras enviadas; o próprio relatório diferencia essa validação de uma transcrição independente. Preserve essa honestidade em novos relatórios.

O vídeo final corrigiu alertas de timestamp na primeira concatenação e foi conferido nas 24 transições. Guarde essa lição de verificação, sem impor a mesma configuração FFmpeg a todos os vídeos.

Antes de reutilizar os scripts locais, leia-os: existem caminhos, título/autor, fontes e quantidades fixos. Parametrize-os para o novo projeto e execute verificações de resultado. Não os distribua como geradores genéricos sem adaptação.

## Luz de Cristal — decisões consolidadas em 26/09/2026

Autor: Vorne Ermel. Registro local: `~/.Codex/specs/luz_de_cristal/producao.md`; materiais em `<pasta-do-livro>/Luz de Cristal`. Não depender desses caminhos nem copiar conteúdo autoral para outros livros. O fluxo reutilizável está em [narração](audiovisual.md), [Filmora](filmora.md) e [YouTube/SRT](youtube.md).

| Decisão ou resultado observado | Aplicação futura |
|---|---|
| Textos, capa, imagens e voz foram aprovados ao longo da conversa | Retomar decisões reais; não pedir novamente aprovações válidas nem refazer materiais |
| Capa ilustrada com título e autoria, rejeição de cristal místico/algodão/metal como conceito de capa | Direção parte da leitura e do gênero; símbolos desta narrativa não viram padrão de outra |
| Ilustrações restritas ao vídeo, excluídas do PDF/EPUB a pedido | Registrar destino das artes antes de diagramar; não incluir no impresso silenciosamente |
| “Dramatis personae” corrigido para “Personagens” em todos os derivados | Textos de interface editorial em pt-BR; propagar correção aos formatos e ao roteiro |
| Primeiro o autor limitou novos capítulos a quatro imagens; depois atualizou para duas ou três | A preferência vigente é duas ou três no total por novo capítulo; preservar capítulos anteriores |
| Ritmo aprovado, mas sotaque estrangeiro no título/capítulos com serviço anterior | Piloto precisa conter esses trechos; ElevenLabs escolhido explicitamente e aprovado |
| Voz Carla, ID `mPDAoQyGzxBSkE0OAOKw`, com alinhamento de caracteres por bloco | Preservar metadados para sincronizar cenas e legendas sem repetir geração paga |
| 76 blocos, 35 capítulos, 136 cenas + capa, 35 cartelas | Contagens específicas deste livro; descobrir quantidades no próximo projeto |
| Filmora comprado pelo autor, exigido para montagem/exportação | Usar o aplicativo e entregar `.wfp`; não alegar uso do Filmora em exportação externa |
| Autor dispensou movimentos/transições para acelerar | Imagens estáticas e cortes diretos são a preferência atual |
| Cartelas de 12 s com número, título, livro e autor | Hierarquia aprovada, com duração ajustável; não equivalem a legendas da fala |
| MP4 gerado pelo Filmora 15.6.4, 1920×1080/25 fps, H.264 8 Mb/s, SDR Rec.709, AAC estéreo 44,1 kHz/192 kb/s | Perfil de referência, não requisito universal do YouTube; conferir configuração real |
| Vídeo de 18.791,320 s (5h13min11s), cerca de 19,28 GB | Duração/tamanho reais devem ser medidos; não prometer tamanho/prazo fixos |
| Áudio decodificado integralmente; 43 quadros inspecionados, incluindo 35 cartelas | Registrar cobertura exata; não houve escuta integral nem decodificação de todos os quadros do vídeo |
| Pedido posterior mostrou que faltava SRT para o campo do YouTube | Incluir SRT sincronizado automaticamente no pacote, separado do MP4; VTT alternativo |
| 3.778 legendas, 45.126 tokens, 76 blocos, até 2 linhas de 42 caracteres, sem sobreposição | Verificar preservação textual e tempos; números não são asserts para outros livros |
| Nenhum upload foi realizado | Gerar e aprovar arquivos não autoriza publicar/agendar |

Os scripts locais têm utilidade como referência, mas incluem caminhos e nomes do livro. O gerador portátil de legendas incluído na skill deve receber o projeto por argumento; não reutilizar arquivos de outra obra por conveniência.

### Atualização posterior de direção visual

O autor pediu incluir automaticamente uma capa/miniatura bonita e representativa do livro para YouTube e definiu **duas ou três imagens por capítulo**, com **alta fidelidade e realismo de personagens e ambientes**. A decisão substitui o teto anterior de quatro nas próximas produções. Não representa pedido para refazer o vídeo ou as ilustrações de Luz de Cristal já entregues. A identidade dos personagens e a fidelidade ao ambiente narrado devem ser verificadas junto com a qualidade visual.
