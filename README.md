1 - запустить main.py -- запустить сервер.

2 - Для создания/изменения/удаления используется файл datachanger.py
    - Для инициализации запускаем файл через командую строку (python3 datachanger.py).
    
    - Появляются значения для ввода:
    
        type - тип операции ( delete , create , change ).
        id - при создании обьекта вводим для него уникальный id.
        name - При создании/изменении обьекта dведите имя обьекта.
        email - При создании/изменении обьекта введите его личный email.
        status -  При создании/изменении обьекта введите его текущий статус.
        
        Для удаления требуется только id , в остальные поля можно вписать любое значение.
        
3 - Можно создать базу данных для теста в файле sss.py

Программа datachanger.py работает на классовой основе. Для инициализции требуется 5 значений - тип операции , id , имя , email , статус пользователя.

Обьект класса Main.theoperation выполняет функцию crud-приложения и создает post-запросы.

Программа sss.py создает случайно сгенерированную базу данных пользователей в размере , которое может быть указано в в цикле for ( для навигации : перед ним стоит комментарий).

Файл datainformation.json служит сейв-файлом для работы сервера . При инициализации одной из программ ( sss.py , datachanger.py ) данные либо записывается в него , либо изменяются/удаляются .

        
        
        
        
        
        
    
    




