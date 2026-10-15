# Fluxo híbrido editorial

Preferência de Israel em 15/10/2026: local sempre que a tarefa for compatível; narração no ElevenLabs. Este fluxo complementa as aprovações e requisitos de qualidade da skill principal.

## Componentes e execução

- Texto: LM Studio, Qwen3.5-9B GGUF Q4_K_M, repositório `lmstudio-community/Qwen3.5-9B-GGUF`, arquivo `Qwen3.5-9B-Q4_K_M.gguf`. Modelo de texto sob Apache 2.0; não confundir sua licença com a do modelo de imagens.
- API de texto em `http://127.0.0.1:1234`, identificador carregado `editor-livros-qwen`, contexto inicial 16384 tokens, uma geração por vez, GPU máxima, descarregamento por inatividade de 600 segundos. O helper usa `reasoning_effort: none` nesta API para desativar raciocínio e reduzir o tempo de geração; `off` não é o valor aceito nesse endpoint. RTX 4060 de 8 GB/64 GB RAM é a máquina desta configuração, não requisito universal.
- Imagens: ComfyUI/Qwen Image existente, conforme [comfyui-local.md](comfyui-local.md). Preservar a pendência de licença comercial ali documentada.
- Voz: ElevenLabs e perfil vigente de [audiovisual.md](audiovisual.md). Não trocar por Qwen3-TTS para economizar sem pedido do autor. Confirmar disponibilidade do serviço e saldo antes de um lote pago.
- PDF/EPUB: ferramentas locais de composição/conversão e validação, conforme [publicacao.md](publicacao.md). O modelo escreve texto; conformidade exige dimensões, margens, fontes, metadados, sumário, validação e provas reais. Não prometer aceitação da Amazon apenas por gerar o arquivo.

O helper usa Python 3 com biblioteca padrão e a CLI `lms`; não usa chave OpenAI nem API externa para inferência. Descobrir Python e `lms` na máquina atual. No Windows, pode localizar `lms.exe` em `~/.lmstudio/bin` ou `~/.lmstudio/apps/bionic/bin`. Não embutir caminhos pessoais na cópia pública.

Para conversar diretamente no LM Studio, importar ou selecionar [o preset de editor pt-BR](../assets/editor-livros-ptbr.preset.json). O helper aplica suas próprias instruções e parâmetros, independentemente do preset selecionado na interface.

```powershell
python <skill>/scripts/editor_local.py --iniciar
python <skill>/scripts/editor_local.py --status
python <skill>/scripts/editor_local.py --entrada <capitulo.md> --saida <revisao-v1> --contexto <resumo-do-livro.md> --orientacoes <folha-de-estilo.md>
python <skill>/scripts/editor_local.py --entrada <trecho-referencia.md> --saida <acrescimo-v1> --modo completar --contexto <resumo-do-livro.md> --orientacoes <briefing-do-acrescimo.md>
python <skill>/scripts/editor_local.py --descarregar
```

Revisão não exige folha de estilo quando ainda não existe. Completar exige briefing explícito; o arquivo de entrada é uma referência curta e o resultado é uma proposta separada, nunca inserida automaticamente no manuscrito. Em ficção, respeitar os limites criativos autorizados; em autobiografia/não ficção, não inventar fatos, lembranças ou fontes. Pedir dados ou marcar lacunas quando necessário.

## Cobertura e retomada

Trabalhar capítulo por capítulo com um resumo global, personagens, cronologia e folha de estilo mantidos em arquivos. O helper divide capítulos grandes em blocos, conserva uma memória curta entre blocos e usa o contexto fornecido em todos eles. Isso não equivale a uma leitura simultânea do livro inteiro. Conferir o inventário de capítulos e executar também uma avaliação de coerência global usando os resumos; registrar o que foi efetivamente examinado. Para completar, fazer um pedido por acréscimo com referência de até um bloco.

As saídas são `revisado.md` ou `acrescimo-proposto.md`, `parecer.md`, `continuidade.md`, respostas brutas, blocos e `manifesto.json`; revisão inclui `alteracoes.diff`. O manifesto vincula fonte e configuração por hash. Uma nova configuração/fonte exige nova pasta. Repetir o comando retoma blocos já concluídos com hashes válidos. Resposta truncada/JSON inválido, redução superior a 30% em revisão ou complementação quase idêntica à fonte interrompe a aceitação; isso não detecta todas as omissões e incoerências. Conferir cenas, falas, nomes, limites de tamanho e sentido antes de apresentar a prova. Não confundir cobertura de blocos com qualidade editorial aprovada.

O texto local é uma proposta. O chat deve examinar o texto efetivamente produzido, o parecer e mudanças, comparar trechos de risco e registrar dúvidas para o autor; ampliar a inspeção diante de cortes ou inconsistências. O parecer pode afirmar que fez algo ausente da saída, portanto não serve como prova sozinho. Se falhar, devolver correções concretas ao Qwen em uma nova versão e conferir novamente, sem tentativas ilimitadas nem substituir o modelo silenciosamente. Evitar imprimir capítulos e respostas integrais no chat sem necessidade. Inferência local elimina cobrança de tokens de uma API de texto nessa etapa, mas usa hardware/energia; o chat e o ElevenLabs continuam com seus próprios custos/limites.

## Transferência entre etapas

1. Revisar e preparar acréscimos locais; consolidar somente no escopo autorizado. Apresentar texto e alterações para aprovação.
2. Com o texto aprovado, preparar briefing de capa e roteiro visual; executar o ComfyUI seguindo o piloto e as aprovações existentes.
3. Descarregar o Qwen antes das imagens (`--descarregar`). O helper também libera o modelo ao terminar revisão/complementação. Antes de carregar Qwen, confere a fila do ComfyUI e solicita liberação se o serviço estiver ocioso; não interrompe lotes ativos. Conferir fila antes de qualquer troca manual.
4. Gerar provas PDF/EPUB com ferramentas locais e executar os checks técnicos e visuais. Conferir requisitos atuais do KDP no fechamento, incluindo declaração de conteúdo gerado por IA quando aplicável. Revisão assistida e criação de texto/imagem são situações diferentes segundo o KDP.
5. Derivar o roteiro da versão aprovada e acionar ElevenLabs com a configuração e o cache existentes. Preservar trechos de áudio válidos; preparar a amostra prevista para um livro novo. Nenhum fallback automático para voz local.

Configurar este fluxo não inicia livros antigos, regeneração de imagens/áudio nem publicação. Para um livro indicado pelo autor, a coordenação pode executar os comandos diretamente neste ambiente com acesso local; uma conversa sem ferramentas de execução local não ganha acesso ao computador apenas por receber a skill.

Fontes técnicas: [CLI LM Studio](https://lmstudio.ai/docs/cli), [modelo quantizado](https://huggingface.co/lmstudio-community/Qwen3.5-9B-GGUF), [saída estruturada](https://lmstudio.ai/docs/developer/openai-compat/structured-output), [formatos Kindle](https://kdp.amazon.com/en_US/help/topic/G200634390), [diretrizes de conteúdo KDP](https://kdp.amazon.com/en_US/help/topic/G200672390).
