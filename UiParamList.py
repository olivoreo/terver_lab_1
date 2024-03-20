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
    paramList.append(initializationParam8())
    paramList.append(initializationParam9())
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
    param.labelText2 = "M:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.pictureName = "Сочетание с повторениями"
    param.function = lambda values: probabilityFunctions.combWithRep(values.num1, values.num2)
    return param

def initializationParam5():
    param = UiParam()
    param.labelText1 = "N:"
    param.labelText2 = "M:"
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
    param.labelText1 = "N:"
    param.labelText2 = "M:"
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.needNum1 = True
    param.needNum2 = True
    param.function = lambda values: probabilityFunctions.task2(values.num1, values.num2)
    return param

def initializationParam8():
    param = UiParam()
    param.labelText1 = "Количество чисел M:"
    param.lineEditVisibility1 = True
    param.labelListText1 = "Числа m:"
    param.nameElementList1 = "m"
    param.listVisibility1 = True
    param.numOfLineEditListenerList1 = 1
    param.needList1 = True
    param.function = lambda values: probabilityFunctions.task4(values.list1)
    return param

def initializationParam9():
    param = UiParam()
    param.labelText1 = "N:"
    param.labelText2 = "M:"
    param.labelText3 = ""
    param.lineEditVisibility1 = True
    param.lineEditVisibility2 = True
    param.lineEditVisibility3 = False
    param.labelListText1 = ""
    param.labelListText2 = ""
    param.listVisibility1 = False
    param.listVisibility2 = False
    return param
