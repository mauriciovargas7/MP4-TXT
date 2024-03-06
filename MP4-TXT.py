import openai
from moviepy.editor import *
import os
from datetime import datetime
import moviepy.editor as mpy
from moviepy.editor import AudioFileClip

# -------------Busca arquivo mp4

arquivo_mp4 = []
for file in os.listdir('.'):
    if file.endswith('.mp4'):
        arquivo_mp4.append(file)
if arquivo_mp4:
    arquivo_mp4 = arquivo_mp4[0]
    print(f"Arquivo .mp4 encontrado: {arquivo_mp4}")
else:
    input("Nenhum arquivo .mp4 encontrado na pasta, aperte Enter para continuar")
arquivo_mp3 = arquivo_mp4[:-4] + ".mp3"
pasta_atual = os.getcwd()

arquivo_mp4_caminho = pasta_atual + '\\' + arquivo_mp4


# -------------Dividindo arquivo mp4

def divide_video(video_path, output_path, duration):
    """
    Divide um vídeo em vários vídeos de duração específica.

      video_path: Caminho do vídeo.
      output_path: Caminho para a pasta onde os vídeos divididos serão salvos.
      duration: Duração de cada vídeo dividido.

    """

    video = mpy.VideoFileClip(video_path)
    duration_in_seconds = duration * 60

    # Calcula o número de vídeos que serão criados.
    num_videos = int(video.duration / duration_in_seconds)

    # Cria uma lista para armazenar os caminhos dos vídeos divididos.
    output_files = []

    # Itera sobre os vídeos divididos.
    for i in range(num_videos):
        # Obtém o início e o fim do vídeo dividido.
        start_time = i * duration_in_seconds
        end_time = start_time + duration_in_seconds

        # Cria um novo vídeo com o trecho selecionado.
        output_file = video.subclip(start_time, end_time)

        # Salva o vídeo dividido.
        output_file.write_videofile(os.path.join(output_path, f"video_{i:03d}.mp4"))

        output_files.append(output_file)

    return output_files


video_path = arquivo_mp4_caminho
output_path = pasta_atual
duration = 10
output_files = divide_video(video_path, output_path, duration)

# -------------Salvando videos em áudio
for arquivo in os.listdir(pasta_atual):
    if arquivo.endswith(".mp4") and "video_0" in arquivo:
        caminho_video = os.path.join(pasta_atual, arquivo)
        with AudioFileClip(caminho_video) as clipe_audio:
            caminho_mp3 = os.path.splitext(caminho_video)[0] + ".mp3"
            clipe_audio.write_audiofile(caminho_mp3)

# -------------Transcrição de áudio e geração de resumo
for arquivo in os.listdir(pasta_atual):
    if arquivo.endswith(".mp3") and "video_0" in arquivo:
        openai.api_key = 'INSIRA SUA KEY'

        # Utilize o gerenciamento de contexto para abrir o arquivo de áudio
        with open(arquivo, 'rb') as audio_file:
            transcript = openai.Audio.transcribe('whisper-1', audio_file)

        data_atual = datetime.now()
        data_arquivo = data_atual.strftime("%Y-%m-%d")
        nome_do_arquivo_txt_completo = data_arquivo + "_" + arquivo[:-4] + '_FULL' + '.txt'
        texto_para_salvar = transcript.text

        try:
            with open(nome_do_arquivo_txt_completo, 'w') as arquivo_txt:
                arquivo_txt.write(texto_para_salvar)
        except Exception as e:
            print("Ocorreu um erro:", str(e))

        # -------------Abrindo TXT para API fazer o resumo

        nome_do_arquivo_txt_resumido = data_arquivo + "_" + arquivo_mp3[:-4] + '_RESUMO_' + arquivo[-7:-4] + '.txt'

        with open(nome_do_arquivo_txt_completo, 'r') as file:
            file_content = file.read()
        prompt = f"Por favor, faça um resumo desse texto de forma extremamente detalhada e em tópicos usando o caracter '-' para marcar os tópicos:\n\n{file_content}"

        # -------------Chamando API do python

        response = openai.Completion.create(
            engine="text-davinci-003",  # modelo será atualizado
            prompt=prompt,
            max_tokens=1024
        )

        # -------------salvando TXT com resposta
        texto_para_salvar = response.choices[0].text.strip()

        try:
            with open(nome_do_arquivo_txt_resumido, 'w') as arquivo_txt:
                arquivo_txt.write(texto_para_salvar)
            print(f"A string foi salva como '{nome_do_arquivo_txt_resumido}' com sucesso.")


        except Exception as e:
            print("Ocorreu um erro:", str(e))
            pass  ##############################


# --------- JUNTA TODOS ARQUIVOS TXT FULL

def juntar_txt_full(diretorio, arquivo_saida):
    """
    Junta todos os arquivos .txt que contêm '_FULL_' no nome, no diretório especificado,
    em um único arquivo.

    :param diretorio: Caminho para o diretório que contém os arquivos .txt.
    :param arquivo_saida: Caminho do arquivo de saída onde todos os textos serão unidos.
    """
    with open(arquivo_saida, 'w') as saida:
        # Itera sobre todos os arquivos no diretório
        for nome_arquivo in os.listdir(diretorio):
            # Verifica se o arquivo é um arquivo .txt e contém '_FULL_'
            if nome_arquivo.endswith('.txt') and '_FULL' in nome_arquivo:
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                with open(caminho_arquivo, 'r') as entrada:
                    # Escreve o conteúdo de cada arquivo no arquivo de saída
                    saida.write(entrada.read() + '\n\n')


diretorio = os.getcwd()
arquivo_saida = data_arquivo + "_" + arquivo_mp4[:-4] + '_FULL' + '.txt'
juntar_txt_full(diretorio, arquivo_saida)


# --------- JUNTA TODOS ARQUIVOS TXT RESUMO


def juntar_txt_resumo(diretorio, arquivo_saida):
    """
    Junta todos os arquivos .txt que contêm '_RESUMO_' no nome, no diretório especificado,
    em um único arquivo.

    :param diretorio: Caminho para o diretório que contém os arquivos .txt.
    :param arquivo_saida: Caminho do arquivo de saída onde todos os textos serão unidos.
    """
    with open(arquivo_saida, 'w') as saida:
        # Itera sobre todos os arquivos no diretório
        for nome_arquivo in os.listdir(diretorio):
            # Verifica se o arquivo é um arquivo .txt e contém '_RESUMO_'
            if nome_arquivo.endswith('.txt') and '_RESUMO_' in nome_arquivo:
                caminho_arquivo = os.path.join(diretorio, nome_arquivo)
                with open(caminho_arquivo, 'r') as entrada:
                    # Escreve o conteúdo de cada arquivo no arquivo de saída
                    saida.write(entrada.read() + '\n\n')


arquivo_saida = data_arquivo + "_" + arquivo_mp4[:-4] + '_RESUMO' + '.txt'
juntar_txt_resumo(diretorio, arquivo_saida)

print(f"Arquivo {arquivo_saida} salvo com sucesso!")


# --------- Excluindo arquivos desnecessários

def excluir_arquivos_com_palavra_chave(diretorio, palavra_chave):
    """
    Exclui todos os arquivos no diretório especificado que contêm a palavra-chave no nome.

    :param diretorio: Caminho para o diretório onde os arquivos estão localizados.
    :param palavra_chave: Palavra-chave para procurar nos nomes dos arquivos.
    """
    for nome_arquivo in os.listdir(diretorio):
        if palavra_chave in nome_arquivo:
            os.remove(os.path.join(diretorio, nome_arquivo))
            print(f"Excluído: {nome_arquivo}")


diretorio = pasta_atual
excluir_arquivos_com_palavra_chave(diretorio, 'RESUMO_0')
excluir_arquivos_com_palavra_chave(diretorio, 'video_00')
