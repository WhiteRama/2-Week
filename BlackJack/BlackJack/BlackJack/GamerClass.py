class Gamer:
  
    name = str()        # 게이머 분류 : 사람 이름 혹은 '딜러'
    hand = []           # 손패
    weight = int()      # 가중치
    weightList = []     # 가중치 저장 리스트
    hit = True          # 히트 여부 :: 초기는 무조건 hit


    def countWeight(self):  # 가중치 판별 메소드
        
        self.weight = 0

        #### 가중치 계산 ####

        for i in range(len(self.hand)):          
            self.weightList.append(self.hand[i][1:])

        for i in range(len(self.weightList)):   

            if self.weightList[i] == 'K' or self.weightList[i] == 'Q' or self.weightList[i] == 'J':
                self.weight += 10
            elif self.weightList[i] == 'A':
                self.weight += 11
            else:
                self.weight += int(self.weightList[i])

        #### A 카드 계산 ####

        numOfA = self.weightList.count('A')

        while self.weight>21:

            if numOfA >0:
                self.weight-=10
                numOfA-=1
            else:
                break


    #end of countWeight

    def drawCard(self, card):   # hit에 따른 드로우 실행    
           
        self.hand.append(card)       # 손패에 card 추가

    #end of drawCard

    def reset(self):            # 초기화

        self.hand = []
        self.hit = True


#end of Class Gamer


class Player(Gamer):        # 블랙잭 참가 Player

    def __init__ (self):
        self.name = 'player'
        self.hand = []
        self.weightList = []

    def askHit(self):       # hit 여부 입력 메소드
        
        #### Hit? ####
        
        if self.hit == True:
            while True:
                answer = input("Hit? (Y/N)")

                if answer == 'Y' or answer == 'y':
                    answer = 'Y'
                    break
                elif answer == 'N' or answer == 'n':
                    answer = 'N'
                    break
                else:
                    print("Wrong Input")
       
        #### 처리 ####

        if answer == 'Y':
            self.hit = True
        else:
            self.hit = False

    #end of askHit
#end of Class Player



class Dealer(Gamer):        # 블랙잭의 딜러

    def __init__(self):
        self.name = 'dealer'
        self.hand = []
        self.weightList = []

    def dealerHitRule(self):    # 딜러 히트 룰에 따라, 가중치 16 이하일 경우 부조건 Hit, 17 이상일 경우 무조건 Stay
        
        if self.weight <= 16:
            print("Dealer : Hit")
            self.hit = True
        else:
            print("Dealer : Stay")
            self.hit = False

    #end of dealerHitRule
#end of Class Dealer


