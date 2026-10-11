---
name: narracao-livro
description: Gere narracao local MOSS-TTS em blocos MP3 numerados de capitulos Markdown para montagem no Filmora.
---

# Narracao local para Filmora

Descubra o Python do ambiente MOSS-TTS instalado nesta maquina. Execute scripts/narrar.py com esse Python; nao use o ambiente de outro projeto. O modelo e Local Transformer 1.7B e requer CUDA neste helper.

Leia config.json. Preserve a referencia feminina brasileira aprovada localmente; esta distribuicao publica nao inclui audio pessoal. Se nao houver referencia nesta maquina, configure um audio fornecido pelo usuario com `--set-voice AUDIO`, gere amostra e obtenha avaliacao de timbre/sotaque. pt-BR no JSON e preferencia, nao seletor garantido do modelo.

Use `--files CAP1.md CAP2.md --output PASTA` ou `--list LISTA.txt --output PASTA`; lista UTF-8 com caminhos por linha, relativos a ela. Use --dry-run para verificar agrupamento. Os blocos agrupam paragrafos em aproximadamente 1000 caracteres sem cortar frases. Preserve conteudo e adapte explicitamente tabelas/codigo antes de narrar. Nao transforme rubricas em fala.

Entregue MP3 192 kbps separados e numerados em blocos/<capitulo>/, com manifesto de texto, duracao e hashes. Nao concatene: usuario monta as juncoes no Filmora. Preserve WAV internos e retome apenas trechos ausentes ou invalidos. Mudanca de agrupamento nao apaga audios anteriores. FFmpeg deve estar no PATH.

O helper usa referencia codificada em cache e move o codec para CPU durante geracao, mantendo precisao e sampling. Nao reduza codebooks nem troque modelo/voz para acelerar sem avaliacao. Verifique audios e reporte medidas reais; nao alegue escuta, transcricao ou conformidade de plataforma sem verifica-las. Esta skill nao publica livros nem inicia geracoes sem pedido.

## Perfil atual Qwen3-TTS

Israel aprovou Qwen3-TTS 0.6B Base com Carla. Para novas narracoes usar scripts/narrar_qwen.py com runtime e referencia/transcricao configurados nesta maquina. Clonagem completa, CUDA BF16 SDPA, MP3 256 kbps em blocos, sem aceleracao posterior. Substitui o helper MOSS acima. Kokoro foi desinstalado; nao reinstalar automaticamente. Nao iniciar lotes sem pedido.

Perfis em config.json permitem --voice carla ou --voice bruna. Configurar referencia/transcricao localmente e marcar approved apos avaliar amostra. Manter default_voice se nao houver escolha; nao substituir voz de projetos existentes. Referencias pessoais nao acompanham a distribuicao publica.

Perfis adicionais: Bruna foi aprovada no computador de origem; Ana Alice (`ana-alice`) foi cadastrada para teste. Consultar status e referencias locais em config.json; nao presumir que os audios pessoais estao instalados em outra maquina.

Carla, Bruna e Ana Alice foram aprovadas no computador de origem. Aceitar escolha pelo nome e usar --voice carla, --voice bruna ou --voice ana-alice. A distribuicao publica nao inclui referencias pessoais; configurar essas referencias em cada maquina. Carla permanece padrao.
