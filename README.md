1 - Сервер запускается в main1.py
2 - Для создания базы данных используем sss.py -- генерирует любое возможное кол-во данных ( загрузка данных происходит геренированием случайного фейкового email , имен ( используется request) и id /



3 - Для создания/изменения/удаления* используем datachanger.py ( классовая основа )




* Не разобрался , как очистить поле в сервере -- удаление банально не происходит ввиду невозможности убрать уже записанные данные на сервер + replit не позволяет полностью раскрыть потенциал из-за бага с табами.
Но в сейв файле datainforamtion.json все успешно сохраняется и работает . Идея заключалась в простом get запросе этого json файла или использовании flask.session.clear() , но из-за бага с табами это невозможно .



**очистить datainformation.json




