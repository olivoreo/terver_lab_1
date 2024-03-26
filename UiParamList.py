from UIParam import UiParam
import probabilityFunctions

def paramList():
    paramList = []
    paramList.append(initializationParam1())
    paramList.append(initializationParam2())
    paramList.append(initializationParam3())
    paramList.append(initializationParam4())
    return paramList
def initializationParam1():
    param = UiParam()
    param.labelText1 = "N [1-500]:"
    param.labelText2 = "M [1-500]:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Сочетание без повторений"
    param.function = lambda values: probabilityFunctions.combWithoutRep(values.num1, values.num2)
    return param

def initializationParam2():
    param = UiParam()
    param.labelText1 = "N [1-500]:"
    param.labelText2 = "K [1-490]:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Сочетание с повторениями"
    param.function = lambda values: probabilityFunctions.combWithRep(values.num1, values.num2)
    return param

def initializationParam3():
    param = UiParam()
    param.labelText1 = "M [1-500]:"
    param.labelText2 = "N [1-500]:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Размещение с повторениями"
    param.function = lambda values: probabilityFunctions.placeWithRep(values.num1, values.num2)
    return param

def initializationParam4():
    param = UiParam()
    param.labelText0 = ("Условие задачи: \nВ партии, состоящей из k изделий, имеется l дефектных.\n"
                        "Из партии выбирается для контроля r изделий."
                        "\nНайти вероятность того, что из них S изделий будут дефектными.")
    param.labelText1 = "Всего изделий k [1-500]:"
    param.labelText2 = "Дефектных изделий l [1-500]:"
    param.labelText3 = "Кол-во изделий для контроля r [1-500]:"
    param.labelText4 = "Кол-во дефектных изделий среди выбранных для контроля S [1-500]:"
    param.lineEditVisibility0 = True
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.lineEditVisibility3 = True
    param.lineEditVisibility4 = True
    param.needNum1 = True
    param.needNum2 = True
    param.needNum3 = True
    param.needNum4 = True
    param.pictureName = "Задача1"
    param.function = lambda values: probabilityFunctions.task1(values.num1, values.num2, values.num3, values.num4)
    return param
