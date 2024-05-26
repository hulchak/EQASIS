# Лабораторна робота №7
## Тема: Клас даних

### Опис проблеми
Оригінальний клас `Product` містить публічні поля, що дозволяють прямий доступ до даних продукту. Це може призвести до порушення інкапсуляції та безпеки даних.

### Аналіз проблеми
Клас `Product` використовує публічні поля для зберігання інформації про продукти. Це робить клас вразливим до неправильного використання ззовні, оскільки поля можуть бути змінені без контролю. Відсутність інкапсуляції ускладнює управління станом об'єктів та може призвести до помилок у програмі.

### Оптимізація методу
**Рефакторинг:** 
1. **Енкапсуляція полів:** Поля `product_id`, `name`, `category`, і `price` було зроблено приватними, а доступ до них тепер здійснюється через гетери та сетери.
2. **Додавання поведінки:** Введено метод `update_price` для безпечної зміни ціни продукту, що включає валідацію нової ціни.

### Результати рефакторингу
Рефакторинг забезпечив захист полям класу `Product` від небажаних зовнішніх впливів. Тепер всі зміни даних продукту контрольовані, що знижує ризик помилок. Введення методів доступу дозволяє краще управляти змінами і забезпечує можливість логування або застосування додаткової логіки під час оновлення полів.

### Висновки
Рефакторинг класу `Product` з зосередженням на інкапсуляції полів та додаванні поведінки забезпечив кращу безпеку та надійність системи. Ці зміни відповідають принципам об'єктно-орієнтованого програмування і забезпечують більш стабільну та підтримувану архітектуру програми.
