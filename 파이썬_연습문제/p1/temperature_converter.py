original_price = int(input("상품 가격을 입력하세요: "))
discount_rate = int(input("할인율을 입력하세요(%): "))

discount_amount = original_price * (discount_rate / 100)
final_price = original_price - discount_amount

print(f"원래 가격: {original_price}원")
print(f"할인율: {discount_rate}%")
print(f"할인 금액: {int(discount_amount)}원")
print(f"최종 가격: {int(final_price)}원")