import random

class Character:
    def __init__(self, name, hp, power):
        self.name=name
        self.hp=hp
        self.power=power

    def is_alive(self):
        return self.hp>0

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name}은(는) {damage}의 피해를 입었습니다. 남은 HP: {self.hp}")

    def attack(self, other):
        print(f"{self.name}이(가) {other.name}을(를) 공격합니다!")
        other.take_damage(self.power)

class Player(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.hp += heal_amount
        print(f"{self.name}이(가) {heal_amount}만큼 회복했습니다. 현재 HP: {self.hp}")

    def run(self):
        return random.random()<0.5


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name,hp,power)

def ran_monster():
    n=random.randint(1,3)
    if n==1:
        return Monster("고블린", 50, 10)
    if n==2:
        return Monster("오크", 80, 15)
    if n==3:
        return Monster("드래곤", 150, 25)

p_name=input("사용자의 이름을 입력하시오: ")
player=Player(p_name, 100, 20)
monster=ran_monster()

print(f"전투 시작! 몬스터 등장: {monster.name} (HP: {monster.hp}, 공격력: {monster.power})")

while player.is_alive() and monster.is_alive():
    print("\n[1] 공격 [2] 회복 [3] 도망")
    choice=int(input("행동 선택: "))

    if choice==1:
        player.attack(monster)
    elif choice==2:
        player.heal()
    elif choice==3:
        if player.run():
            print("도망에 성공했습니다!")
            break
        else:
            print("도망에 실패했습니다.")

    else:
        print("잘못된 입력입니다.")
        continue


    if monster.is_alive():
        monster.attack(player)


if player.is_alive():
    print(f"\n당신은 {monster.name}을(를) 쓰러뜨렸습니다!")
else:
    print(f"\n당신은 {monster.name}에게 패배했습니다...")

        


