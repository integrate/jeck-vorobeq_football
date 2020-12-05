import pygame, random


def ugol(ball, platform):
    ot_verha = ball.centery - platform.top
    if ot_verha <= 80:
        print(1)
        return (2, -8)
    if ot_verha <= 160 and ot_verha > 80:
        print(2)
        return (5, -5)
    if ot_verha <= 240 and ot_verha > 160:
        print(3)
        return (9, 0)
    if ot_verha <= 320 and ot_verha > 240:
        print(4)
        return (5, 5)
    if ot_verha > 320:
        print(5)
        return (2, 8)
