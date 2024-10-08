class BigNumberError(Exception):
    def __init__(self, msg="한 자리 숫자만 입력하세요."):
        self.msg = msg
    def __str__(self):
        return self.msg


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError(f"입력값: {num1}, {num2}")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러! 한 자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.") # 에러가 발생하든 안하든 무조건 실행됨