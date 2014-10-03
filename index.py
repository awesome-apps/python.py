#global data
UIGridArray = [0,1,2,3,4,5,6,7,8]
UIMessageArray = ["X IS THE WINNER", "O IS THE WINNER", "IT IS A DRAW", "X STARTS FIRST"]

class UIViewController:
    UIViewLine = "_______"
    def UIGridView(self):
        print(UIViewController.UIViewLine)
        print("|" + str(UIGridArray[0]) + "|" + str(UIGridArray[1]) + "|" + str(UIGridArray[2]) + "|")
        print(UIViewController.UIViewLine)
        print("|" + str(UIGridArray[3]) + "|" + str(UIGridArray[4]) + "|" + str(UIGridArray[5]) + "|")
        print(UIViewController.UIViewLine) 
        print("|" + str(UIGridArray[6]) + "|" + str(UIGridArray[7]) + "|" + str(UIGridArray[8]) + "|")
        print(UIViewController.UIViewLine) 
UIView = UIViewController()
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
            UIIteration -=1
            x = 0
            y = x + 1
            z = x + 2
            a = x + 3
            b = x + 4
            c = 2
            t = 3
            while x<=6:
                if UIGridArray[x] == 'X' and UIGridArray[y] == 'X' and UIGridArray[z] == 'X':
                    break
                    UIMessageArray[0]
                x = x + 3
                    
UIApp = AppDelegate()
UIApp.UIInstruct()
UIApp.UIGame()
