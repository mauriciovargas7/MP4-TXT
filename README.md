🎬📊 Automação de Transcrição e Resumo de Vídeos com IA

⚠️ Observação: Este projeto foi desenvolvido como uma automação prática utilizando Inteligência Artificial para transformar vídeos em conteúdo estruturado (transcrição + resumo), simulando um fluxo real de produtividade.

🚀 Sobre o projeto

Este script automatiza todo o processo de:

➡️ Processamento de vídeos
➡️ Extração de áudio
➡️ Transcrição automática com IA
➡️ Geração de resumos detalhados
➡️ Organização e consolidação dos resultados

A solução transforma vídeos longos em conteúdo textual estruturado, ideal para estudos, documentação ou criação de conteúdo.

⚙️ Funcionalidades

🎥 Identificação automática de arquivos .mp4 na pasta

✂️ Divisão do vídeo em múltiplos segmentos

🔊 Conversão de vídeo para áudio (.mp3)

🧠 Transcrição automática com IA (OpenAI Whisper)

📝 Geração de resumos detalhados em tópicos

📂 Organização automática dos arquivos gerados

📄 Consolidação de transcrições completas

📊 Consolidação de resumos em um único arquivo

🧹 Limpeza automática de arquivos temporários

🛠️ Tecnologias utilizadas

Python

MoviePy

OpenAI API (Whisper + GPT)

OS / File System

Datetime

🔄 Fluxo da automação
1. Script identifica automaticamente um vídeo (.mp4)
2. Divide o vídeo em partes menores
3. Converte partes do vídeo em áudio (.mp3)
4. Envia o áudio para transcrição via IA (Whisper)
5. Salva a transcrição completa (.txt)
6. Envia o texto para geração de resumo (GPT)
7. Salva os resumos em arquivos separados
8. Consolida todos os textos FULL em um único arquivo
9. Consolida todos os RESUMOS em um único arquivo
10. Remove arquivos temporários automaticamente

📁 Estrutura de saída
📂 projeto/
│
├── video.mp4
├── 2026-XX-XX_video_FULL.txt        # Transcrição completa consolidada
├── 2026-XX-XX_video_RESUMO.txt      # Resumo consolidado
├── (arquivos intermediários removidos automaticamente)

▶️ Como executar

Instale as dependências:

pip install moviepy openai


Configure sua API Key da OpenAI:

openai.api_key = "SUA_API_KEY"


Coloque um arquivo .mp4 na pasta do script

Execute:

python script.py

💡 Aplicações

📚 Estudo de aulas e cursos gravados

🎙️ Transcrição de reuniões

🎥 Criação de conteúdo (YouTube, TikTok, etc.)

📄 Documentação automática de vídeos

🧠 Resumo inteligente de conteúdos longos

📈 Benefícios

⏱️ Economia de tempo na análise de vídeos longos

🤖 Automação completa com IA

📊 Conteúdo estruturado pronto para uso

🔄 Processo reutilizável e escalável

⚠️ Observações

É necessário uma API Key válida da OpenAI

O modelo text-davinci-003 pode ser atualizado conforme versões mais recentes

O script considera apenas o primeiro .mp4 encontrado na pasta

Arquivos grandes podem impactar tempo de processamento

🔥 Diferencial

Este projeto demonstra na prática a integração de:

Automação de processos (RPA)

Manipulação de mídia (vídeo/áudio)

Inteligência Artificial aplicada (transcrição + NLP)

👉 Transformando conteúdo bruto em informação estruturada de forma totalmente automatizada.
