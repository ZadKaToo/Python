#all of this thing is about boolean
# or คือ ถ้ามีเงื่อนไขอันไหนเป็นจริง เเสดงว่าต้องเป็นจริงทั้งหมด
# not คือ นิเสธ
# and คือ ต้องตรงทุกต้องเงื่อนไข ถึงเป็นจริง

leaf = 30
is_money = False

if leaf <= 5 and is_money:
    print("damn where you get that?")
    print("You got damn poor")
elif leaf == 0 and is_money:
    print("nothing")
    print("but still money")
elif 40 > leaf > 0 and is_money:
    print("damn where you get that?")
    print("You got damn rich")
elif leaf <= 5 and not is_money:
    print("damn where you get that?")
    print("it's just leaf")
elif leaf == 0 and not is_money:
    print("nothing")
    print("it's just leaf")
elif 40 > leaf > 0 and not is_money:
    print("damn where you get that?")
    print("it's just leaf")