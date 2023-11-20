
# from turtle import Turtle;

# timmy = Turtle();
# print(timmy);

# timmy.shape("turtle");
# timmy.color("coral");

# 창 생성 후 바로 닫기 방지
# my_screen = timmy.screen;
# my_screen.exitonclick()

# 외부 패키지(prettytable) 설치 후 테이블 생성
from prettytable import PrettyTable;
table = PrettyTable();
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander","Bulbasaur"]);
table.add_column("Type",["Electirc","Water","Fire","Grass,Poison"]);

print(table);
