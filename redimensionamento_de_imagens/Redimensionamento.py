'''
Pillow: Redimensionamento de várias imagens automaticamente
'''
import os
from PIL import Image

def main(main_images_folder, new_width):
    # Verifica se o caminho existe no computador
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            # caminho completo dos arquivos existentes no caminho passado
            path_file_name = os.path.join(root,file)

            converted_tag = '_CONVERTED' # tag usada para os arquivos que serão convertidos

            #Caso seja necessário apagar os arquivos convertidos pra executar o programa denovo
            # if converted_tag in path_file_name:
            #     print('Imagem convertida deletada!')
            #     os.remove(path_file_name)
            # continue

            file_name, extension = os.path.splitext(file) # Separa o nome do arquivo e sua extensão

            new_file_name = file_name + converted_tag + extension # nome do arquivo que será convertido
            new_path_file_name = os.path.join(root, new_file_name) # caminho completo do arquivo que será convertido

            # verifica se a imagem em questão ja tem sua versão ja convertida
            if os.path.isfile(new_path_file_name):
                print('Já houve conversão dessa imagem!')
                continue

            # verifica se a imagem ja está convertida
            if converted_tag in path_file_name:
                print('Imagem já esta convertida')
                continue


            img_pillow = Image.open(path_file_name) # Abre e identifica o arquivo de imagem fornecido
            width, height = img_pillow.size

            # calcula a nova largura da imagem com base na altura fornecida pelo usuário pelo parâmetro da função (Regra de três)
            new_heigth = round((height * new_width)/width)

            new_image = img_pillow.resize((new_width, new_heigth), Image.LANCZOS)   # Redimensionamento da imagem, Image.LANCZOS -> Filtro de redimensionamento de imagem
            new_image.save(new_path_file_name, optimize=True, quality=70, exif = img_pillow.info['exif']) # Salva a imagem ja convertida
            # exif ->  informações sobre quais foram as condições técnicas (ou configurações) na hora da captura junto ao arquivo da foto

            print('Imagem convertida com sucesso!')
            new_image.close()
            img_pillow.close()


if __name__ == '__main__':
    main_images_folder = r'C:\Users\iaraa\OneDrive\Imagens\minhas fotos\fotos'
    main(main_images_folder, new_width = 600)



