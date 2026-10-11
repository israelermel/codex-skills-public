# Narração e vídeo ilustrado

## Voz, scripts e credenciais

A preferência atual de Israel para novas produções é **ElevenLabs em português brasileiro, modelo Eleven v4 (`eleven_v4`), voz `rwMvgbQxwV0LJTium7sd` (Lucy Fennek — Immersive and Inviting)**, escolhida pelo usuário em 05/10/2026 em substituição ao padrão anterior, por script com cache e alinhamento de caracteres. [Voz indicada pelo autor](https://elevenlabs.io/voices/rwMvgbQxwV0LJTium7sd). Voz reafirmada junto ao modelo v4 pelo autor em 11/10/2026. Use essa combinação como padrão nas novas narrações, salvo escolha explícita diferente para o projeto. Não peça novamente a escolha da voz ou do modelo; avalie ritmo, pronúncias e interpretação na amostra de 60–90 segundos antes do lote. A consulta de metadados em 05/10/2026 confirmou esse ID e nome, com idioma de origem `de-DE`; isso não comprova a qualidade em pt-BR. Avalie especialmente sotaque e nomes brasileiros na amostra. Verifique a disponibilidade da voz e os modelos/parâmetros aceitos antes de uma nova chamada, sem trocar o ID silenciosamente.

Para v4, consulte a [documentação de modelos](https://elevenlabs.io/docs/overview/models) e o [Text to Dialogue com timestamps](https://elevenlabs.io/docs/api-reference/text-to-dialogue/convert-with-timestamps). Envie a voz nos `inputs`, `model_id: eleven_v4` e `language_code: pt`; guarde alinhamento e request ID. Os controles desse endpoint usam `settings`; não copie `voice_settings`, `style`, `speed` ou `use_speaker_boost` de um preset v2 sem suporte confirmado. Direção expressiva deve acompanhar o gênero, com texto falado preservado e tags separadas no registro. Valide a interpretação em pt-BR pela amostra antes do lote. Verifique saldo e custo estimado de todas as obras; não habilite excedentes ou compre créditos para concluir um lote sem autorização correspondente.

Escolhas de projeto preservadas: A Água do Despertar e A Casa Onde Guardamos o Amanhã têm voz `mPDAoQyGzxBSkE0OAOKw` com `eleven_v4` por pedido específico registrado. Não trocar essas escolhas pelo padrão global sem novo pedido do autor.

Referência histórica de Luz de Cristal: a voz escolhida e aprovada naquele projeto foi `mPDAoQyGzxBSkE0OAOKw` (identificada como Carla — Energetic and Confident), modelo `eleven_multilingual_v2`. Configuração aprovada naquele projeto: stability `0.55`, similarity boost `0.8`, style `0`, speed `1.0`, speaker boost ativado. Esse preset histórico não comprova a configuração nem a qualidade da nova voz escolhida; ajuste modelo e parâmetros conforme disponibilidade e avaliação da amostra.

Preserve a voz aprovada do projeto ao retomar. Thalita (`pt-BR-ThalitaMultilingualNeural`, via Edge/Azure quando disponível) pertence ao fluxo anterior e continua válida em projetos que a aprovaram; não a use como substituição silenciosa se ElevenLabs falhar. A nova voz padrão não autoriza trocar ou regenerar audiobooks já aprovados.

- Teste 60–90 segundos incluindo **título do livro, autor, número/título do capítulo e nomes próprios**. A rejeição anterior foi de sotaques de outros idiomas, mesmo com ritmo aprovado. Corrija a amostra antes do lote e mantenha a aprovação existente quando a configuração não mudou.
- Reutilize script/configuração já disponíveis; descoberta do runtime local, sem caminhos Python de outra máquina embutidos no gerador. Separe texto falado de rubricas e ajustes de pronúncia.
- Procure credencial já configurada sem imprimir seu conteúdo. No caso de origem, o script usava `~/.config/elevenlabs/api_key`. Preferir cofre, ambiente existente ou arquivo privado (`0600`); nunca gravar chave literal no script, comandos, logs, Git ou chat.
- Se faltar chave, fornecer configuração local com entrada oculta (`getpass`/`read -s`) e verificar somente presença/autenticação. Nunca pedir que o autor envie a chave. Para um comando colado no zsh, não iniciar com `#!/bin/bash`: shebang pertence a arquivo executável, não à linha interativa. Não escapar `_` em caminhos reais.
- Guardar por bloco: ID, texto e hash, provedor/voice ID/modelo/settings, fingerprint, áudio/hash/duração e alinhamento original com caracteres/inícios/fins. Registrar progresso em disco e retomar apenas blocos ausentes ou inválidos, sem cobrar nova geração de trechos já válidos.
- Repetições de erro devem interromper o lote com diagnóstico; não trocar voz/provedor silenciosamente. Antes de um lote pago novo, respeitar orçamento e autorização existentes. Não prometer licença comercial sem verificar o plano/termos aplicáveis ao destino.
- Avisar quando a geração de voz terminar e distinguir esse marco da montagem/exportação do vídeo. Uma notificação futura exige um mecanismo real de acompanhamento, não uma promessa sem execução.

## Direção expressiva

Objetivo: a voz conversa com o ouvinte, desperta curiosidade e sustenta a escuta com clareza, calor humano e variação natural. Engajamento vem da interpretação coerente com o texto, sem inventar chamadas ou dramatização.

| Passagem | Direção desejada |
|---|---|
| Convite e abertura | Acolhedora, próxima, com energia moderada |
| Pergunta e descoberta | Curiosidade, pausa curta e variação de entonação |
| Reflexão | Ritmo mais tranquilo, espaço entre ideias |
| Explicação | Clareza, continuidade e ênfase nos termos essenciais |
| Lembrança delicada | Suavidade, sem melodrama ou sussurro constante |
| Conclusão motivadora | Convicção serena, crescendo discreto e pausa de fechamento |

Use inicialmente cerca de 140–165 palavras/minuto, ajustando pela amostra e pelo gênero. Evite uma leitura inteira com taxa fixa excessivamente lenta, volume artificialmente alto ou pitch alterado para simular emoção. Esses números são diretrizes artísticas, não requisitos de plataforma.

Prepare amostra de 60–90 segundos com uma pergunta, uma reflexão e uma conclusão; permita avaliar pronúncias de nomes e palavras recorrentes. Mostre áudio reproduzível e texto correspondente. Quando houver escuta disponível, ouça antes de apresentar; metadados não provam naturalidade. Registre o que foi ouvido e a avaliação do autor.

## Roteiro e integridade

- Derive `audiobook-text/` do `livro.md` aprovado. Use IDs estáveis por seção, sem fixar quantidade de capítulos; inclua abertura, introdução, capítulos, notas e encerramento conforme o conteúdo real.
- Guarde direção de voz em campos separados do texto falado. A narração é uma interpretação do texto, não uma nova versão editorial. Não mude gênero gramatical, autobiografia ou pessoa narrativa do autor só porque a voz é feminina.
- Expanda números, unidades e siglas quando ajudar a pronúncia; registre equivalências. Defina pronúncias de nomes com o autor se não forem claras. URLs, tabelas, notas e imagens precisam de adaptação audível explícita; não elimine conteúdo para encurtar o livro.
- Créditos de abertura/encerramento devem corresponder aos dados reais. Diferencie autoria e voz sintética; não atribua a autoria à voz nem apresente síntese como interpretação humana contratada.
- Registre hash do manuscrito e de cada roteiro. Se o manuscrito mudar, reconcilie os roteiros afetados antes de gerar áudio; anexar o hash novo a um roteiro velho não demonstra sincronização.
- Divida em limites de parágrafo/frase e respeite limites atuais do serviço. Preserve continuidade nas fronteiras; não corte palavras.

## Geração e conferência do audiobook

Use cache por hash do texto efetivamente enviado, provedor, voz, modelo/configuração e parâmetros. Grave primeiro em temporário; valide antes de promover à edição final. Retome apenas trechos válidos, com tentativas limitadas e recuo progressivo; falha persistente deve ficar visível, sem trocar a voz como fallback silencioso.

Preserve os blocos de áudio para importação separada na timeline; gerar um MP3 único não é pré-requisito para editar no Filmora. Entregue faixa integral separada somente quando solicitada. Quando uma conversão for necessária, use intermediário sem perdas e codifique apenas na saída final. Escolha taxa de amostragem, canais, codec, loudness, picos e limites de ruído segundo a plataforma de destino; não confunda MP3 de distribuição local com master aceito por qualquer loja. Reencodar áudio de baixa qualidade em bitrate maior não recupera detalhe.

Verifique:

- Decodificação de todos os arquivos e duração plausível por trecho/capítulo.
- Correspondência de quantidade, IDs, ordem e texto falado previsto; ausência de repetição ou truncamento nas junções.
- Metadados de palavras do TTS, quando disponíveis, comparados ao texto enviado. Rotule isso como **conferência dos metadados**, nunca como transcrição independente do áudio.
- Escuta das amostras, começos/finais e junções de cada capítulo, nomes e passagens expressivas. Transcrição independente, se disponível, ajuda a localizar omissões, mas também tem erros e não substitui a escuta.
- Clipping, silêncios indevidos, ruído, loudness consistente e ausência de rubricas faladas. Registre medições e duração final efetivas.

## Vídeo do audiobook

Por padrão para vídeo horizontal: 1920×1080, 16:9, 25 fps constantes neste fluxo Filmora (preservar outra taxa já escolhida no projeto), MP4/H.264, `yuv420p`, AAC e, quando disponível, `faststart` para distribuição web, salvo outro destino. Confirme o destino quando ele mudar o resultado; vídeo de audiobook integral não é automaticamente um trailer ou Reel.

Associe cada capítulo à sequência de cenas aprovada no [roteiro visual](publicacao.md#ilustrações-de-capítulos), e cada cena ao trecho correspondente do áudio vigente, com início e fim na timeline. Troque de imagem acompanhando acontecimentos, mudanças de lugar/tempo ou ideias da narração; não use uma imagem única como padrão para o capítulo inteiro, nem distribua duas ou três imagens em intervalos iguais só para cumprir quantidade. Preserve a ordem narrativa e confira as transições dentro dos capítulos, além das passagens entre capítulos. A preferência atual é **imagens estáticas e cortes diretos, sem zoom, pan ou transições** para acelerar a exportação. Não adicionar efeitos para alegar acabamento profissional. Use títulos legíveis; preserve enquadramento e margens. Se o autor pedir movimento/transições, ajuste o piloto e registre a exceção. Música só quando pedida ou aprovada, com direitos de uso e volume que preserve a inteligibilidade.

A duração visual deve cobrir todo o áudio. Não use `-shortest` para mascarar divergências e truncar narração. Ao ajustar para quadros inteiros, acrescente no máximo o silêncio tecnicamente necessário, registrando-o; nunca remova amostras de fala. Valide o piloto antes da renderização integral.

Normalize parâmetros dos segmentos, verifique timestamps e concatene de forma que preserve continuidade de áudio. Erros de DTS/PTS, seek ou cortes em quadros B exigem correção e nova decodificação. Desativar quadros B foi uma solução do projeto de origem, não uma regra universal de qualidade.

Gere capítulos individuais e edição integral quando solicitados. Derive horários da timeline renderizada, não de estimativas do roteiro. Para vídeo de YouTube, entregue sempre legendas completas em SRT com tempos da fala; VTT como alternativa. Use os alinhamentos já guardados e os offsets da timeline, conforme [legendas para YouTube](youtube.md#legendas-completas-da-narração). Não gravar na imagem nem reexportar o MP4 para um simples upload de SRT. Para entrega destinada ao YouTube, inclua miniatura e o [pacote de textos de publicação](youtube.md); não publique automaticamente.

Confira vídeo completo por decodificação e duração, além de quadros iniciais, intermediários, finais e de todas as trocas de cena e de capítulo. Compare a timeline com a narração integral e registre hashes dos áudios de origem. Se houve AAC/reencodificação, não espere hashes idênticos no áudio embutido: confira duração, alinhamento e conteúdo. Declare as verificações realizadas e as limitações de escuta/revisão visual.

A edição no aplicativo, as cartelas, a exportação e as verificações estão em [Filmora](filmora.md). Registre o que foi realmente executado: se a conferência visual/decodificação do vídeo foi por amostragem, não a descreva como revisão integral.
