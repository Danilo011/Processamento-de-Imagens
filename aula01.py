import cv2
import numpy
import matplotlib.pyplot as plt

imagem = cv2.imread("imagens/paisagem.jpg")

# Colunas da matriz
print("\nLargura em pixels: ", end='')
print(imagem.shape[1]) # largura da imagem

# Linhas da matriz
print("Altura em pixels: ", end='')
print(imagem.shape[0]) # altura da imagem

# Quantidade de Canais da Imagem - Imagem colorida possui 3 canais RGB
print("Qtde de canais: ", end='')
print(imagem.shape[2])

#cv2.imshow("Tigre", imagem)
cv2.waitKey(0) #  espera pressionar qualquer tecla

# Salvar a imagem no disco
cv2.imwrite("imagens/saida.jpg", imagem)

(b, g, r) = imagem[0,0]
print("\n", b, "\n", g, "\n", r)
print("Azul: ", b)
print("Verde: ", g)
print("Vermelho: ", r)
print("Corpo", imagem.shape)
print("Tamanho", imagem.size)
print("Número de dimensões", imagem.ndim)

canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.int8)
canalGreen = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.int8)
canalRed = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.int8)

canalBlue[:,:,0] = imagem[:,:,0]
canalGreen[:,:,1] = imagem[:,:,1]
canalRed[:,:,2] = imagem[:,:,2]

#cv2.imshow("Canal Blue", canalBlue)
#cv2.imshow("Canal Green", canalGreen)
#cv2.imshow("Canal Red", canalRed)


canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.int8)
for i in  range(imagem.shape[0]):
    for j in range (imagem.shape[1]):
        copia = imagem[i,j]
        cinza = int(copia[0]+ copia[1]+ copia[2])// 3
        canalCinza[i,j] = cinza

#criar eixo x
pixel = 256*[0]
for i in range(256):
    pixel[i]=i

#nome eixo x
plt.xlabel('pixel')

#nome eixo y
plt.ylabel('quantidade')

plt.title('histograma da imagem em tons de Cinza')

histograma = 256*[0]
for i in  range(canalCinza.shape[0]):
    for j in range (canalCinza.shape[1]):
        copia = canalCinza[i,j]
        histograma[copia] += 1


plt.bar(pixel,histograma ,color ='blue')
plt.show()

cv2.imshow("Canal Cinza", canalCinza)
cv2.waitKey(0)