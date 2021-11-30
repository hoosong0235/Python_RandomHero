
import time
import random
import winsound
import cv2

image_goblin = cv2.imread('C:\TGPMonster\goblin.jpg', cv2.IMREAD_UNCHANGED)
image_ork = cv2.imread('C:\TGPMonster\ork.jpg', cv2.IMREAD_UNCHANGED)
image_undead = cv2.imread('C:\TGPMonster\daednu.jpg', cv2.IMREAD_UNCHANGED)
image_gnoll = cv2.imread('C:\TGPMonster\gnoll.jpg', cv2.IMREAD_UNCHANGED)
image_lycanthrope = cv2.imread('C:\TGPMonster\lycanthrope.jpg', cv2.IMREAD_UNCHANGED)
image_ogre = cv2.imread('C:\TGPMonster\ogre.jpg', cv2.IMREAD_UNCHANGED)
image_golem = cv2.imread('C:\TGPMonster\golem.jpg', cv2.IMREAD_UNCHANGED)
image_psyclops = cv2.imread('C:\TGPMonster\psyclops.png', cv2.IMREAD_UNCHANGED)
image_dragon = cv2.imread('C:\TGPMonster\dragon.jpg', cv2.IMREAD_UNCHANGED)

주사위_결과_플레이어 = '기본값'
지문_결과_플레이어 = '기본값'
주사위_결과_몬스터 = '기본값'
지문_결과_몬스터 = '기본값'
전리품_결과_몬스터 = '기본값'
단축키_스킬 = '기본값'
단축키_굴림 = '기본값'
주사위_수정치 = 0
주사위_임시_수정치 = 0
공격력_임시_수정치 = 0
방어력_임시_수정치 = 0
단계 = 0
부활 = 0

적 = '기본값'
적_수 = '기본값'
적_체력 = '기본값'

플레이어_체력 = '기본값'
플레이어_마력 = '기본값'

def introduce_text_game_project() :
    global 플레이어
    global 플레이어_체력
    global 플레이어_마력
    global list_shop
    winsound.PlaySound('C:\TGPBGMwav\Mstart.wav',winsound.SND_ASYNC)
    one()
    print('텍스트 게임(데모 버전)에 오신 것을 환영합니다.')
    wait()
    print('이 게임에서는 공격 여부, 데미지, 몬스터의 수 등 모든 변수가 무작위로 결정됩니다.')
    wait()
    print('당신의 이름은?')
    name = input()
    one()
    print(name + '님, 이 게임에는 총 세 가지의 직업이 있습니다.')
    wait()
    print('검사, 궁수, 그리고 마법사가 그것입니다.')
    wait()
    print('각 직업의 특징을 설명해드리겠습니다. 천천히 읽어보십시오.')
    wait()
    print('')
    print('====================================================================================================')
    print('')
    one()
    print('검사 : 판금 갑옷(방어력 30), 대검(공격력 100)')
    print('1. 삼연속 베기 : 3연속 공격, 마나 10')
    print('2. 방패 세우기 : 한 전투동안 방어력 20 증가 및 주사위 수정치 -3 (방패 받아치기 사용 시 재사용 가능), 마나 15')
    print('3. 방패 받아치기 : 일반 공격의 5배 데미지 및 방패 세우기의 효과 삭제, 마나 15')
    one()
    print('')
    print('====================================================================================================')
    print('')
    one()
    print('궁수 : 가죽 갑옷(방어력 25), 활(공격력 100)')
    print('1. 네 발 끼워쏘기 : 4연속 공격, 마나 15')
    print('2. 게릴라전 : 일반 공격의 3배 데미지 및 한 전투동안 주사위 수정치 +3 (누적 가능), 마나 15')
    print('3. 기관단총 : 주사위 수정치 -15 판정 성공시 15연속 공격, 마나 25')
    one()
    print('')
    print('====================================================================================================')
    print('')
    one()
    print('마법사 : 로브(방어력 20), 지팡이(공격력 100)')
    print('1. 마탄 세례 : 5연속 공격, 마나 20')
    print('2. 마나 충전 : 한 전투동안 공격력 25 증가 및 주사위 수정치 +5 (누적 가능), 마나 20')
    print('3. 아포칼립스 : 주사위 수정치 -25 판정 성공시 10배 데미지 10연속 공격, 마나 50')
    one()
    print('')
    print('====================================================================================================')
    print('')
    wait()
    print(name + ', 당신의 직업은?')
    one()
    print(list_job)
    직업 = input()
    while 직업 != '검사' and 직업 != '궁수' and 직업 != '마법사':
        print(name + ', 당신의 직업은?!')
        one()
        print(list_job)
        직업 = input()
    if 직업 == '검사':
        플레이어 = swordsman()
        플레이어.name = name
        list_shop = list_shop + list_swordman_shop
    if 직업 == '궁수':
        플레이어 = archer()
        플레이어.name = name
        list_shop = list_shop + list_archer_shop
    if 직업 == '마법사':
        플레이어 = magician()
        플레이어.name = name
        list_shop = list_shop + list_magician_shop
    플레이어_체력 = 플레이어.hp
    플레이어_마력 = 플레이어.mp

def set_shortcut() :
    global 단축키_스킬
    global 단축키_굴림
    one()
    if 플레이어.job == '검사':
        print(플레이어.job, 플레이어.name+"님의 주 스킬은 '삼연속 베기' 입니다.")
    if 플레이어.job == '궁수':
        print(플레이어.job, 플레이어.name+"님의 주 스킬은 '네 발 끼워쏘기' 입니다.")
    if 플레이어.job == '마법사':
        print(플레이어.job, 플레이어.name+"님의 주 스킬은 '마탄 세례' 입니다.")
    one()
    print('주 스킬을 지정할 단축키를 설정해 주십시오.')
    typed_skill = input()
    단축키_스킬 = typed_skill
    one()
    print(플레이어.name+'님의 주 스킬 단축키는', 단축키_스킬, '입니다.')
    one()
    print("주사위 판정 시 '굴림' 대신 입력할 단축키를 설정해 주십시오.")
    typed_roll = input()
    단축키_굴림 = typed_roll
    one()
    print(플레이어.name+'님의 주사위 판정 단축키는', 단축키_굴림, '입니다.')

def one():
    time.sleep(0.75)
def wait():
    time.sleep(1.5)
def dot():
    one()
    for i in range(3):
        print('.')
        one()

def roll_player(dice): #dice=숫자, 대성공=5, 성공=2, 실패=1
    global 주사위_결과_플레이어
    global 주사위_수정치
    one()
    print(dice, '면체 주사위, 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
    one()
    print('굴림을 입력하세요')
    typed = input()
    while typed != '굴림' and typed != 단축키_굴림 :
        print('굴림을 입력하세요!')
        typed = input()
    value = random.randrange(1, dice + 1)
    value = value - (주사위_수정치 + 주사위_임시_수정치)
    if value <= 0:
        value = 1
    if value >= 51:
        value = 50
    one()
    print('주사위를 굴리는 중입니다...')
    dot()
    if value <= dice / 5:
        print(value, '/', dice)
        one()
        print('대성공!')
        주사위_결과_플레이어 = 5
        주사위_수정치 = 주사위_수정치 - 1
    elif value <= dice / 2:
        print(value, '/', dice)
        one()
        print('성공.')
        주사위_결과_플레이어 = 2
    else:
        print(value, '/', dice)
        one()
        print('실패...')
        주사위_결과_플레이어 = 1
        주사위_수정치 = 주사위_수정치 + 1

def roll_temporary_player(dice): #dice=숫자
    global 지문_결과_플레이어
    지문_결과_플레이어 = random.randrange(1, dice+1)

def roll_monster(dice): #dice=숫자, 주사위_결과 하나=20%
    global 주사위_결과_몬스터
    value = random.randrange(1, dice+1)
    if value <= (dice / 10):
        주사위_결과_몬스터 = 1
    elif value <= 2 * (dice / 10):
        주사위_결과_몬스터 = 2
    elif value <= 3 * (dice / 10):
        주사위_결과_몬스터 = 3
    elif value <= 4 * (dice / 10):
        주사위_결과_몬스터 = 4
    elif value <= 5 * (dice / 10):
        주사위_결과_몬스터 = 5
    elif value <= 6 * (dice / 10):
        주사위_결과_몬스터 = 6
    elif value <= 7 * (dice / 10):
        주사위_결과_몬스터 = 7
    elif value <= 8 * (dice / 10):
        주사위_결과_몬스터 = 8
    elif value <= 9 * (dice / 10):
        주사위_결과_몬스터 = 9
    elif value <= 10 * (dice / 10):
        주사위_결과_몬스터 = 10

def roll_temporary_monster(dice): #dice=숫자
    global 지문_결과_몬스터
    지문_결과_몬스터 = random.randrange(1, dice+1)

def roll_loot_monster(dice): #dice=숫자
    global 전리품_결과_몬스터
    전리품_결과_몬스터 = random.randrange(1, dice+1)


def fight(monster_name, monster_eng_name, monster_class, monster_image):
#moster_name=한국어 '문자열', monster_eng_name=영어 '문자열', monster_clas=클래스, monster_image=이미지
    global 적
    global 적_수
    global 적_체력
    global 단계
    global 부활
    적_수 = random.randrange(1, dict_name[monster_name] + 1)
    적 = monster_class()
    적.hp = 적.hp * 적_수
    적_체력 = 적.hp
    print(적_수, '마리의', monster_name+'와(과) 전투가 일어났습니다!')
    wait()
    cv2.imshow(monster_eng_name, monster_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    wait()
    if monster_name == '고블린' :
        print(monster_name+'은(는)', 플레이어.name+'을(를) 둘러싸고 있습니다!')
    if monster_name == '오크' :
        print(monster_name+'은(는)', 플레이어.name+'을(를) 향해 달려오고 있습니다!')
    if monster_name == '언데드' :
        print(monster_name+'은(는)', 플레이어.name, '쪽을 향해 삐걱삐걱 걸어옵니다!')
    if monster_name == '놀' :
        print(monster_name+'은(는)', 플레이어.name+'의 냄새를 맡고 네 발로 뛰어오고 있습니다!')
        wait()
        print('크기로 보나 생김새로 보나 마치 하이에나 같은 모양새입니다.')
    if monster_name == '라이칸스로프' :
        print(monster_name+'은(는)', 플레이어.name+'을(를) 본 뒤 아우우, 울음소리를 내고는 저벅저벅 걸어옵니다.')
        wait()
        print('보름달이 뜨면 변신하는 웨어울프, 그의 위용에 뒷골이 서늘해집니다.')
    if monster_name == '오우거' :
        print(플레이어.name+'은(는) 대형 트럭 한대에 맞먹는 크기의', monster_name+'을(를) 마주합니다.')
        wait()
        print('그 압도적인 크기에', 플레이어.name+'의 손발이 벌벌 떨립니다.')
    if monster_name == '골렘' :
        print(플레이어.name+'은(는) 집 한 채 크기의', monster_name+'을(를) 마주합니다.')
        wait()
        print(monster_name+'(이)가 한 걸음을 내딛을 때마다 땅이 흔들리고 갈라집니다.')
        wait()
        print('과연', 플레이어.name+'(이)가', monster_name+'을(를) 이길 수 있을까요...')
    if monster_name == '사이클로프스' :
        print(플레이어.name + '은(는) 아파트 한 채 크기의', monster_name + '을(를) 마주합니다.')
        wait()
        print(monster_name + '에게서 이길 가능성은 정말로 없어 보입니다.')
        wait()
        print(플레이어.name+', 정말로', monster_name+'와(과) 싸울 셈입니까?')
    if monster_name == '드래곤' :
        print(플레이어.name + '은(는) 거대한 날개를 펼쳐 날아오르는, 63빌딩 높이의', monster_name + '을(를) 바라봅니다.')
        wait()
        print(monster_name, '또한 소름끼치도록 날카로운 눈빛으로', 플레이어.name + '을(를) 마주 바라봅니다.')
        wait()
        print(monster_name + '은(는)', 플레이어.name + '을(를) 말없이 쳐다보다, 마치 천둥과 같은 포효를 내지르더니 순식간에', 플레이어.name + '에게로 날아옵니다.')
        wait()
        print(플레이어.name + '은(는) 고개를 들어', monster_name + '을(를) 쳐다봅니다.')
        wait()
        print('그야말로 압도적인 크기,', monster_name + '의 얼굴조차도 보이지 않습니다.')
        wait()
        print(플레이어.name + '의 마음 속 두려움이 당장 도망쳐야만 한다고 소리치고 있습니다.')
    wait()
    print(monster_name+'은(는)', 적.weapon+'을(를) 쥐고 있습니다!')
    wait()
    while 적.hp >= 1:
        if 플레이어.hp == 0 :
            if 부활 == 0 :
                winsound.PlaySound(None, winsound.SND_ASYNC)
                winsound.PlaySound('C:\TGPBGMwav\Moblivion.wav',winsound.SND_ASYNC)
                wait()
                print(플레이어.name+'은(는) 사망했습니다.')
                end()
            if 부활 >= 1 :
                winsound.PlaySound(None, winsound.SND_ASYNC)
                winsound.PlaySound('C:\TGPBGMwav\Moblivion.wav', winsound.SND_ASYNC)
                부활 = 부활 - 1
                플레이어.hp = 100
                wait()
                print(플레이어.name+'은(는) 사망했습니다.')
                dot()
                print('...그 순간!')
                winsound.PlaySound(None, winsound.SND_ASYNC)
                winsound.PlaySound('C:\TGPBGMwav\Mresurrection.wav', winsound.SND_ASYNC)
                wait()
                print(플레이어.name+'의 몸이 하늘 높이 붕 떠오르더니 하늘에서 한 줄기의 신성한 빛이 내려옵니다.')
                wait()
                print('그 빛은', 플레이어.name + '을(를) 찬란하게 비추고,', 플레이어.name + '의 몸은 점점 높이 떠오릅니다.')
                wait()
                print('빛이 점점 강해져 성스러운 광채가', 플레이어.name + '의 시야를 모두 덮어 빛날 때')
                wait()
                print(플레이어.name + '은(는) 비로소 두 눈을 뜹니다.')
                wait()
                print(플레이어.name + '은(는) 부활했습니다.')
                wait()
                print('남은 부활 횟수 :', 부활)
                show_player_hp()
                if 0 <= 단계 <= 2 :
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    winsound.PlaySound('C:\TGPBGMwav\Mnervous.wav', winsound.SND_ASYNC)
                if 3 <= 단계 <= 5 :
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    winsound.PlaySound('C:\TGPBGMwav\Mnorvous.wav', winsound.SND_ASYNC)
                if 6 <= 단계 <= 8 :
                    winsound.PlaySound(None, winsound.SND_ASYNC)
                    winsound.PlaySound('C:\TGPBGMwav\Mnenenervous.wav', winsound.SND_ASYNC)
        one()
        print(플레이어.name+'은(는) 무엇을 합니까?')
        one()
        print(플레이어.action+플레이어.inventory)
        typed = input()
        while typed not in 플레이어.action + 플레이어.inventory + [단축키_스킬] :
            print(플레이어.name + '은(는) 무엇을 합니까?!')
            one()
            print(플레이어.action + 플레이어.inventory)
            typed = input()
        if typed == 단축키_스킬 :
            if 플레이어.job == '검사' :
                mana_cost('삼연속 베기')
                플레이어.three_consecutive_cut()
                if 적.hp >= 1:
                    적.action()
            if 플레이어.job == '궁수' :
                mana_cost('네 발 끼워쏘기')
                플레이어.shoot_four_arrow()
                if 적.hp >= 1:
                    적.action()
            if 플레이어.job == '마법사' :
                mana_cost('마탄 세례')
                플레이어.magic_missile_perfusion()
                if 적.hp >= 1:
                    적.action()
        if typed == '삼연속 베기':
            mana_cost('삼연속 베기')
            플레이어.three_consecutive_cut()
            if 적.hp >= 1:
                적.action()
        if typed == '방패 세우기':
            mana_cost('방패 세우기')
            플레이어.lift_shield()
            if 적.hp >= 1:
                적.action()
        if typed == '방패 받아치기':
            mana_cost('방패 받아치기')
            플레이어.push_shield()
            if 적.hp >= 1:
                적.action()
        if typed == '네 발 끼워쏘기':
            mana_cost('네 발 끼워쏘기')
            플레이어.shoot_four_arrow()
            if 적.hp >= 1:
                적.action()
        if typed == '게릴라전':
            mana_cost('게릴라전')
            플레이어.guerrilla()
            if 적.hp >= 1:
                적.action()
        if typed == '기관단총':
            mana_cost('기관단총')
            플레이어.submachine_gun()
            if 적.hp >= 1:
                적.action()
        if typed == '마탄 세례':
            mana_cost('마탄 세례')
            플레이어.magic_missile_perfusion()
            if 적.hp >= 1:
                적.action()
        if typed == '마나 충전':
            mana_cost('마나 충전')
            플레이어.mana_charge()
            if 적.hp >= 1:
                적.action()
        if typed == '아포칼립스':
            mana_cost('아포칼립스')
            플레이어.apocalypse()
            if 적.hp >= 1:
                적.action()
        if typed == 'HP 회복':
            플레이어.inventory.remove('HP 회복')
            플레이어.hp = 플레이어_체력
            one()
            print(플레이어.name + '의 HP를 회복합니다.')
            one()
            print(플레이어.name, 'HP :', 플레이어.hp, '/', 플레이어_체력)
            적.action()
        if typed == 'MP 회복':
            플레이어.inventory.remove('MP 회복')
            플레이어.mp = 플레이어_마력
            one()
            print(플레이어.name + '의 MP를 회복합니다.')
            one()
            print(플레이어.name, 'MP :', 플레이어.mp, '/', 플레이어_마력)
            적.action()
    단계 = 단계 + 1
    one()
    print('축하합니다!')
    one()
    print(플레이어.name+'은(는)', 적_수, '마리의', monster_name+'을(를) 처치했습니다!')
    loot()
    temporary_value_reset()

def player_damage_function(count, multiple) : #숫자
    if 주사위_결과_플레이어 == 5 :
        for i in range(count) :
            damage = random.randrange(1, dict_weapon[플레이어.weapon] + 1 + 공격력_임시_수정치) - dict_armor[적.armor]
            if damage <= 0 :
                damage = 1
            damage = damage * multiple * 3
            적.hp = 적.hp - damage
            if 적.hp <= 0 :
                적.hp = 0
            one()
            print(플레이어.name + '은(는)', 플레이어.weapon + '(으)로', 적.name + '에게', damage, '데미지를 주었습니다!')
    if 주사위_결과_플레이어 == 2 :
        for i in range(count) :
            damage = random.randrange(1, dict_weapon[플레이어.weapon] + 1 + 공격력_임시_수정치) - dict_armor[적.armor]
            if damage <= 0 :
                damage = 1
            damage = damage * multiple
            적.hp = 적.hp - damage
            if 적.hp <= 0 :
                적.hp = 0
            one()
            print(플레이어.name + '은(는)', 플레이어.weapon + '(으)로', 적.name + '에게', damage, '데미지를 주었습니다!')
    if 주사위_결과_플레이어 == 1 :
        wait()
        print(적.name + '은(는)', 플레이어.name + '의 공격을 피했습니다!')
    wait()
    show_enemy_hp()

def monster_damage_function(count, multiple) : #숫자
    wait()
    if 주사위_결과_몬스터 == 1 :
        for i in range(count) :
            damage = random.randrange(1, dict_weapon[적.weapon] + 1) - (dict_armor[플레이어.armor] + 방어력_임시_수정치)
            if damage <= 0 :
                damage = 1
            damage = damage * multiple * 2
            플레이어.hp = 플레이어.hp - damage
            if 플레이어.hp <= 0 :
                플레이어.hp = 0
            print(적.name + '은(는)', 적.weapon + '(으)로', 플레이어.name + '에게', damage, '데미지를 주었습니다!')
            wait()
        show_player_hp()
    if 2<= 주사위_결과_몬스터 <= 5 :
        for i in range(count) :
            damage = random.randrange(1, dict_weapon[적.weapon] + 1) - (dict_armor[플레이어.armor] + 방어력_임시_수정치)
            if damage <= 0 :
                damage = 1
            damage = damage * multiple
            플레이어.hp = 플레이어.hp - damage
            if 플레이어.hp <= 0 :
                플레이어.hp = 0
            print(적.name + '은(는)', 적.weapon + '(으)로', 플레이어.name + '에게', damage, '데미지를 주었습니다!')
            wait()
        show_player_hp()
    if 6 <= 주사위_결과_몬스터 <= 9 :
        print(플레이어.name + '은(는)', 적.name + '의 공격을 피했습니다!')
        wait()
        show_player_hp()
    if 주사위_결과_몬스터 == 10 :
        damage = random.randrange(1, dict_weapon[플레이어.weapon] + 1 + 공격력_임시_수정치) - dict_armor[적.armor]
        if damage <= 0:
            damage = 1
        damage = damage * 5
        적.hp = 적.hp - damage
        if 적.hp <= 0:
            적.hp = 0
        print(플레이어.name + '은(는)', 플레이어.weapon + '(으)로', 적.name + '에게', damage, '데미지를 주었습니다!')
        wait()
        show_enemy_hp()

def show_player_hp() :
    one()
    print(플레이어.name, 'HP :', 플레이어.hp, '/', 플레이어_체력)

def show_player_mp() :
    one()
    print(플레이어.name, 'MP :', 플레이어.mp, '/', 플레이어_마력)

def show_player_weapon() :
    one()
    print(플레이어.name, '무기 :', 플레이어.weapon)

def show_player_armor() :
    one()
    print(플레이어.name, '방어구 :', 플레이어.armor)

def show_player_money() :
    one()
    print(플레이어.name, '돈 :', 플레이어.money, '원')

def show_player_inventory() :
    one()
    print(플레이어.name, '인벤토리 :', 플레이어.inventory)

def show_enemy_hp() :
    one()
    print(적_수, '마리의', 적.name, 'HP :', 적.hp, '/', 적_체력)

def temporary_value_reset():
    global 주사위_임시_수정치
    global 공격력_임시_수정치
    global 방어력_임시_수정치
    주사위_임시_수정치 = 0
    공격력_임시_수정치 = 0
    방어력_임시_수정치 = 0
    if '방패 받아치기' in 플레이어.action:
        플레이어.action.remove('방패 받아치기')
        플레이어.action.append('방패 세우기')

def loot():
    플레이어.money = 플레이어.money + (적.money * 적_수)
    roll_loot_monster(10)
    if 1 <= 전리품_결과_몬스터 <= 2 :
        적.inventory.append('HP 회복')
    if 8 <= 전리품_결과_몬스터 <= 10 :
        적.inventory.append('MP 회복')
    wait()
    print(적.money * 적_수, '원을 획득했습니다!')
    show_player_money()
    if len(적.inventory) >= 1 :
        플레이어.inventory = 플레이어.inventory + 적.inventory
        wait()
        print('전리품으로', 적.inventory, '을(를) 획득했습니다!')
        show_player_inventory()
    wait()
    print("전투를 마치시려면 'Enter' 을(를) 입력하십시오.")
    typed = input()
    while typed != '' :
        one()
        print("전투를 마치시려면 'Enter' 를 입력하십시오!")
        typed = input()

def rest():
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound('C:\TGPBGMwav\Mrest.wav',winsound.SND_ASYNC)
    wait()
    print('이곳은', 단계, '단계와', 단계+1, '단계 사이의 휴식공간입니다.')
    one()
    print(플레이어.name, '은(는) 무엇을 합니까?')
    show_player_hp()
    show_player_mp()
    one()
    print(플레이어.inventory+['상점', '다음 단계'])
    one()
    print("다음 단계로 가시려면 'Enter' 를 입력하십시오.")
    typed = input()
    while typed not in 플레이어.inventory+['상점', '다음 단계', ''] :
        one()
        print(플레이어.name, '은(는) 무엇을 합니까?!')
        one()
        print(플레이어.inventory + ['상점', '다음 단계'])
        typed = input()
    if typed == 'HP 회복' :
        플레이어.inventory.remove('HP 회복')
        플레이어.hp = 플레이어_체력
        one()
        print(플레이어.name+'의 HP를 회복합니다.')
        show_player_hp()
    if typed == 'MP 회복' :
        플레이어.inventory.remove('MP 회복')
        플레이어.mp = 플레이어_마력
        one()
        print(플레이어.name+'의 MP를 회복합니다.')
        show_player_mp()
    if typed == '상점' :
        shop()
    if typed == '다음 단계' or typed == '' :
        one()
        print(플레이어.name + '은(는) 다음 단계로 향합니다.')

def monster_sword_action() :
    wait()
    print(적.name + '(이)가', 플레이어.name + '을(를) 공격합니다!')
    dot()
    roll_monster(50)
    global 주사위_결과_몬스터
    if 주사위_결과_몬스터 == 1:
        print(플레이어.name + '의 급소를 노려 날카롭게 들어오는', 적.name + '이(의) 공격!')
    if 2<= 주사위_결과_몬스터 <= 5:
        roll_temporary_monster(4)
        if 지문_결과_몬스터 == 1:
            print(적.name + '의 무자비한 공격!')
        if 지문_결과_몬스터 == 2:
            print('재빠르게 다가와 공격하는', 적.name + '!')
        if 지문_결과_몬스터 == 3:
            print(플레이어.name + '의 빈틈을 노려 들어오는', 적.name + '의 찌르기!')
        if 지문_결과_몬스터 == 4:
            print(적.name + '은(는)', 플레이어.name + '을(를) 횡으로 벱니다.')
    if 6<= 주사위_결과_몬스터 <= 9:
        roll_temporary_monster(4)
        if 지문_결과_몬스터 == 1:
            print(플레이어.name + '은 급하게 몸을 비틀어', 적.name + '의 공격을 피하려고 시도합니다!')
        if 지문_결과_몬스터 == 2:
            print('재빨리 뒤로 한바퀴 구르는', 플레이어.name)
        if 지문_결과_몬스터 == 3:
            print('아슬아슬하게 스쳐지나가는', 적.name + '의 공격!')
        if 지문_결과_몬스터 == 4:
            print('그런데, 이게 뭔가요.', 적.name + '은(는) 돌부리에 걸려 넘어지고 맙니다.')
    if 주사위_결과_몬스터 == 10:
        print('하지만', 플레이어.name + '은(는) 이미', 적.name + '의 공격을 예상하고 있었습니다.')
        wait()
        print(플레이어.name + '은(는)', 적.name + '의 공격을 부드럽게 피해 역으로 공격합니다!')
    monster_damage_function(2, 0.5)

def monster_breath_action() :
    wait()
    print(적.name + '(이)가', 플레이어.name + '을(를) 공격합니다!')
    dot()
    roll_monster(50)
    global 주사위_결과_몬스터
    if 주사위_결과_몬스터 == 1:
        print('거대하게 불타오르는', 적.name + '의 브레스...')
        wait()
        print('마치 작렬하는 태양과도 같은, 거대한 불덩어리의 형상이 하늘을 가득 덮어', 플레이어.name+'에게로 떨어져 내려옵니다.')
        dot()
        print('불덩어리는', 플레이어.name+'에게로 떨어지고, 천둥같은 굉음과 함께 엄청난 폭발이 일어납니다.')
        wait()
        print('땅은 마치 운석이 충돌한 듯 움푹 패였고, 존재하는 모든 것들이 불타오르고 있습니다.')
        wait()
        print('처참한 광경이군요. 그 누구라도 살아남지 못할 듯 합니다...')
    if 2<= 주사위_결과_몬스터 <= 5:
        roll_temporary_monster(4)
        if 지문_결과_몬스터 == 1:
            print('마구잡이로 쏘아지는', 적.name + '의 브레스.')
            wait()
            print(플레이어.name + '은(는) 자신을 향해 날아오는 수십 개의 불덩이들에게 무차별적으로 적중당합니다.')
        if 지문_결과_몬스터 == 2:
            print('먼발치에서 쏘아지는', 적.name + '의 브레스.')
            wait()
            print('수 개의 불덩이들은 소름끼치는 포물선의 궤적을 그리며, 순식간에', 플레이어.name + '에게로 날아와 적중합니다.')
        if 지문_결과_몬스터 == 3:
            print(적.name + '은 하늘에 날아올라', 플레이어.name + '을(를) 향해 브레스를 내뿜습니다.')
            wait()
            print(플레이어.name + '(이)가 미처 반응할 틈도 없이, 수 개의 화염구가', 플레이어.name + '에게로 날아와 적중합니다.')
        if 지문_결과_몬스터 == 4:
            print(적.name + '은(는)', 플레이어.name + '을(를) 향해 울부짖으며 브레스를 내뿜습니다.')
            wait()
            print(플레이어.name + '은(는) 그 압도적인 무력 앞에 몸이 굳어버렸습니다.')
            wait()
            print('아...', 플레이어.name + '은(는) 자신을 향해 날아오는 불덩이를 바라만 볼 수 밖에 없습니다.')
    if 6<= 주사위_결과_몬스터 <= 9:
        roll_temporary_monster(4)
        if 지문_결과_몬스터 == 1:
            print(플레이어.name + '침을 꿀꺽 삼키며 정신을 바짝 차리고,', 적.name + '의 브레스를 피하려고 시도합니다.')
            wait()
            print(플레이어.name + '은(는) 땅을 박차고, 뛰어오르고, 이리저리 몸을 던지며 수 개의 화염구들을 피해냅니다.')
        if 지문_결과_몬스터 == 2:
            print('정신없이 땅을 수 차례 구르며 화염구를 피해내는', 플레이어.name)
        if 지문_결과_몬스터 == 3:
            print('아슬아슬하게 스쳐지나가는', 적.name + '의 브레스!')
        if 지문_결과_몬스터 == 4:
            print('그런데, 이게 뭔가요.', 적.name + '은(는) 사실 브레스를 쏘려던 게 아니라 갑자기 재채기가 마려워 숨을 들이마쉰 것이었습니다!')
            wait()
            print(적.name, ': 엣취!!!')
    if 주사위_결과_몬스터 == 10:
        print('하지만', 플레이어.name + '은(는) 이미', 적.name + '의 화염구가 날아올 것을 예상하고 있었습니다.')
        wait()
        print(플레이어.name + '은(는)', 적.name + '의 공격을 부드럽게 피해 역으로 공격합니다!')
    monster_damage_function(3, 0.5)

def end() :
    dot()
    print(플레이어.name)
    wait()
    print(플레이어.job)
    wait()
    print('무기 :', 플레이어.weapon)
    wait()
    print('방어구 :', 플레이어.armor)
    wait()
    print('HP :', 플레이어.hp, '/', 플레이어_체력)
    wait()
    print('MP :', 플레이어.mp, '/', 플레이어_마력)
    wait()
    print('돈 :', 플레이어.money, '원')
    wait()
    print('아이템 :', 플레이어.inventory)
    wait()
    print(단계+1, '단계 :', 적.name)
    dot()
    print('==========The END==========')
    time.sleep(3600)

def mana_cost(skill_name) : #skill_name=문자열
    if 플레이어.mp - dict_skill[skill_name] < 0:
        show_player_mp()
        one()
        print('마나가 부족하여 체력이 대신 소모됩니다.')
        one()
        print('체력', dict_skill[skill_name] - 플레이어.mp, '감소')
        one()
        print('마나', 플레이어.mp, '감소')
        one()
        플레이어.hp = 플레이어.hp - (dict_skill[skill_name] - 플레이어.mp)
        플레이어.mp = 0
        if 플레이어.hp <= 0:
            플레이어.hp = 0
        show_player_hp()
        show_player_mp()
    if 플레이어.mp - dict_skill[skill_name] >= 0:
        플레이어.mp = 플레이어.mp - dict_skill[skill_name]
        one()
        print('마나', dict_skill[skill_name], '감소')
        show_player_mp()

def shop() :
    one()
    print(플레이어.name+'은(는) 상점에 들어갑니다.')
    wait()
    if 플레이어.money <= 999 :
        print('상점 주인 : 뭐시여? 시방 천원도 없는 거지눔의 시키가 여긴 왜 온 것이여!')
        wait()
        print(플레이어.name, ': 아! 아! 할머니! 때리지 마세요!!')
        dot()
        print(플레이어.name+'은(는) 상점에서 쫓겨났습니다.')
        wait()
        print('아무래도 돈을 좀 더 벌어와야 할 듯 합니다.')
    else :
        print('상점 주인 : 아따 이런 곳에도 손님이 계시는구마. 여기, 골라 보시랑께요.')
        menu()
        buy = input()
        one()
        while buy not in list_shop :
            print('상점 주인 : 잉? 내가 나이를 먹어서 그런가... 똑바로 좀 말해보쇼!')
            one()
            print(list_shop)
            buy = input()
            one()
        if buy != '나가기' :
            purchase(buy)
        if buy == '나가기' :
            print('상점 주인 : 안 살 거면 뭣하러 왔어? 쯧...')
            wait()
            print(플레이어.name + '은(는) 상점을 나갑니다.')

def menu() :
    one()
    print('')
    print('====================================================================================================')
    print('')
    one()
    print('HP 회복 :', dict_buy['HP 회복'], '원')
    print('MP 회복 :', dict_buy['MP 회복'], '원')
    print('부활의 영약 :', dict_buy['부활의 영약'], '원')
    if 플레이어.job == '검사' :
        print('질 좋은 대검 (공격력 150) :', dict_buy['질 좋은 대검'], '원')
        print('전설의 판금 갑옷 (방어력 50) :', dict_buy['전설의 판금 갑옷'], '원')
    if 플레이어.job == '궁수' :
        print('마법 활 (공격력 200, 주사위 수정치 +5) :', dict_buy['마법 활'], '원')
        print('마법 가죽 갑옷 (방어력 40, 남은 부활 횟수 +1) :', dict_buy['마법 가죽 갑옷'], '원')
    if 플레이어.job == '마법사' :
        print('전설의 지팡이 (공격력 300) :', dict_buy['전설의 지팡이'], '원')
        print('질 좋은 로브 (방어력 30) :', dict_buy['질 좋은 로브'], '원')
    one()
    print('')
    print('====================================================================================================')
    print('')
    one()
    print('상점 주인 : 더도 말고 덜도 말고 딱 하나만 팔 거니께, 잘 거시기 하쇼잉~')
    one()
    print(list_shop)

def purchase(thing): #thing=문자열
    global 주사위_수정치
    global list_shop
    global 부활
    if 플레이어.money <= dict_buy[thing]:
        print('상점 주인 : 어디 이눔이 지금 돈도 없으면서 사기를 치려고... 예끼!')
        wait()
        print(플레이어.name, ': 아! 아! 할머니! 때리지 마세요!!')
        dot()
        print(플레이어.name + '은(는) 상점에서 쫓겨났습니다.')
    if 플레이어.money >= dict_buy[thing]:
        print('상점 주인 : 자, ' + thing + '(이)오.', dict_buy[thing], '원일세.')
        one()
        print(dict_buy[thing], '원 감소')
        플레이어.money = 플레이어.money - dict_buy[thing]
        if thing == 'HP 회복' or thing == 'MP 회복' :
            플레이어.inventory.append(thing)
            one()
            print(thing, '획득')
            show_player_money()
            show_player_inventory()
        if thing == '부활의 영약' :
            one()
            print(thing, '사용')
            show_player_money()
            if thing == '부활의 영약' :
                부활 = 부활 + 1
                one()
                print('남은 부활 횟수 :', 부활)
        if thing == '질 좋은 대검' or thing == '마법 활' or thing == '전설의 지팡이' :
            플레이어.weapon = thing
            list_shop.remove(thing)
            one()
            print(thing, '장착')
            show_player_money()
            show_player_weapon()
            if 플레이어.weapon == '마법 활' :
                주사위_수정치 = 주사위_수정치 + 5
                one()
                print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
        if thing == '전설의 판금 갑옷' or thing == '마법 가죽 갑옷' or thing == '질 좋은 로브' :
            플레이어.armor = thing
            list_shop.remove(thing)
            one()
            print(thing, '장착')
            show_player_money()
            show_player_armor()
            if 플레이어.armor == '마법 가죽 갑옷' :
                부활 = 부활 + 1
                one()
                print('남은 부활 횟수 :', 부활)
        one()
        print('상점 주인 : 어여 가쇼~ 다음에 또 오시던가.')
        wait()
        print(플레이어.name+'은(는) 상점을 나갑니다.')

###################################################################################################################

list_job = ['검사', '궁수', '마법사']
list_shop = ['나가기', 'HP 회복', 'MP 회복', '부활의 영약']
list_swordman_shop = ['질 좋은 대검', '전설의 판금 갑옷']
list_archer_shop = ['마법 활', '마법 가죽 갑옷']
list_magician_shop = ['전설의 지팡이', '질 좋은 로브']
dict_name = {'고블린': 5, '오크': 3, '언데드': 10, '놀': 3, '라이칸스로프': 1, '오우거': 1, '골렘': 1, '사이클로프스': 1, '드래곤': 1}
dict_weapon = {'맨손': 0, '대검': 100, '활': 100, '지팡이': 100, '질 좋은 대검': 150, '마법 활': 200, '전설의 지팡이': 300,
               '녹슨 단검': 20, '단검': 30, '뼈 칼': 40, '단창': 50, '마체테': 60, '거대한 도끼': 70, '거대한 바위': 80, '거대한 삼지창': 90, '브레스': 100}
dict_armor = {'맨몸': 0, '판금 갑옷': 30, '가죽 갑옷': 25, '로브': 20, '전설의 판금 갑옷': 50, '마법 가죽 갑옷': 40, '질 좋은 로브': 30}
dict_skill = {'삼연속 베기': 10, '방패 세우기': 15, '방패 받아치기': 15, '네 발 끼워쏘기': 15, '게릴라전': 15, '기관단총': 25, '마탄 세례': 20, '마나 충전': 20, '아포칼립스': 50}
dict_buy = {'HP 회복': 10000, 'MP 회복': 5000, '부활의 영약': 50000, '질 좋은 대검': 100000, '전설의 판금 갑옷': 50000, '마법 활': 75000, '마법 가죽 갑옷': 75000, '전설의 지팡이': 100000, '질 좋은 로브': 50000}

class player:
    name = '이름'
    hp = 100
    mp = 100
    job = '직업'
    weapon = '맨손'
    armor = '맨몸'
    action = []
    inventory = ['HP 회복', 'MP 회복']
    money = 0

class swordsman(player):
    job = '검사'
    weapon = '대검'
    armor = '판금 갑옷'
    action = ['삼연속 베기', '방패 세우기']

    def three_consecutive_cut(self):
        global 주사위_결과_플레이어
        roll_player(50)
        if 주사위_결과_플레이어 == 5 :
            wait()
            print(플레이어.name+'은(는) 검을 들어올립니다.')
            wait()
            print('지금 이 순간,', 플레이어.name + '에게는', 적.name + '와(과) 자신 외에 아무 것도 보이지 않습니다.')
            wait()
            print('오로지', 적.name + '의 숨통을 끊는 데에만 집중하며,', 플레이어.name + '은(는) 검을 내려칩니다.')
        if 주사위_결과_플레이어 == 2 :
            wait()
            roll_temporary_player(5)
            if 지문_결과_플레이어 == 1 :
                print(플레이어.name+'은(는)', 적.name+'의 신형을 횡으로 크게 벱니다.')
            if 지문_결과_플레이어 == 2 :
                print(플레이어.name+'은(는)', 적.name+'의 몸통을 노려 검을 쑤셔넣습니다.')
            if 지문_결과_플레이어 == 3 :
                print(플레이어.name+'은(는)', 적.name+'을(를) 위에서 아래로 내려찍습니다.')
            if 지문_결과_플레이어 == 4 :
                print(플레이어.name+'은(는)', 적.name+'을(를) 사정없이 내려칩니다.')
            if 지문_결과_플레이어 == 5 :
                print(플레이어.name+'은(는)', 적.name+'을(를) 향해 돌진합니다.')
        if 주사위_결과_플레이어 == 1 :
            wait()
            roll_temporary_player(5)
            if 지문_결과_플레이어 == 1 :
                print('허공을 가르는', 플레이어.name+'의 공격.')
            if 지문_결과_플레이어 == 2 :
                print(적.name+'(이)가', 플레이어.name+'의 엉성한 공격을 비웃습니다.')
            if 지문_결과_플레이어 == 3 :
                print(플레이어.name + '님, 어딜 공격하시는 겁니까...? 거긴 반대쪽입니다.')
            if 지문_결과_플레이어 == 4 :
                print(플레이어.name + '(이)가 한 발 늦었습니다.')
            if 지문_결과_플레이어 == 5 :
                print(적.name + '의 민첩한 몸놀림!')
        player_damage_function(3, 1)

    def lift_shield(self):
        global 방어력_임시_수정치
        global 주사위_임시_수정치
        global 주사위_결과_플레이어
        roll_player(50)
        wait()
        if 주사위_결과_플레이어 == 5:
            print('방패 세우기 대성공')
            방어력_임시_수정치 = 20
            주사위_임시_수정치 = 0
            wait()
            print('현재 방어력 :', dict_armor[플레이어.armor] + 방어력_임시_수정치)
            one()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
            플레이어.action.remove('방패 세우기')
            플레이어.action.append('방패 받아치기')
        if 주사위_결과_플레이어 == 2:
            print('방패 세우기 성공')
            방어력_임시_수정치 = 20
            주사위_임시_수정치 = -3
            wait()
            print('현재 방어력 :', dict_armor[플레이어.armor] + 방어력_임시_수정치)
            one()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
            플레이어.action.remove('방패 세우기')
            플레이어.action.append('방패 받아치기')
        if 주사위_결과_플레이어 == 1:
            print('방패 세우기 실패')

    def push_shield(self):
        global 방어력_임시_수정치
        global 주사위_임시_수정치
        global 주사위_결과_플레이어
        roll_player(50)
        wait()
        if 주사위_결과_플레이어 == 5:
            방어력_임시_수정치 = 0
            주사위_임시_수정치 = 0
            print('방패 받아치기 대성공')
            wait()
            print('현재 방어력 :', dict_armor[플레이어.armor] + 방어력_임시_수정치)
            one()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
            플레이어.action.remove('방패 받아치기')
            플레이어.action.append('방패 세우기')
        if 주사위_결과_플레이어 == 2:
            방어력_임시_수정치 = 0
            주사위_임시_수정치 = 0
            print('방패 받아치기 성공')
            wait()
            print('현재 방어력 :', dict_armor[플레이어.armor] + 방어력_임시_수정치)
            one()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
            플레이어.action.remove('방패 받아치기')
            플레이어.action.append('방패 세우기')
        if 주사위_결과_플레이어 == 1:
            print('방패 받아치기 실패')
        player_damage_function(1, 5)

class archer(player):
    job = '궁수'
    weapon = '활'
    armor = '가죽 갑옷'
    action = ['네 발 끼워쏘기', '게릴라전', '기관단총']

    def shoot_four_arrow(self):
        global 주사위_결과_플레이어
        wait()
        roll_player(50)
        if 주사위_결과_플레이어 == 5 :
            print(플레이어.name+'은(는) 눈을 감습니다.')
            wait()
            print('그러고는 후우, 하고 숨을 가다듬은 뒤 다시 눈꺼풀을 들어올려', 적.name+'을(를) 신중하게 조준합니다.')
            wait()
            print('곧 끊어질 듯이 팽팽해진 활시위, 몸이 앞뒤로 흔들릴 만큼 큰 반동을 주며 쏘아진 화살은 눈 깜짝할 사이에', 적.name+'의 심장을 관통합니다.')
        if 주사위_결과_플레이어 == 2 :
            roll_temporary_player(5)
            if 지문_결과_플레이어 == 1 :
                print(플레이어.name+'은(는) 재빠르게', 적.name+'의 왼쪽으로 달려갑니다.')
                wait()
                print('그러고는', 적.name+'의 옆구리를 노려 화살을 쏩니다!')
            if 지문_결과_플레이어 == 2 :
                print(플레이어.name+'은(는)', 적.name+'의 몸통을 노려 화살을 발사합니다.')
            if 지문_결과_플레이어 == 3 :
                print(플레이어.name+'은(는) 앞으로 달려나가며', 적.name+'을(를) 향해 화살을 난사합니다.')
            if 지문_결과_플레이어 == 4 :
                print(플레이어.name+'은(는)', 적.name+'을(를) 정확히 노려 화살을 발사합니다.')
            if 지문_결과_플레이어 == 5 :
                print(플레이어.name+'은(는) 천천히 뒷걸음질 치며, 다가오는', 적.name+'을(를) 향해 화살을 쏩니다.')
        if 주사위_결과_플레이어 == 1 :
            roll_temporary_player(5)
            if 지문_결과_플레이어 == 1 :
                print('허공을 가르는', 플레이어.name+'의 화살.')
            if 지문_결과_플레이어 == 2 :
                print(적.name+'(이)가', 플레이어.name+'의 엉성한 활솜씨을 비웃습니다.')
            if 지문_결과_플레이어 == 3 :
                print(플레이어.name + '님, 어딜 공격하시는 겁니까...? 거긴 반대쪽입니다.')
            if 지문_결과_플레이어 == 4 :
                print(플레이어.name + '(이)가 한 발 늦었습니다.')
            if 지문_결과_플레이어 == 5 :
                print(적.name + '의 민첩한 몸놀림!')
        player_damage_function(4, 1)

    def guerrilla(self):
        global 주사위_임시_수정치
        global 주사위_결과_플레이어
        wait()
        roll_player(50)
        if 주사위_결과_플레이어 == 5:
            주사위_임시_수정치 = 주사위_임시_수정치 + 3
            print('게릴라전 대성공')
            wait()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
        if 주사위_결과_플레이어 == 2:
            주사위_임시_수정치 = 주사위_임시_수정치 + 3
            print('게릴라전 성공')
            wait()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
        if 주사위_결과_플레이어 == 1:
            print('게릴라전 실패')
        player_damage_function(1, 3)

    def submachine_gun(self):
        global 주사위_임시_수정치
        global 주사위_결과_플레이어
        주사위_임시_수정치 = 주사위_임시_수정치 - 15
        roll_player(50)
        주사위_임시_수정치 = 주사위_임시_수정치 + 15
        wait()
        if 주사위_결과_플레이어 == 5:
            print('기관단총 대성공')
        if 주사위_결과_플레이어 == 2:
            print('기관단총 성공')
        if 주사위_결과_플레이어 == 1:
            print('기관단총 실패')
        player_damage_function(15, 1)

class magician(player):
    job = '마법사'
    weapon = '지팡이'
    armor = '로브'
    action = ['마탄 세례', '마나 충전', '아포칼립스']

    def magic_missile_perfusion(self):
        global 주사위_결과_플레이어
        roll_player(50)
        wait()
        if 주사위_결과_플레이어 == 5 :
            print(플레이어.name+'(이)가 주문을 외우자,', 플레이어.name, '주변의 마력이 들끓습니다.')
            wait()
            print('어느새', 플레이어.name+'의 주변에 하나둘씩 생성된 수십개의 마탄.')
            wait()
            print('웅웅대며 진동하던 마탄은 눈 깜짝할 사이에', 적.name+'을(를) 향해 날아가 굉음을 내며 폭발합니다.')
        if 주사위_결과_플레이어 == 2 :
            roll_temporary_player(5)
            if 지문_결과_플레이어 == 1 :
                print(플레이어.name+'은(는) 마나의 흐름에 몸을 맡기고 떠오릅니다.')
                wait()
                print('그러고는, 하늘 위에서', 적.name+'을 노려 마탄을 발사합니다.')
            if 지문_결과_플레이어 == 2 :
                print(플레이어.name+'은(는)', 적.name+'을(를) 향해 손을 뻗으며 여러 발의 마탄을 난사합니다.')
            if 지문_결과_플레이어 == 3 :
                print(플레이어.name+'은(는) 집중하여', 적.name+'을(를) 조준해 마탄을 발사합니다.')
            if 지문_결과_플레이어 == 4 :
                print(플레이어.name+'(이)가 주문을 외우자, 여러 개의 마탄이', 적.name+'을(를) 향해 발사됩니다.')
            if 지문_결과_플레이어 == 5 :
                print(플레이어.name+'은(는) 앞으로 걸어나가며, 다가오는', 적.name+'을(를) 향해 마탄을 쏩니다.')
        if 주사위_결과_플레이어 == 1 :
            roll_temporary_player(5)
            if 지문_결과_플레이어 == 1 :
                print('허공을 가르는', 플레이어.name+'의 마탄.')
            if 지문_결과_플레이어 == 2 :
                print(적.name+'(이)가', 플레이어.name+'의 엉성한 마법을 비웃습니다.')
            if 지문_결과_플레이어 == 3 :
                print(플레이어.name + '님, 어딜 공격하시는 겁니까...? 거긴 반대쪽입니다.')
            if 지문_결과_플레이어 == 4 :
                print(플레이어.name + '(이)가 한 발 늦었습니다.')
            if 지문_결과_플레이어 == 5 :
                print(적.name + '의 민첩한 몸놀림!')
        player_damage_function(5, 1)

    def mana_charge(self):
        global 주사위_임시_수정치
        global 공격력_임시_수정치
        global 주사위_결과_플레이어
        roll_player(50)
        wait()
        if 주사위_결과_플레이어 == 5:
            print('마나 충전 대성공')
            주사위_임시_수정치 = 주사위_임시_수정치 + 10
            공격력_임시_수정치 = 공격력_임시_수정치 + 50
            wait()
            print('현재 공격력 :', dict_weapon[플레이어.weapon] + 공격력_임시_수정치)
            one()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
        if 주사위_결과_플레이어 == 2:
            print('마나 충전 성공')
            주사위_임시_수정치 = 주사위_임시_수정치 + 5
            공격력_임시_수정치 = 공격력_임시_수정치 + 25
            wait()
            print('현재 공격력 :', dict_weapon[플레이어.weapon] + 공격력_임시_수정치)
            one()
            print('현재 주사위 수정치 :', 주사위_수정치 + 주사위_임시_수정치)
        if 주사위_결과_플레이어 == 1:
            print('마나 충전 실패')

    def apocalypse(self):
        global 주사위_임시_수정치
        global 주사위_결과_플레이어
        주사위_임시_수정치 = 주사위_임시_수정치 - 25
        roll_player(50)
        주사위_임시_수정치 = 주사위_임시_수정치 + 25
        wait()
        if 주사위_결과_플레이어 == 5:
            print('아포칼립스 대성공')
        if 주사위_결과_플레이어 == 2:
            print('아포칼립스 성공')
        if 주사위_결과_플레이어 == 1:
            print('아포칼립스 실패')
        player_damage_function(10, 10)

class monster:
    name = '이름'
    hp = 0
    weapon = '맨손'
    armor = '맨몸'
    inventory = []
    money = 0

class goblin(monster):
    name = '고블린'
    hp = 25
    weapon = '녹슨 단검'
    armor = '맨몸'
    inventory = []
    money = 100
    def action(self):
        monster_sword_action()


class ork(monster) :
    name = '오크'
    hp = 40
    weapon = '단검'
    armor = '맨몸'
    inventory = []
    money = 250
    def action(self):
        monster_sword_action()


class undead(monster) :
    name = '언데드'
    hp = 25
    weapon = '뼈 칼'
    armor = '맨몸'
    inventory = []
    money = 250
    def action(self):
        monster_sword_action()


class gnoll(monster) :
    name = '놀'
    hp = 75
    weapon = '단창'
    armor = '맨몸'
    inventory = []
    money = 1000
    def action(self):
        monster_sword_action()


class lycanthrope(monster) :
    name = '라이칸스로프'
    hp = 200
    weapon = '마체테'
    armor = '맨몸'
    inventory = []
    money = 5000
    def action(self):
        monster_sword_action()


class ogre(monster) :
    name = '오우거'
    hp = 300
    weapon = '거대한 도끼'
    armor = '맨몸'
    inventory = []
    money = 10000
    def action(self):
        monster_sword_action()


class golem(monster) :
    name = '골렘'
    hp = 500
    weapon = '거대한 바위'
    armor = '맨몸'
    inventory = []
    money = 50000
    def action(self):
        monster_sword_action()


class psyclops(monster) :
    name = '사이클로프스'
    hp = 1000
    weapon = '거대한 삼지창'
    armor = '맨몸'
    inventory = []
    money = 200000
    def action(self):
        monster_sword_action()


class dragon(monster) :
    name = '드래곤'
    hp = 2500
    weapon = '브레스'
    armor = '맨몸'
    inventory = []
    money = 1000000
    def action(self):
        monster_breath_action()

class clear(monster) :
    name = '클리어'


########################################################################################################################

introduce_text_game_project()
set_shortcut()

dot()
print(플레이어.job +' ' + 플레이어.name + '...')

wait()
print('모험의 세계에 오신 것을 환영합니다.')

wait()
print('')
print('====================================================================================================')
print('')

wait()
print('데모 버전 : 9단계로 이루어진 전투에서 죽지 않고 승리하면 게임을 클리어합니다.')

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnorvous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========고블린과의 전투==========')
print('')
wait()
fight('고블린', 'goblin', goblin, image_goblin)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnorvous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========오크과의 전투==========')
print('')
wait()
fight('오크', 'ork', ork, image_ork)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnorvous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========언데드과의 전투==========')
print('')
wait()
fight('언데드', 'undead', undead, image_undead)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnervous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========놀과의 전투==========')
print('')
wait()
fight('놀', 'gnoll', gnoll, image_gnoll)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnervous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========라이칸스로프과의 전투==========')
print('')
wait()
fight('라이칸스로프', 'lycanthrope', lycanthrope, image_lycanthrope)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnervous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========오우거과의 전투==========')
print('')
wait()
fight('오우거', 'ogre', ogre, image_ogre)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnenenervous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========골렘과의 전투==========')
print('')
wait()
fight('골렘', 'golem', golem, image_golem)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnenenervous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========사이클로프스과의 전투==========')
print('')
wait()
fight('사이클로프스', 'psyclops', psyclops, image_psyclops)

rest()
winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Mnenenervous.wav',winsound.SND_ASYNC)
wait()
print('')
print('==========드래곤과의 전투==========')
print('')
wait()
fight('드래곤', 'dragon', dragon, image_dragon)

winsound.PlaySound(None, winsound.SND_ASYNC)
winsound.PlaySound('C:\TGPBGMwav\Moblivion.wav',winsound.SND_ASYNC)
적 = clear()
wait()
print('축하드립니다!')
wait()
print(플레이어.name+'은(는) 게임을 클리어했습니다.')
end()