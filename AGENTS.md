# Manutenção das skills públicas

Ao atualizar `livro-profissional` ou `kdp-publicar-livros`, sincronizar o pacote completo na pasta `skills/<nome-da-skill>`, incluindo referências, modelos, scripts, assets e remoções intencionais. A origem nesta máquina fica em `/Users/israelermel/.agents/skills/<nome-da-skill>`; localizar a instalação equivalente em outros computadores.

Toda atualização autorizada dessas skills inclui commit e push para `israelermel/codex-skills-public`, branch `main`, sem pedir confirmação adicional. Validar a skill e os links internos, executar checks adequados para scripts alterados e confirmar o commit remoto antes de declarar conclusão. Commits devem ser pequenos e focados; não incluir mudanças de outros trabalhos.

A cópia pública deve usar referências portáteis. Em `references/licoes-do-projeto.md`, substituir o prefixo local dos exemplos históricos por `<pasta-do-livro>/`. Publicar somente recursos da skill; nunca credenciais, manuscritos, áudios, vídeos ou arquivos dos projetos. Se a sincronização falhar, informar a pendência.

O envio ao GitHub mantém a versão pública atualizada; instalações em outro computador precisam receber a atualização separadamente.
