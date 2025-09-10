import cv2
import numpy
import matplotlib.pyplot as plt
import numpy as np

def dadosImagem(imagem):
    print("\nLargura em pixels: ", end='')
    print(imagem.shape[1]) # Largura da imagem
    print("Altura em pixels: ", end='')
    print(imagem.shape[0]) # Altura da imagem
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
    canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)     
    canalGreen = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)
    canalRed = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)

    canalBlue[:,:,0] = imagem[:,:,0] #Copia o canal azul para a nova matriz
    canalGreen[:,:,1] = imagem[:,:,1]
    canalRed[:,:,2] = imagem[:,:,2]

    return canalBlue[:,:,0] , canalGreen[:,:,1], canalRed[:,:,2]

def transformarCinza(imagem):
    canalGray = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            canalGray[i,j] = int(imagem[i, j].sum() // 3)
    return canalGray

def histograma(imagem, cor):
    pixel = 256*[0] #Define eixo x
    for i in range(256):
        pixel[i]=i

    plt.xlabel('Pixel')  #Nome eixo x
    plt.ylabel('Quantidade') #Nome eixo y
    plt.title('Histograma da imagem') #Titulo do plot

    histograma = numpy.zeros(256, dtype=int) #Cria o histograma da imagem
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            histograma[imagem[i,j]] += 1

    plt.bar(pixel, histograma, color = cor)
    plt.show()

# Codigo do professor
def hist(imagem, canal):
    pixel = 256*[0] #Define eixo x
    for i in range(256):
        pixel[i]=i

    plt.xlabel('Pixel')  #Nome eixo x
    plt.ylabel('Quantidade') #Nome eixo y
    plt.title('Histograma da imagem') #Titulo do plot

    histograma = numpy.zeros(256, dtype=numpy.uint8)
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] += 1

    plt.bar(pixel, histograma, color = canal)
    plt.show()

def limiar(imagem, ponto, modo):
    copia = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            if modo == 1: # Remove parte clara
                if imagem[i, j] > ponto:
                    copia[i, j] = 255
                else:
                    copia[i, j] = imagem[i, j]
            else: # Remove parte escura
                if imagem[i, j] > ponto:
                    copia[i, j] = imagem[i, j]
                else:
                    copia[i, j] = 255
    return copia

def limiar3ton(imagem, p1, p2):
    copia = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
                if imagem[i, j] < p1: # Remove antes do primeiro ponto
                    copia[i, j] = 255
                if imagem[i, j] > p1 and imagem[i, j] < p2: # Remove entre o primeiro ponto e o segundo
                    copia[i, j] = 255
                if (imagem[i, j] > p2): # Remove depois do segundo ponto
                    copia[i, j] = 255
                else:
                    copia[i, j] = imagem[i, j]
    return copia

# f(r) = s = cr + l
def curvadeTom(imagem, c, l): # c é o contraste, l é luminosidade
    plt.xlabel('Origem - r')  #Nome eixo x
    plt.ylabel('Destino - s') #Nome eixo y
    plt.title('Curva de Tom Original') #Titulo do plot
    copia = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            if (imagem[i, j]*c + l) > 255:
                copia[i, j] = 255
            else:
                copia[i, j] = imagem[i, j]*c + l

    pixel = 256*[0]
    saida = 256*[0]
    for i in range(256):
        pixel[i] = i
        resultado = i*c + l
        if (resultado > 255):
            saida[i] = 255
        else:
            saida[i] = resultado
    plt.plot(pixel,saida)
    plt.show()
    return copia

def curvadeTomNegativo(imagem):
    pixel = 256*[0]
    for i in range(256):
        pixel[i] = i
    plt.xlabel('Origem - r')  #Nome eixo x
    plt.ylabel('Destino - s') #Nome eixo y
    plt.title('Curva de Tom do Negativo da Imagem Original') #Titulo do plot
    copia = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            copia[i, j] = 255 - imagem[i, j]
            
    saida = 256*[0]
    for i in range(256):
        resultado =  255 - pixel[i]
        if (resultado > 255):
            saida[i] = 255
        else:
            saida[i] = resultado
    plt.plot(pixel,saida)
    plt.show()
    return copia

def curvadeTomParabolica(imagem):
    pixel = 256*[0]
    saida = 256*[0]

    for i in range(256):
        pixel[i] = i
    plt.xlabel('Origem - r')  #Nome eixo x
    plt.ylabel('Destino - s') #Nome eixo y
    plt.title('Curva de Tom do Parabólica') #Titulo do plot
    copia = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8)
    for i in  range(imagem.shape[0]):
        for j in range (imagem.shape[1]):
            copia[i, j] = ((1/256)*imagem[i, j])**2
            
    
    for i in range(256):
        resultado =  ((1/256)*pixel[i])**2
        if (resultado > 255):
            saida[i] = 255
        else:
            saida[i] = resultado*255
    plt.plot(pixel,saida)
    plt.show()
    return copia

def main():
    imagem = cv2.imread("imagens/3t.png")
    dadosImagem(imagem)
    canalBlue, canalGreen, canalRed = separarCamada(imagem)
    canalGray = transformarCinza(imagem)
    histograma(canalGray, "Gray")
    cv2.imshow("CINZA",canalGray)
    #cv2.imwrite("imagens/saida.jpg", canalGray)

    #histograma(canalBlue, "Blue")
    #histograma(canalGreen, "Green")
    #histograma(canalRed, "Red")
    #hist(imagem[:,:,0], "Blue") # Codigo do Professor
    #hist(imagem[:,:,1], "Green") # Codigo do Professor
    #hist(imagem[:,:,2], "Red") # Codigo do Professor
    #cv2.imshow("Canal Blue", canalBlue)
    #cv2.imshow("Canal Green", canalGreen)
    #cv2.imshow("Canal Red", canalRed)
    #cv2.imshow("Canal gray", canalGray)

    #limiarizada = limiar(canalGray, 130, 1)
    #limiarizada = limiar3ton(canalGray, 100, 200)
    #cv2.imshow("Imagem Limiarizada", limiarizada)
    
    ct = curvadeTomParabolica(canalGray)
    cv2.imshow("Imagem", ct)
    cv2.waitKey(0)

if __name__ =='__main__':
    main()