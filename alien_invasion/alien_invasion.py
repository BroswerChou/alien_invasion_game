import sys
import pygame
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))  # 使用指定窗口大小
    pygame.display.set_caption("Alien Invasion")
    # 设置背景色,根据RGB三色确定
    bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环都重新绘制屏幕,用背景色填充屏幕
        screen.fill(bg_color)
        # 让最近绘制的屏幕可见,不断更新屏幕
        pygame.display.flip()
run_game()

