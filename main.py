
import cv2
import numpy as np
import matplotlib.pyplot as plt

def process_images(image_paths):
    # Carregar imagens e convertê-las para o mesmo tamanho
    images = [cv2.imread(img) for img in image_paths]
    height, width = images[0].shape[:2]
    images = [cv2.resize(img, (width, height)) for img in images]
    
    # Passo 1: Juntar todas as imagens em uma única
    combined_image = np.hstack(images)
    
    # Passo 2: Trocar as cores (exemplo: inverter canais RGB)
    swapped_colors = cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB)
    
    # Passo 3: Aplicar espelhamento
    mirrored_image = cv2.flip(swapped_colors, 1)

    # Passo 4: Recortar um pinguim favorito (ajustar manualmente os valores)
    x, y, w, h = 50, 50, 200, 300  # Ajuste conforme necessário
    cropped_penguin = mirrored_image[y:y+h, x:x+w]
    
    # Passo 5: Analisar o histograma
    gray_image = cv2.cvtColor(cropped_penguin, cv2.COLOR_RGB2GRAY)
    plt.hist(gray_image.ravel(), bins=256, range=[0,256])
    plt.title("Histograma do Pinguim")
    plt.show()
    
    # escolhi este threshold pois está entre os dois picos do histograma
    _, thresholded = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    
    # Passo 6: Aplicar cor favorita nos pixels abaixo do threshold
    favorite_color = [255, 0, 0] 
    mask = thresholded == 0
    color_image = cropped_penguin.copy()
    color_image[mask] = favorite_color
    
    plt.imshow(color_image)
    plt.title("Resultado Final")
    plt.axis("off")
    plt.show()
    

image_paths = ["P1.png", "P2.png", "P3.jpg", "P4.png"]  
processed_image = process_images(image_paths)

