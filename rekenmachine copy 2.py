# rekenmachine
# vraag om twee getallen en een operator
num1 = input ("Voer het eerste getal in: ")
# operator
operator = input ("Voer de operator in (+, -, *, /): ")
# Voer het tweede getal in
num2 = input ("Voer het tweede getal in: ")
# converteer de getallen naar float
num1 = float(num1)
num2 = float(num2)
# welke operator is gekozen
if operator == "+":
    resultaat = num1 + num2
elif operator == "-":
    resultaat = num1 - num2
elif operator == "*":
    resultaat = num1 * num2
elif operator == "/":
    resultaat = num1 / num2
# toon het resultaat
print ("Het resultaat is: ", resultaat)
