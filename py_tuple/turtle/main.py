import turtle as t;
import random;

turtle = t.Turtle();
t.colormode(255);

def random_color():
    r = random.randint(0,255);
    g = random.randint(0,255);
    b = random.randint(0,255);
    return (r,g,b);

# 스피로그래피 그리기
turtle.speed("fastest");

def draw_spirogragh(size_of_gap):
    for num in range(int(360 / size_of_gap)):
        turtle.color(random_color());
        turtle.circle(100);
        current_heading = turtle.heading();
        turtle.setheading(current_heading + 10);
draw_spirogragh(10);

# 랜덤 길 그리기
# def random_color():
#     r = random.randint(0,255);
#     g = random.randint(0,255);
#     b = random.randint(0,255);
#     return (r,g,b);

# dirctions = [0,90,180,270];
# turtle.pensize(10);
# turtle.speed("fastest");

# for num in range(200):
#     turtle.color(random_color());
#     turtle.forward(30);
#     turtle.setheading(random.choice(dirctions));

# 도형 그리기
# def draw_shape(num_sides):
#     angle = 360 / num_sides;
#     for num in range(num_sides):
#         turtle.forward(100);
#         turtle.right(angle);
# for shape_side_num  in range(3,11):
#        turtle.color(random.choice(colours));
#        draw_shape(shape_side_num);

# 점선 그리기
# for num in range(15):
#     turtle.forward(10);
#     turtle.penup();
#     turtle.forward(10);
#     turtle.pendown();


# 정사각형 그리기
# for num in range(4):
#     turtle.forward(100);
#     turtle.left(90);
#     turtle.steps(10);





screen = turtle.screen;
screen.exitonclick();