import turtle

# 設定環境
screen = turtle.Screen()
screen.setup(width=480, height=360)
screen.title("Scratch Project: Untitled-24")

# 建立角色 (Sprite)
player = turtle.Turtle()
player.shape("classic")  # 這裡可以根據您的角色形狀修改
player.penup()

def run_project():
    # 根據 Scratch 的邏輯：當綠旗被點擊
    player.goto(0, 0) # 初始位置
    
    # 進入主循環
    while True:
        player.forward(10) # 移動 10 步
        
        # 碰到邊緣就反彈
        x, y = player.position()
        if abs(x) > 230 or abs(y) > 170:
            player.left(180) # 簡單的反轉邏輯

if __name__ == "__main__":
    try:
        run_project()
    except turtle.Terminator:
        pass
