import cv2
import numpy
import matplotlib.pyplot as plt


def dadosImagem(imagem):
    print("\nLargura em pixels: ", end='')
    print(imagem.shape[1]) # largura da imagem
    print("Altura em pixels: ", end='')
    print(imagem.shape[0]) # altura da imagem
    print("Qtde de canais: ", imagem.shape[2]) # Quantidade de Canais da Imagem - Imagem colorida possui 3 canais RGB

    (b, g, r) = imagem[0,0] # RGB de pixel especifico
    print("cor RGB de pixel especifico:", end="")
    print("Azul: ", b , end="")
    print(" Verde: ", g,  end="")
    print(" Vermelho: ", r )
    print("Corpo", imagem.shape)
    print("Tamanho", imagem.size)
    print("Número de dimensões", imagem.ndim)


def separarCamada(imagem):
    #Cria uma matriz do tamanho da imagem contendo somente 0
    canalBlue = canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)     
    canalGreen = canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)
    canalRed = canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)

    canalBlue[:,:,0] = imagem[:,:,0]    #copia o canal azul para a nova matriz
    canalGreen[:,:,1] = imagem[:,:,1]
    canalRed[:,:,2] = imagem[:,:,2]

    return canalBlue , canalGreen, canalRed

def transformarCinza(imagem):
    canalGray = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            canalGray[i,j] = int(imagem[i, j].sum() // 3)
    
    return canalGray

def plotGrafico(imagem):

    pixel = 256*[0] #Define eixo x
    for i in range(256):
        pixel[i]=i

    plt.xlabel('pixel')  #nome eixo x
    plt.ylabel('quantidade') #nome eixo y
    plt.title('histograma da imagem em tons de Cinza') #Titulo do plot

    histograma = numpy.zeros(256, dtype=int)        #Cria o histograma da imagem
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            histograma[imagem[i,j]] += 1

    plt.bar(pixel,histograma ,color ='blue')
    plt.show()


def main():

    imagem = cv2.imread("imagens/Wolf and moon poster.jpg")

    dadosImagem(imagem)
    canalBlue, canalGreen, canalRed = separarCamada(imagem)
    canalGray = transformarCinza(imagem)
    plotGrafico(canalGray)


    cv2.imwrite("imagens/saida.jpg", imagem)
    cv2.imshow("Canal Blue", canalBlue)
    cv2.imshow("Canal Green", canalGreen)
    cv2.imshow("Canal Red", canalRed)
    cv2.imshow("Canal gray", canalGray)
    cv2.imwrite("imagens/saida.jpg",canalGray)
    cv2.waitKey(0)

if __name__ =='__main__':
    main()