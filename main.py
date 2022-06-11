from pytube import YouTube
import os

link = input('Informe o link do video: ')
#Salvando na pasta vídeos do usuário
pasta = os.path.expanduser("~\Videos")
#Intanciando obejto link para a classe youtube
yt = YouTube(link)

def download_Video():
    #Realizando download com a máxima resolução
    video = yt.streams.get_highest_resolution()
    if video is None:
        print('Necessário digitar um link válido!')
    else:
        while video:
            print('Realizando dowload')
            break
        video.download(output_path=f'{pasta}')
        print('Download efetuado com sucesso!')

if __name__ == '__main__':
    download_Video()