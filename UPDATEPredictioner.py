import pygame
import random
import time
import sys
import datetime
import webbrowser
import os

# Инициализация Pygame
pygame.init()
pygame.font.init()

# Создание окна
screen_width = 800
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Predictioner")

# Путь к HTML-файлу на компьютере
html_file = r'"C:\Users\Belsbbang\Desktop\hamlet predictioner\cameras.html"'

# Функция открытия локальной веб-страницы
def open_local_html(file_path):
    url = 'file://' + os.path.abspath(file_path)
    webbrowser.open(url, autoraise=False)

open_local_html(html_file)  # Открываем веб-страницу


#дата и время
def get_current_datetime():
    current_datetime = datetime.datetime.now()
    datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return datetime_str

#получаем рандомную фразу из текста
def get_random_phrase(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        phrases = [line.strip().strip('«»') for line in file if line.strip()]
    random_phrase = random.choice(phrases)
    return random_phrase

text_file = r'C:\Users\Belsbbang\Desktop\hamlet predictioner\aihamlet.txt'

#custom_font = pygame.font.Font("LCD5x8HRU.ttf", 24) #Шрифты
custom_font = pygame.font.Font(r"C:\Users\Belsbbang\Desktop\hamlet predictioner\LCD5x8HRU.ttf", 24)

# Отображение текущей даты и времени на экране
#def display_datetime(screen, font, color):
    #datetime_str = get_current_datetime()  # Получаем текущую дату и время
    #datetime_surface = font.render(f"Текущая дата и время: {datetime_str}", True, color)
    #screen.blit(datetime_surface, (10, 10))
    
clock = pygame.time.Clock()

def text_wrap(text, font, max_width): #говнючая функция переноса строки
    words = text.split(' ')
    lines = []
    current_line = ''
    
    for word in words:
        test_line = current_line + word + ' '
        
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '
            
    if current_line:
        lines.append(current_line)
    #lines.append(current_line)
    return lines

pygame.time.set_timer(pygame.USEREVENT, 1000)

phrase_updater_timer = pygame.USEREVENT + 1
pygame.time.set_timer(phrase_updater_timer, 30000)

current_phrase = get_random_phrase(text_file)

running = True
random_phrase = get_random_phrase(text_file)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.quit()
            #sys.exit() #quit()
        elif event.type == phrase_updater_timer:
            current_phrase = get_random_phrase(text_file)
            
    screen.fill((0, 0, 0))
    text_lines = text_wrap(current_phrase, custom_font, screen_width)
    
    y_position = 50
    for line in text_lines:
        text = custom_font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(left=10, top=y_position)
        screen.blit(text, text_rect)
        y_position += text.get_height() + 10
        
        #textt = custom_font.render(get_current_datetime(), True, (255, 255, 255))
        #screen.blit(textt, (10, 10))
    current_datetime_str = get_current_datetime()
    textt = custom_font.render(current_datetime_str, True, (255, 255, 255))
    screen.blit(textt, (10, 10))
        
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

            

    #random_phrase = get_random_phrase(text_file)
    #datetime_str = get_current_datetime()

    #screen.fill((0, 0, 0))

    #datetime_surface = custom_font.render(f"{datetime_str}", True, (255, 255, 255))
    #date_rect = datetime_surface.get_rect(topleft=(0,0))
    #wrapped_phrase = text_wrap(random_phrase, custom_font, screen_width)
    #y_offset = 30
    #for line in wrapped_phrase:
            #text_surface = custom_font.render(line, True, (255, 255, 255))
            #text_rect = text_surface.get_rect(topleft=(0, 30))
    
            #text_surface = custom_font.render(line, True, (255, 255, 255))
            #text_rect = text_surface.get_rect(topleft=(0, y_offset))
            #screen.blit(text_surface, text_rect)
            #y_offset += custom_font.size(line)[1]
    
    
    #screen.blit(datetime_surface, date_rect)

    #pygame.display.update()
    #pygame.display.flip()
    #clock.tick(30)

    #time.sleep(60)

