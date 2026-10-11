# Imagens de capítulos no ComfyUI

Escolha de Israel em 11/10/2026: integrar a geração local com o arquivo existente `qwen-image-2.1-UC-Q6_K.gguf`, do repositório `abenzerps/Qwen-Image-2.1-Uncensored-GGUF`. Usar o script [gerar_imagens_comfyui.py](../scripts/gerar_imagens_comfyui.py). Não regenerar livros ou artes anteriores automaticamente.

## Instalação e perfil

Descobrir a pasta do ComfyUI e o endpoint local; usar ambiente Python isolado. Instalar ComfyUI atual e o fork `leejet/ComfyUI-GGUF`, necessário para `qwen_image21`. Ler o modelo existente por `extra_model_paths.yaml`, sem duplicar pesos. Os complementos são `qwen3vl_8b_int8_convrot.safetensors` em `models/text_encoders` e `qwen_image_2.1_vae_bf16.safetensors` em `models/vae`.

No Windows de Israel: RTX 4060 com 8 GB e aproximadamente 64 GB de RAM. Perfil inicial: encoder no CPU, `--lowvram --disable-dynamic-vram --reserve-vram 1 --preview-method none`, escutando somente em `127.0.0.1:8188`. Não executar narração e geração de imagens simultaneamente na mesma GPU. Conferir a instalação local antes de usar esse caminho em outro computador; a cópia pública da skill não instala pesos ou dependências.

## Roteiro e lote

Ler os capítulos inteiros, escolher momentos distintos e registrar a ligação com o texto. A quantidade local é variável e pode superar a antiga faixa de duas ou três cenas. Não criar cenas repetidas para preencher a contagem. Manter aprovação do piloto e do conjunto, salvo dispensa específica do autor. A preparação técnica não autoriza montar imagens inéditas em um livro aprovado.

O JSON tem `livro`, `estilo` e `cenas`. Cada cena tem `capitulo`, `cena` (inteiros positivos), `trecho`, `prompt`, `seed`, `resolucao` (quadrada), `passos` e opcionais `cfg`, `negativo`. Descrever explicitamente a identidade dos personagens, roupas, ambiente e época. Este script inicial gera texto para imagem, sem referências visuais conectadas; identidade facial entre cenas precisa de inspeção, não é garantida por seed.

```json
{"livro":"exemplo","estilo":"Cinematic photorealism, natural materials, no text.","cenas":[{"capitulo":1,"cena":1,"trecho":"Trecho que motiva a cena","prompt":"Scene description with characters and setting","seed":123456,"resolucao":768,"passos":30}]}
```

Executar `python scripts/gerar_imagens_comfyui.py roteiro.json --saida <pasta-de-imagens> --validar` para conferir disponibilidade dos nós e salvar workflows API sem gerar. Esse check não testa carga dos modelos. Remover `--validar` para gerar um piloto real. Medir tempo, conferir memória e inspecionar PNG antes do lote. Se houver falha, corrigir a causa e preservar cenas concluídas; não trocar modelo ou baixar outra quantização silenciosamente.

O script gera uma cena por vez, salva PNGs numerados, workflows API e `manifesto-imagens.json`, com prompt, seed, trecho, duração, hashes, prompt ID e licença. Repetir o comando preserva cenas concluídas com hashes válidos. Alteração do workflow exige nova pasta de saída para preservar versões. Em timeout, o trabalho pode continuar no servidor: conferir a fila antes de reenviar. Não confundir workflow API com workflow de interface visual.

Imagens geradas aguardam inspeção e aprovação. Conferir fidelidade ao trecho, anatomia, rostos, mãos, objetos, continuidade e qualidade visual. Associar ao roteiro audiovisual e/ou EPUB/miolo conforme o destino confirmado, sem incluir ilustrações no impresso silenciosamente. Prompts e revisão pelo chat continuam usando o chat; a inferência local não chama a geração de imagens do ChatGPT.

## Licença

UC significa Uncensored. A variante mantém a **Qwen Research License**, com uso do modelo limitado a pesquisa/avaliação e licença comercial separada exigida pelas cláusulas 2(a) e 2(b). Israel pediu configurar o modelo após ser informado; isso não modifica a licença. Manter essa pendência nos registros de produção e não afirmar que está autorizado para livros vendidos.

Fontes: [variante](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF), [licença original](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/main/LICENSE). Contato comercial indicado: `model-business@notice.qwencloud.com`. Não enviar mensagens ao fornecedor sem pedido explícito.
