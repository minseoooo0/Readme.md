import datetime

print("💰 [용돈 비서] 시스템을 시작합니다! 💰")
total=int(input("이번 달 총 용돈은 얼마인가요? (원): "))
payday_input= input("다음 용돈 받는 날은 언제인가요? (예: 2026-07-24): ")

payday = datetime.datetime.strptime(payday_input, "%Y-%m-%d").date()
today = datetime.date.today()
leftdays= (payday - today).days

if leftdays > 0:
    recommend = total//leftdays
else:
    recommend = total

print(f"\n📅 다음 용돈 날까지 {leftdays}일 남았어요.")
print(f"💡 오늘부터 하루에 약 {recommend}원씩 쓰면 안전해요!\n")
print("-" * 40)

expense = int(input("오늘 쓴 돈을 입력해 주세요 (원): "))

if expense > recommend*1.5:
    print("\n🚨🚨🚨 [경고] 과소비 폭발! 🚨🚨🚨")
    print(f"오늘 권장 금액({recommend}원)보다 훨씬 많이 썼어요!")
    print("내일부터는 진짜 삼각김밥만 먹으면서 아껴야 해요! 😭")
elif expense > recommend:
    print("\n⚠️ [알림] 조금 삐뽀삐뽀! ⚠️")
    print("오늘 예산을 살짝 넘겼네요. 내일은 지갑을 조금 닫아두는 걸 추천해요! 😉")
else:
    print("\n🥰 [칭찬] 아주 훌륭해요! 🥰")
    print("돈을 아주 현명하게 잘 썼군요? 이대로만 하면 부자가 될 거예요! 👍")

remain = total - expense
print(f"\n💵 남은 용돈: {remain}원")
