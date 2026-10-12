# Capas e imagens de capítulos no ComfyUI

Escolha de Israel em 11/10/2026: integrar a geração local com o arquivo existente `qwen-image-2.1-UC-Q6_K.gguf`, do repositório `abenzerps/Qwen-Image-2.1-Uncensored-GGUF`. Usar o script [gerar_imagens_comfyui.py](../scripts/gerar_imagens_comfyui.py). Não regenerar livros ou artes anteriores automaticamente.

## Instalação e perfil

Descobrir a pasta do ComfyUI e o endpoint local; usar ambiente Python isolado. Instalar ComfyUI atual e o fork `leejet/ComfyUI-GGUF`, necessário para `qwen_image21`. Ler o modelo existente por `extra_model_paths.yaml`, sem duplicar pesos. Os complementos são `qwen3vl_8b_int8_convrot.safetensors` em `models/text_encoders` e `qwen_image_2.1_vae_bf16.safetensors` em `models/vae`.

No Windows de Israel: RTX 4060 com 8 GB e aproximadamente 64 GB de RAM. Perfil inicial: encoder no CPU, `--lowvram --disable-dynamic-vram --reserve-vram 1 --preview-method none`, escutando somente em `127.0.0.1:8188`. Não executar narração e geração de imagens simultaneamente na mesma GPU. Conferir a instalação local antes de usar esse caminho em outro computador; a cópia pública da skill não instala pesos ou dependências.

Validado em 11/10/2026: ComfyUI 0.39.0, PyTorch 2.14.1+cu130 e loader GGUF leejet; imagem real de ambiente/objetos em 512 × 512 com 20 passos em 132,3 s, e padrão 768 × 768 com 30 passos em 198,3 s, sem erro de memória. PNGs inspecionados e retomada real sem duplicação. Tempos incluem etapas de carregamento/encoding/decodificação, variam com a cena e não validam consistência facial. Os hashes completos de UC Q6_K, encoder e VAE coincidiram com os publicados.

## Capas locais

Escolha de Israel em 11/10/2026: a IA local é o padrão também para novas capas e estudos de renovação. Usar o mesmo ComfyUI/Qwen existente, sem chamar a geração de imagens do ChatGPT salvo pedido específico. Não substituir automaticamente capas aprovadas ou regenerar derivados publicados.

Antes de gerar, procurar no diretório do livro `capa-briefing.md`, registros de produção/aprovação, referências visuais, contracapa e `titulo.txt` vigente. Conferir o conceito no manuscrito: idade dos personagens, arquitetura, objetos e clima narrativo. Orientações antigas de pintura ou autoria ausente cedem ao pedido atual de realismo e aos dados mais recentes confirmados. Seguir [qualidade-capas.md](qualidade-capas.md) para cena forte, luz cinematográfica, contraste e leitura em miniatura. Na frente, usar somente título, frase de impacto vigente e autoria confirmada.

Reutilizar o script existente com uma cena identificada por `capitulo: 1` e `cena: 1`, em pasta exclusiva da capa; esses IDs são técnicos e não ligam a capa a um único capítulo. A primeira referência define a proporção: escolher uma referência vertical para a frente e horizontal para YouTube. Inspecionar a referência e declarar seu papel no prompt; a capa anterior pode orientar conceito e formato sem obrigar copiar estilo ou detalhes incompatíveis com o texto. Não esticar nem recortar indiscriminadamente para obter outro destino. Sem referência, este script produz imagem quadrada.

Perfil de partida testado na RTX 4060 de 8 GB: `resolucao: 896`, 30 passos, CFG 4, Euler/simple. Ajustar conforme memória, qualidade e formato; não é resolução universal de publicação. O teste realista de A Casa Onde Guardamos o Amanhã gerou uma frente nativa de 736 × 1088 em 336,6 segundos (5 min 37 s), usando uma referência vertical. Madeira, vegetação e luz ficaram convincentes, e o modelo acertou título, frase, autoria e acentos. Ainda elevou demais a plataforma da casa e estreitou a escada: qualidade fotográfica não garante fidelidade espacial.

Para testar a capacidade de letras do modelo, pode-se gerar a frente completa, fornecendo os textos exatos e conferindo palavra por palavra. Para o acabamento editorial, preferir arte sem letras e tipografia aplicada separadamente e editável; isso continua usando IA local para a arte. Inspecionar a frente inteira, detalhes e miniatura de 160–200 px, conferindo contraste, margens, anatomia, perspectiva e texto. Salvar original, prompt, workflow, tempo e hashes; distinguir dimensões nativas de ampliação. Interpolação não cria detalhe de impressão. Registrar o estudo como aguardando autor; incorporar em PDF/EPUB ou substituir a capa somente no escopo autorizado.

## Roteiro e lote

Ler os capítulos inteiros, escolher momentos distintos e registrar a ligação com o texto. A quantidade local é variável e pode superar a antiga faixa de duas ou três cenas. Não criar cenas repetidas para preencher a contagem. Manter aprovação do piloto e do conjunto, salvo dispensa específica do autor. A preparação técnica não autoriza montar imagens inéditas em um livro aprovado.

O JSON tem `livro`, `estilo` e `cenas`. Cada cena tem `capitulo`, `cena` (inteiros positivos), `trecho`, `prompt`, `seed`, `resolucao`, `passos` e opcionais `cfg`, `negativo`. Descrever explicitamente a identidade dos personagens, roupas, ambiente e época. Sem referências, a imagem é quadrada; com referências, a proporção vem da primeira imagem e `resolucao` controla sua área aproximada. Identidade facial precisa de inspeção, não é garantida por seed.

```json
{"livro":"exemplo","estilo":"Cinematic photorealism, natural materials, no text.","cenas":[{"capitulo":1,"cena":1,"trecho":"Trecho que motiva a cena","prompt":"Scene description with characters and setting","seed":123456,"resolucao":768,"passos":30}]}
```

## Referências de personagens

Preferência de Israel em 11/10/2026: preparar poucas imagens principais (capa e personagens/características) e reutilizá-las no ComfyUI para várias cenas por capítulo. Aproveitar capa e artes já aprovadas; preparar fichas frontais com rosto, cabelo, idade visual, compleição e roupas reconhecíveis. Distinguir detalhes confirmados no manuscrito de decisões de direção visual. Se houver envelhecimento, criar referências próprias por fase, sem envelhecer todos os capítulos automaticamente.

Usar `referencias` no nível do livro como padrão ou em cada cena como substituição: lista de caminhos absolutos ou relativos à pasta do JSON, em PNG/JPEG/WebP. Uma lista vazia por cena desliga o condicionamento. O script envia essas imagens à API local, cria nós LoadImage e liga `images.image_1` etc. ao TextEncodeQwenImage21 com VAE. Registrar o papel de cada imagem no prompt: identidade, roupa, ambiente ou estilo. Usar a saída latent desse nó, que corresponde à primeira referência; não substituir por um latent de outro tamanho. A primeira referência também define a proporção, portanto escolher seu formato conforme o destino.

O workflow usa QwenImage21Cache no CPU com precisão padrão, para reduzir pressão na RTX de 8 GB sem quantizar o cache adicionalmente. Começar com `resolucao: 640` e 24 passos em um piloto; medir antes de ampliar. Seeds diferentes ajudam a testar se a identidade vem da referência e não de cenas quase repetidas. Não misturar a capa automaticamente ao condicionamento de todas as cenas: letras, personagens de outra fase e acontecimentos futuros podem ser copiados. No capítulo 1 do piloto A Casa Onde Guardamos o Amanhã, por exemplo, a casa na árvore da capa ainda não existe.

```json
{"livro":"exemplo","referencias":["referencias/personagens.png"],"estilo":"Image 1 defines the identities of Miguel and Clara; preserve faces and clothes, create one new cinematic frame.","cenas":[{"capitulo":1,"cena":1,"trecho":"Trecho narrativo","prompt":"New action and setting","seed":510111,"resolucao":640,"passos":24}]}
```

Uploads usam nomes derivados do hash do conteúdo. O manifesto registra arquivos/hash das referências; alterar uma referência muda o workflow e impede sobrescrita silenciosa. `--validar` lê e confere referências locais e nós, mas não faz upload nem carrega os modelos. Em testes no Ryzen 5700X, FP32 foi mais rápido em uma multiplicação isolada, porém as primeiras gerações completas por referência em FP16 e FP32 ficaram próximas de 204 segundos; não prometer ganho de produção com base só no microbenchmark. O perfil FP16 anterior permanece válido; `--fp32-text-enc` é uma alternativa testada, com mais RAM necessária para cálculo.

O piloto de cinco cenas confirmou execução real com uma referência principal e uma edição com duas referências na RTX de 8 GB. Com referência 3:2, resolução de área 640 e 24 passos, foram geradas imagens 768 × 512 em aproximadamente 3–4 minutos, incluindo carga/fila quando aplicável. A avaliação visual encontrou boa continuidade de cabelo, roupas, idade aparente e traços gerais, com variações faciais; um controle só por texto também manteve aparência geral semelhante. Não concluir que a referência trava identidade facial a partir de um único controle. Uma edição de cena gerada endureceu texturas; regenerar diretamente da referência principal com prompt corrigido preservou melhor a aparência natural. Registrar objetos recorrentes e relações espaciais explicitamente, além da ficha dos personagens. Retomada do lote completo preservou as cinco imagens sem duplicação.

Executar `python scripts/gerar_imagens_comfyui.py roteiro.json --saida <pasta-de-imagens> --validar` para conferir disponibilidade dos nós e salvar workflows API sem gerar. Esse check não testa carga dos modelos. Remover `--validar` para gerar um piloto real. Medir tempo, conferir memória e inspecionar PNG antes do lote. Se houver falha, corrigir a causa e preservar cenas concluídas; não trocar modelo ou baixar outra quantização silenciosamente.

O script gera uma cena por vez, salva PNGs numerados, workflows API e `manifesto-imagens.json`, com prompt, seed, trecho, duração, hashes, prompt ID e licença. Repetir o comando preserva cenas concluídas com hashes válidos. Alteração do workflow exige nova pasta de saída para preservar versões. Em timeout, o trabalho pode continuar no servidor: conferir a fila antes de reenviar. Não confundir workflow API com workflow de interface visual.

Ao concluir um lote com fila vazia, o script solicita descarregar os modelos para liberar memória para a narração e outras tarefas. O servidor permanece aberto. Não descarregar modelos no meio de um lote ou enquanto outra execução está na fila.

Imagens geradas aguardam inspeção e aprovação. Conferir fidelidade ao trecho, anatomia, rostos, mãos, objetos, continuidade e qualidade visual. Associar ao roteiro audiovisual e/ou EPUB/miolo conforme o destino confirmado, sem incluir ilustrações no impresso silenciosamente. Prompts e revisão pelo chat continuam usando o chat; a inferência local não chama a geração de imagens do ChatGPT.

## Licença

UC significa Uncensored. A variante mantém a **Qwen Research License**, com uso do modelo limitado a pesquisa/avaliação e licença comercial separada exigida pelas cláusulas 2(a) e 2(b). Israel pediu configurar o modelo após ser informado; isso não modifica a licença. Manter essa pendência nos registros de produção e não afirmar que está autorizado para livros vendidos.

Fontes: [variante](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF), [licença original](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE). Contato comercial indicado: `model-business@notice.qwencloud.com`. Não enviar mensagens ao fornecedor sem pedido explícito.
