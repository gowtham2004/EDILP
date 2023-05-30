from moviepy.editor import *
import pygame

pygame.display.set_mode((1920,1080),0 ,24)
clip = VideoFileClip('BGvedio/vedio.mp4').resize((1920,1080))
clip.preview()
pygame.quit()