#global data
UIGridArray = [0,1,2,3,4,5,6,7,8]
UIMessageArray = ["X IS THE WINNER", "O IS THE WINNER", "IT IS A DRAW", "X STARTS"]
class AppDelegate:
    def UIInstruct(self):
        print UIMessageArray[3]
    def UIGame(self):
        UIIteration = 9
        UITurnManager = 0
        while UIIteration > 0:
            UITurnTester = UITurnManager%2
            UIGridPosition = int(input("Enter a position"))
            if UITurnTester == 0:
                UIGridArray[UIGridPosition] = 'O'
            else:
                UIGridArray[UIGridPosition] = 'X'
            UITurnManager += 1
            UIView.UIGridView()
            print(str(UITurnManager) + " turns are over")
            UIIteration-=1
            UIRowCheck()
