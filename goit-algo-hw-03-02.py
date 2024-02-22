import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order-1, size/3)
            turtle.left(angle)

def koch_snowflake_flake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

def main():
   
    while True:
        order = input("Введіть рівень бажаної рекурсії, має бути ціле число: ")
        try:
            order = int(order)
        except ValueError:
            continue
        else: 
            break

    turtle.speed(6)
    turtle.up()
    turtle.goto(-150, -75)
    turtle.down()
    
    # Намалюємо сніжинку Коха з порядком 3 та розміром 450
    koch_snowflake_flake(turtle, order, 450)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()