salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital = 0

for i in range(months):
    capital = capital + spend - salary
    spend = spend * 1.03

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(capital))
