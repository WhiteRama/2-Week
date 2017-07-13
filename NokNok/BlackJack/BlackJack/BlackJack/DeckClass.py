import random

class Deck:         # Deck Ŭ����

    cardList = []           ## ���� ī���� ��� ����

    def draw(self):         ## �� �̱�

        while True:
            mark = random.randint(0,3)  ## ���� ���ϱ�

            if mark==0:
                mark = 'S'
            if mark==1:
                mark = 'D'
            if mark==2:
                mark = 'H'
            if mark==3:
                mark = 'C'

            num = random.randint(1,13) ## ���� ���ϱ�

            if num == 11:
                num = 'J'
            if num == 12:
                num = 'Q'
            if num == 13:
                num = 'K'
            if num == 1:
                num = 'A'

            card = str(mark) + str(num)

            if not(card in self.cardList):
                self.cardList.append(card)
                return card

    #end of draw

    def reset(self):        # ī�� ��� ����
        self.cardList = []

    #end of reset
#end of class
