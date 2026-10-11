# Skills públicas de Israel Ermel

Skills para instalar no Codex em outros computadores. Cada pasta em `skills/` é um pacote completo, com `SKILL.md` e seus recursos de apoio.

## Livro profissional

[Ver a skill](skills/livro-profissional/SKILL.md)

Produção editorial em português brasileiro: transcrição e revisão, capas e ilustrações, EPUB/Kindle e impressão, audiobook, Filmora no Mac ou no Windows, legendas e textos para YouTube e cadastro no Amazon KDP. O pacote inclui referências, modelos, imagem de referência e gerador de legendas.

A skill conserva as preferências editoriais de Israel, incluindo voz, composição visual e fluxo de aprovação. Instruções explícitas do projeto prevalecem. Ferramentas de imagem, ElevenLabs, Filmora e validadores de EPUB/PDF dependem da disponibilidade e das licenças no computador; instalar a skill não instala esses aplicativos nem configura credenciais.

## Instalar em outro computador

Abra o Codex no computador de destino e envie:

```text
Use $skill-installer para instalar a skill deste repositório:
https://github.com/israelermel/codex-skills-public/tree/main/skills/livro-profissional
```

A instalação pelo `skill-installer` usa `$CODEX_HOME/skills`, ou `~/.codex/skills` quando `CODEX_HOME` não está definido. Se já existir uma skill com esse nome, preserve a versão local e compare antes de substituir. Depois da instalação, a skill estará disponível no próximo turno.

Para usar:

```text
Use $livro-profissional para trabalhar no meu livro, preservando as decisões e aprovações já registradas.
```

Para atualizar, peça ao Codex que compare a versão instalada com a deste repositório e aplique a atualização preservando eventuais personalizações locais.

## Sincronização da versão mais recente

Toda atualização da `livro-profissional` feita pelo Codex deve ser sincronizada com este repositório na branch `main`, incluindo todos os recursos da skill. Essa regra está no próprio `SKILL.md` e nas instruções de manutenção do repositório. A atualização só é concluída após commit, push e confirmação remota.

O GitHub fica com a versão mais recente; a instalação do outro computador não se atualiza automaticamente. Para obter uma atualização, peça ao Codex que compare a skill instalada com este repositório e aplique as diferenças preservando suas personalizações.

## Conteúdo do repositório

Somente os arquivos da skill e os recursos necessários são publicados aqui. Manuscritos, áudios, vídeos, credenciais e arquivos dos projetos de livros não acompanham o pacote. A capa de exemplo acompanha a skill como referência visual; não constitui permissão de reutilização como capa de outra obra.
