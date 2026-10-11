---
name: kdp-publicar-livros
description: Cadastre, envie e submeta os eBooks de Israel Ermel ao Amazon KDP, individualmente ou em lote, usando as decisões comerciais já autorizadas, sem repetir seleções nem pedir aprovação intermediária. Use para upload/publicação Kindle de livros ou pastas indicados pelo autor; não inclui impressão, YouTube ou produção de novos manuscritos.
---

# Publicar os livros de Israel no Kindle

Execute o cadastro real no KDP até a confirmação de envio para análise. A skill guarda as escolhas; o agente realiza o trabalho nas ferramentas disponíveis. Não há serviço em segundo plano nem upload fora de uma execução solicitada.

## Escolhas e autorização permanentes

Israel pediu em **10/10/2026**: “quero apenas executar a skill e vc fazer tudo sem eu precisar selecionar as respostas” e “quero que essa skill fazca o upload de todos eles”. Este pedido autoriza reutilizar as escolhas abaixo e **submeter para análise/publicação os livros que ele indicar em cada execução**, sem perguntar novamente se pode publicar. Um pedido atual de “apenas preparar”, “rascunho” ou qualquer alteração explícita prevalece. A descoberta automática desta skill sozinha não autoriza publicar livros: é necessário um pedido do usuário para executar upload/publicação ou invocar a skill com esse objetivo.

| Campo | Escolha autorizada |
|---|---|
| Direitos | Direitos próprios do autor para seus livros indicados; não domínio público |
| Loja principal | Amazon.com.br |
| Preço de lista | **R$ 5,99** |
| Plano de royalties | **70%**, conforme elegibilidade vigente |
| KDP Select | **Sim**, com exclusividade digital de 90 dias |
| Territórios | **Somente Brasil**, nunca direitos globais por padrão |
| DRM | **Sem DRM**, permitindo EPUB/PDF para compradores quando oferecido pelo KDP |
| Lançamento de um título novo | Disponibilizar após aprovação da Amazon; sem pré-venda |
| Operação final | Enviar para análise/publicação; não parar no rascunho salvo por padrão |
| Aprovações de produção/cadastro | Dispensadas nesta rotina; não pedir revisão de descrição, capa ou seleção comercial já decidida |

As escolhas vieram das respostas “Sim, direitos próprios e Amazon.com.br”, “Sem DRM, permitir EPUB/PDF”, “R$ 5,99”, “Com KDP Select e plano de 70%”, “Vender somente no Brasil” e “Sim, enviar para publicação”, seguidas do pedido de reutilização para os outros livros. Não atribua uma aprovação individual fictícia a cada obra: registre **autorização pelo perfil desta skill e pelo pedido de execução atual**.

O nome literário recorrente é **Vorne Ermel** e o idioma recorrente é português brasileiro. Confira ambos na edição de cada livro. Título, subtítulo, série, edição, colaboradores, descrição, palavras-chave, categorias, conteúdo explícito, faixa etária, uso de IA e acessibilidade são **fatos de cada obra**, não respostas fixas a copiar de Ecos da Névoa. Responda com base nos arquivos e no processo documentado, sem perguntar quando a informação estiver disponível.

## Execução de um livro ou lote

Leia [o procedimento operacional](references/procedimento.md) antes de operar o KDP. Confira requisitos atuais na interface e nas fontes oficiais ali indicadas; não use índices de UI, preços mínimos ou categorias históricos como regras atuais.

1. Delimite o lote pelo pedido atual: livro aberto, lista de pastas ou diretório explicitamente indicado. Acesso a uma pasta não inclui automaticamente todos os seus livros no lote. Se for pedido “todos os livros nesta pasta”, inventarie os projetos atuais nela, excluindo histórico, backups, originais alternativos e duplicatas. Não transforme a quantidade aproximada “10” em dez títulos inventados.
2. Localize por obra o EPUB final, a capa Kindle, o manuscrito, os metadados e registros de produção/cadastro. Reutilize os arquivos vigentes; nomes e datas sozinhos não comprovam a edição correta. Prepare descrição, palavras-chave e campos ausentes que possam ser obtidos do texto, dentro do escopo de cadastro. Não regenere o livro, audiobook, vídeo, PDF ou arte sem necessidade/pedido.
3. Consulte a Biblioteca KDP e o registro local antes de criar um título. Retome o rascunho correspondente. Para obra já em revisão, publicando ou à venda, registre o estado e pule uma nova submissão; atualizar uma edição à venda exige pedido correspondente. Não duplique Ecos da Névoa, já enviado anteriormente.
4. Cadastre e envie **um livro por vez** na sessão autenticada do titular. Aplique as escolhas acima, valide os arquivos e a prévia, salve e confira a persistência dos campos antes da submissão. Prossiga até a confirmação real e o estado na Biblioteca, sem nova autorização.
5. Atualize o registro de cada livro logo após seu envio e depois avance ao seguinte. Em bloqueio específico, preserve o rascunho, registre o motivo e continue os demais livros independentes. Interrompa a operação da conta somente quando o impedimento afetar todo o lote.

## Retomada, limites e relato

Use `editorial/cadastro-kdp-sessao.json` por projeto ou o registro existente equivalente. Guarde caminhos/hashes, decisões aplicadas, ID KDP, confirmações de processamento, inspeção da prévia, submissão e estado observado. Sem credenciais, dados fiscais/bancários ou tokens temporários de prévia. Atualize o registro global de produção existente em `~/.Codex/specs/<projeto>/`; para um lote, mantenha também `~/.Codex/specs/kdp-publicacao-livros/lote.json` com pasta/ID/estado por obra. Esses registros são checkpoints, não prova substituta da interface.

Não pergunte novamente pelas escolhas salvas. Peça intervenção apenas para um impedimento concreto que não possa resolver: acesso/login/2FA do titular, edição final ambígua, arquivo ausente, evidência contraditória de direitos/exclusividade ou regra atual que rejeite R$ 5,99/70%/Brasil/sem DRM. Não altere as escolhas silenciosamente para contornar rejeição. Não contrate serviço, anúncio ou assinatura paga.

Após um resultado incerto do botão de publicação, consulte a Biblioteca antes de repetir qualquer envio. Se o estado continuar inconclusivo, registre-o e pare **esse livro**; não crie outro título para tentar novamente.

Finalize com tabela curta por obra: enviada/em revisão, já existente, rascunho bloqueado ou disponível para compra. Inclua IDs/links verificados e os impedimentos reais. **“Enviado” não significa “à venda”**: só afirme disponibilidade após verificação. Não prometa aprovação nem prazo fixo. Não crie agendamento para acompanhar a análise sem pedido do usuário.

## Integração com a produção editorial

A skill complementar [livro-profissional](../livro-profissional/SKILL.md) conduz revisão, capas, EPUB e derivados. Ao receber um livro produzido por ela, reutilizar a edição vigente, os hashes, o pacote `entrega/kdp/` e o registro de produção. Se o pedido atual for somente produzir ou preparar o livro, não iniciar a publicação. Se incluir envio ao KDP, aplicar esta rotina às obras indicadas, sem repetir decisões comerciais já autorizadas. Uma edição ausente ou ambígua continua sendo impedimento concreto; não criar um novo manuscrito para contorná-lo.

## Manutenção e sincronização pública

Toda alteração autorizada nesta skill e seus recursos inclui sincronização do pacote completo em `https://github.com/israelermel/codex-skills-public`, branch `main`, pasta `skills/kdp-publicar-livros`, antes de declarar a atualização concluída. Fazer commits pequenos e focados e push da origem versionada e da cópia pública, sem pedir confirmação adicional. Preservar mudanças alheias, validar a skill e os links e confirmar o commit remoto. Publicar somente recursos da skill, nunca credenciais, dados fiscais/bancários ou materiais dos livros. Se o envio falhar, reportar a pendência. As instalações em outro computador precisam ser atualizadas separadamente.
