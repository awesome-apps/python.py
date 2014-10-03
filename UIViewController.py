#global data
UIGridArray = [0,1,2,3,4,5,6,7,8]
UIMessageArray = ["X IS THE WINNER", "O IS THE WINNER", "IT IS A DRAW", "X STARTS FIRST"]
def UIRowCheck():
    x = 0
    y = x+ 1
    z = x + 2
    while x<=6:
        if UIGridArray[x] == 'X' and UIGridArray[y] == 'X' and UIGridArray[z] == 'X':
            UIMessageArray[0]
            break
        x +=3
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
