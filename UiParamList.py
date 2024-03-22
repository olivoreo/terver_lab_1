from UIParam import UiParam
import probabilityFunctions

def paramList():
    paramList = []
    paramList.append(initializationParam1())
    paramList.append(initializationParam2())
    paramList.append(initializationParam3())
    paramList.append(initializationParam4())
    paramList.append(initializationParam5())
    paramList.append(initializationParam6())
    paramList.append(initializationParam7())
    return paramList
def initializationParam1():
    param = UiParam()
    param.labelText1 = "N:"
    param.lineEditVisibility1 = True
    param.needNum1 = True
    param.pictureName = "Перестановка без повторений"
    param.function = lambda values: probabilityFunctions.factorial(values.num1)
    return param

def initializationParam2():
    param = UiParam()
    param.labelText1 = "N:"
    param.labelText2 = "M:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Сочетание без повторений"
    param.function = lambda values: probabilityFunctions.combWithoutRep(values.num1, values.num2)
    return param

def initializationParam3():
    param = UiParam()
    param.labelText1 = "N:"
    param.labelText2 = "M:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Размещение без повторений"
    param.function = lambda values: probabilityFunctions.placeWithoutRep(values.num1, values.num2)
    return param

def initializationParam4():
    param = UiParam()
    param.labelText1 = "N:"
    param.labelText2 = "K:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Сочетание с повторениями"
    param.function = lambda values: probabilityFunctions.combWithRep(values.num1, values.num2)
    return param

def initializationParam5():
    param = UiParam()
    param.labelText1 = "M:"
    param.labelText2 = "N:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Размещение с повторениями"
    param.function = lambda values: probabilityFunctions.placeWithRep(values.num1, values.num2)
    return param

def initializationParam6():
    param = UiParam()
    param.labelText1 = "Количество чисел N:"
    param.lineEditVisibility1 = True
    param.labelListText1 = "Числа n:"
    param.nameElementList1 = "n"
    param.listVisibility1 = True
    param.numOfLineEditListenerList1 = 1
    param.needList1 = True
    param.pictureName = "Перестановка с повторениями"
    param.function = lambda values: probabilityFunctions.permutationsWithRep(values.list1)
    return param

def initializationParam7():
    param = UiParam()
    param.labelText0 = ("Условие задачи: \nВ партии, состоящей из k изделий, имеется l дефектных.\n"
                        "Из партии выбирается для контроля r изделий."
                        "\nНайти вероятность того, что из них S изделий будут дефектными.")
    param.labelText1 = "Всего изделий k:"
    param.labelText2 = "Дефектных изделий l:"
    param.labelText3 = "Кол-во изделий для контроля r:"
    param.labelText4 = "Кол-во дефектных изделий среди выбранных для контроля S:"
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
