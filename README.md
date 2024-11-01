# Инвайтер в телеграм группы

## Необходиоме ПО
- python3

## Как использовать
1. Создайте приложение в телеграмме через https://my.telegram.org/apps  
Полученные `API_ID`, `API_HASH` положите в `.env`
```
   API_ID=...
   API_HASH=...
   ```
2. Запишите `GROUP_ID` в `.env`
3. Подготовте `.txt` файл с id пользователей, которых хотите добавить в группу  
Например:  
```text
124125215
124151
15135
```
4. Установка зависимостей
```shell
pip install -r requirements.txt
```
5. Запуск скрипта:  
```shell
python main.py -f users.txt
```
При первом запуске потребуется авторизация через номер телефона (придет код в телеграм)  
В дальнейшем авторизовываться не нужно, так как сохранится сессия `session.session`